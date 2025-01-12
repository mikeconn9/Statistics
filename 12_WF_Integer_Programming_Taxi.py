# Problem Statement
# We want to distribute taxis across zones to minimize unmet demand during rush hours. The constraints include:

# A fixed number of taxis available.
# Each taxi can only be assigned to one zone.
# Each zone has a demand that needs to be met.

# The aim of pulp is to allow an Operations Research (OR) practitioner or programmer to express Linear Programming (LP), 
# and Integer Programming (IP) models in python in a way similar to the conventional mathematical notation. 
# Pulp will also solve these problems using a variety of free and non-free LP solvers.

# 2: Sample data
import pandas as pd

# Define zones and their demands
zones = ["Zone A", "Zone B", "Zone C", "Zone D"]
demand = [40, 60, 50, 30]  # Number of ride requests per zone

# Define available taxis
total_taxis = 100

# Cost of assigning taxis to zones (e.g., distance or priority score)
#cost = {
#    ("Zone A", "Taxi"): 2,
#    ("Zone B", "Taxi"): 3,
#    ("Zone C", "Taxi"): 1,
#    ("Zone D", "Taxi"): 4,
#}
cost = {
    ("Zone A"): 2,
    ("Zone B"): 3,
    ("Zone C"): 1,
    ("Zone D"): 4,
}

# Maximum capacity for each zone
max_taxis_per_zone = [50, 70, 60, 40]

# 3: Set Up the Model
from pulp import LpProblem, LpMinimize, LpVariable, lpSum

# Create a Linear Programming Problem
model = LpProblem("Taxi_Distribution", LpMinimize)

# Decision variables: Number of taxis allocated to each zone
x = {zone: LpVariable(f"Taxis_in_{zone}", lowBound=0, cat="Integer") for zone in zones}

# Objective Function: Minimize the unmet demand or assignment cost
model += lpSum(cost[zone] * x[zone] for zone in zones), "Total_Cost"

# Constraints
# 1. Total taxis allocated cannot exceed available taxis
model += lpSum(x[zone] for zone in zones) <= total_taxis, "Total_Taxis_Constraint"

# 2. Taxis allocated to each zone must not exceed maximum capacity
for i, zone in enumerate(zones):
    model += x[zone] <= max_taxis_per_zone[i], f"Max_Taxis_{zone}"

# 3. Taxis allocated must meet or exceed demand where possible
for i, zone in enumerate(zones):
    model += x[zone] >= demand[i], f"Min_Demand_{zone}"

# 4: Solve the Model
# Solve the optimization problem
model.solve()

# Display results
print("Optimal Taxi Allocation:")
for zone in zones:
    print(f"{zone}: {x[zone].value()} taxis")
print(f"Total Cost: {model.objective.value()}")

'''
Results:
Welcome to the CBC MILP Solver 
Version: 2.10.3 
Build Date: Dec 15 2019 

command line - c:\Data\Michael work\Projects\venv\Lib\site-packages\pulp\solverdir\cbc\win\64\cbc.exe C:\Users\micha\AppData\Local\Temp\4bb17d3d6f1f4a54afc9aee5708b8e3b-pulp.mps -timeMode elapsed -branch -printingOptions all -solution C:\Users\micha\AppData\Local\Temp\4bb17d3d6f1f4a54afc9aee5708b8e3b-pulp.sol (default strategy 1)
At line 2 NAME          MODEL
At line 3 ROWS
At line 14 COLUMNS
At line 39 RHS
At line 49 BOUNDS
At line 54 ENDATA
Problem MODEL has 9 rows, 4 columns and 12 elements
Coin0008I MODEL read with 0 errors
Option for timeMode changed from cpu to elapsed
Problem is infeasible - 0.00 seconds
Option for printingOptions changed from normal to all
Total time (CPU seconds):       0.03   (Wallclock seconds):       0.03

Optimal Taxi Allocation:
Zone A: 40.0 taxis
Zone B: 60.0 taxis
Zone C: 50.0 taxis
Zone D: 30.0 taxis
Total Cost: 430.0
'''