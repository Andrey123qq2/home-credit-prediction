from prediction_model.config import config
from prediction_model import train_pipeline
from prediction_model.predict import make_prediction
from prediction_model.processing.data_management import load_dataset, load_pipeline

if config.RUN_TRAINING:
    # Run training and save Pipeline with trained model as pickle object classification_v1.pkl
    train_pipeline.run_training()

test_df = load_dataset(config.BASE_DS_FILE, config.DS_FILES, mode='test')
test_df = test_df.to_dict()

_loan_pipe = load_pipeline(config.PIPELINE_FILE_NAME)
test_pred = make_prediction(test_df, _loan_pipe)
print(test_pred)