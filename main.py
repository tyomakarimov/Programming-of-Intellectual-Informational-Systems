import pygame

from window import *
import shields
import aliens
from helpers import laser_shots
from helpers import the_alien_shots
from helpers import the_asteroids
from helpers import random_shot
from helpers import current_position
from helpers import change_direction
from collections import deque
import torch
from skimage import color as skc, transform as skt
import random
from plotter import plot
from model import *

FPS = 60
MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LR = 0.001
SCORE = 0

n_games = 0
epsilon = 0
gamma = 0.9
memory = deque(maxlen = MAX_MEMORY)
device = torch.device('cpu')
model = Linear_QNet(20 * 20 * 10 * 10, 256, 4, device)
trainer = QTrainer(model, lr = LR, gamma = gamma, device = device)

def get_state():
  screen_state = pygame.surfarray.array3d(pygame.display.get_surface())
  image_processed = skc.rgb2gray(screen_state)
  image_processed = skt.resize(image_processed, (20 * 10, 20 * 10))
  return np.array(image_processed).flatten()

def remember(state, action, reward, next_state, game_over):
    global memory
    memory.append((state, action, reward, next_state, game_over))

def train_long_memory():
    if len(memory) > BATCH_SIZE:
        mini_sample = random.sample(memory, BATCH_SIZE)
    else:
        mini_sample = memory
    states, actions, rewards, next_states, game_overs = zip(*mini_sample)
    trainer.train_step(states, actions, rewards, next_states, game_overs)

def train_short_memory(state, action, reward, next_state, game_over):
    trainer.train_step(state, action, reward, next_state, game_over)

def get_action(state):
    global epsilon
    epsilon = 180 - n_games
    final_move = np.zeros(4)
    if random.randint(0, 400) < epsilon:
        move = random.randint(0, 3)
        final_move[move] = 1
    else:
        state0 = torch.tensor(state, dtype = torch.float, device = device)
        prediction = model(state0)
        move = torch.argmax(prediction).item()
        final_move[move] = 1
    return final_move

def main():
  run_global = True
  best_score = 0
  plot_scores = []
  plot_mean_scores = []
  total_score = 0
  while run_global:
    i = 0
    move_left = True
    run = True
    score = 0
    laser_image[0] = 0
    for idx, image in enumerate(shield_images):
      shield_images[idx] = 0
    new_aliens = []
    for i in range(15):
      new_aliens.append(pygame.Rect(
        aliens.initial_alien_coordinates[i]['x'],
        aliens.initial_alien_coordinates[i]['y'],
        30,
        30
      ))
    aliens.aliens = new_aliens
    laser.laser_rect = pygame.Rect(480, 540, 30, 30)
    while run_global and run:
      if (result[0]):
        break
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          run_global = False
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_UP or event.key == pygame.K_w:
            shot = pygame.Rect(
              laser.laser_rect.x + laser.laser_rect.width / 2,
              laser.laser_rect.y, 
              5,
              10
            )
            shots.append(shot)
          if event.key == pygame.K_z:
            if current_algorithm[0] < 2:
              current_algorithm[0] += 1
            else:
              current_algorithm[0] = 0
          if (
            event.key == pygame.K_LEFT or event.key == pygame.K_a
          ) and laser.laser_rect.x - 3 > 0:
            laser.laser_rect.x -= 30
            laser.laser_coordinates['x'] -= 30
          if (
            event.key == pygame.K_RIGHT or event.key == pygame.K_d
          ) and laser.laser_rect.x + laser.laser_rect.width + 10 < WIDTH:
            laser.laser_rect.x += 30
            laser.laser_coordinates['x'] += 30
      state_old = get_state()
      final_move = get_action(state_old)
      if (final_move[1] == 1 and laser.laser_rect.x - 3 > 0):
        laser.laser_rect.x -= 30
        laser.laser_coordinates['x'] -= 30
      if (final_move[2] == 1 and laser.laser_rect.x + laser.laser_rect.width + 10 < WIDTH):
        laser.laser_rect.x += 30
        laser.laser_coordinates['x'] += 30
      if (final_move[3] == 1):
        shot = pygame.Rect(
            laser.laser_rect.x + laser.laser_rect.width / 2,
            laser.laser_rect.y, 
            5,
            10
          )
        shots.append(shot)
      cur_score = score
      score = laser_shots.handle_laser_shots(
        shots,
        aliens.aliens,
        shields.shields,
        shield_images,
        aliens.alien_coordinates,
        previous_paths,
        score
      )
      the_alien_shots.handle_alien_shots(
        laser.laser_rect,
        alien_shots,
        laser_image,
        shields.shields,
        shield_images
      )
      the_asteroids.handle_asteroids(
        laser.laser_rect,
        asteroids,
        laser_image,
        shields.shields,
        shield_images
      )
      reward = 0
      if cur_score < score:
        reward = 1
      if (laser_image[0] == 7):
        reward = -1
      draw_window()
      if len(aliens.aliens) == 0:
        draw_result('You have won!!!')
      if laser_image[0] > 6:
        draw_result('You have lost.')
      if (i % 60 == 0) and len(aliens.aliens) > 0:
        random_shot.get_random_shot(len(aliens.aliens), alien_shots, aliens.aliens)
        current_position.change_current_position(current)
        move_left_value, max_y = change_direction.change_current_direction(
          move_left,
          aliens.aliens,
          aliens.alien_coordinates
        )
        move_left = move_left_value
        if max_y > 440:
          draw_result('You have lost.')
      i += 1
      state_new = get_state()
      game_over = laser_image[0] == 7 or len(aliens.aliens) == 0
      train_short_memory(state_old, final_move, reward, state_new, game_over)
      remember(state_old, final_move, reward, state_new, game_over)
    result[0] = ''
    global n_games
    n_games += 1
    train_long_memory()
    if score > best_score:
        best_score = score
        model.save()
    the_result = laser_image[0] == 7
    def show_result(result):
      if result:
        return 'defeat'
      return 'win'
    print("Game №" + str(n_games), 'finished with', show_result(the_result), 'the score was', score, 'the best score so far is', best_score)
    plot_scores.append(score)
    total_score += score
    avg_score = total_score / n_games
    plot_mean_scores.append(avg_score)
    plot(plot_scores, plot_mean_scores)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run_global = False

if __name__ == '__main__':
  main()
