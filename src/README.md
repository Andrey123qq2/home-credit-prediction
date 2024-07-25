This project is a simple solution of Kaggle competition https://www.kaggle.com/competitions/home-credit-credit-risk-model-stability/ . It doesn't use all of the features of competitions data (only depth 0 tables) and implement simple ML model.

#### Problem
Company wants to automate the loan eligibility process based on customer detail provided while filling online application form. 
It is a classification problem where we have to predict whether a loan would be approved or not. 

#### Data
The data corresponds to a set of financial transactions associated with individuals. 

Source: Kaggle

 
## Developement mode

Go to the project directory and install dependencies

```python
pip install -r requirements.txt  
```

Create a pickle file

```python
python prediction_model/train_pipeline.py
```

Creating a source distribution and wheel

```python
python setup.py sdist bdist_wheel
```
## Running Tests

To run tests, run the following command

```bash
  pytest -v
```
This will look for `test_*.py` or `*_test.py` files into directories and sub-directories

## Virtual Environment
Install virtualenv

```python
python3 -m pip install virtualenv
```

Check version
```python
virtualenv --version
```

Create virtual environment

```python
virtualenv venv_package
```

Activate virtual environment

For Linux
```python
source venv_package/bin/activate
```
For Windows
```python
venv_package\Scripts\activate
```

Deactivate virtual environment

```python
deactivate
```


## Installation

#### Install this project with pip

Go to project directory where `setup.py` file is located

To install it in editable or developer mode
```python
pip install -e .
```
```.``` refers to current directory

```-e``` refers to --editable mode

Normal installation
```python
pip install .
```
```.``` refers to current directory

#### To install from GitHub repository

With git
```python
pip install git+https://github.com/suhas-ds/prediction_model.git
```
Without git
```python
pip install https://github.com/suhas-ds/prediction_model/tarball/master
```
or
```python
pip install https://github.com/suhas-ds/prediction_model/zipball/master
```
or
```python
pip install https://github.com/suhas-ds/prediction_model/archive/master.zip
```


## Usage/Examples

Start python console

Import package and make the predictions

```python
>>> from prediction_model.config import config
>>> from prediction_model import train_pipeline
>>> from prediction_model.predict import make_prediction
>>> from prediction_model.processing.data_management import load_dataset, load_pipeline

>>> if config.RUN_TRAINING:
Run training and save Pipeline with trained model as pickle object classification_v1.pkl
>>>     train_pipeline.run_training()

>>> test_df = load_dataset(config.BASE_DS_FILE, config.DS_FILES, mode='test')
>>> test_df = test_df.to_dict()

>>> _loan_pipe = load_pipeline(config.PIPELINE_FILE_NAME)
>>> test_pred = make_prediction(test_df, _loan_pipe)
>>> print(test_pred)
```