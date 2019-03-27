from pulp import *

# declare your variables
x = LpVariable("x", lowBound=0, cat=LpInteger)   # 0<=x
y = LpVariable("y", lowBound=0, cat=LpInteger) # 0<=y

# defines the problem
prob = LpProblem("factory_problem", LpMaximize)

# defines the constraints
prob += x + 3*y <= 20
prob += 6*x +2*y <= 45

# defines the objective function to maximize
prob += 200*x + 300*y

# solve the problem
status = prob.solve()
print(LpStatus[status])

# print the results x = 5, y = 5
print(value(x))
print(value(y))

