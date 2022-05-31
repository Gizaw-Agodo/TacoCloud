import numpy as np

landscape = np.random.randint(1, high=9, size=(10,10))
print(landscape)
start_state = (3, 6)  
current_state = start_state
count = 1
ascending = True
print ( landscape.shape)


# while ascending:
#     print("\nStep #", count)
#     print("Current state coordinates: ", current_state)
#     print("Current state value: ", landscape[current_state[0]][current_state[1]])
#     count += 1
#     # ascending, current_state = hill_climb(current_state, landscape)

# print("\nStep #", count)
# print("Optimization objective reached.")
# print("Final state coordinates: ", current_state)
# print("Final state value: ", landscape[current_state[0]][current_state[1]])