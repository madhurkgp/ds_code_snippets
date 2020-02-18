

#mean absolute percentage error
def mape(y_true, y_pred):
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return round(np.mean(np.abs((y_pred - y_true) / y_pred)) * 100, 3)

