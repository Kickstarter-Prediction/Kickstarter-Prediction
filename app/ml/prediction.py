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


# Setup the prediction process (how the data will be passed to the model)
def predict(main_category,
            currency,
            goal,
            country,
            duration_days
            ):
    """Predict the best value for the Airbnb host's property based on
    specific features found in historical data.
    Parameters are the selected features of most importance (based on
    EDA and model testing).
    Returns a result in dollar amount.
    """

    # Pass the arguments into a dataframe to be passed into predictive model
    df = pd.DataFrame(columns=["main_category",
                               "currency",
                               "goal",
                               "country",
                               "duration_days"
                               ],
                      data=[[main_category,
                             currency,
                             goal,
                             country,
                             duration_days,
                             ]]
                      )

    # Generate a prediction based on the information in the dataframe
    y_pred = model.predict(df)[0][0]

    # Revert prediction logarithmic values and round for cents
    result = (y_pred)

    return f"${result} per night"


# Route the inputs from the HTML form into the predictive model
@router.post('/prediction')
def echo(
    request: Request,
    main_category: str=Form(...),
    currency: str=Form(...),
    goal: int=Form(...),
    country: str=Form(...),
    duration_days: int=Form(...)
        ):
    """Gets the input data from predict.html (with respective dtypes
    included) and passes them into the predict function (used as a
    helper function).
    Parameters are the request (cleverly utilized by Minh Nuyen to
    pass into the response template) as well as values for the features
    necessary for the prediction, collested from the HTML form.
    Returns an HTML template supplied through Jinja which displays the
    recommended price per night as well as the selections made by the
    user (Airbnb host) to make the reccomendation.
    """

    # Make the prediction
    prediction = predict(main_category,
                         currency,
                         goal,
                         country,
                         duration_days
                         )

    return templates.TemplateResponse('prediction.html',
                                      {"request": request,
                                       "prediction": prediction,
                                       "main_category":
                                       f'main_category: {main_category}',
                                       "currency": f'currency: {currency}',
                                       "goal":
                                       f'goal: {goal}',
                                       "country": f'country: {country}',
                                       "duration_days": f'duration_days: {duration_days}'
                                       })


# Route for display of the prediction page
@router.get('/prediction')
def display_index(request: Request):
    return templates.TemplateResponse('prediction.html', {"request": request})