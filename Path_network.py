
from Path_node import Node
from networkx import DiGraph
import networkx as nx
import matplotlib.pyplot as plt
from Genome_extremities_and_adjacencies import Extremities_and_adjacencies
from Biological_Constraints import  Constraints
from networkx.drawing.nx_agraph import graphviz_layout


get_adjacencies = Extremities_and_adjacencies()






def build_hash_table(current_node, hash_table, adjacencies_genomeB, weights, genomeB, genomeA):
    '''
    Builds a hash table representing the state space of "Genolve".
    The algorithm explores possible operations on a given node and recursively builds
    the state space tree while updating the hash table to avoid redundant computations.
    
    @param current_node The current node in the state space tree.
    @param hash_table The hash table used to store previously visited states.
    @param adjacencies_genomeB The adjacency information for Genome B.
    @param weights The weights used to calculate operation weights.

    '''
    node = current_node
    intergen = Constraints(genomeB)
    intergenic_regions = intergen.inter_generator(adjacencies_genomeB)
    adjacencies_genomeA = get_adjacencies.ordered_and_sorted_adjacencies(genomeA)
    operations_with_intergenic = intergen.operations_intergenic_regions(intergenic_regions, adjacencies_genomeA, adjacencies_genomeB)
    operation_weights_dict = intergen.intergenic_weight(intergenic_regions, operations_with_intergenic)
    inner_dict = list(operation_weights_dict.values())[0]
    W1 = inner_dict['W1']
    W2 = inner_dict['W2']
   
    


    if node.join_adjacency != 0:

        operations = node.get_decircularization_operations(adjacencies_genomeB)

        for operation in operations:

            child_state = node.take_action(operation)[0]  
            check_hash_table = check_hash_key(child_state,
                                            hash_table) 


            if node.join_adjacency in operation[0]:
                operation_type = 'trp1'
                operation_weight = 0.5 * W1 * weights[1]
                
                

            else:
                operation_type = 'trp2'
                operation_weight = 1.5 * W1 * weights[1]
                

            if check_hash_table[0]:  

                child = check_hash_table[1]  
                node.children.append(child)  
                node.children_weights.append(operation_weight)  
                node.children_operations.append((operation, operation_type))

            else:  
                child = Node(child_state)
                child.join_adjacency=0
                hash_key = hash(str(child.state))
                hash_table.update({hash_key: child})
                node.children.append(child)
                node.children_weights.append(operation_weight)
                node.children_operations.append((operation, operation_type))

                build_hash_table(child, hash_table, adjacencies_genomeB, weights, genomeB, genomeA)


    else:  

        operations = node.get_legal_operations(adjacencies_genomeB)

        for operation in operations:

            operation_result = node.take_action(operation)
            child_state = operation_result[0]
            op_type = operation_result[1]
            

            check_hash_table = check_hash_key(child_state, hash_table)

            if check_hash_table[0]:
                child = check_hash_table[1]
                node.children.append(child)

                child.find_chromosomes(child.state)

                if child.circular_chromosomes:
                    node.children_weights.append(0.5 * W1 * weights[1])
                    node.children_operations.append((operation, 'trp0'))

                    if isinstance(operation[-1][0], tuple) and isinstance(operation[-1][1], tuple):

                        for adjacency in operation[-1]:
                            if adjacency in child.circular_chromosomes[0]:
                                child.join_adjacency = adjacency


                    elif isinstance(operation[-1][0], tuple):
                        if operation[-1][0] in child.circular_chromosomes[0]:
                            child.join_adjacency = operation[-1][0]
                        else:
                            print('error')

                    elif isinstance(operation[-1][1], tuple):
                        if operation[-1][1] in child.circular_chromosomes[0]:
                            child.join_adjacency = operation[-1][1]
                        else:
                            print('error')

                    else:

                        if operation[-1] in child.circular_chromosomes[0]:

                            child.join_adjacency = operation[-1]
                        else:
                            print('error')

                else:
                    child.join_adjacency = 0
                    if op_type == 'fis':
                        operation_type = op_type
                        op_weight = 1 * W2 * weights[4]
                        

                    elif op_type == 'fus':
                        operation_type = op_type
                        op_weight = 1 * W2 * weights[5]
                       
                        
                    elif op_type == 'u_trl':
                        operation_type = op_type
                        op_weight = 1 * W2 * weights[3]
                        
                        

                    elif op_type == 'b_trl':
                        operation_type = op_type
                        op_weight = 1 * W2 * weights[2]
                        
                        

                    elif op_type == 'inv':
                        operation_type = op_type
                        op_weight = 1 * W2 * weights[0]
                        
                        
                    
                    elif op_type == 'ins':
                        operation_type = op_type
                        op_weight = 0.15 * W2 * weights[5]
                        
                        
                    
                    elif op_type == 'dup':
                        operation_type = op_type
                        op_weight = 0.3 * W2 * weights[4]
                        
                        
                    elif op_type == 'dele':
                        operation_type = op_type
                        op_weight = 0.05 * W2 * weights[3]
                        
                    
                        
                    

                    else:
                        print('You have got a problem, the op type is: ', op_type, '')

                    node.children_weights.append(op_weight)
                    node.children_operations.append((operation, operation_type))


            else:  # if the child is not in the hash table
                child = Node(child_state)
                child.find_chromosomes(child.state)

                if child.circular_chromosomes:  # if a circular chromosome has been created:

                    if isinstance(operation[-1][0], tuple) and isinstance(operation[-1][1], tuple):

                        for adjacency in operation[-1]:
                            if adjacency in child.circular_chromosomes[0]:
                                child.join_adjacency = adjacency


                    elif isinstance(operation[-1][0], tuple):
                        if operation[-1][0] in child.circular_chromosomes[0]:
                            child.join_adjacency = operation[-1][0]
                        else:
                            print('error')

                    elif isinstance(operation[-1][1], tuple):
                        if operation[-1][1] in child.circular_chromosomes[0]:
                            child.join_adjacency = operation[-1][1]
                        else:
                            print('error')

                    else:
                        if operation[-1] in child.circular_chromosomes[0]:
                            #child.join_adjacency = operation[-1][0]
                            child.join_adjacency = operation[-1]
                        else:
                            print('error')

                    hash_key = hash(str(child.state))
                    hash_table.update({hash_key: child})
                    node.children.append(child)
                    node.children_operations.append((operation, 'trp0'))
                    node.children_weights.append(0.5 * weights[1])
                    

                    build_hash_table(child, hash_table, adjacencies_genomeB, weights, genomeB, genomeA)


                else:
                    child.join_adjacency = 0
                    hash_key = hash(str(child.state))
                    hash_table.update({hash_key: child})
                    node.children.append(child)

                    if op_type == 'fis':
                        operation_type = op_type
                        op_weight = 1 * W2 * weights[4]
                        
                      

                    elif op_type == 'fus':
                        operation_type = op_type
                        op_weight = 1 * W2 * weights[5]
                        

                    elif op_type == 'u_trl':
                        operation_type = op_type
                        op_weight = 1 * W2 * weights[3]
                        

                    elif op_type == 'inv':
                        operation_type = op_type
                        op_weight = 1 * W2 * weights[0]
                        

                    elif op_type == 'b_trl':
                        operation_type = op_type
                        op_weight = 1 * W2 * weights[2]
                        
                        
                    elif op_type == 'ins':
                        operation_type = op_type
                        op_weight = 0.15 * W2 * weights[5]
                        
                       
                        
                    elif op_type == 'dup':
                        operation_type = op_type
                        op_weight = 0.3 * W2 * weights[4]
                        
                        
                    elif op_type == 'dele':
                        operation_type = op_type
                        op_weight = 0.05 * W2 * weights[3]
                        
                    
                       
                        
                        
                    else:
                        print("There's a problem at the .find_op_type node function")
                        print('You have got a problem, the op_type is: ', op_type, '')

                    node.children_weights.append(op_weight)
                    node.children_operations.append((operation, operation_type))

                    build_hash_table(child, hash_table, adjacencies_genomeB, weights, genomeB, genomeA)

def check_hash_key(child_state, hash_table):
    """
    Checks if a given hash key for a child state exists in the provided hash table.

    Parameters:
    - child_state (any): The child state for which the hash key needs to be checked.
    - hash_table (dict): The hash table to check for the existence of the hash key.

    Returns:
    - tuple: A tuple containing a boolean value indicating whether the key exists in the hash table
            and the corresponding value if the key exists, otherwise None.

    Example:
    >>> state = [1, 2, 3]
    >>> table = {123: 'value'}
    >>> check_hash_key(state, table)
    (True, 'value')
    """
    key = hash(str(child_state))
    if key in hash_table.keys():
        return True, hash_table.get(key)
    return False, None


# def build_network(hash_table):
#     """
#     Builds a directed graph network based on a given hash table.

#     This function takes a hash table as input and constructs a directed graph (DiGraph) network. It extracts unique nodes and their children from the hash table, creating nodes in the network for each unique value. Weighted edges are added to represent the relationships between nodes and their children.

#     Parameters:
#         hash_table (dict): A hash table containing nodes and their children with associated weights.

#     Returns:
#         networkx.DiGraph: A directed graph representing the relationships between nodes and their children.
#     """

#     network = DiGraph()
#     nodes = []
#     weighted_edges = []
#     weights = []

#     list_of_values = hash_table.values()

#     for value in list_of_values:
#         if value not in nodes:
#             nodes.append(value)
#     for node in nodes:
#         number_of_children = len(node.children)
#         network.add_node(node)

#         for i in range(0, number_of_children):
#             weighted_edges.append((node, node.children[i], node.children_weights[i]))
#             weights.append(node.children_weights[i])

#     network.add_weighted_edges_from(weighted_edges)

#     return network





def build_network(hash_table):
    """
    Builds a directed acyclic graph (DAG) based on a given hash table.

    This function takes a hash table as input and constructs a directed acyclic graph (DiGraph). It extracts unique nodes and their children from the hash table, creating nodes in the network for each unique value. Weighted edges are added to represent the relationships between nodes and their children.

    Parameters:
        hash_table (dict): A hash table containing nodes and their children with associated weights.

    Returns:
        networkx.DiGraph: A directed acyclic graph representing the relationships between nodes and their children.
    """
    network = DiGraph()
    list_of_values = hash_table.values()

    for node in list_of_values:
        network.add_node(str(node))  # Convert node to string
        for i, child in enumerate(node.children):
            network.add_edge(str(node), str(child), weight=node.children_weights[i])

    # Check if the graph is a DAG
    if not nx.is_directed_acyclic_graph(network):
        raise ValueError("The constructed network is not a DAG.")

    return network

def visualize_network(network, filename=None):
    """
    Visualizes the network using matplotlib and saves it to a file if a filename is provided.

    Parameters:
        network (networkx.DiGraph): The directed graph network to visualize.
        filename (str, optional): The filename to save the visualization to. Defaults to None.
    """
    #pos = nx.spring_layout(network)
    network.add_edges_from([(i, i + 1) for i in range(100)] + [(i, i + 2) for i in range(98)])

    # Get the first 100 nodes (or fewer if the graph has less than 100 nodes)
    nodes_to_include = list(network.nodes())[:100]

    # Create a subgraph with only the specified nodes
    H = network.subgraph(nodes_to_include).copy()
    pos = graphviz_layout(H, prog='dot')
    edge_labels = {(u, v): d['weight'] for u, v, d in network.edges(data=True)}
    plt.figure(figsize=(12, 12))
    #nx.draw(network, pos, with_labels=False, node_size=30, node_color='lightblue', font_size=10, font_weight='bold')
    nx.draw(network, pos, with_labels=False, node_size=50, node_color='lightblue', font_size=10, font_weight='bold', arrows=True)
    nx.draw_networkx_edge_labels(network, pos, edge_labels=edge_labels)
    if filename:
        plt.savefig(filename)
    plt.show()

def save_network_to_file(network, filename):
    """
    Saves the network to a file in GML or GraphML format based on the file extension.

    Parameters:
        network (networkx.DiGraph): The directed graph network to save.
        filename (str): The filename to save the network to.
    """
    if filename.endswith('.gml'):
        nx.write_gml(network, filename)
    elif filename.endswith('.graphml'):
        nx.write_graphml(network, filename)
    else:
        raise ValueError("Unsupported file format. Use .gml or .graphml.")

# Example usage:
# hash_table = {}  # This should be populated by build_hash_table function
# network = build_network(hash_table)
# visualize_network(network, "network_visualization.png")
# save_network_to_file(network, "network.gml")
