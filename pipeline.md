

### 📘 Code Overview

`pipeline.py` demonstrates how a neural network learns, generalizes, and represents data internally.
It focuses on **training dynamics, feature representation, and interpretability** rather than raw prediction accuracy.
It shows how to look *inside* a model,  understanding how deep layers form structured, meaningful embeddings from complex input data.

---

### ⚙️ What the Code Does

1. Builds a **custom feedforward neural network** using PyTorch.
2. Trains it on a synthetic binary classification dataset with **mini-batch gradient descent**.
3. Implements **early stopping** to prevent overfitting.
4. Tracks and plots **training vs validation loss curves**.
5. Extracts **hidden layer embeddings** to visualize learned representations.
6. Uses **t-SNE** to project those embeddings into 2D space for interpretability.

---

### 🎯 Significance

This project highlights how **deep learning models transform raw data into meaningful internal structures**.
It connects model performance with understanding — showing how neural embeddings cluster and separate data naturally as learning progresses.

Applications include:

* Feature representation learning
* Neural network visualization
* Training diagnostics and interpretability research

---

### 🧩 Key Skills Demonstrated

| Category                | Skills Demonstrated                              |
| ----------------------- | ------------------------------------------------ |
| **Deep Learning**       | Neural architecture design, activation functions |
| **Model Optimization**  | Gradient descent, early stopping                 |
| **Model Evaluation**    | Training/validation loss tracking                |
| **Data Representation** | Feature embedding extraction                     |
| **Visualization**       | t-SNE projection of learned representations      |

---

### 🧰 Requirements

```bash
pip install torch scikit-learn matplotlib
```

---

### 🚀 How to Run

```bash
pipeline.py
```

---

### 📈 Example Output

```
Epoch 010 | Train Loss: 0.3542 | Val Loss: 0.3627
Epoch 020 | Train Loss: 0.2874 | Val Loss: 0.2941
...
Early stopping triggered.
```

You’ll also see two visualizations:

* **t-SNE plot** showing feature embeddings
* **Learning curves** showing training and validation loss

---
