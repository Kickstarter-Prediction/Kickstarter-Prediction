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


model = joblib.load('app/ml/model_xgb999.pkl')


# Setup the prediction process (how the data will be passed to the model)
def predict(currency,
            goal,
            country,
            duration_days,
            category
            ):
    

    # Pass the arguments into a dataframe to be passed into predictive model
    df = pd.DataFrame(columns=["currency",
                               "goal",
                               "country",
                               "duration_days",
                               "category"
                               ],
                      data=[[currency,
                             goal,
                             country,
                             duration_days,
                             category
                             ]]
                      )

    # Generate a prediction based on the information in the dataframe
    y_pred = model.predict(df)[0]

    # Revert prediction logarithmic values and round for cents
    result = (y_pred)

    
    if y_pred == 1:
        return f'Congratulations! Your Kickstarter Campaign Was \
            Successfuly Funded!'
    else:
        return f'We Are Sorry But Your Kickstarter Campaign Was Not \
            Successfuly Funded! Please revise your inputs and try again!'
    

# Route the inputs from the HTML form into the predictive model
@router.post('/prediction')
def echo(
    request: Request,
    currency: str=Form(...),
    goal: int=Form(...),
    country: str=Form(...),
    duration_days: int=Form(...),
    category: str=Form(...)
        ):
    

    # Make the prediction
    prediction = predict(currency,
                         goal,
                         country,
                         duration_days,
                         category
                         )

    return templates.TemplateResponse('prediction.html',
                                      {"request": request,
                                       "prediction": prediction,
                                       "currency": f'Currency: {currency}',
                                       "goal":
                                       f'Goal: {goal}',
                                       "country": f'Country: {country}',
                                       "duration_days": f'Duration of Days: {duration_days}',
                                       "category":
                                       f'Category: {category}',
                                       })


# Route for display of the prediction page
@router.get('/prediction')
def display_index(request: Request):
    return templates.TemplateResponse('prediction.html', {"request": request})