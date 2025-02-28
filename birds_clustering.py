# Import Required Packages
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Step 1 - Loading and examining the dataset
penguins_df = pd.read_csv("penguins.csv")
print(penguins_df.head())
print(penguins_df.info())

# Step 2 - Perform preprocessing steps on the dataset to create dummy variables
# Convert categorical variables into dummy/indicator variables
penguins_df = pd.get_dummies(penguins_df, columns=['sex'], dtype='int') # Convert only the 'sex' column

# Step 3 - Perform preprocessing steps on the dataset - standardizing/scaling
# Scaling variables (also called standardizing) is recommended before performing a clustering algorithm
numeric_features = ['culmen_length_mm', 'culmen_depth_mm', 'flipper_length_mm', 'body_mass_g']
X = penguins_df[numeric_features]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
penguins_preprocessed = pd.DataFrame(data=X_scaled, columns=numeric_features)

# Step 4 - Detect the optimal number of clusters for k-means clustering
inertia = []
for k in range(1, 10):
    kmeans = KMeans(n_clusters=k, random_state=42).fit(penguins_preprocessed)
    inertia.append(kmeans.inertia_)    
plt.plot(range(1, 10), inertia, marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.title('Elbow Method')
plt.show()
n_clusters = 3  # Adjusted based on the elbow plot

# Step 5 - Run the k-means clustering algorithm with the optimal number of clusters
kmeans = KMeans(n_clusters=n_clusters, random_state=42).fit(penguins_preprocessed)
penguins_df['label'] = kmeans.labels_

# Visualize the clusters (example using two features)
plt.scatter(penguins_df['culmen_length_mm'], penguins_df['flipper_length_mm'], c=penguins_df['label'], cmap='viridis')
plt.xlabel('Culmen Length (mm)')
plt.ylabel('Flipper Length (mm)')
plt.title(f'K-means Clustering (K={n_clusters})')
plt.colorbar(label='Cluster')
plt.show()

# Step 6 - Create final `stat_penguins` DataFrame
stat_penguins = penguins_df[numeric_features + ['label']].groupby('label').mean()
print(stat_penguins)
