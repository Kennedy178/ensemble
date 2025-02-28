# 🐧 K-Means Clustering on Penguin Dataset

This project applies **K-Means Clustering** to the **Palmer Penguins** dataset to group penguins into clusters based on their physical characteristics. The goal is to explore how well unsupervised learning can classify penguins based on their features.

## 📌 Dataset Overview

The **Palmer Penguins** dataset contains measurements of different penguin species collected from islands in Antarctica. The dataset includes:

- **Species**: Adelie, Gentoo, Chinstrap (Not used in clustering)
- **Culmen Length** (bill length)
- **Culmen Depth** (bill depth)
- **Flipper Length**
- **Body Mass**
- **Sex** (Categorical, converted into numerical form)

## 📊 Steps in the Analysis

### 1️⃣ Data Preprocessing
- Categorical feature `sex` is converted into numerical form using **one-hot encoding**.
- Missing values are handled.
- Features are **standardized** using `StandardScaler()` for better clustering.

### 2️⃣ Choosing the Optimal Number of Clusters
- The **Elbow Method** is used to determine the best number of clusters (`k`).
- The sum of squared distances (WCSS) is plotted to identify the elbow point.

### 3️⃣ Applying K-Means Clustering
- **K-Means algorithm** is used with the chosen `k` value.
- Cluster labels are assigned to the dataset.

### 4️⃣ Visualization & Interpretation
- A **scatter plot** is created to visualize clusters.
- Cluster centers and feature means are analyzed to interpret the results.

## 🔧 Installation & Usage

### Prerequisites
Make sure you have Python installed along with the required libraries.

```bash
pip install pandas numpy scikit-learn matplotlib seaborn
