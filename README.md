# Diamond Price Predictor

Project Overview

The Diamond Price Predictor is a machine learning application designed to predict the price of diamonds based on their characteristics. This project utilizes FastAPI for serving the model predictions through a REST API, allowing users to interact with the model via HTTP requests. The model itself is trained on a dataset containing various features of diamonds, including cut, color, and clarity, among others.

Features

FastAPI Framework: Utilizes FastAPI for efficient and easy-to-use API endpoints.
Machine Learning Model: Employs a machine learning model trained to predict diamond prices based on features such as cut, color, and clarity.
Data Preprocessing: Includes preprocessing steps to encode categorical variables and prepare the data for model training and predictions.
Model Persistence: Utilizes Pickle for saving and loading the trained model, ensuring predictions can be made without retraining.
Interactive Visualization: Provides interactive visualizations of the diamond dataset, helping to understand the distribution of various features.

Installation

To set up the project environment, follow these steps:
Clone the repository to your local machine.
Ensure you have Python 3.8 or later installed.
Install the required dependencies by running pip install -r requirements.txt in your terminal.

Usage

To start the FastAPI server and interact with the model, follow these steps:
Navigate to the project directory in your terminal.
Start the FastAPI server by running uvicorn main:app --reload.
Open your web browser and go to http://127.0.0.1:8000/docs to see the interactive API documentation provided by FastAPI.
Use the /predict_diamond_price endpoint to make predictions by providing the diamond features as input.


API Endpoints

GET /: A welcome message to confirm the API is running.
POST /predict_diamond_price: Accepts input data in JSON format to predict the price of a diamond. The input data should include the cut, color, and clarity of the diamond.

Example Request
{
  "cut": "Premium",
  "color": "E",
  "clarity": "SI1"
}

Contributing

Contributions to the Diamond Price Predictor are welcome. Please follow these steps to contribute:
Fork the repository.
Create a new branch for your feature or bug fix.
Commit your changes with clear, descriptive commit messages.
Push your branch and submit a pull request to the main repository.


If you would like to contribute to this project, please feel free to fork it and submit a pull request. All contributions are greatly appreciated!

License
#######