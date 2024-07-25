import pandas as pd
from prediction_model.config import config

def make_prediction(input_data, _loan_pipe):
    """Predicting the output"""
    data = pd.DataFrame(input_data)
    all_feats = config.NUMERICAL_FEATURES + config.CATEGORICAL_FEATURES + config.DATE_FEATURES
    # prediction = _loan_pipe.predict(input_data[all_feats])
    prediction = _loan_pipe.predict_proba(data[all_feats])[:,1]
    return prediction