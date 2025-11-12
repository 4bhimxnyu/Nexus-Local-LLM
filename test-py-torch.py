# test_tf_torch.py
# Simple test file for TensorFlow and PyTorch setup

import torch
import torch.nn as nn
import torch.optim as optim
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np

# --- TensorFlow section ---
print("\n--- TensorFlow Test ---")
print("TensorFlow version:", tf.__version__)

# Create a tiny TF model: y = 2x - 1
X = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
Y = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)

model_tf = keras.Sequential([layers.Dense(units=1, input_shape=[1])])
model_tf.compile(optimizer="sgd", loss="mean_squared_error")
model_tf.fit(X, Y, epochs=500, verbose=0)

print("TF prediction for x=10.0:", model_tf.predict([10.0])[0][0])

# --- PyTorch section ---
print("\n--- PyTorch Test ---")
print("PyTorch version:", torch.__version__)
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Running on device: {device}")

# Create a simple PyTorch linear model: y = 2x - 1
X_t = torch.tensor(X, dtype=torch.float32).unsqueeze(1)
Y_t = torch.tensor(Y, dtype=torch.float32).unsqueeze(1)

model_torch = nn.Linear(1, 1)
loss_fn = nn.MSELoss()
optimizer = optim.SGD(model_torch.parameters(), lr=0.01)

for epoch in range(500):
    y_pred = model_torch(X_t)
    loss = loss_fn(y_pred, Y_t)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

with torch.no_grad():
    test_val = torch.tensor([[10.0]])
    pred = model_torch(test_val).item()

print("Torch prediction for x=10.0:", pred)

print("\n TensorFlow and PyTorch tests completed successfully.")
