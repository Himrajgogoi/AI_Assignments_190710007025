## Assignment 1: Write a python program to solve the waterjug problem.

from collections import deque

# Function to solve the water jug problem
def solve_water_jug_problem(capacity_x, capacity_y, target):
    # Created a visited set to store visited states
    visited = set()

    # Created a queue to store states to explore
    queue = deque()

    # Added the initial state (0, 0) to the queue
    queue.append((0, 0))

    # Started the breadth-first search
    while queue:
        x, y = queue.popleft()

        # Checked if the target amount of water is reached
        if x == target or y == target:
            return True

        # Checked if the current state is visited
        if (x, y) in visited:
            continue

        # Marked the current state as visited
        visited.add((x, y))

        # Performed all possible actions and add resulting states to the queue
        # 1. Filled the first jug
        queue.append((capacity_x, y))
        # 2. Filled the second jug
        queue.append((x, capacity_y))
        # 3. Emptied the first jug
        queue.append((0, y))
        # 4. Emptied the second jug
        queue.append((x, 0))
        # 5. Poured water from the first jug to the second jug until it is full or the first jug is empty
        amount = min(x, capacity_y - y)
        queue.append((x - amount, y + amount))
        # 6. Poured water from the second jug to the first jug until it is full or the second jug is empty
        amount = min(capacity_x - x, y)
        queue.append((x + amount, y - amount))

    # Target amount of water cannot be reached
    return False

# Example usage
capacity_x = 5  # Capacity of the first jug
capacity_y = 3  # Capacity of the second jug
target = 4      # Target amount of water

if solve_water_jug_problem(capacity_x, capacity_y, target):
    print("Target amount of water can be obtained.")
else:
    print("Target amount of water cannot be obtained.")
