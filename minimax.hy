(setv playing_field [
    [0 2 2 0 0]
    [0 0 0 0 0]
    [0 0 0 0 0]
    [3 4 0 3 4]
    [0 0 1 0 0]
  ]
)

(defn evaluate_with_move_left [score position]
  (if (= (get position 1) 0)
    (return 0)
  )
  (setv previous (- (get position 1) 1))
  (if (= (get playing_field (- (get position 0) 1) previous) 4)
    (return (- score 15))
  )
  (return score)
)

(defn evaluate_with_move_right [score position]
  (if (= (get position 1) 4)
    (return 0)
  )
  (setv next (+ (get position 1) 1))
  (if (= (get playing_field (- (get position 0) 1) next) 4)
    (return (- score 15))
  )
  (return score)
)

(defn minimax [current_depth max_turn score target_depth current_position result_position]
  (if (= current_depth target_depth)
    (return result_position)
  )
  (setv y (get current_position 1))
  (setv left_position [4 (- y 1)])
  (setv right_position [4 (+ y 1)])
  (setv left_result (if (= current_depth 0) left_position result_position))
  (setv right_result (if (= current_depth 0) right_position result_position))
  (if max_turn
    (if (> (evaluate_with_move_left score current_position) (evaluate_with_move_right score current_position))
      (return (minimax (+ current_depth 1) False score target_depth left_position left_result))
      (return (minimax (+ current_depth 1) False score target_depth right_position right_result))
    )
  )
  (if (> (evaluate_with_move_left score current_position) (evaluate_with_move_right score current_position))
    (return (minimax (+ current_depth 1) True score target_depth right_position right_result))
    (return (minimax (+ current_depth 1) True score target_depth left_position left_result))
  )
)

(setv player_position [4 2])
(setv next_move (minimax 0 True 1000 2 player_position player_position))
(print "Player's next move is into position" next_move)
