

## ==================================================
## Solution 2: Use Gradient Descent
## ==================================================

import pandas as pd

# Input data
# Visualized scatterplot on Desmos: https://www.desmos.com/calculator/gib8bgngo6

# Input data
data = pd.read_csv('https://bit.ly/2UBhrMG', header=None)
X = data.iloc[:, 0]
Y = data.iloc[:, 1]

# Building the model
a = 0.0
b = 0.0

L = .00001  # The learning Rate
epochs = 1000000  # The number of iterations to perform gradient descent

n = float(len(X))  # Number of elements in X

# f(x) = ax^2 + b

# Performing Gradient Descent
# This will probably take a few minutes to run
for i in range(epochs):
    Y_pred = a * X**2 + b  # The current predicted value of Y
    D_a = (-2 / n) * sum(X * (Y - Y_pred))  # d/da derivative of loss function
    D_b = (-2 / n) * sum(Y - Y_pred)  # d/db derivative of loss function
    a = a - L * D_a  # Update a
    b = b - L * D_b  # Update b


print(a, b) # prints approximately 4,50 



