import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

# Loadthe dataset
crops = pd.read_csv("soil_measures.csv")

# Check for missing values
print(crops.isna().sum())

# Display unique crop types s to verify multi-class target
print(crops.crop.unique())

# Separate features and target variable
X = crops.drop(columns="crop")
y = crops["crop"]

# Printing the columns to verify the feature names
print(X.columns)

# Spliting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Dictionary to store performance scores for each feature
feature_performance = {}

# Train a logistic regression model for each feature individually
for feature in ["N", "P", "K", "pH"]:
    if feature in X_train.columns:
        log_reg = LogisticRegression(multi_class="multinomial", max_iter=1000)
        log_reg.fit(X_train[[feature]], y_train)
        y_pred = log_reg.predict(X_test[[feature]])
        
        # Calculate the F1 score for the current feature
        f1 = metrics.f1_score(y_test, y_pred, average="weighted")
        
        # Store the feature and its F1 score in the dictionary
        feature_performance[feature] = f1
        print(f"F1-score for {feature}: {f1}")
    else:
        print(f"Feature {feature} not found in the dataset.")

# Identify the feature with the highest F1 score
best_feature = max(feature_performance, key=feature_performance.get)
best_score = feature_performance[best_feature]

# Create a dictionary with the best feature and its score
best_predictive_feature = {best_feature: best_score}

print(best_predictive_feature)
