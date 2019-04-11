from pulp import *


# declare your variables
x_a = LpVariable("x_a", cat=LpBinary)
x_b = LpVariable("x_b", cat=LpBinary)
x_c = LpVariable("x_c", cat=LpBinary)
x_d = LpVariable("x_d", cat=LpBinary)

# defines the problem
prob = LpProblem("Knapsack Problem", LpMaximize)

# defines the weight constraint where items can't exceed 24
prob += 5*x_a + 10*x_b + 4*x_c + 12*x_d <= 24

# defines the objective function to maximize
prob += 10*x_a + 50*x_b + 30*x_c + 40*x_d

# solve the problem
status = prob.solve()
print(LpStatus[status])

# print the results x_a=0.0, x_b=1.0, x_c=1.0, x_d=1.0
print(value(x_a))
print(value(x_b))
print(value(x_c))
print(value(x_d))

