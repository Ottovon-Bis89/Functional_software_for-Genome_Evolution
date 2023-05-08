
from Rearrangements import Node_rearrangement
from networkx import DiGraph






def build_hash_table(node, hash_table, adjacenciesB, weights):
# def build_hash_table(current_node: Node, hash_table: Dict[str, Node], adjacencies: List[Tuple[int, int]], weights: List[float]) -> Dict[str, Node]:

    """
    Recursively builds a hash table of intermediary genomes, where each node represents an intermediary genome and is
    indexed by a hash of its string representation.
    :param current_node: the node representing the current intermediary genome
    :param hash_table: the hash table to add nodes to
    :param adjacenciesB: the list of adjacencies in the input genome
    :param weights: a list of weights corresponding to different types of genome rearrangements
    :return: the hash table containing all intermediary genomes
    """

    node = Node_rearrangement

    # Check if previous operation was a circularization
    if node.join_adjacency != 0:

        # Get list of possible reinsertion operations
        operations = node.get_reinsertion_operations(adjacenciesB)

        # Check each operation
        for operation in operations:

            # Perform operation to get child state
            child_state = node.take_action(operation)[0]

            # Check if intermediate node already exists in hash table
            check_hash_table = check_hash_key(child_state, hash_table)

            # Determine operation type and weight
            if node.join_adjacency in operation[0]:
                operation_type = 'trp1'
                operation_weight = 0.5 * weights[1]
            else:
                operation_type = 'trp2'
                operation_weight = 1.5 * weights[1]

            if check_hash_table[0]:  # If intermediate node exists in hash table
                child = check_hash_table[1]  # Link to intermediate node
                node.children.append(child)
                node.children_weights.append(operation_weight)
                node.children_operations.append((operation, operation_type))

            else:  # If intermediate node does not exist in hash table
                child = Node_rearrangement(child_state)  # Create new node for intermediate state
                child.join_adjacency = 0
                hash_key = hash(str(child.state))
                hash_table.update({hash_key: child})  # Add child node to hash table
                node.children.append(child)
                node.children_weights.append(operation_weight)
                node.children_operations.append((operation, operation_type))

                # Recursively call function with new child node
                build_hash_table(child, hash_table, adjacenciesB, weights)
    

    # If the previous operation was not a circularization (i.e. the current intermediary genome consists of only linear chromosomes)
    else:

        # Get legal operations to perform on the current node's genome
        operations = node.get_legal_operations(adjacenciesB)

        # Iterate over each legal operation
        for operation in operations:
            
            # Get the resulting state and type of operation
            operation_result = node.take_action(operation)
            child_state = operation_result[0]
            op_type = operation_result[1]

            # Check if the child node with the resulting state already exists in the hash table
            check_hash_table = check_hash_key(child_state, hash_table)

            # If the child exists in the hash table:
            if check_hash_table[0]:
                child = check_hash_table[1]
                node.children.append(child)

                # If the child node has at least one circular chromosome, set its join adjacency to the appropriate adjacency
                child.find_chromosomes(child.state)
                if len(child.circular_chromosomes) != 0:
                    node.children_weights.append(0.5 * weights[1])
                    node.children_operations.append((operation, 'trp0'))

                    if type(operation[-1][0]) is tuple and type(operation[-1][1]) is tuple:
                        for adjacency in operation[-1]:
                            if adjacency in child.circular_chromosomes[0]:
                                child.join_adjacency = adjacency

                    elif type(operation[-1][0]) is tuple:
                        if operation[-1][0] in child.circular_chromosomes[0]:
                            child.join_adjacency = operation[-1][0]
                        else:
                            print('error')

                    elif type(operation[-1][1]) is tuple:
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
                # Check if the child node resulting from the operation exists in the hash table or not.
                # check_hash_table = check_hash_key(child_state, hash_table)

                # if check_hash_table[0]:  # if the child exists in the hash table:
                #     child = check_hash_table[1]
                #     node.children.append(child)

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
                        print('You have got a problem, the op type is:', op_type, '#2')

                    # Add the operation type and weight to the current node's children list.
                    node.children_weights.append(op_weight)
                    node.children_operations.append((operation, operation_type))

            else:  # if the child is not in the hash table

                # Create a new child node, find chromosomes, and check if a circular chromosome has been created.
                child = Node_rearrangement(child_state)
                child.find_chromosomes(child.state)

                if len(child.circular_chromosomes) != 0:  # if a circular chromosome has been created:

                    # Find the adjacency in the circular chromosome that is involved in the circularization operation.
                    if type(operation[-1][0]) is tuple and type(operation[-1][1]) is tuple:
                        for adjacency in operation[-1]:
                            if adjacency in child.circular_chromosomes[0]:
                                    child.join_adjacency = adjacency

                    elif type(operation[-1][0]) is tuple:
                        if operation[-1][0] in child.circular_chromosomes[0]:
                                child.join_adjacency = operation[-1][0]
                        else:
                            print('error')

                    elif type(operation[-1][1]) is tuple:
                        if operation[-1][1] in child.circular_chromosomes[0]:
                                child.join_adjacency = operation[-1][1]
                        else:
                            print('error')

                    else:
                        if operation[-1] in child.circular_chromosomes[0]:
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
                    build_hash_table(child, hash_table, adjacenciesB, weights)
 
                
                # If no circular chromosome has been created
                else:
                    child.join_adjacency = 0

                    # Add the child to the hash table and update the node
                    hash_table[hash_key] = child
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
                        print("There's a problem at the .find_optype node function")
                        print('You have got a problem, the op type is: ', op_type, '#4')

                    # Update the node and build the hash table
                    node.children_weights.append(op_weight)
                    node.children_operations.append((operation, operation_type))
                    build_hash_table(child, hash_table, adjacenciesB, weights)

    def check_hash_key(child_state, hash_table):
        key = hash(str(child_state))
        if key in hash_table:
            return True, hash_table[key]
        return False, None


    

    def build_network(hash_table):
        # create an empty directed graph
        network = DiGraph()
        # create empty lists to store nodes and edges
        nodes = []
        weighted_edges = []

        # extract all the values from the hash table and remove duplicates
        for value in hash_table.values():
            if value not in nodes:
                nodes.append(value)

        # add each node to the graph and its corresponding edges to the edge list
        for node in nodes:
            # get the number of children for the current node
            number_of_children = len(node.children)
            # add the current node to the graph

            network.add_node(node)

            # iterate over the node's children and add the weighted edge to the edge list
            for i in range(number_of_children):
                # create a tuple representing the edge and its weight
                weighted_edges.append((node, node.children[i], node.children_weights[i]))

        # add all the edges to the graph
        network.add_weighted_edges_from(weighted_edges)

        # return the resulting graph
        return network





