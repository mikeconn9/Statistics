'''
Resources Per Role for Each Project Type: 

Large projects: [2,4,6,20][2, 4, 6, 20][2,4,6,20] (PM, A, AN, C). 

Medium projects: [1,2,3,10][1, 2, 3, 10][1,2,3,10]. 

Small projects: [1,2,2,5][1, 2, 2, 5][1,2,2,5]. 

Utilization Thresholds: 

Architect (A): 80%. 

Project Manager (PM) and Analyst (AN): 85%. 

Constructor (C): 90%. 

 

Adjusted Mathematical Formulation 

Objective: 

Minimize the total number of resources: 

Minimize: RPM+RA+RAN+RC\text{Minimize: } R_{PM} + R_{A} + R_{AN} + R_{C}Minimize: RPM +RA +RAN +RC  

Constraints: 

Utilization Thresholds: 

PM: 0.85×RPM≥Demand for PM across projects0.85 \times R_{PM} \geq \text{Demand for PM across projects}0.85×RPM ≥Demand for PM across projects. 

A: 0.80×RA≥Demand for A across projects0.80 \times R_{A} \geq \text{Demand for A across projects}0.80×RA ≥Demand for A across projects. 

AN: 0.85×RAN≥Demand for AN across projects0.85 \times R_{AN} \geq \text{Demand for AN across projects}0.85×RAN ≥Demand for AN across projects. 

C: 0.90×RC≥Demand for C across projects0.90 \times R_{C} \geq \text{Demand for C across projects}0.90×RC ≥Demand for C across projects. 

Role Demand for Each Project Type: 

Large: 3×[2,4,6,20]3 \times [2, 4, 6, 20]3×[2,4,6,20]. 

Medium: 10×[1,2,3,10]10 \times [1, 2, 3, 10]10×[1,2,3,10]. 

Small: 30×[1,2,2,5]30 \times [1, 2, 2, 5]30×[1,2,2,5].

'''

from pulp import LpProblem, LpMinimize, LpVariable, lpSum

# Parameters
large_projects = 3
medium_projects = 10
small_projects = 30

# Resources required per project type (PM, A, AN, C)
resources_per_project = {
    "Large": [2, 4, 6, 20],
    "Medium": [1, 2, 3, 10],
    "Small": [1, 2, 2, 5]
}

# Utilization thresholds
utilization = {"PM": 0.85, "A": 0.80, "AN": 0.85, "C": 0.90}

# Total project demands
total_demand = {
    "PM": (large_projects * resources_per_project["Large"][0] +
           medium_projects * resources_per_project["Medium"][0] +
           small_projects * resources_per_project["Small"][0]),
    "A": (large_projects * resources_per_project["Large"][1] +
          medium_projects * resources_per_project["Medium"][1] +
          small_projects * resources_per_project["Small"][1]),
    "AN": (large_projects * resources_per_project["Large"][2] +
           medium_projects * resources_per_project["Medium"][2] +
           small_projects * resources_per_project["Small"][2]),
    "C": (large_projects * resources_per_project["Large"][3] +
          medium_projects * resources_per_project["Medium"][3] +
          small_projects * resources_per_project["Small"][3])
}

# Create the optimization model
model = LpProblem("Workforce_Optimization", LpMinimize)

# Decision variables for number of resources
resources = {
    role: LpVariable(f"R_{role}", lowBound=0, cat="Integer")
    for role in ["PM", "A", "AN", "C"]
}

# Objective function: Minimize total resources
model += lpSum(resources[role] for role in resources), "Total_Resources"

# Constraints for utilization thresholds
for role in ["PM", "A", "AN", "C"]:
    model += utilization[role] * resources[role] >= total_demand[role], f"Demand_{role}"

# Solve the model
model.solve()

# Output the results
print("Optimal Resource Allocation:")
for role in resources:
    print(f"{role}: {resources[role].value()}")

print(f"Total Resources: {sum(resources[role].value() for role in resources)}")

'''
Results:

Welcome to the CBC MILP Solver 
Version: 2.10.3
Build Date: Dec 15 2019

command line - c:\Data\Michael work\Projects\venv\Lib\site-packages\pulp\solverdir\cbc\win\64\cbc.exe C:\Users\micha\AppData\Local\Temp\3f9667546bb94d77b824e2fc2f033ae1-pulp.mps -timeMode elapsed -branch -printingOptions all -solution C:\Users\micha\AppData\Local\Temp\3f9667546bb94d77b824e2fc2f033ae1-pulp.sol (default strategy 1)
At line 2 NAME          MODEL
At line 3 ROWS
At line 9 COLUMNS
At line 26 RHS
At line 31 BOUNDS
At line 36 ENDATA
Problem MODEL has 4 rows, 4 columns and 4 elements
Coin0008I MODEL read with 0 errors
Option for timeMode changed from cpu to elapsed
Continuous objective value is 640.621 - 0.00 seconds
Cgl0004I processed model has 0 rows, 0 columns (0 integer (0 of which binary)) and 0 elements
Cbc3007W No integer variables - nothing to do
Cuts at root node changed objective from 643 to -1.79769e+308
Probing was tried 0 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
Gomory was tried 0 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
Knapsack was tried 0 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
Clique was tried 0 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
MixedIntegerRounding2 was tried 0 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
FlowCover was tried 0 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
TwoMirCuts was tried 0 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
ZeroHalf was tried 0 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)

Result - Optimal solution found

Objective value:                643.00000000
Enumerated nodes:               0
Total iterations:               3
Time (CPU seconds):             0.01
Time (Wallclock seconds):       0.01

Option for printingOptions changed from normal to all
Total time (CPU seconds):       0.03   (Wallclock seconds):       0.03

Optimal Resource Allocation:
PM: 55.0
A: 115.0
AN: 128.0
C: 345.0
Total Resources: 643.0

'''