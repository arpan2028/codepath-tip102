#Problem 1

# Problem 1: Can Rebook Flight
# Oh no! You're flight has been cancelled and you need to rebook. Given an adjacency matrix of today's flights flights where each flight is labeled 0 to n-1 and flights[i][j] = 1 indicates that there is an available flight from location i to location j, return True if there exists a path from your current location source to your final destination dest. Otherwise return False.

# Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.

# def can_rebook(flights, source, dest):
#     pass

#Solution 1 (dfs)
# def can_rebook(flights, source, dest):
#     n = len(flights)
#     visited = set()

#     def dfs(node):
#         if node == dest:
#             return True
#         visited.add(node)
#         for neighbor in range(n):
#             if flights[node][neighbor] == 1 and neighbor not in visited:
#                 if dfs(neighbor):
#                     return True
#         return False

#     return dfs(source)


# - Initialize an empty list of visited nodes
#     - Initialize an empty queue 
#     - Add the node we would like to start our traversal from to the queue 
#     - Add the node we would like to start our traversal from to visited
#     - While the queue is not empty:
#         - Remove an element from the queue and store it in a variable, `current`
#         - Loop through each of the current node's neighbors:
#             - If the neighbor has not yet been visited:
#                 - Add the neighbor to the queue
#                 - Add the neighbor to the list of visited nodes
#     - Return the list of visited nodes



# Problem 2: Can Rebook Flight II
# If you solved the above problem can_rebook() using Breadth First Search, try solving it using Depth First Search. If you solved it using Depth First Search, solve it using Breadth First Search.

# Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.


#Solution 2 (bfs)

# from collections import deque

# def can_rebook(flights, source, dest):
#     n = len(flights)
#     visited = set()
#     q = deque([source])

#     while q:
#         city = q.popleft()

#         if city == dest:
#             return True
        
#         visited.add(city)

#         for neighbor in range(n):
#             if flights[city][neighbor] == 1 and neighbor not in visited:
#                 q.append(neighbor)

#     return False





# flights1 = [
#     [0, 1, 0], # Flight 0
#     [0, 0, 1], # Flight 1
#     [0, 0, 0]  # Flight 2
# ]

# flights2 = [
#     [0, 1, 0, 1, 0],
#     [0, 0, 0, 1, 0],
#     [0, 0, 0, 0, 1],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0]
# ]

# print(can_rebook(flights1, 0, 2))
# print(can_rebook(flights2, 0, 2)) 



# Problem 3: Number of Flights
# You are a travel planner and have an adjacency matrix flights with n airports labeled 0 to n-1 where flights[i][j] = 1 indicates CodePath Airlines offers a flight from airport i to airport j. You are planning a trip for a client and want to know the minimum number of flights (edges) it will take to travel from airport start to their final destination airport destination on CodePath Airlines.

# Return the minimum number of flights needed to travel from airport i to airport j. If it is not possible to fly from airport i to airport j, return -1.

# def counting_flights(flights, i, j):
#     pass


# from collections import deque

# def counting_flights(flights, start, destination):
#     n = len(flights)
#     visited = set()
#     q = deque()
#     q.append((start, 0))  # (current_city, flights_taken_so_far)

#     while q:
#         city, steps = q.popleft()

#         if city == destination:
#             return steps

#         visited.add(city)

#         for neighbor in range(n):
#             if flights[city][neighbor] == 1 and neighbor not in visited:
#                 q.append((neighbor, steps + 1))

#     return -1  # destination not reachable

# # Example usage
# flights = [
#     [0, 1, 1, 0, 0], # Airport 0
#     [0, 0, 1, 0, 0], # Airport 1
#     [0, 0, 0, 1, 0], # Airport 2
#     [0, 0, 0, 0, 1], # Airport 3
#     [0, 0, 0, 0, 0]  # Airport 4
# ]

# print(counting_flights(flights, 0, 2))  
# print(counting_flights(flights, 0, 4))
# print(counting_flights(flights, 4, 0))