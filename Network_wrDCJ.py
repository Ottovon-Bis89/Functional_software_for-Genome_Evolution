
from new_Node import Node
from networkx import DiGraph
from Class_extremities_and_adjacencies import Extremities_and_adjacencies

get_genome = Extremities_and_adjacencies()

class Network:
    def __init__(self):
        self.operation_weight = 0
        self.op_weight = 0

    def build_hash_table(self,current_node, hash_table, adjacenciesB, weights):
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


        # if the previous operation was a cicularization (i.e. a trp0) do:

        if node.join_adjacency != 0:

            operations = node.get_decircularization_operations(adjacenciesB)

            for operation in operations:

                child_state = node.take_action(operation)[0]  
                check_hash_table = self.check_hash_key(child_state,
                                                hash_table) 


                if node.join_adjacency in operation[0]:
                    operation_type = 'trp1'
                    self.operation_weight = 0.5 * weights[1]
                    # print('operation1:', self.operation_weight)
                    #operation_weight = 1 * weights[1]

                else:
                    operation_type = 'trp2'
                    self.operation_weight = 1.5 * weights[1]
                    #print('operation2:', self.operation_weight)


                if check_hash_table[0]:  

                    child = check_hash_table[1]  
                    node.children.append(child)  
                    node.children_weights.append(self.operation_weight)  
                    node.children_operations.append((operation, operation_type))

                else:  
                    child = Node(child_state)
                    child.join_adjacency=0
                    hash_key = hash(str(child.state))
                    hash_table.update({hash_key: child})
                    node.children.append(child)
                    node.children_weights.append(self.operation_weight)
                    node.children_operations.append((operation, operation_type))

                    self.build_hash_table(child, hash_table, adjacenciesB, weights)


        else:  

            operations = node.get_legal_operations(adjacenciesB)

            for operation in operations:

                operation_result = node.take_action(operation)
                child_state = operation_result[0]
                op_type = operation_result[1]
                #print(operation_result[1])
                

                check_hash_table = self.check_hash_key(child_state, hash_table)

                if check_hash_table[0]:
                    child = check_hash_table[1]
                    node.children.append(child)

                    child.find_chromosomes(child.state)

                    if len(child.circular_chromosomes) != 0:
                        node.children_weights.append(0.5 * weights[1])
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
                            self.op_weight = 1 * weights[4]
                            #print('operation3:', self.op_weight)
                            # print(self.op_weight)

                        elif op_type == 'fus':
                            operation_type = op_type
                            self.op_weight = 1 * weights[5]
                            #print('operation4:', self.op_weight)

                        elif op_type == 'u_trl':
                            operation_type = op_type
                            self.op_weight = 1 * weights[3]
                            #print('operation5:', self.op_weight)

                        elif op_type == 'b_trl':
                            operation_type = op_type
                            self.op_weight = 1 * weights[2]
                            #rint('operation6:', self.op_weight)

                        elif op_type == 'inv':
                            operation_type = op_type
                            self.op_weight = 1 * weights[0]
                            #print('operation8:', self.op_weight)
                        
                        elif op_type == 'ins':
                            operation_type = op_type
                            self.op_weight = 0.15 * weights[5]
                            #print('operation9:', self.op_weight)
                        
                        elif op_type == 'dup':
                            operation_type = op_type
                            self.op_weight = 0.3 * weights[4]
                            
                        elif op_type == 'dele':
                            operation_type = op_type
                            self.op_weight = 0.05 * weights[3]
                            #print('operation10:', self.op_weight)
                        
                            

                        else:
                            print('You have got a problem, the op type is: ', op_type, '')

                        node.children_weights.append(self.op_weight)
                        node.children_operations.append((operation, operation_type))


                else:  # if the child is not in the hash table
                    child = Node(child_state)
                    child.find_chromosomes(child.state)

                    if len(child.circular_chromosomes) != 0:  # if a circular chromosome has been created:

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

                        self.build_hash_table(child, hash_table, adjacenciesB, weights)



                    else:
                        child.join_adjacency = 0
                        hash_key = hash(str(child.state))
                        hash_table.update({hash_key: child})
                        node.children.append(child)

                        if op_type == 'fis':
                            operation_type = op_type
                            self.op_weight = 1 * weights[4]
                            # print(self.op_weight)

                        elif op_type == 'fus':
                            operation_type = op_type
                            self.op_weight = 1 * weights[5]

                        elif op_type == 'u_trl':
                            operation_type = op_type
                            self.op_weight = 1 * weights[3]

                        elif op_type == 'inv':
                            operation_type = op_type
                            self.op_weight = 1 * weights[0]

                        elif op_type == 'b_trl':
                            operation_type = op_type
                            self.op_weight = 1 * weights[2]
                            
                        elif op_type == 'ins':
                            operation_type = op_type
                            self.op_weight = 0.15 * weights[5]
                            # print(self.op_weight)
                            
                        elif op_type == 'dup':
                            operation_type = op_type
                            self.op_weight = 0.3 * weights[4]
                            
                        elif op_type == 'dele':
                            operation_type = op_type
                            self.op_weight = 0.05 * weights[3]
                            
                            
                        else:
                            print("There's a problem at the .find_op_type node function")
                            print('You have got a problem, the op_type is: ', op_type, '')

                        node.children_weights.append(self.op_weight)
                        node.children_operations.append((operation, operation_type))

                        self.build_hash_table(child, hash_table, adjacenciesB, weights)

    def check_hash_key(self, child_state, hash_table):
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


    def build_network(self, hash_table):
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





