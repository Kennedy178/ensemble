import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset, random_split
from sklearn.datasets import make_classification
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import numpy as np

# Creating synthetic dataset for binary classification
X, y = make_classification(n_samples=2000, n_features=20, n_informative=10,
                           n_redundant=5, n_classes=2, random_state=42)
X = torch.tensor(X, dtype=torch.float32)
y = torch.tensor(y, dtype=torch.long)

# Spliting into training and validation sets
train_size = int(0.8 * len(X))
val_size = len(X) - train_size
train_data, val_data = random_split(TensorDataset(X, y), [train_size, val_size])

train_loader = DataLoader(train_data, batch_size=64, shuffle=True)
val_loader = DataLoader(val_data, batch_size=128)

# Define a simple fully connected neural network
class NeuralClassifier(nn.Module):
    def __init__(self, input_dim, hidden_dim=64):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(hidden_dim, hidden_dim // 2),
            nn.ReLU(),
            nn.Linear(hidden_dim // 2, 2)
        )

    def forward(self, x):
        return self.net(x)

# Instantiate model, optimizer, and loss function
model = NeuralClassifier(input_dim=X.shape[1])
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Early stopping configuration
best_val_loss = np.inf
patience, patience_counter = 10, 0
train_losses, val_losses = [], []

# Training loop with early stopping
for epoch in range(100):
    model.train()
    total_loss = 0
    for xb, yb in train_loader:
        optimizer.zero_grad()
        preds = model(xb)
        loss = criterion(preds, yb)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    avg_train_loss = total_loss / len(train_loader)
    train_losses.append(avg_train_loss)

    # Validation
    model.eval()
    with torch.no_grad():
        val_loss = sum(criterion(model(xb), yb).item() for xb, yb in val_loader) / len(val_loader)
    val_losses.append(val_loss)
    print(f"Epoch {epoch+1:03d} | Train Loss: {avg_train_loss:.4f} | Val Loss: {val_loss:.4f}")

    if val_loss < best_val_loss:
        best_val_loss = val_loss
        patience_counter = 0
        best_model_state = model.state_dict()
    else:
        patience_counter += 1
        if patience_counter >= patience:
            print("Early stopping triggered.")
            break

# Load best model
model.load_state_dict(best_model_state)

# Extract embeddings from the second hidden layer for visualization
model.eval()
with torch.no_grad():
    hidden_layer_output = model.net[:-1](X).numpy()

# Use t-SNE for embedding visualization
tsne = TSNE(n_components=2, perplexity=30, random_state=42)
X_embedded = tsne.fit_transform(hidden_layer_output)

# Plot t-SNE projection of learned features
plt.figure(figsize=(8, 6))
plt.scatter(X_embedded[:, 0], X_embedded[:, 1], c=y, cmap='coolwarm', s=25, alpha=0.7)
plt.title("t-SNE Visualization of Learned Neural Embeddings")
plt.xlabel("Dimension 1")
plt.ylabel("Dimension 2")
plt.grid(True)
plt.show()

# Plot learning curves
plt.figure(figsize=(8, 5))
plt.plot(train_losses, label='Training Loss')
plt.plot(val_losses, label='Validation Loss')
plt.title("Learning Curves with Early Stopping")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.legend()
plt.grid(True)
plt.show()
