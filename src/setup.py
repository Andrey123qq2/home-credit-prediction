import io
import os
from pathlib import Path

from setuptools import find_packages
from distutils.core import setup

# Package meta-data.
NAME = 'prediction_model'
DESCRIPTION = 'Train and deploy prediction model'
URL = 'https://github.com/*****/prediction_model'
EMAIL = '****@gmail.com'
AUTHOR = 'Andrey Nesterov'
REQUIRES_PYTHON = '>=3.10.9'

here = os.path.abspath(os.path.dirname(__file__))

# What packages are required for this module to be executed?
def list_reqs(fname='requirements.txt'):
    with io.open(os.path.join(here, fname), encoding='utf-8', errors='ignore') as fd:
        return fd.read().splitlines()

try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION


# Load the package's __version__.py module as a dictionary.
ROOT_DIR = Path(__file__).resolve().parent
PACKAGE_DIR = ROOT_DIR / NAME
about = {}
with open(PACKAGE_DIR / 'VERSION') as f:
    _version = f.read().strip()
    about['__version__'] = _version


# Where the magic happens:
setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    package_data={'prediction_model': ['VERSION']},
    install_requires=list_reqs(),
    extras_require={},
    include_package_data=True,
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)
