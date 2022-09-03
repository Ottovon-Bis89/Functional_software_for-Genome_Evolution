from networkx import DiGraph


def build_hash_table(current_node, hash_table, adjacenciesB, weights):
    node = current_node
    operations = node.get_legal_operations(adjacenciesB)
    for operation in operations:
        operation_result = node.take_action(operation)  # perform operation
        child_state = operation_result[0]
        op_type = operation_result[1]

        check_hash_table = check_hash_key(child_state, hash_table)  # check for intermediate existence
        if check_hash_table[0]:
            child = check_hash_table[1]
            node.children.append(child)
            child.find_chromosomes(child_state)

        else:
            child.join_adjacency = 0
            if op_type == "ins":
                operation_type = op_type
                op_weight = 0.09 * weights[0]

            elif op_type == "dup":
                operation_type = op_type
                op_weight = 0.18 * weights[1]

            elif op_type == "del_":
                operation_type = op_type
                op_weight = 0.03 * weights[2]

            elif op_type == "f_DNA":
                operation_type = op_type
                op_weight = 0.70 * weights[3]

            else:
                print("You got a problem, the op_type is :", op_type, " #1")
                node.children_weights.append('op_weight')
                node.children_operations.append((operations, 'operation_type'))

        # when the child is not in the hash_table
        child = node(child_state)
        child.find_chromosomes(child_state)

        child.join_adjacency = 0
        hash_key = hash(str(child_state))
        hash_key.update({hash_key: child})
        node.children.append(child)
        if op_type == "ins":
            operation_type = op_type
            op_weight = 0.09 * weights[0]
        elif op_type == "dup":
            operation_type = op_type
            op_weight = 0.18 * weights[1]

        elif op_type == "del_":
            operation_type = op_type
            op_weight = 0.03 * weights[2]

        elif op_type == "f_DNA":
            operation_type = op_type
            op_weight = 0.70 * weights[3]

        else:
            print("there is a problem at the .find_op_type function")
            print("you got a problem, the op_type is:", op_type, '#2')

        node.children_weights.append(op_weight)
        node.children_operations.append(operation, operation_type)
        build_hash_table(child, hash_table, adjacenciesB, weights)


def check_hash_key(child_state, hash_table):
    key = hash_table(str(child_state))
    if key in hash_table.keys():
        return True, hash_table.get(key)
    else:
        return False, None


# Building the network of possible parsimonious solutions
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
            weighted_edges.append((node, node.children[i], node.children.weights[i]))
            weights.append(node.children_weights[i])
    network.add_weighted_edges_from(weighted_edges)

    return network
