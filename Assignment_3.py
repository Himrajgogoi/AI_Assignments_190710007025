# Assignment 3: Implement alpha-beta pruning in any language.

import math

# Function to calculate the heuristic value of a state
def calculate_heuristic(state):
    # In this example, the heuristic value is the negation of the state value
    return -state

# Function to perform the alpha-beta pruning algorithm
def alpha_beta_pruning(state, depth, alpha, beta, maximizing_player):
    if depth == 0:
        return calculate_heuristic(state)

    if maximizing_player:
        value = -math.inf
        for child_state in generate_child_states(state):
            value = max(value, alpha_beta_pruning(child_state, depth - 1, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = math.inf
        for child_state in generate_child_states(state):
            value = min(value, alpha_beta_pruning(child_state, depth - 1, alpha, beta, True))
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value

# Function to generate child states from a given state (example implementation)
def generate_child_states(state):
   
    child_states = []
    for i in range(state):
        child_states.append(i)
    return child_states

# Example
initial_state = 10
depth = 3
alpha = -math.inf
beta = math.inf
maximizing_player = True

best_value = alpha_beta_pruning(initial_state, depth, alpha, beta, maximizing_player)
print("Best value:", best_value)


