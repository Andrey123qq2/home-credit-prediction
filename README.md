# Description
This project is a simple solution of Kaggle competition https://www.kaggle.com/competitions/home-credit-credit-risk-model-stability/ . It's goal is to create test CI/CD pipeline using GitHub Actions and GCP.
Also keep in mind educational purposes of this project it doesn't use all of the features of competitions data (only depth 0 tables) and implement simple ML model. Full competitive solution was implemented in the notebook https://www.kaggle.com/code/andreynesterov/home-credit-inference-final-no-hack/ .

## Key features:

* Sklearn based Pipeline for preprocessing and prediction
* Tests are implemented using pytest
* Application based on prediction model is built upon FastAPI
* Dockerized app is deployed on GCP
* GitHub Actions is used for CI/CD pipeline