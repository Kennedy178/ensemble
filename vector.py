import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, StackingClassifier
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import shap

# Custom transformer for feature engineering
class StatisticalFeatures(BaseEstimator, TransformerMixin):
    """
    Custom transformer that generates statistical aggregates per sample.
    Demonstrates how domain-specific preprocessing can enhance model learning.
    """
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        df = pd.DataFrame(X)
        stats = pd.DataFrame()
        stats['mean'] = df.mean(axis=1)
        stats['std'] = df.std(axis=1)
        stats['min'] = df.min(axis=1)
        stats['max'] = df.max(axis=1)
        return stats.values

# Simulated dataset for demonstration
np.random.seed(42)
X = np.random.randn(1000, 10)
y = np.random.randint(0, 2, 1000)

# Base learners for model stacking
base_learners = [
    ('rf', RandomForestClassifier(n_estimators=100, random_state=42)),
    ('gb', GradientBoostingClassifier(random_state=42))
]

# Meta learner (level 2 model)
meta_model = LogisticRegression(max_iter=1000)

# Defining a full pipeline from feature engineering to stacking
pipeline = Pipeline([
    ('features', StatisticalFeatures()),
    ('scaler', StandardScaler()),
    ('stack', StackingClassifier(estimators=base_learners, final_estimator=meta_model, cv=5))
])

# Evaluate model with stratified cross-validation 
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(pipeline, X, y, cv=cv, scoring='accuracy')

print(f"Cross-validation accuracy: {scores.mean():.4f} ± {scores.std():.4f}")

# Fit model to entire dataset for interpretability analysis
pipeline.fit(X, y)

# Feature importance using SHAP for explainability
explainer = shap.Explainer(pipeline.named_steps['stack'].final_estimator,
                           feature_names=['mean', 'std', 'min', 'max'])
shap_values = explainer(np.random.randn(10, 4))

print("\nSHAP value summary for meta model features:")
print(pd.DataFrame(shap_values.values, columns=['mean', 'std', 'min', 'max']).head())

"""
Study Notes:
1. Demonstrates hierarchical model design via stacking, combining ensemble learners.
2. Shows the use of a custom transformer integrated seamlessly into a scikit-learn pipeline.
3. Introduces SHAP for interpretable AI to understand model reasoning.
4. Encourages experimentation with feature engineering as the most creative layer in ML.
5. A reminder that advanced ML is not just about algorithms, but the art of data representation.
"""
