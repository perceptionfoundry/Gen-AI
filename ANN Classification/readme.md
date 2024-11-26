# Artificial-Neural-Network-Streamlit

This repository contains the implementation of an Artificial Neural Network (ANN) for predicting customer churn. The project includes data preprocessing, model training, and deployment using Streamlit.

**[Try the live demo here!](https://ann-classification-churn-cgemagzs6cxooufbazqcuf.streamlit.app/)**

## Table of Contents

- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Results](#results)

## Project Overview

Customer churn prediction is crucial for businesses to retain customers and maintain revenue. This project utilizes an ANN to predict whether a customer will churn based on various features. The model is trained, evaluated, and deployed using Streamlit for user interaction.

## Dataset

The dataset used for this project is `Churn_Modelling.csv`, which includes the following features:

- CustomerID
- Surname
- CreditScore
- Geography
- Gender
- Age
- Tenure
- Balance
- NumOfProducts
- HasCrCard
- IsActiveMember
- EstimatedSalary
- Exited (Target variable)

## Installation

To install the required dependencies, run:

```bash
pip install -r requirements.txt
```

## Usage
#### Training the Model
To train the model, run the following Jupyter notebook:

```bash
experiments.ipynb
```
This notebook includes data preprocessing, model training, and evaluation steps.

#### Deployment
To deploy the model using Streamlit, run:
```bash
streamlit run app.py
```
This will start a local web server where you can interact with the model and make predictions.

## Project Structure
The repository is structured as follows:

- Churn_Modelling.csv: The dataset used for training the model.
- LICENSE: GNU GENERAL PUBLIC LICENSE.
- app.py: Script for deploying the model using Streamlit.
- experiments.ipynb: Jupyter notebook containing the data preprocessing, model training, and evaluation steps.
- label_encoder_gender.pkl: Label encoder for the gender feature.
- model.h5: Trained ANN model.
- onehot_encoder_geo.pkl: One-hot encoder for the geography feature.
- prediction.ipynb: Jupyter notebook for making predictions.
- requirements.txt: List of dependencies required for the project.
- scaler.pkl: Scaler used for feature scaling.
## Results
The model achieved an accuracy of 87% on the test set. Detailed performance metrics and model evaluation results are available in the experiments.ipynb notebook.