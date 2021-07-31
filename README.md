# Kickstarter Success Predictor
​
## What is it?
​
Kickstarter Success Predictor is a web app that allows a user to quickly determine if their Kickstarter Campaign will be successful based on data from prior campaigns.
​
## Where to find it?
​
[Kickstarter Success Predictor](https://kickstarter-app-prediction.herokuapp.com/)
[Product Vision Document](https://docs.google.com/document/d/1Q2jKUo_xsH7Kz0mUpEaJC0iBGpPyH5JdMkRlqjz0PA8/edit?usp=sharing)
​
## How was it built?
​
This web app is built on FastAPI and depolyed on Heroku. The app uses an XGBoost model with certain optimized hyperparameters to generate a prediction.
​
## Main Features
    
    Uses the following inputs to generate a prediction:
    - Funding Goal (between 0 and 1,000,000): the amount the user wants to raise in their Kickstarter Campaign
    - Campaign Duration (between 1 and 91 Days): the umber of days the user wants their Kickstarter Campaign to be live
    - Currency Type: the currency in which the user wants their Kickstarter Campaign to be denominated
    - Country: the location of the user's Kickstarter Campaign
    - Category: the specific category for the user's Kickstarter Campaign (e.g. 3D Printing, Bacon, Textiles, Theater, Webseries, etc.)
​
    A prediction of an unsuccessful campaign invites the user to adjust their inputs to determine the optimal inputs that will allow them to run a Successful Kickstarter Campaign.
​
## Contributors
​
Thanks to the following people who have contributed to this project:
​
* [@Gabriel Nosek](https://github.com/gaben3722)
* [@Ivan Mihailov](https://github.com/ivan-mihailov) 
​
## License
[MIT](https://choosealicense.com/licenses/mit/)
