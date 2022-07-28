"""
You are trying to create a better guinea pig food blend. For a day’s worth of food, you 
would like it to contain a minimum of 25 grams (g) of fat, 32 grams of carbohydrates, and 
5 grams of protein. But the guinea pig can only have 4 oz of food a day. 

You have two existing foods: Food A and Food B, and you want to blend them to create 
your balanced diet. Food A contains 6g of fat, 13g of carbohydrates, and 3g of protein per 
ounce, and costs $0.40 per ounce. Food B contains 11g of fat, 14g of carbohydrates, and 
2g of protein per ounce, at a cost of $0.30 per ounce.

How many ounces of each food should you mix each day, while minimizing cost? Complete
the code below by replacing the ?'s. 
"""


from pulp import *

# declare your variables
x = LpVariable("x", lowBound=0, cat=LpContinuous)   # 0<=x
y = LpVariable("y", lowBound=0, cat=LpContinuous) # 0<=y

# defines the problem
prob = LpProblem("Guinea Pig Food Optimization", LpMinimize)

# defines the constraints

# fat, carbs, and protein
prob += 25 <= ?
prob += ? <= 13*x + 14*y
prob += 5 <= ?

# weight
prob += 4 <= x + y

# defines the objective function to maximize
prob += .30 * ? + .40 * ?

# solve the problem
status = prob.solve()
print(LpStatus[status])

print(value(x))
print(value(y))
