#Import Libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score 

#Import other files/modules
from prediction_model.config import config
from prediction_model.processing.data_management import load_dataset, save_pipeline
import prediction_model.processing.preprocessors as pp
import prediction_model.pipeline as pl
from prediction_model.predict import make_prediction

# import config
# from processing.data_management import load_dataset, save_pipeline
# import processing.preprocessors as pp
# import pipeline as pl
# from predict import make_prediction

def run_training():
    """Train the model"""
    all_feats = config.NUMERICAL_FEATURES + config.CATEGORICAL_FEATURES + config.DATE_FEATURES
    train_df = load_dataset(base_file=config.BASE_DS_FILE, file_names=config.DS_FILES)
    y = train_df[config.TARGET]
    train_df = train_df[all_feats]
    train_df, val_df, y_train, y_val = train_test_split(train_df, y, test_size=0.2, random_state=42)
    pl.loan_pipe.fit(train_df, y_train)
    val_pred = pl.loan_pipe.predict_proba(val_df[all_feats])[:,1]
    val_score = roc_auc_score(y_val, val_pred)
    print("val_score:", val_score)

    save_pipeline(pipeline_to_save=pl.loan_pipe)

# if __name__=='__main__':
#     run_training()