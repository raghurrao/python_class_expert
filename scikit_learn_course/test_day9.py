import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

y_true = np.array([100, 100, 100, 100, 1000])
y_pred_A = np.array([100, 100, 100, 100, 0])
y_pred_B = np.array([300, 300, 300, 300, 700])

mae_A = mean_absolute_error(y_true, y_pred_A)
rmse_A = np.sqrt(mean_squared_error(y_true, y_pred_A))

mae_B = mean_absolute_error(y_true, y_pred_B)
rmse_B = np.sqrt(mean_squared_error(y_true, y_pred_B))

assert mae_A < mae_B
assert rmse_A > rmse_B

y_actual = np.array([10, 20, 30, 40])
y_predict = np.array([10, 20, 30, 40])
perfect_r2 = r2_score(y_actual, y_predict)
assert perfect_r2 == 1.0

y_mean_predict = np.array([25, 25, 25, 25])
mean_r2 = r2_score(y_actual, y_mean_predict)
assert mean_r2 == 0.0

def evaluate_regression(y_t, y_p):
    mae = mean_absolute_error(y_t, y_p)
    mse = mean_squared_error(y_t, y_p)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_t, y_p)

evaluate_regression(y_true, y_pred_A)

try:
    y_true_bug = np.array([1, 2, 3, 4, 5])
    y_pred_bug = np.array([1.1, 2.1, 2.9, 4.2, 5.0])
    bad_r2 = r2_score(y_pred_bug, y_true_bug)
    # the bug might not crash, but yields wrong R2.
    assert r2_score(y_true_bug, y_pred_bug) != bad_r2
except Exception as e:
    print('Error:', e)

n = len(y_true)
p = 2
r2_A = r2_score(y_true, y_pred_A)
adj_r2 = 1 - ( (1 - r2_A) * (n - 1) / (n - p - 1) )
assert adj_r2 < r2_A

print("All Day 9 codes executed successfully!")
