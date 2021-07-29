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


<<<<<<< Updated upstream
model = joblib.load('app/ml/model_xgb2.pkl')
=======
model = joblib.load('app/ml/model_xgb999.pkl')
>>>>>>> Stashed changes


# Setup the prediction process (how the data will be passed to the model)
def predict(currency,
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
    df = pd.DataFrame(columns=["currency",
                               "goal",
                               "country",
                               "duration_days"
                               ],
                      data=[[currency,
                             goal,
                             country,
                             duration_days,
                             ]]
                      )

    # Generate a prediction based on the information in the dataframe
    y_pred = model.predict(df)[0][0]

    # Revert prediction logarithmic values and round for cents
    result = (y_pred)

<<<<<<< Updated upstream
    return f"${result} per night"

=======
    #return f"${result} per night"
    if y_pred == 1:
        return f'Congratulations! Your Kickstarter Campaign Was \
            Successfuly Funded!'
    else:
        return f'We Are Sorry But Your Kickstarter Campaign Was Not \
            Successfuly Funded! Please revise your inputs and try again!'
    
>>>>>>> Stashed changes

# Route the inputs from the HTML form into the predictive model
@router.post('/prediction')
def echo(
    request: Request,
    currency: str=Form(...),
    goal: int=Form(...),
    country: str=Form(...),
    duration_days: int=Form(...)
        ):
    

    # Make the prediction
    prediction = predict(currency,
                         goal,
                         country,
                         duration_days
                         )

    return templates.TemplateResponse('prediction.html',
                                      {"request": request,
                                       "prediction": prediction,
                                       "currency": f'Currency: {currency}',
                                       "goal":
<<<<<<< Updated upstream
                                       f'goal: {goal}',
                                       "country": f'country: {country}',
                                       "duration_days": f'duration_days: {duration_days}'
=======
                                       f'Goal: {goal}',
                                       "country": f'Country: {country}',
                                       "duration_days": f'Duration of Days: {duration_days}',
                                       "category":
                                       f'Category: {category}',
>>>>>>> Stashed changes
                                       })


# Route for display of the prediction page
@router.get('/prediction')
def display_index(request: Request):
    return templates.TemplateResponse('prediction.html', {"request": request})