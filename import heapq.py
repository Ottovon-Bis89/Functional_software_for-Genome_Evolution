import heapq
import networkx as nx
import matplotlib.pyplot as plt


def transform_genome(start_genome, end_genome, mutations):
    # Create a dictionary to store the cumulative costs of mutations for each genome
    costs = {start_genome: 0}

    # Create a priority queue to store the genomes and their cumulative costs
    queue = [(0, start_genome)]

    # Create a dictionary to store the previous genomes in the transformation paths
    previous = {start_genome: []}

    while queue:
        current_cost, current_genome = heapq.heappop(queue)

        # Check if we reached the end genome
        if current_genome == end_genome:
            # Generate all transformation paths with the optimal cumulative cost
            paths = []
            for path in previous[current_genome]:
                new_path = path + [current_genome]
                paths.append(new_path)
            return paths

        for mutation, weight in mutations[current_genome].items():
            new_cost = costs[current_genome] + weight
            if mutation not in costs or new_cost < costs[mutation]:
                costs[mutation] = new_cost
                heapq.heappush(queue, (new_cost, mutation))
                previous.setdefault(mutation, [])
                for path in previous[current_genome]:
                    new_path = path + [current_genome]
                    previous[mutation].append(new_path)
            # If there is an alternative path with the same cost, add it to previous as well
            elif new_cost == costs[mutation]:
                for path in previous[current_genome]:
                    new_path = path + [current_genome]
                    previous[mutation].append(new_path)

    # If there is no path from start to end genome
    return []


def get_intermediates(path):
    intermediates = []
    for i in range(len(path) - 1):
        intermediates.append(apply_mutation(path[i], path[i + 1]))
    return intermediates


def apply_mutation(genome, mutation):
    # Implement your mutation logic here
    if mutation == 'insertion':
        # Apply insertion mutation
        pass
    elif mutation == 'deletion':
        # Apply deletion mutation
        pass
    elif mutation == 'duplication':
        # Apply duplication mutation
        pass
    elif mutation == 'fDNA':
        # Apply fDNA mutation
        pass

    # Return the resulting genome after mutation
    return genome


# Example usage
source_genome = [['*6', '1', '*7', '2', '*8', '3', '*7', '4', '*9', '1', '*7', '5'],
                 ['*8', '4', '*9', '1', '*8', '1', '*8', '2', '*6', '8', '*9', '7', '*10', '6', '*7', '5', '*5', '1']]

target_genome = [['*8', '1', '*6', '2', '*7', '3', '*9', '4', '*8', '5', '*8', '6', '*6', '7', '*6', '8'],
                 ['*9', '9', '*8', '10', '*8', '11', "*9"]]

# Convert source and target genomes to strings for dictionary access
start_genome = str(source_genome)
end_genome = str(target_genome)

mutations = {
    'insertion': 0.15,
    'deletion': 0.05,
    'duplication': 0.30,
    'fDNA': 0.50
}

optimal_paths = transform_genome(start_genome, end_genome, mutations)
if optimal_paths:
    # Find the minimum cumulative cost among all paths
    min_cost = min(sum(mutations[genome1][genome2] for genome1, genome2 in zip(path, path[1:])) for path in optimal_paths)

    print("Optimal Transformation Paths:")
    for i, path in enumerate(optimal_paths, start=1):
        # Only print the paths with the minimum cumulative cost
        if sum(mutations[genome1][genome2] for genome1, genome2 in zip(path, path[1:])) == min_cost:
            intermediates = get_intermediates(path)
            print(f"Path {i}:")
            for genome in path + intermediates:
                print(genome)
            print('---')
else:
    print("No transformation paths exist.")


    # Create a directed acyclic graph (DAG) for visualization
    graph = nx.DiGraph()

    # Add nodes to the graph
    for path in optimal_paths:
        for i in range(len(path) - 1):
            graph.add_edge(path[i], path[i + 1], weight=mutations[path[i + 1]])

    # Set layout for the graph
    pos = nx.spring_layout(graph)

    # Draw the nodes and edges of the graph
    nx.draw_networkx_nodes(graph, pos)
    nx.draw_networkx_edges(graph, pos)
    nx.draw_networkx_labels(graph, pos)

    # Draw edge weights
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels)

    # Show the graph
    plt.title("Optimal Transformation Paths (DAG)")
    plt.axis('off')
    plt.show()
