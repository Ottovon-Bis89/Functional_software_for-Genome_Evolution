from Rearrangement_node import Node
from networkx import DiGraph
from logger import log


def build_hash_table(current_node, hash_table, adjacencies_genomeB, weights):
    
    '''
     Builds a hash table representing the state space of "Genolve".
    The algorithm explores possible operations on a given node and recursively builds
    the state space tree while updating the hash table to avoid redundant computations.
    
    @param current_node The current node in the state space tree.
    @param hash_table The hash table used to store previously visited states.
    @param adjacencies_genomeB The adjacency information for Genome B.
    @param weights The weights used to calculate operation weights.
 
    '''
    log.debug(build_hash_table)
    node = current_node

    if node.join_adjacency != 0:

        operations = node.get_decircularization_operations(adjacencies_genomeB)

        for operation in operations:

            child_state = node.take_action(operation)[0]  
            check_hash_table = check_hash_key(child_state,hash_table)   

            if node.join_adjacency in operation[0]:
                operation_type = 'trp1'
                operation_weight = 0.5 * weights[1]

            else:
                operation_type = 'trp2'
                operation_weight = 1.5 * weights[1]

            if check_hash_table[0]: 
                child = check_hash_table[1]  
                node.children.append(child) 
                node.children_weights.append(operation_weight) 
                node.children_operations.append((operation, operation_type))  
            else:  
                child = Node(child_state) 
                child.join_adjacency = 0
                hash_key = hash(str(child.state))
                hash_table.update({hash_key: child})  
                node.children.append(child)
                node.children_weights.append(operation_weight)  
                node.children_operations.append((operation, operation_type))  

                build_hash_table(child, hash_table, adjacencies_genomeB, weights)
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

                    node.children_weights.append(op_weight)
                    node.children_operations.append((operation, operation_type))

            else: 
                child = Node(child_state)
                child.find_chromosomes(child.state)

                if len(child.circular_chromosomes) != 0:  
               
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

                    hash_key = hash(str(child.state))
                    hash_table.update({hash_key: child})
                    node.children.append(child)
                    node.children_operations.append((operation, 'trp0'))
                    node.children_weights.append(0.5 * weights[1])

                    build_hash_table(child, hash_table, adjacencies_genomeB, weights)

                else:  
                    child.join_adjacency = 0
              
                    hash_key = hash(str(child.state))
                    hash_table.update({hash_key: child})
                    node.children.append(child)

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

                    node.children_weights.append(op_weight)
                    node.children_operations.append((operation, operation_type))

                    build_hash_table(child, hash_table, adjacencies_genomeB, weights)


def check_hash_key(child_state, hash_table):

    log.debug(check_hash_key)

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



def build_network(hash_table):

    log.debug(hash_table)

    """
    Builds a directed graph network based on a given hash table.

    This function takes a hash table as input and constructs a directed graph (DiGraph) network. It extracts unique nodes and their children from the hash table, creating nodes in the network for each unique value. Weighted edges are added to represent the relationships between nodes and their children.

    Parameters:
        hash_table (dict): A hash table containing nodes and their children with associated weights.

    Returns:
        networkx.DiGraph: A directed graph representing the relationships between nodes and their children.
    """
    network = DiGraph()
    
    nodes = []
    weighted_edges = []
    weights = []
    list_of_values = hash_table.values()
    for value in list_of_values:
        if value not in nodes:
            nodes.append(value)

    for node in nodes:
        number_of_children = len(node.children)
        network.add_node(node)

       
        for i in range(0, number_of_children):
          
            weighted_edges.append((node, node.children[i], node.children_weights[i]))
            weights.append(node.children_weights[i])
    
    network.add_weighted_edges_from(weighted_edges)
    
    return network
