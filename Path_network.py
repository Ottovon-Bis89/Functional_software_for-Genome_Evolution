
from Path_node import Node
from networkx import DiGraph
from Genome_extremities_and_adjacencies import Extremities_and_adjacencies
from Biological_Constraints import  Constraints


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

    # Instantiate biological constraints and intergenic region generator for Genome B
    intergen = Constraints(genomeB)
    intergenic_regions = intergen.inter_generator(adjacencies_genomeB)

    # Retrieve the ordered and sorted adjacencies for Genome A
    adjacencies_genomeA = get_adjacencies.ordered_and_sorted_adjacencies(genomeA)

     # Generate operations with intergenic regions
    operations_with_intergenic = intergen.operations_intergenic_regions(intergenic_regions, adjacencies_genomeA, adjacencies_genomeB)

    # Calculate weights for the operations
    operation_weights_dict = intergen.intergenic_weight(intergenic_regions, operations_with_intergenic)
    inner_dict = list(operation_weights_dict.values())[0]
    W1 = inner_dict['W1']
    W2 = inner_dict['W2']
   
    

    # Check if the node has a circular chromosome to linearize (join_adjacency
    if node.join_adjacency != 0:

        operations = node.get_decircularization_operations(adjacencies_genomeB)

        for operation in operations:

            child_state = node.take_action(operation)[0]  
            check_hash_table = check_hash_key(child_state,
                                            hash_table)

            # Determine the type of operation based on join_adjacency presence
            operation_type = 'trp1' if node.join_adjacency in operation[0] else 'trp2'
            operation_weight = (0.5 if operation_type == 'trp1' else 1.5) * W1 * weights[1]
                
            
            if check_hash_table[0]:  

                child = check_hash_table[1]  
                node.children.append(child)  
                

            else:  
                child = Node(child_state)
                child.join_adjacency=0
                hash_key = hash(str(child.state))
                hash_table.update({hash_key: child})
                node.children.append(child)

                # Recursively build the hash table for the child node
                build_hash_table(child, hash_table, adjacencies_genomeB, weights, genomeB, genomeA)

            # Update the node's children, weights, and operations
            node.children_weights.append(operation_weight)  
            node.children_operations.append((operation, operation_type))

    # Process other legal operations if no circular chromosome linearization is required
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

                    # Define the dictionary to map op_type to (weight_multiplier, index) tuple
                    op_type_mapping = {
                        'fis': (W2, weights[4]),
                        'fus': (W2, weights[5]),
                        'u_trl': (W2, weights[3]),
                        'b_trl': (W2, weights[2]),
                        'inv': (W2, weights[0]),
                        'ins': (0.15 * W2, weights[5]),
                        'dup': (0.3 * W2, weights[4]),
                        'dele': (0.05 * W2, weights[3])
                    }

                    if op_type in op_type_mapping:
                        # Retrieve the operation's weight and corresponding values from the dictionary
                        operation_type = op_type
                        multiplier, weight = op_type_mapping[op_type]
                        op_weight = multiplier * weight

                        node.children_weights.append(op_weight)
                        node.children_operations.append((operation, operation_type))

                    else:
                        print('You have got a problem, the op type is: ', op_type)


             # Create new child node and check for circular chromosomes  
             # if the child is not already in the hash table  
            else:  
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

                    # Define a dictionary that maps each op_type to a tuple of (operation_type, op_weight_multiplier)
                    op_type_mapping = {
                        'fis':  (op_type, W2 * weights[4]),
                        'fus':  (op_type, W2 * weights[5]),
                        'u_trl': (op_type, W2 * weights[3]),
                        'inv':  (op_type, W2 * weights[0]),
                        'b_trl': (op_type, W2 * weights[2]),
                        'ins':  (op_type, 0.15 * W2 * weights[5]),
                        'dup':  (op_type, 0.3 * W2 * weights[4]),
                        'dele': (op_type, 0.05 * W2 * weights[3])
                    }

                    # Get operation_type and op_weight from the dictionary
                    if op_type in op_type_mapping:
                        operation_type, op_weight = op_type_mapping[op_type]
                    else:
                        print("There's a problem at the .find_op_type node function")
                        print('You have got a problem, the op_type is:', op_type)

                    # Append the calculated weight and operation to node attributes
                    node.children_weights.append(op_weight)
                    node.children_operations.append((operation, operation_type))

                    # Recursively build the hash table
                    build_hash_table(child, hash_table, adjacencies_genomeB, weights, genomeB, genomeA)


def check_hash_key(child_state, hash_table):
    """
    Checks if a given child state exists in the hash table by generating a hash key.

    Parameters:
    - child_state (any): The state of the child node to be checked.
    - hash_table (dict): The hash table containing previous states.

    Returns:
    - tuple: (bool, Node) - Whether the state exists in the hash table and the corresponding Node.
    """
    key = hash(str(child_state))
    return (True, hash_table[key]) if key in hash_table else (False, None)


def build_network(hash_table):
    """
    Builds a directed graph network based on a given hash table.

    This function takes a hash table as input and constructs a directed graph (DiGraph) network. It extracts unique nodes and their children from the hash table, creating nodes in the network for each unique value. Weighted edges are added to represent the relationships between nodes and their children.

    Parameters:
        hash_table (dict): A hash table containing nodes and their children with associated weights.

    Returns:
        networkx.DiGraph: A directed graph representing the relationships between nodes and their children.
    """
    
    network = DiGraph()
    nodes = list(hash_table.values())
    weighted_edges = []

    for node in nodes:
        network.add_node(node)
        for i, child in enumerate(node.children):
            weighted_edges.append((node, child, node.children_weights[i]))

    # Add weighted edges to the network
    network.add_weighted_edges_from(weighted_edges)

    return network


    




