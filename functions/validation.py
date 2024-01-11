from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, median_absolute_error


def performance_evaluation(y_true, predictions):
    """
    Avalia o desempenho de um modelo usando diversas métricas.

    Parâmetros:
    - y_true: array ou lista, valores reais
    - predictions: array ou lista, valores previstos pelo modelo

    Retorna:
    - Dicionário contendo as métricas: MSE, MAD, MAE e R².
    """
    mse = mean_squared_error(y_true, predictions)
    mad = median_absolute_error(y_true, predictions)
    mae = mean_absolute_error(y_true, predictions)
    r2 = r2_score(y_true, predictions)

    performance_metrics = {
        'Mean Squared Error (MSE)': mse,
        'Median Absolute Deviation (MAD)': mad,
        'Mean Absolute Error (MAE)': mae,
        'R-squared (R²)': r2
    }

    return performance_metrics
