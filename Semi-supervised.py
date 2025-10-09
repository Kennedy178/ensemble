import numpy as np
import pandas as pd
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import mutual_info_classif
from sklearn.decomposition import PCA
from sklearn.cluster import DBSCAN
from sklearn.semi_supervised import LabelPropagation
from sklearn.metrics import adjusted_rand_score
import matplotlib.pyplot as plt

# Generate synthetic data for demonstration
# This represents complex, overlapping distributions often found in real data
X, y_true = make_blobs(n_samples=1000, centers=5, cluster_std=1.5, n_features=8, random_state=42)

# Scale the data for better numerical performance
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Compute mutual information for each feature relative to class labels
# Helps quantify nonlinear dependency between features and target
mi_scores = mutual_info_classif(X_scaled, y_true, random_state=42)
mi_ranking = np.argsort(mi_scores)[::-1]

print("Feature ranking based on mutual information:")
for i, idx in enumerate(mi_ranking):
    print(f"Feature {idx}: MI Score = {mi_scores[idx]:.4f}")

# Apply PCA for dimensionality reduction
# This demonstrates how to preserve variance and reveal structure in data
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Perform density-based clustering to uncover natural groupings
# DBSCAN is robust to noise and irregular cluster shapes
dbscan = DBSCAN(eps=0.8, min_samples=10)
clusters = dbscan.fit_predict(X_pca)

print("\nNumber of clusters discovered (excluding noise):", len(set(clusters)) - (1 if -1 in clusters else 0))

# Introduce partial labels to simulate semi-supervised learning scenario
rng = np.random.RandomState(42)
n_labeled = int(0.2 * len(y_true))
y_partial = np.full_like(y_true, -1)
labeled_indices = rng.choice(len(y_true), n_labeled, replace=False)
y_partial[labeled_indices] = y_true[labeled_indices]

# Apply label propagation to infer labels for unlabeled data
# Demonstrates graph-based semi-supervised learning
label_prop = LabelPropagation(kernel='knn', n_neighbors=10)
label_prop.fit(X_scaled, y_partial)
y_pred = label_prop.transduction_

# Evaluate how well propagated labels match ground truth
score = adjusted_rand_score(y_true, y_pred)
print(f"Adjusted Rand Index (Label Propagation vs True Labels): {score:.4f}")

# Visualize PCA projection colored by propagated labels
plt.figure(figsize=(8, 6))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y_pred, cmap='viridis', s=25, alpha=0.7)
plt.title("PCA Projection with Semi-Supervised Label Propagation")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.grid(True)
plt.show()


