ARIMA vs Random Forest: Time Series Analysis and Performance Comparison

Overview

This repository contains the code for a time series analysis project comparing the performance of two models:

ARIMA (AutoRegressive Integrated Moving Average)

Random Forest

The project evaluates the models using performance metrics such as Root Mean Squared Error (RMSE) and Mean Absolute Error (MAE). Additionally, a Streamlit application is provided for interactive visualization and exploration of the results.

Features

Data Preprocessing: Time series data is preprocessed, including handling missing values and differencing for ARIMA.

Model Comparison: Random Forest and ARIMA models are trained and evaluated.

Error Metrics: Performance is measured using RMSE and MAE.

Interactive Visualization: A Streamlit app allows users to visualize time series trends, model predictions, and residuals.

Repository Structure

.
|-- data/                       # Folder for datasets (if any)
|-- notebooks/                  # Jupyter notebooks
|   |-- arima_rf_comparison.ipynb  # Main analysis and modeling notebook
|-- app/                        # Streamlit application
|   |-- streamlit_app.py        # Streamlit code
|-- requirements.txt            # Python dependencies
|-- README.md                   # Project description

Getting Started

Prerequisites

Ensure you have Python 3.7 or higher installed on your system.

Installation

Clone this repository:

git clone https://github.com/yourusername/arima-rf-comparison.git
cd arima-rf-comparison

Install the required dependencies:

pip install -r requirements.txt

Dataset

Prepare or load your time series data. Ensure the dataset includes a time-indexed column and a target variable for modeling.

Running the Jupyter Notebook

Open the Jupyter notebook:

jupyter notebook notebooks/arima_rf_comparison.ipynb

Follow the step-by-step instructions in the notebook to preprocess data, fit models, and evaluate performance.

Running the Streamlit App

Navigate to the app/ directory.

Run the Streamlit app:

streamlit run app/streamlit_app.py

Open your browser and go to http://localhost:8501 to access the app.

Results

Performance Metrics

Random Forest:

RMSE: 15.27

MAE: 10.84

ARIMA:

RMSE: 14.21

MAE: 1.71

Key Insights

ARIMA outperformed Random Forest in this time series analysis.

The significantly lower MAE for ARIMA suggests its consistency and accuracy for this dataset.

Streamlit App Features

Data Visualization: View raw time series data and trends.

Model Predictions: Compare actual vs. predicted values for both models.

Residual Analysis: Visualize model residuals to check for white noise.

Error Metrics: Display RMSE and MAE for both models.

Technologies Used

Programming Language: Python

Libraries:

Time Series Analysis: statsmodels, numpy, pandas

Machine Learning: scikit-learn

Visualization: matplotlib, seaborn

Web App: streamlit

Contributing

Fork the repository.

Create a feature branch (git checkout -b feature-name).

Commit your changes (git commit -m 'Add feature').

Push to the branch (git push origin feature-name).

Open a Pull Request.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments

ARIMA model implementation: statsmodels

Random Forest implementation: scikit-learn

Streamlit framework for interactive visualizations

Contact

For any questions or issues, please reach out:

Author: Akash Verma

GitHub: Akashhverma

Email: akashverma35722@gmail.com
