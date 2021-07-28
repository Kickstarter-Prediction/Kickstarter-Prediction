"""Machine learning functions / success prediction tool"""

# Import packages
import pickle
import joblib
from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates 
import pandas as pd
import numpy as np
from xgboost import XGBClassifier 

# Instatiate the router
router = APIRouter()

# Instantiate templates
templates = Jinja2Templates(directory="app/templates/")


model = joblib.load('app/ml/model_xgb2.pkl')
