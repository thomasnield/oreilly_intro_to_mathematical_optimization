"""
Two columns of data are stored here: https://bit.ly/3EHfgtO

Use gradient descent to solve for the `m` and `b` values 
with accuracy to three decimal places.

The slopes with respect to `m` and `b` against the loss function 
(sum of squares) are also provided below as expressions `D_m` and `D_b`. 

Replace the ?'s and execute the script.
"""
import pandas as pd

# Import points from CSV
points = list(pd.read_csv("https://bit.ly/3EHfgtO").itertuples())

# Building the model
m = 0.0
b = 0.0

# The learning Rate
L = .0001

# The number of iterations
iterations = 100_000

n = float(len(points))  # Number of elements in X

# Perform Gradient Descent
for i in range(iterations):

    # slope with respect to m
    D_m = sum(2 * p.x * ((m * p.x + b) - p.y) for p in points)

    # slope with respect to b
    D_b = sum(2 * ((m * p.x + b) - p.y) for p in points)

    # update m and b
    m -= L * D_m
    b -= L * D_b

print("y = {0}x + {1}".format(m, b))
