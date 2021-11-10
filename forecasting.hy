(import [pandas :as pd])
(import [numpy :as np])
(import [matplotlib.pyplot :as plt])
(import [sklearn.linear_model [LinearRegression]])
(import [csv_writer [write_result]])

(setv columns ["win" "time" "score" "player_health" "algorithm"])
(setv data_frame (pd.read_csv "output.csv" :usecols columns))

(setv x (np.array data_frame.score))
(setv xs (x.reshape -1 1))
(setv y (np.array data_frame.time))

(setv linear_regression_model (LinearRegression))
(linear_regression_model.fit xs y)
(linear_regression_model.score xs y)

(defn show_chart[x xs y]
  (plt.scatter x y)

  (setv result (linear_regression_model.predict xs))
  (print result)

  (plt.plot data_frame.score result)
  (plt.show)
)

(show_chart x xs y)

(setv scores [[165] [180] [195] [210] [225] [240] [255] [270] [295] [310]])

(defn write_prediction[x xs y]
  (plt.scatter x y)

  (setv result (linear_regression_model.predict xs))
  (write_result xs result)
)

(write_prediction x scores y)

; (plt.scatter data_frame.time data_frame.score)

; (setv x (np.array data_frame.score data_frame.player_health))
; (setv xs (x.reshape -1 1))
; (setv y (np.array data_frame.time))

; (setv linear_regression_model (LinearRegression))
; (linear_regression_model.fit xs y)
; (linear_regression_model.score xs y)
; (setv result (linear_regression_model.predict xs))
; (print result)
; (plt.plot data_frame.score result)
; (plt.show)
