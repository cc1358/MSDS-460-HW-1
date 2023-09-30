#!/usr/bin/env python
# coding: utf-8

# In[3]:


from pulp import LpVariable, LpProblem, LpMaximize, LpStatus, value, LpMinimize

# declare your variables
x1 = LpVariable("x1", 0, None) # x1>=0
x2 = LpVariable("x2", 0, None) # x2>=0
x3 = LpVariable("x3", 0, None) # x3>=0
x4 = LpVariable("x4", 0, None) # x4>=0
x5 = LpVariable("x5", 0, None) # x5>=0




# defines the problem
prob = LpProblem("problem", LpMinimize)

# defines the constraints 

prob += 580*x2 + 50*x4 + 760*x5 <= 5000
prob += 210*x1 + 280*x2 + 80*x3 + 120*x4 + 470*x5 >= 2000
prob += 6*x1 + 9*x2 + 1*x3 + 28*x4 + 9*x5 >=  50 
prob += 2*x4 >= 20
prob += 20*x1 + 150*x2 + 20*x3 + 50*x5 >=  1300
prob += 0.7*x1 + 2*x2 + 0.2*x3 + 0.72*x4 + 1.3*x5 >=  18
prob += 170*x1 + 300*x2 + 240*x3 + 430*x5 >= 4700


# defines the objective function to maximize
prob += 0.436*x1 + 3.79*x2 + 0.689*x3 + 2.248*x4 + 3.49*x5

# solve the problem
status = prob.solve()
LpStatus[status]

# print the results
print("Pulp Solution for x1, x2, x3, x4, x5")
print(value(x1))
print(value(x2))
print(value(x3))
print(value(x4))
print(value(x5))


# In[8]:


from pulp import LpVariable, LpProblem, LpMaximize, LpStatus, value, LpMinimize

# declare your variables
x1 = LpVariable("x1", 0, None) # x1>=0
x2 = LpVariable("x2", 0, None) # x2>=0
x3 = LpVariable("x3", 0, None) # x3>=0
x4 = LpVariable("x4", 0, None) # x4>=0
x5 = LpVariable("x5", 0, None) # x5>=0




# defines the problem
prob = LpProblem("problem", LpMinimize)

# defines the constraints 

prob += 580*x2 + 50*x4 + 760*x5 <= 5000
prob += 210*x1 + 280*x2 + 80*x3 + 120*x4 + 470*x5 >= 2000
prob += 6*x1 + 9*x2 + 1*x3 + 28*x4 + 9*x5 >=  50 
prob += 2*x4 >= 20
prob += 20*x1 + 150*x2 + 20*x3 + 50*x5 >=  1300
prob += 0.7*x1 + 2*x2 + 0.2*x3 + 0.72*x4 + 1.3*x5 >=  18
prob += 170*x1 + 300*x2 + 240*x3 + 430*x5 >= 4700
prob += 2*x2 + 9*x5 <= 20
prob += 1*x1 + 5*x2 + 2*x3 + 9*x5 >= 28



# defines the objective function to maximize
prob += 0.436*x1 + 3.79*x2 + 0.689*x3 + 2.248*x4 + 3.49*x5

# solve the problem
status = prob.solve()
LpStatus[status]

# print the results
print("Pulp Solution for x1, x2, x3, x4, x5")
print(value(x1))
print(value(x2))
print(value(x3))
print(value(x4))
print(value(x5))


# In[ ]:




