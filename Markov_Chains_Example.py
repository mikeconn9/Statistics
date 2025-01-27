import numpy as np

# Transition matrix (rows represent states, columns are probabilities of transitioning to other states)
transition_matrix = np.array([
    [0.8, 0.2],
    [0.4, 0.6]
])

# Initial state distribution
initial_state = np.array([1, 0])  # Starting in state 0

# Simulate 10 steps
state = initial_state
for _ in range(10):
    print(f"State: {state}")
    state = np.dot(state, transition_matrix)

#State: [1 0]
#State: [0.8 0.2]
#State: [0.72 0.28]
#State: [0.688 0.312]
#State: [0.6752 0.3248]
#State: [0.67008 0.32992]
#State: [0.668032 0.331968]
#State: [0.6672128 0.3327872]
#State: [0.66688512 0.33311488]
#State: [0.66675405 0.33324595]