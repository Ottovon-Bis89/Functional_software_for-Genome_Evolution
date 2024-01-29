from Class_wrDCJ_Node import Node
from networkx import DiGraph
from Class_extremities_and_adjacencies import Extremities_and_adjacencies

get_genome = Extremities_and_adjacencies()


def build_hash_table(current_node, hash_table, adjacenciesB, weights):
    node = current_node


    # if the previous operation was a cicularization (i.e. a trp0) do:

    if node.join_adjacency != 0:

        operations = node.get_reinsertion_operations(adjacenciesB)

        for operation in operations:

            child_state = node.take_action(operation)[0]  # perform operation
            check_hash_table = check_hash_key(child_state,
                                              hash_table)  # check whether the intermediate create exists already


            # if it is a trp1 type operation
            if node.join_adjacency in operation[0]:
                operation_type = 'trp1'
                operation_weight = 0.5 * weights[1]
                #operation_weight = 1 * weights[1]

            # else it is a trp2 type operation
            else:
                operation_type = 'trp2'
                operation_weight = 1.5 * weights[1]


            if check_hash_table[0]:  # if the intermediate exists

                child = check_hash_table[1]  # let the child = (point to) the intermediate node in the hash table
                node.children.append(child)  # add the child to the list of children of the current node
                node.children_weights.append(
                    operation_weight)  # add the weight of the operation that generated the child to the list of weights
                node.children_operations.append((operation,
                                                 operation_type))  # add the operation and its type to the list of operations that generated the node children


            else:  # if the intermediate does not exist in the hash table
                child = Node(child_state)  # create a node for the state
                child.join_adjacency=0
                hash_key = hash(str(child.state))
                hash_table.update({hash_key: child})  # add child node to hash table
                node.children.append(child)
                node.children_weights.append(operation_weight)
                node.children_operations.append((operation, operation_type))

                build_hash_table(child, hash_table, adjacenciesB, weights)



    else:  # if the previous operation was not a circularization, i.e. the current intermediary genome consists of only linear chromosomes

        operations = node.get_legal_operations(adjacenciesB)

        for operation in operations:

            operation_result = node.take_action(operation)
            child_state = operation_result[0]
            op_type = operation_result[1]

            check_hash_table = check_hash_key(child_state, hash_table)

            if check_hash_table[0]:  # if the child exists in the hash table:
                child = check_hash_table[1]
                node.children.append(child)

                child.find_chromosomes(child.state)

                if len(child.circular_chromosomes) != 0:  # if a circularization occurred
                    node.children_weights.append(0.5 * weights[1])
                    #node.children_weights.append(1 * weights[1])
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


            else:  # if the child is not in the hash table
                child = Node(child_state)
                child.find_chromosomes(child.state)

                if len(child.circular_chromosomes) != 0:  # if a circular chromosome has been created:

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
                        #if operation[-1][0] in child.circular_chromosomes[0]:
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
                    #node.children_weights.append(1 * weights[1])

                    build_hash_table(child, hash_table, adjacenciesB, weights)



                else:  # else if no circular chromosome has been created:
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
                        print("There's a problem at the .find_optype node function")
                        print('You have got a problem, the op type is: ', op_type, '    #4')

                    node.children_weights.append(op_weight)
                    node.children_operations.append((operation, operation_type))

                    build_hash_table(child, hash_table, adjacenciesB, weights)


def check_hash_key(child_state, hash_table):
    key = hash(str(child_state))
    if key in hash_table.keys():
        return True, hash_table.get(key)
    return False, None


def build_network(hash_table):

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
