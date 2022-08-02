
from pulp import *

# declare your variables
x = LpVariable("x", lowBound=0, cat=LpContinuous)   # 0<=x
y = LpVariable("y", lowBound=0, cat=LpContinuous) # 0<=y

# defines the problem
prob = LpProblem("Guinea Pig Food Optimization", LpMinimize)

# defines the constraints

# fat, carbs, and protein
prob += 25 <= 6*x + 11*y
prob += 32 <= 13*x + 14*y
prob += 5 <= 3*x + 2*y

# weight
prob += 4 <= x + y

# defines the objective function to maximize
prob += .30 * x + .40 * y

# solve the problem
status = prob.solve()
print(LpStatus[status])

# print the results x = 3.8, y = .2
print(value(x))
print(value(y))
