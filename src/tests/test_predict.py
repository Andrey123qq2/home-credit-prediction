#Import libraries
import pytest

#Import files/modules
from prediction_model.config import config
from prediction_model.processing.data_management import load_dataset, load_pipeline
from prediction_model.predict import make_prediction


@pytest.fixture
def single_prediction():
	''' This function will predict the result for a single record'''
	test_df = load_dataset(config.BASE_DS_FILE, config.DS_FILES, mode='test')
	test_df = test_df.iloc[0:2]
	test_df = test_df.to_dict()
	pipeline_file_name = config.PIPELINE_FILE_NAME
	_loan_pipe = load_pipeline(pipeline_file_name)
	result = make_prediction(test_df, _loan_pipe)
	return result

#Test Prediction
def test_single_prediction_not_none(single_prediction):
	''' This function will check if result of prediction is not None'''
	assert single_prediction is not None

def test_single_prediction_dtype(single_prediction):
	''' This function will check if data type of result of prediction is str i.e. string '''
	assert isinstance(single_prediction[0], float)

def test_single_prediction_output_range(single_prediction):
	''' This function will check if result of prediction is in range [0,1] '''
	result = single_prediction[0]
	assert result >= 0 and result <= 1