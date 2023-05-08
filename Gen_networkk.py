import heapq
import networkx as nx
import matplotlib.pyplot as plt
import math


# # Define the nodes of the graph
# nodes = ["ins", "del", "dup", "f_dna"]

# # Define the edges of the graph
# edges = {
#     "ins": {"del": 0.15, "dup": 0.45, "f_dna": 0.50},
#     "del": {"ins": 0.05, "dup": 0.35, "f_dna": 0.50},
#     "dup": {"ins": 0.30, "del": 0.35, "f_dna": 0.50},
#     "f_dna": {"ins": 0.50, "del": 0.50, "dup": 0.50},
# }

# # Define a function to run Dijkstra's algorithm
# def dijkstra(start, end):
#     # Initialize the cost and path dictionaries
#     cost = {node: float("inf") for node in nodes}
#     cost[start] = 0
#     path = {node: [] for node in nodes}

#     # Initialize the heap with the starting node and its cost
#     heap = [(0, start)]

#     while heap:
#         # Pop the node with the smallest cost
#         (current_cost, current_node) = heapq.heappop(heap)

#         # If we have already found a shorter path to this node, skip it
#         if current_cost > cost[current_node]:
#             continue

#         # Check all the neighbors of the current node
#         for neighbor, weight in edges[current_node].items():
#             # Calculate the cost of the path to the neighbor
#             neighbor_cost = current_cost + weight

#             # If we have found a shorter path to the neighbor, update its cost and path
#             if neighbor_cost < cost[neighbor]:
#                 cost[neighbor] = neighbor_cost
#                 path[neighbor] = path[current_node] + [current_node]

#                 # Add the neighbor to the heap
#                 heapq.heappush(heap, (neighbor_cost, neighbor))

#     # Return the shortest path to the end node
#     return path[end] + [end]

# # Find the shortest path between all pairs of nodes
# for start in nodes:
#     for end in nodes:
#         if start != end:
#             path = dijkstra(start, end)
#             print(f"{start} -> {end}: {' -> '.join(path)}")


# # Define the mutations and their weights/costs
# mutations = {
#     'ins': 0.15,
#     'del': 0.05,
#     'dup': 0.30,
#     'f_dna': 0.50
# }

# # Create a directed graph using NetworkX
# G = nx.DiGraph()

# # Add nodes to the graph
# for mutation in mutations:
#     G.add_node(mutation)


# # Calculate the shortest path using Dijkstra's algorithm
# shortest_path = nx.dijkstra_path(G, source='ins', target='f_dna')

# # Print the shortest path
# print('Shortest path:', shortest_path)

# # Draw the graph
# nx.draw(G, with_labels=True)
# plt.show()

# path.reverse()
# print(f'The shortest path from {start} to {nodes} is {path}')








# # Define the edges and weights of the graph
# edges = {
#     'ins': [('ins', 0.15), ('del', 0.05), ('dup', 0.30), ('f_dna', 0.50)],
#     'del': [('ins', 0.15), ('del', 0.05), ('dup', 0.30), ('f_dna', 0.50)],
#     'dup': [('ins', 0.15), ('del', 0.05), ('dup', 0.30), ('f_dna', 0.50)],
#     'f_dna': [('ins', 0.15), ('del', 0.05), ('dup', 0.30), ('f_dna', 0.50)],
# }

# # Define the start node
# start = 'ins'

# # Define a priority queue to keep track of the nodes to visit
# queue = [(0, start)]

# # Define a dictionary to keep track of the distances from the start node
# distances = {node: math.inf for node in edges}
# distances[start] = 0

# # Define a dictionary to keep track of the previous node in the shortest path
# previous = {node: None for node in edges}

# # Define a set to keep track of the nodes that have already been visited
# visited = set()

# # Implement the Dijkstra algorithm
# while queue:
#     (cost, current) = heapq.heappop(queue)
    
#     if current in visited:
#         continue
        
#     visited.add(current)
    
#     for neighbor, weight in edges[current]:
#         if neighbor in visited:
#             continue
            
#         new_cost = cost + weight
        
#         if new_cost < distances[neighbor]:
#             distances[neighbor] = new_cost
#             previous[neighbor] = current
#             heapq.heappush(queue, (new_cost, neighbor))

# # Print the distances from the start node
# print(distances)

# # Print the shortest path from the start node to each node
# for node in edges:
#     path = [node]
#     while previous[node]:
#         node = previous[node]
#         path.append(node)
        
        
        
# # Define the mutations and their weights/costs
# mutations = {
#     'ins': 0.15,
#     'del': 0.05,
#     'dup': 0.30,
#     'f_dna': 0.50
# }

# # Create a directed graph using NetworkX
# G = nx.DiGraph()

# # Add nodes to the graph
# for mutation in mutations:
#     G.add_node(mutation)

# # Add edges to the graph and set the weights/costs
# for mutation1, cost1 in mutations.items():
#     for mutation2, cost2 in mutations.items():
#         if mutation1 != mutation2:
#             G.add_edge(mutation1, mutation2, weight=cost1 + cost2)

# # Calculate the shortest path using Dijkstra's algorithm
# shortest_path = nx.dijkstra_path(G, source='ins', target='f_dna')

# # Print the shortest path
# print('Shortest path:', shortest_path)

# # Draw the graph
# nx.draw(G, with_labels=True)
# plt.show()

# path.reverse()
# print(f'The shortest path from {start} to {node} is {path}')






# Define the nodes of the graph
nodes = ["ins", "del", "dup", "f_dna"]

# Define the edges of the graph
edges = {
    "ins": {"del": 0.15, "dup": 0.45, "f_dna": 0.50},
    "del": {"ins": 0.05, "dup": 0.35, "f_dna": 0.50},
    "dup": {"ins": 0.30, "del": 0.35, "f_dna": 0.50},
    "f_dna": {"ins": 0.50, "del": 0.50, "dup": 0.50},
}

# Define a function to run Dijkstra's algorithm
def dijkstra(start, end):
    # Initialize the cost and path dictionaries
    cost = {node: float("inf") for node in nodes}
    cost[start] = 0
    path = {node: [] for node in nodes}

    # Initialize the heap with the starting node and its cost
    heap = [(0, start)]

    while heap:
        # Pop the node with the smallest cost
        (current_cost, current_node) = heapq.heappop(heap)

        # If we have already found a shorter path to this node, skip it
        if current_cost > cost[current_node]:
            continue

        # Check all the neighbors of the current node
        for neighbor, weight in edges[current_node].items():
            # Calculate the cost of the path to the neighbor
            neighbor_cost = current_cost + weight

            # If we have found a shorter path to the neighbor, update its cost and path
            if neighbor_cost < cost[neighbor]:
                cost[neighbor] = neighbor_cost
                path[neighbor] = path[current_node] + [current_node]

                # Add the neighbor to the heap
                heapq.heappush(heap, (neighbor_cost, neighbor))

    # Perform a topological sorting to get the nodes in a directed acyclic order
    visited = set()
    order = []
    for node in nodes:
        if node not in visited:
            dfs(node, visited, order)
    order.reverse()

    # Return the shortest path to the end node in the DAG order
    dag_path = [start]
    for node in order:
        if node in path[end]:
            dag_path.append(node)
    dag_path.append(end)
    return dag_path

# Define a function to perform a depth-first search (DFS) for topological sorting
def dfs(node, visited, order):
    visited.add(node)
    for neighbor in edges[node]:
        if neighbor not in visited:
            dfs(neighbor, visited, order)
    order.append(node)

# Find the shortest path between all pairs of nodes
G = nx.DiGraph()
for start in nodes:
    for end in nodes:
        if start != end:
            path = dijkstra(start, end)
            # G.add_path(path)
            edges_list = [(path[i], path[i+1]) for i in range(len(path)-1)]
            G.add_edges_from(edges_list)
            print(f"{start} -> {end}: {' -> '.join(path)}")
            print(f'The shortest path from {start} to {end} is {path}')                                                                                   


# Draw the graph
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=1000)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
plt.axis("off")
plt.show()

