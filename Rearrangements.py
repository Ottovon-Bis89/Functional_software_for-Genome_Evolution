class Node_rearrangement:

    join_adjacency = 0
    
    def __init__(self, state=None):
        self.state = state
        self.children = []
        self.children_weights = []
        self.children_operations = []
        self.linear_chromosomes = []
        self.circular_chromosomes = []
        self.next_operation = 0
        self.next_operation_weight = 1
        # self.join_adjacency = 0

        

        # Find chromosomes and store them in instance variables
        self.linear_chromosomes, self.circular_chromosomes = self.find_chromosomes(self.state)
        
    def find_next_extremity(self, current, next_extremity):
        # Determine the next extremity for the given current extremity
        next = current[1] + 0.5 if current[0] == next_extremity and current[1] % 1 == 0 else \
               current[1] - 0.5 if current[0] == next_extremity and current[1] % 1 != 0 else \
               current[0] + 0.5 if current[1] == next_extremity and current[0] % 1 == 0 else \
               current[0] - 0.5

        return next

    def find_next_adjacency(self, next_extremity, chromosome, not_telomeres):
        # Find the next adjacency cycle in the given chromosome
        for element in not_telomeres:
            if element[0] == next_extremity or element[1] == next_extremity:
                current = element
                chromosome.append(current)
                not_telomeres.remove(current)
                next_extremity = self.find_next_extremity(current, next_extremity)
                return next_extremity, chromosome, not_telomeres

        return [next_extremity]

    def find_adjacency_cycle(self, next_extremity, chromosome, not_telomeres):
        # Find the next adjacency cycle in the given chromosome
        while True:
            next_adjacency = self.find_next_adjacency(next_extremity, chromosome, not_telomeres)

            if len(next_adjacency) == 1:
                next_extremity = next_adjacency[0]
                break
            else:
                next_extremity, chromosome, not_telomeres = next_adjacency[0], chromosome, not_telomeres

        return next_extremity, chromosome, not_telomeres



    def find_chromosomes(self, adjacencies):
        # Separate telomeres and not telomeres
        telomeres = [element for element in adjacencies if not isinstance(element, tuple)]
        not_telomeres = [element for element in adjacencies if isinstance(element, tuple)]

        # Initialize output lists
        linear_chromosomes = []
        circular_chromosomes = []

        # Find linear chromosomes
        while telomeres:
            # Initialize a new chromosome
            chromosome = [telomeres.pop(0)]

            # Get the next extremity
            if chromosome[0] % 1 == 0:
                next_extremity = chromosome[0] + 0.5
            else:
                next_extremity = chromosome[0] - 0.5

            # If single gene chromosome, append to the output list
            if next_extremity in telomeres:
                chromosome.append(telomeres.pop(telomeres.index(next_extremity)))
                linear_chromosomes.append(chromosome)

            # Else find adjacency cycle
            else:
                adjacency_cycle = Node_rearrangement.find_adjacency_cycle(self, next_extremity, chromosome, not_telomeres)
                next_extremity = adjacency_cycle[0]
                while next_extremity not in telomeres:
                    chromosome.extend(adjacency_cycle[1])
                    adjacency_cycle = Node_rearrangement.find_adjacency_cycle(self, next_extremity, chromosome, not_telomeres)
                    next_extremity = adjacency_cycle[0]
                chromosome.extend(adjacency_cycle[1])
                chromosome.append(telomeres.pop(telomeres.index(next_extremity)))
                linear_chromosomes.append(chromosome)

        # Find circular chromosomes
        while not_telomeres:
            # Initialize a new chromosome
            chromosome = [not_telomeres.pop(0)]

            # Get the next extremity
            if chromosome[0][0] % 1 == 0:
                next_extremity = chromosome[0][0] + 0.5
            else:
                next_extremity = chromosome[0][0] - 0.5

            # If single gene chromosome, append to the output list
            if next_extremity == chromosome[0][1]:
                circular_chromosomes.append(chromosome)

            # Else find adjacency cycle
            else:
                adjacency_cycle = Node_rearrangement.find_adjacency_cycle(self, next_extremity, chromosome, not_telomeres)
                next_extremity = adjacency_cycle[0]
                while next_extremity != chromosome[0][1]:
                    chromosome.extend(adjacency_cycle[1])
                    adjacency_cycle = Node_rearrangement.find_adjacency_cycle(self, next_extremity, chromosome, not_telomeres)
                    next_extremity = adjacency_cycle[0]
                chromosome.extend(adjacency_cycle[1])
                circular_chromosomes.append(chromosome)

        return linear_chromosomes, circular_chromosomes

    
    def get_legal_operations(self, adjacenciesB):

        list_of_legal_operations = []

        # Get the current state of adjacencies
        adjacenciesA = self.state

        # Loop through each element in adjacenciesB
        for element in adjacenciesB:

        # If the element is already in adjacenciesA, do nothing
            if element in adjacenciesA:
                pass

        # If the element is not in adjacenciesA, perform some operations
            else:
                adjacenciesA_copy = adjacenciesA[:]

            # If the element is an adjacency, perform some operations
            if type(element) is tuple:
                p, q = element[0], element[1]
                u, v = 0, 0

                # Check if the elements containing p and q respectively in adjacenciesA are adjacencies
                for marker in adjacenciesA_copy:
                    if type(marker) is tuple:
                        if marker[0] == p or marker[1] == p:
                            u = marker
                        if marker[0] == q or marker[1] == q:
                            v = marker

                # If the element containing p in adjacenciesA is a telomere, set u to p
                if u == 0:
                    u = p

                # If the element containing q in adjacenciesA is a telomere, set v to q
                if v == 0:
                    v = q

                # If u and v are not equal, perform some operations
                if u != v:

                    # Add the adjacency (p,q) to adjacenciesA_copy
                    adjacenciesA_copy.append((p, q))

                    # Remove u and v from adjacenciesA_copy
                    adjacenciesA_copy.remove(u)
                    adjacenciesA_copy.remove(v)

                    # If u is an adjacency, perform some operations
                    if type(u) is tuple:

                        # Calculate u'p and v'q
                        if u[0] == p:
                            u_not_p = u[1]
                        else:
                            u_not_p = u[0]
                        if v[0] == q:
                            v_not_q = v[1]
                        else:
                            v_not_q = v[0]

                        # Add the adjacency (u'p, v'q) to adjacenciesA_copy
                        adjacenciesA_copy.append((u_not_p, v_not_q))

                        # Order the operations before appending to list_of_legal_operations
                        op_1 = (u, v) if u[0] < v[0] else (v, u)
                        op_2_1 = (p, q) if p < q else (q, p)
                        op_2_2 = (u_not_p, v_not_q) if u_not_p < v_not_q else (v_not_q, u_not_p)
                        op_2 = (op_2_1, op_2_2) if op_2_1[0] < op_2_2[0] else (op_2_2, op_2_1)
                        ordered_operation = (op_1, op_2)

                        # Append the ordered operation to list_of_legal_operations if it's not already in the list
                        if ordered_operation not in list_of_legal_operations:

                            list_of_legal_operations.append(ordered_operation)
    

    def take_action(self, operation):

        """
        This function takes an operation and modifies the state of the current node.

        :param operation: tuple, an operation to modify the state of the current node
        :return: tuple, a new ordered and sorted node state and a string representing the type of operation performed
        """
        # Make a copy of the current state
        state_copy = self.state.copy()
        # Initialize the operation type as None
        operation_type = None

            # If the operation is a fusion or fission:
        if len(operation) == 3:

            # If it is a fission operation
            if type(operation[0]) is tuple:
                # Remove the first tuple from the state
                state_copy.remove(operation[0])
                # Add the second and third tuples to the state
                state_copy.append(operation[1])
                state_copy.append(operation[2])
                # Set the operation type to 'fis'
                operation_type = 'fis'

        # If it is a fusion operation
            else:
            # Remove the first and second tuples from the state
                state_copy.remove(operation[0])
                state_copy.remove(operation[1])

            # Ensure the gene extremities are in the correct order for downstream comparisons with genome B extremities
            if operation[2][0] < operation[2][1]:
                state_copy.append(operation[2])
            else:
                state_copy.append((operation[2][1], operation[2][0]))

            # Set the operation type to 'fus'
                operation_type = 'fus'

            # If the operation is another rearrangement
        elif len(operation) == 2:
                # If it is an inversion, transposition, or balanced translocation
            if type(operation[0][0]) is tuple and type(operation[0][1]) is tuple:
                    # Remove the first and second tuples from the state
                    state_copy.remove(operation[0][0])
                    state_copy.remove(operation[0][1])

            # Ensure the gene extremities are in the correct order for downstream comparisons with genome B extremities
            if operation[1][0][0] < operation[1][0][1]:
                state_copy.append(operation[1][0])
            else:
                state_copy.append((operation[1][0][1], operation[1][0][0]))

            if operation[1][1][0] < operation[1][1][1]:
                state_copy.append(operation[1][1])
            else:
                state_copy.append((operation[1][1][1], operation[1][1][0]))

            # Transpositions happen in two steps:
            # Balanced translocations - the adjacencies to cut are on different chromosomes
            # Inversions - the adjacencies to cut are on the same chromosome
            # Transpositions occur in two steps
            # Find the chromosomes in the state
            chromosomes = self.find_chromosomes(self.state)
            circular_chromosomes = chromosomes[1]

            # If there are circular chromosomes in the state
            if len(circular_chromosomes) != 0:
                # Set the operation type to 'trp_reinsertion'
                operation_type = 'trp_reinsertion'

            else:
                # Otherwise, find the linear chromosomes in the state
                linear_chromosomes = chromosomes[0]

                # Find the chromosome that contains the first gene in the first tuple of the operation
                for chromosome in linear_chromosomes:
                    if operation[0][0] in chromosome:
                        test_chromosome = chromosome

                # If the second gene in the first tuple of the operation is also in the test chromosome,
                # the operation is an inversion
                if operation[0][1] in test_chromosome:
                    operation_type = 'inv'
                # Otherwise, it is a balanced translocation
                else:
                        operation_type = 'b_trl'
            
            # check if operation is a translocation or intrachromosomal transposition to end of chromosome or inversion at end of chromosome
        elif type(operation[0][0]) is not tuple or type(operation[0][-1]) is not tuple:

            # remove genes being modified from current state
            state_copy.remove(operation[0][0])
            state_copy.remove(operation[0][1])

            # ensure gene extremities in correct order for downstream comparisons with genome B extremities
            if operation[1][0][0] < operation[1][0][1]:
                state_copy.append(operation[1][0])
            else:
                state_copy.append((operation[1][0][1], operation[1][0][0]))

            # append gene being moved to new position
            state_copy.append(operation[1][1])

            # transpositions occur in two steps
            chromosomes = self.find_chromosomes(self.state)
            circular_chromosomes = chromosomes[1]

            # check if transposition to end of chromosome is possible
            if len(circular_chromosomes) != 0:
                operation_type = 'trp_reinsertion'

            else:
                linear_chromosomes = chromosomes[0]

            # find adjacency and telomere of linear chromosome
            for element in operation[0]:
                if type(element) is tuple:
                    adjacency = element
                else:
                    telomere = element
            
            # find chromosome containing adjacency
            for chromosome in linear_chromosomes:
                if adjacency in chromosome:
                    test_chromosome = chromosome

            # determine if operation is an inversion or unbalanced translocation
            if telomere in test_chromosome:
                operation_type = 'inv'
            else:
                operation_type = 'u_trl'

        else:
        # raise an error if operation is not valid
            raise ValueError("Invalid operation type")

        # order and sort the modified state of the node
        ordered_and_sorted = Node_rearrangement.order_and_sort(self, state_copy)

        # return the modified state and the type of operation performed
        return ordered_and_sorted, operation_type

    

    def adjacencies_equivalent(self, adjacenciesB):
        # create a copy of adjacenciesA (the current node's state) and adjacenciesB (the input state)
        adjacenciesA = self.state.copy()
        adjacenciesB = adjacenciesB

        # order the adjacencies in adjacenciesA and store them in ordered_adjacenciesA
        ordered_adjacenciesA = []
        for element in adjacenciesA:
            if type(element) is tuple:
                # if the adjacency is a tuple, sort the tuple and append it to ordered_adjacenciesA
                if int(element[0]) < int(element[1]):
                    ordered_adjacenciesA.append(element)
                else:
                    ordered_adjacenciesA.append((element[1], element[0]))
            else:
                # if the adjacency is not a tuple, append it to ordered_adjacenciesA
                ordered_adjacenciesA.append(element)

        # compare each adjacency in adjacenciesB with ordered_adjacenciesA
        for element in adjacenciesB:
            if element in ordered_adjacenciesA:
                # if the adjacency is in ordered_adjacenciesA, do nothing and continue to the next adjacency
                pass
            else:
                # if the adjacency is not in ordered_adjacenciesA, the states are not equivalent, so return False
                return False
        # if all adjacencies in adjacenciesB are in ordered_adjacenciesA, the states are equivalent, so return True
        return True
    

    def sort_adjacencies_and_telomeres(self, adjacencies):
        telomeres = []
        gene_adjacencies = []
    
        # Separate gene adjacencies and telomeres
        for element in adjacencies:
            if type(element) is tuple:
                # If it is a single gene adjacency e.g. (4.5, 4.0)
                if element[0] == element[1]:
                    # If the gene identifier is an integer
                    if element[0].is_integer():
                        gene_adjacencies.append(element)
                    else:
                        gene_adjacencies.append((element[1], element[0]))
                # If it is a regular gene adjacency e.g. (4.0, 5.0)
                elif element[0] < element[1]:
                    gene_adjacencies.append(element)
                else:
                    gene_adjacencies.append((element[1], element[0]))
            else:
                telomeres.append(element)
        
        # Sort telomeres and gene adjacencies
        telomeres.sort()
        gene_adjacencies.sort()

        # Concatenate and return the sorted list
        sorted_adjacencies = telomeres + gene_adjacencies
        return sorted_adjacencies
    

    def get_decircularization_operations(self, adjacenciesB):
        # get all legal operations
        operations = self.get_legal_operations(adjacenciesB)

        # filter out operations that don't involve decircularization
        decircularization_operations = []
        for operation in operations:
            # check if both adjacencies are in the circular chromosome
            if operation[0][0] in self.circular_chromosomes[0] and operation[0][1] in self.circular_chromosomes[0]:
                pass
            # check if only one adjacency is in the circular chromosome
            elif operation[0][0] in self.circular_chromosomes[0] or operation[0][1] in self.circular_chromosomes[0]:
                decircularization_operations.append(operation)
            else:
                pass

        return decircularization_operations













