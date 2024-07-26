from fastapi import FastAPI
import uvicorn
import os

from fastapi.middleware.cors import CORSMiddleware

from loan_pred import LoanPred
from prediction_model.config import config
from prediction_model.predict import make_prediction
from prediction_model.processing.data_management import load_pipeline

app = FastAPI(
	title="Loan Default Prediction App",
    description="A simple API that use ML model to predict the Loan application status",
    version="0.1",
	)

origins = [
    "*"
	]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
	)

port = int(os.environ.get("PORT", 8000))

_loan_pipe = load_pipeline(config.PIPELINE_FILE_NAME)

@app.get('/')
def index():
    return {'message': 'Loan Default Prediction App'}

@app.get('/health')
def healthcheck():
    return {'status':'ok'}

@app.post('/predict')
def predict_loan_status(loan_details: LoanPred):
	data_dict = loan_details.__dict__
	prediction = make_prediction([data_dict], _loan_pipe)[0]
	return {'predict_proba': prediction}

if __name__ == '__main__':
	uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)