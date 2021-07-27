"""Machine learning functions / price recommendation tool"""

# Import packages
import pickle
from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates 
import pandas as pd
import numpy as np


# Instatiate the router
router = APIRouter()

# Instantiate templates
templates = Jinja2Templates(directory="app/templates/")


infile = open(model_xgb2.plk, 'rb')
model = pickle.load(infile)
infile.close()
