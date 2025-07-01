# Tutorial

## Start Backend

Go to /api directory
``cd api``

Start the Backend
``python3 api_app.py``
NOTE: you might use another version of python

## Start Frontend

Go to /frontend directory
``cd ../``
``cd frontend``

Install dependencies

``npm i``

Start the App

``npm run dev``

# Project Description

<div>
  <p>Discover <b>PhonePredictor</b>, an innovative application that leverages a probabilistic model to forecast smartphone preferences based on user demographics.</p>
  <br>
  <p>This project is divided into two core components: a robust <b>Python Flask API</b> and an intuitive <b>React frontend</b>. The backend dynamically generates a substantial dataset (100,000 entries) simulating user age, wealth, and their corresponding phone choices (Apple or Android).</p>
  <br>
  <p>Through this generated data, the API calculates and learns the underlying probabilities of phone ownership given specific age and wealth parameters. This sophisticated probabilistic model, specifically $P(\text{Phone} | \text{Age, Wealth})$, forms the intelligence behind the predictions.</p>
  <br>
  <p>The user-friendly React frontend allows you to interact with this powerful prediction engine. Simply input the probability of an individual being "young" and "rich" (values between 0 and 1). In real-time, the application will provide a prediction of whether the individual is more likely to own an Apple or Android phone, along with the precise probabilities for each outcome.</p>
  <br>
  <p><b>PhonePredictor</b> is an excellent demonstration of how data generation, probabilistic modeling, and a responsive web interface can be combined to create an insightful and practical prediction tool.</p>
</div>
