# Import required modules
import pandas as pd #to aid in loading the dataset
import numpy as np
from statsmodels.formula.api import logit

# Load the dataset
data = pd.read_csv('car_insurance.csv')

# Handle missing values by filling with the mean
data["credit_score"].fillna(data["credit_score"].mean(), inplace=True)
data["annual_mileage"].fillna(data["annual_mileage"].mean(), inplace=True)

# Initialize variables to store the best feature and its accuracy
best_feature = None
best_accuracy = 0

# Feature columns
features = data.drop(columns=['id', 'outcome']).columns

# Empty list to store model results
models = []

# Loop through each feature to find the best one
for col in features:
    # Create and fit the logistic regression model
    model = logit(f'outcome ~ {col}', data=data).fit()
    # Add the model to the list
    models.append(model)

# Empty list to store accuracies
accuracies = []

# Loop through models to compute accuracies
for model in models:
    # Compute the confusion matrix
    conf_matrix = model.pred_table()
    # True negatives
    tn = conf_matrix[0,0]
    # True positives
    tp = conf_matrix[1,1]
    # False negatives
    fn = conf_matrix[1,0]
    # False positives
    fp = conf_matrix[0,1]
    # Compute accuracy
    acc = (tn + tp) / (tn + fn + fp + tp)
    accuracies.append(acc)

# Find the feature with the highest accuracy
best_feature = features[accuracies.index(max(accuracies))]

# Create a DataFrame to store the best feature and its accuracy
best_feature_df = pd.DataFrame({
    'best_feature': [best_feature],
    'best_accuracy': [max(accuracies)]
})

# Display the result
print(best_feature_df)
