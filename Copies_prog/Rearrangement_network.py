from Rearrangement_node import Node
from networkx import DiGraph


def build_hash_table(current_node, hash_table, adjacencies_genomeB, weights):

    """
    The function recursively builds a hash table of intermediary genomes, where each node represents an intermediary genome and is
    indexed by a hash of its string representation.It takes the node, representing the current intermediary genome,
    the hash table, representing hash table to add nodes to, adjacencies_genomeB, representing the list of adjacencies in the input genome,
    and weights which represents a list of weights corresponding to different types of genome rearrangements
    """

    node = current_node

    # if the previous operation was a cicularization do:

    if node.join_adjacency != 0:

         # Get list of possible reinsertion operations
        operations = node.get_reinsertion_operations(adjacencies_genomeB)

    # Check each operation
        for operation in operations:

            child_state = node.take_action(operation)[0]  # Perform operation to get child state
            check_hash_table = check_hash_key(child_state,hash_table)   # Check if intermediate node already exists in hash table

            # Determine operation type and weight
            if node.join_adjacency in operation[0]:
                operation_type = 'trp1'
                operation_weight = 0.5 * weights[1]

            # else it is a trp2 type operation
            else:
                operation_type = 'trp2'
                operation_weight = 1.5 * weights[1]

            if check_hash_table[0]: # If intermediate node exists in hash table

                child = check_hash_table[1]  # let the child = (point to) the intermediate node in the hash table
                node.children.append(child)  # add the child to the list of children of the current node
                node.children_weights.append(operation_weight)  # add the weight of the operation that generated the child to the list of weights
                node.children_operations.append((operation, operation_type))  # add the operation and its type to the list of operations that generated the node children


            else:  # if the intermediate does not exist in the hash table
                child = Node(child_state)  # create a node for the state
                child.join_adjacency = 0
                hash_key = hash(str(child.state))
                hash_table.update({hash_key: child})  # add child node to hash table
                node.children.append(child)
                node.children_weights.append(operation_weight)  # Append the operation weight to the children_weights list of the node
                node.children_operations.append((operation, operation_type))  # Append the operation and operation_type tuple to the children_operations list of the node

            # Call the build_hash_table function to recursively build the hash table for the child node
                build_hash_table(child, hash_table, adjacencies_genomeB, weights)



    else:  # if the previous operation was not a circularization, i.e. the current intermediary genome consists of
        # only linear chromosomes

        # Get legal operations to perform on the current node's genome
        operations = node.get_legal_operations(adjacencies_genomeB)

         # Iterate over each legal operation
        for operation in operations:


        # Get the resulting state and type of operation
            operation_result = node.take_action(operation)
            child_state = operation_result[0]
            op_type = operation_result[1]

        # Check if the child node with the resulting state already exists in the hash table
            check_hash_table = check_hash_key(child_state, hash_table)

            if check_hash_table[0]:  # if the child exists in the hash table:
                child = check_hash_table[1]
                node.children.append(child)

             # If the child node has at least one circular chromosome, set its join adjacency to the appropriate adjacency
                child.find_chromosomes(child.state)

                if len(child.circular_chromosomes) != 0:  # if a circularization occurred
                    node.children_weights.append(0.5 * weights[1])
                    node.children_operations.append((operation, 'trp0'))

                    if type(operation[-1][0]) is tuple and type(operation[-1][1]) is tuple:  # Check if both operation[-1][0] and operation[-1][1] are tuples

                        for adjacency in operation[-1]:  # Iterate over each adjacency in operation[-1]
                            if adjacency in child.circular_chromosomes[0]:  # Check if the adjacency is present in child.circular_chromosomes[0]
                                child.join_adjacency = adjacency   #Set child.join_adjacency to the found adjacency



                    elif type(operation[-1][0]) is tuple:  # Check if only operation[-1][0] is a tuple
                        if operation[-1][0] in child.circular_chromosomes[0]:  # Check if operation[-1][0] is present in child.circular_chromosomes[0]
                            child.join_adjacency = operation[-1][0]   # Set child.join_adjacency to operation[-1][0]
                        else:
                            print('error')

                    elif type(operation[-1][1]) is tuple:    # Check if only operation[-1][1] is a tuple
                        if operation[-1][1] in child.circular_chromosomes[0]:   # Check if operation[-1][1] is present in child.circular_chromosomes[0]
                            child.join_adjacency = operation[-1][1]  # Set child.join_adjacency to operation[-1][1]
                        else:
                            print('error')

                    else:

                        if operation[-1] in child.circular_chromosomes[0]:  # Check if operation[-1] is present in child.circular_chromosomes[0]

                            child.join_adjacency = operation[-1]  # Set child.join_adjacency to operation[-1]
                        else:
                            print('error')



                else:
                    child.join_adjacency = 0
                
                 # Check if the child node resulting from the operation exists in the hash table or not.
                    # Set the operation type and weight based on the type of operation performed.
                    if op_type == 'fis':
                        operation_type = op_type
                        op_weight = 1 * weights[4]

                    elif op_type == 'fus':
                        operation_type = op_type
                        op_weight = 1 * weights[5]

                    elif op_type == 'u_trl':
                        operation_type = op_type
                        op_weight = 1 * weights[3]

                    elif op_type == 'b_trl':
                        operation_type = op_type
                        op_weight = 1 * weights[2]

                    elif op_type == 'inv':
                        operation_type = op_type
                        op_weight = 1 * weights[0]

                    else:
                        print('You have got a problem, the op type is: ', op_type, '   #2')

                 # Add the operation type and weight to the current node's children list.
                    node.children_weights.append(op_weight)
                    node.children_operations.append((operation, operation_type))


            else:  # if the child is not in the hash table
                child = Node(child_state)
                child.find_chromosomes(child.state)

                if len(child.circular_chromosomes) != 0:  # if a circular chromosome has been created:


                # Find the adjacency in the circular chromosome that is involved in the circularization operation.
                    if type(operation[-1][0]) is tuple and type(operation[-1][1]) is tuple: # Check if both operation[-1][0] and operation[-1][1] are tuples

                        for adjacency in operation[-1]:  
                            if adjacency in child.circular_chromosomes[0]:
                                child.join_adjacency = adjacency


                    elif type(operation[-1][0]) is tuple:  # Check if operation[-1][0] is a tuple
                        if operation[-1][0] in child.circular_chromosomes[0]:  # Check if operation[-1][0] is present in child.circular_chromosomes[0]
                            child.join_adjacency = operation[-1][0]  # Set child.join_adjacency to operation[-1][0]
                        else:
                            print('error')

                    elif type(operation[-1][1]) is tuple:
                        if operation[-1][1] in child.circular_chromosomes[0]:
                            child.join_adjacency = operation[-1][1]
                        else:
                            print('error')

                    else:
                        # if operation[-1][0] in child.circular_chromosomes[0]:
                        if operation[-1] in child.circular_chromosomes[0]:
                            # child.join_adjacency = operation[-1][0]
                            child.join_adjacency = operation[-1]
                        else:
                            print('error')


                    # Update the hash table, add the new child node to the current node's children list,
                     # and add the operation type and weight to the current node's children list.
                    hash_key = hash(str(child.state))
                    hash_table.update({hash_key: child})
                    node.children.append(child)
                    node.children_operations.append((operation, 'trp0'))
                    node.children_weights.append(0.5 * weights[1])

                # Recursively build the hash table for the new child node.
                    build_hash_table(child, hash_table, adjacencies_genomeB, weights)



                else:   # If no circular chromosome has been created
                    child.join_adjacency = 0
                # Add the child to the hash table and update the node
                    hash_key = hash(str(child.state))
                    hash_table.update({hash_key: child})
                    node.children.append(child)

                 # Compute the operation weight based on the operation type
                    if op_type == 'fis':
                        operation_type = op_type
                        op_weight = 1 * weights[4]

                    elif op_type == 'fus':
                        operation_type = op_type
                        op_weight = 1 * weights[5]

                    elif op_type == 'u_trl':
                        operation_type = op_type
                        op_weight = 1 * weights[3]

                    elif op_type == 'inv':
                        operation_type = op_type
                        op_weight = 1 * weights[0]

                    elif op_type == 'b_trl':
                        operation_type = op_type
                        op_weight = 1 * weights[2]
                    else:
                        print("There's a problem at the find op_type node function")
                        print('You have got a problem, the op type is: ', op_type, ' #4')

                    # Update the node and build the hash table
                    node.children_weights.append(op_weight)
                    node.children_operations.append((operation, operation_type))

                    build_hash_table(child, hash_table, adjacencies_genomeB, weights)


def check_hash_key(child_state, hash_table):
    # Generate a hash key from the string representation of child_state
    key = hash(str(child_state))
    # Check if the generated key exists in the hash_table
    if key in hash_table.keys():
        return True, hash_table.get(key)  # If the key exists, return True and the corresponding value from the hash_table
    return False, None      # If the key doesn't exist, return False and None



def build_network(hash_table):
     # create an empty directed graph
    network = DiGraph()
     # create empty lists to store nodes and edges
    nodes = []
    weighted_edges = []
    weights = []

     # extract all the values from the hash table and remove duplicates
    list_of_values = hash_table.values()
    for value in list_of_values:
        if value not in nodes:
            nodes.append(value)

     # add each node to the graph and its corresponding edges to the edge list
    for node in nodes:
         # get the number of children for the current node
        number_of_children = len(node.children)
        # add the current node to the graph
        network.add_node(node)

        # iterate over the node's children and add the weighted edge to the edge list
        for i in range(0, number_of_children):
            # create a tuple representing the edge and its weight
            weighted_edges.append((node, node.children[i], node.children_weights[i]))
            weights.append(node.children_weights[i])
     # add all the edges to the graph
    network.add_weighted_edges_from(weighted_edges)
    
     # return the resulting graph
    return network
