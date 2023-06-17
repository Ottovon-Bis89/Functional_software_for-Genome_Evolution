from networkx import DiGraph
from GEN_NODE import Node

# This program creates a key-value pair data structure that will used to generate a graph of network of solutions paths from the source genome to the target genome
def build_hash_table(current_node, hash_table, target_genome, weights):
    Node = current_node
    operations = Node.get_legal_operations(target_genome)
    for operation in operations:
        operation_result = Node.do_mutation(operation)  # perform all the possible mutations that are required to transform genome_A into genome_B.
        child_state = operation_result[0]
        op_type = operation_result[1]

        check_hash_table = check_hash_key(child_state, hash_table)  # check for intermediate existence
        if check_hash_table[0]:
            child = check_hash_table[1]
            Node.children.append(child)
            child.find_chromosomes(child_state)

        else:
            child.join_adjacency = 0
            if op_type == "ins":
                operation_type = op_type
                op_weight = 0.15 * weights[0]

            elif op_type == "dup":
                operation_type = op_type
                op_weight = 0.3 * weights[1]

            elif op_type == "del_":
                operation_type = op_type
                op_weight = 0.05 * weights[2]

            elif op_type == "f_DNA":
                operation_type = op_type
                op_weight = 0.50 * weights[3]

            else:
                print("You got a problem, the op_type is :", op_type, " #1")
                Node.children_weights.append('op_weight')
                Node.children_operations.append((operations, 'operation_type'))

        # when the child is not in the hash_table
        child = Node(child_state)
        child.find_chromosomes(child_state)

        child.join_adjacency = 0
        hash_key = hash(str(child_state))
        hash_key.update({hash_key: child})
        Node.children.append(child)
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

        Node.children_weights.append(op_weight)
        Node.children_operations.append(operation, operation_type)
        build_hash_table(child, hash_table, target_genome, weights)


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
