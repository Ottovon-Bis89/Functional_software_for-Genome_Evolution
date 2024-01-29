
# import heapq
# import networkx as nx
# import matplotlib.pyplot as plt
# from GEN_NODE import Node
# from ForeignDNA import Foreign_DNA


# class Gen_net_work:

#     def __init__(self, source_genome, target_genome, mutations):
#         self.source_genome =tuple(map(tuple, source_genome))
#         self.target_genome = tuple(map(tuple, target_genome))
#         self.mutations = mutations
#         self.node = Node()
#         self.foreign =Foreign_DNA()

#     def transform_genome(self):
#         costs = {self.source_genome: 0}
#         queue = [(0, self.source_genome)]
#         previous = {self.source_genome: []}
#         print("hhhhhhhhhhhhhhhhhhh")
#         while queue:
#             current_genome = heapq.heappop(queue)
#             print(current_genome)
#             if current_genome == self.target_genome:
#                 paths = []
#                 for path in previous[current_genome]:
#                     new_path = path + [current_genome]
#                     paths.append(new_path)
#                     print(paths)
#                 return paths
                   
#             mutations.setdefault(current_genome, {})
#             for mutation, weight in mutations[current_genome].items():
               
#                 new_cost = costs[current_genome] + weight
#                 if mutation not in costs or new_cost < costs[mutation]:
#                     costs[mutation] = new_cost
                   
#                     heapq.heappush(queue, (new_cost, mutation))
#                     previous.setdefault(mutation, [])
#                     for path in previous[current_genome]:
#                         new_path = path + [current_genome]
#                         previous[mutation].append(new_path)
#                 elif new_cost == costs[mutation]:
#                     for path in previous[current_genome]:
#                         new_path = path + [current_genome]
#                         previous[mutation].append(new_path)

#         return []

#     def get_intermediates(self, path):
#         intermediates = []
#         for i in range(len(path) - 1):
#             intermediates.append(self.apply_mutation(path[i], path[i + 1]))
#             print("here:",intermediates)
#         return intermediates



#     def apply_mutation(self, current_genome, mutation):
#         # Implement your mutation logic here
#         if mutation == 'insertion':
#             # Apply insertion mutation
#             self.node.insertion()
#         elif mutation == 'deletion':
#             # Apply deletion mutation
#             self.node.deletion()
#         elif mutation == 'duplication':
#             # Apply duplication mutation
#             self.node.duplication()
#         elif mutation == 'foreign_DNA':
#             # Apply fDNA mutation
#             self.foreign.insert_foreign_dna()

#         # Return the resulting genome after mutation
#         return current_genome



#     def find_optimal_paths(self):
#         optimal_paths = self.transform_genome()
#         print(optimal_paths)
#         if optimal_paths:
#             min_cost = min(
#                 sum(self.mutations[genome1][genome2] for genome1, genome2 in zip(path, path[1:])) for path in optimal_paths
#             )
#             print("Optimal Transformation Paths:")
#             for i, path in enumerate(optimal_paths, start=1):
#                 if sum(self.mutations[genome1][genome2] for genome1, genome2 in zip(path, path[1:])) == min_cost:
#                     intermediates = self.get_intermediates(path)
#                     print(f"Path {i}:")
#                     for genome in path + intermediates:
#                         print(genome)
#                     print('---')
#         else:
#             print("No transformation paths exist.")

#         # Create a directed acyclic graph (DAG) for visualization
#         graph = nx.DiGraph()

#         # Add nodes and edges to the graph
#         for path in optimal_paths:
#             for i in range(len(path) - 1):
#                 graph.add_edge(path[i], path[i + 1], weight=self.mutations[path[i + 1]])

#         # Set layout for the graph
#         pos = nx.spring_layout(graph)

#         # Draw the nodes and edges of the graph
#         nx.draw_networkx_nodes(graph, pos)
#         nx.draw_networkx_edges(graph, pos)
#         nx.draw_networkx_labels(graph, pos)

#         # Draw edge weights
#         edge_labels = nx.get_edge_attributes(graph, 'weight')
#         nx.draw_networkx_edge_labels(graph, pos, edge_labels)

#         # Show the graph
#         plt.title("Optimal Transformation Paths (DAG)")
#         plt.axis('off')
#         plt.show()


# # Example usage
# source_genome = [['*6', '1', '*7', '2', '*8', '3', '*7', '4', '*9', '1', '*7', '5'],['*8', '4', '*9', '1', '*8', '1', '*8', '2', '*6', '8', '*9', '7', '*10', '6', '*7', '5', '*5', '1']]

# target_genome = [['*8', '1', '*6', '2', '*7', '3', '*9', '4', '*8', '5', '*8', '6', '*6', '7', '*6', '8'],['*9', '9', '*8', '10', '*8', '11', '*9']]

# mutations = {
#     'insertion': 0.15,
#     'deletion': 0.05,
#     'duplication': 0.30,
#     'foreign_DNA': 0.50
# }

# gen_network = Gen_net_work(source_genome, target_genome, mutations)
# gen_network.find_optimal_paths()


import heapq
from collections import defaultdict
from GEN_NODE import Node


class ParsimoniousPathsFinder:
    def __init__(self, mutations):
        self.mutations = mutations
        self.node = Node()  # Create an instance of the other class

    def find_parsimonious_paths(self, source_genome, target_genome):
        costs = {source_genome: 0}
        queue = [(0, source_genome)]
        previous = defaultdict(list)

        while queue:
            current_genome = heapq.heappop(queue)

            if current_genome == target_genome:
                paths = []
                for path in previous[current_genome]:
                    new_path = path + [current_genome]
                    paths.append(new_path)
                return paths

            for required_mutation, weight in self.mutations.items():
                new_cost = costs[current_genome] + weight
                mutated_genome = Node.do_mutation(current_genome, required_mutation)

                if mutated_genome not in costs or new_cost < costs[mutated_genome]:
                    costs[mutated_genome] = new_cost
                    heapq.heappush(queue, (new_cost, mutated_genome))
                    previous[mutated_genome] = [path + [mutated_genome] for path in previous[current_genome]]
                elif new_cost == costs[mutated_genome]:
                    previous[mutated_genome].extend([path + [mutated_genome] for path in previous[current_genome]])

        return []

    def get_intermediates(self, path):
        intermediates = []
        for i in range(len(path) - 1):
            intermediates.append(Node.do_mutation(path[i], path[i + 1]))
        return intermediates


source_genome = [['*6', '1', '*7', '2', '*8', '3', '*7', '4', '*9', '1', '*7', '5'],['*8', '4', '*9', '1', '*8', '1', '*8', '2', '*6', '8', '*9', '7', '*10', '6', '*7', '5', '*5', '1']]
target_genome = [['*8', '1', '*6', '2', '*7', '3', '*9', '4', '*8', '5', '*8', '6', '*6', '7', '*6', '8'],['*9', '9', '*8', '10', '*8', '11', '*9']]

mutations = {
    'insertion': 0.15,
    'deletion': 0.05,
    'duplication': 0.30,
    'foreign_DNA': 0.50
}

finder = ParsimoniousPathsFinder(mutations)
parsimonious_paths = finder.find_parsimonious_paths(source_genome, target_genome)

if parsimonious_paths:
    print("Parsimonious Paths:")
    for i, path in enumerate(parsimonious_paths, start=1):
        print(f"Path {i}:")
        intermediates = finder.get_intermediates(path)
        for genome in path + intermediates:
            print(genome)
        print("---")
else:
    print("No parsimonious paths exist.")
