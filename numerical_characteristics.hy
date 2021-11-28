(import [pandas :as pd])

(setv columns ["win" "time" "score" "player_health" "algorithm"])
(setv data_frame (pd.read_csv "output.csv" :usecols columns))

(setv time_collection (get data_frame "time"))
(setv score_collection (get data_frame "score"))

(defn calculate_expectation [collection]
  (setv result 0)
  (setv number_of_elements (len collection))
  (setv probability (/ 1 number_of_elements))
  (for [value collection]
    (setv result (+ result (* value probability)))
  )
  (return result)
)

(defn calculate_variance [collection]
  (setv mathematical_expectation (calculate_expectation collection))
  (setv square_of_mathematical_expectation (* mathematical_expectation mathematical_expectation))
  (setv square_collection (lfor x collection (* x x)))
  (setv mathematical_expectation_of_squares (calculate_expectation square_collection))
  (setv result (- mathematical_expectation_of_squares square_of_mathematical_expectation))
  (return result)
)

(print "Mathematical expectation of time is" (calculate_expectation time_collection))
(print "Variance of time scores is" (calculate_variance score_collection))
