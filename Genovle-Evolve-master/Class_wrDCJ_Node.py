class Node:

    def __init__(self, state=None):
        self.state = state
        self.children = []
        self.children_weights = []
        self.children_operations =[]
        self.linear_chromosomes = []
        self.circular_chromosomes = []
        self.next_operation = 0
        self.next_operation_weight = 1
        self.join_adjacency = 0

        get_chromosomes = Node.find_chromosomes(self, self.state)
        self.linear_chromosomes = get_chromosomes[0]
        self.circular_chromosomes = get_chromosomes[1]



    def find_next_extremity(self, current, next_extremity):
        """
        Finds the next extremity based on the current extremity and the target extremity.

        Parameters:
        - current (tuple): A tuple representing the current extremity, where current[0] is the x-coordinate and current[1] is the y-coordinate.
        - next_extremity (int): The target extremity to be compared with the x-coordinate of the current extremity.

        Returns:
        - float: The next extremity coordinate.

        Example:
        ```python
        current_extremity = (3, 4)
        target_extremity = 3
        result = find_next_extremity(current_extremity, target_extremity)
        print(result)  # Output: 3.5
        ```
        """
        if current[0] == next_extremity:
            if current[1] % 1 == 0:
                next = current[1] + 0.5
            else:
                next = current[1] - 0.5
        else:
            if current[0] % 1 == 0:
                next = current[0] + 0.5
            else:
                next = current[0] - 0.5
        return next

    def find_next_adjacency(self, next_extremity, chromosome, not_telomeres):
        """
        Finds the next adjacency in a chromosome.

        This method searches for the next adjacency in the chromosome given the current extremity, and updates
        the chromosome and the list of non-telomeric elements accordingly.

        :param next_extremity: The current extremity to find the next adjacency from.
        :type next_extremity: YourExtremityType

        :param chromosome: The chromosome to which the adjacency will be added.
        :type chromosome: list

        :param not_telomeres: List of non-telomeric elements.
        :type not_telomeres: list

        :return: A tuple containing the updated next_extremity, chromosome, and not_telomeres.
                 If no adjacency is found, a list containing next_extremity is returned.
        :rtype: tuple or list
        """
        for element in not_telomeres:
            if element[0] == next_extremity or element[1] == next_extremity:
                current = element
                chromosome.append(current)
                not_telomeres.remove(current)
                next_extremity = Node.find_next_extremity(self, current, next_extremity)
                return next_extremity, chromosome, not_telomeres
        return [next_extremity]

    def find_adjacency_cycle(self, next_extremity, chromosome, not_telomeres):
        """
        Finds an adjacency cycle in the graph starting from a given extremity.

        Parameters:
        - next_extremity (object): The starting extremity for the adjacency cycle.
        - chromosome (object): The chromosome related to the starting extremity.
        - not_telomeres (list): List of extremities that are not telomeres.

        Returns:
        tuple: A tuple containing the following elements:
            - next_extremity (object): The last extremity in the adjacency cycle.
            - chromosome (object): The chromosome related to the adjacency cycle.
            - not_telomeres (list): List of extremities that are not telomeres.
        """

        next_adjacency = Node.find_next_adjacency(self, next_extremity, chromosome, not_telomeres)

        while len(next_adjacency) != 1:
            next_extremity = next_adjacency[0]
            next_adjacency = Node.find_next_adjacency(self, next_extremity, chromosome, not_telomeres)
        else:
            next_extremity = next_adjacency[0]

            return next_extremity, chromosome, not_telomeres

    def find_chromosomes(self, adjacencies):
        """
        Finds linear and circular chromosomes in a given set of adjacencies.

        This method takes a list of adjacencies and identifies linear and circular chromosomes
        based on the presence of telomeres and adjacency cycles.

        :param adjacencies: A list of adjacencies to analyze.
        :return: A tuple containing lists of linear and circular chromosomes.
        """

        telomeres = [element for element in adjacencies if type(element) is not tuple]
        not_telomeres = [element for element in adjacencies if type(element) is tuple]

        linear_chromosomes = []
        circular_chromosomes = []
        chromosome = []
        i = 0

        # find linear chromosomes
        while len(telomeres) > 0:

            i += 1
            current = telomeres[0]

            telomeres.remove(current)
            chromosome.append(current)

            if current % 1 == 0:
                next_extremity = current + 0.5
            else:
                next_extremity = current - 0.5

            # if single gene chromosome
            if next_extremity in telomeres:
                current = next_extremity

                telomeres.remove(current)
                chromosome.append(current)
                linear_chromosomes.append(chromosome)
                chromosome = []

            # else find adjacency cycle
            else:
                adjacency_cycle = Node.find_adjacency_cycle(self, next_extremity, chromosome, not_telomeres)
                next_extremity = adjacency_cycle[0]

                if next_extremity in telomeres:
                    current = next_extremity
                    telomeres.remove(current)
                    chromosome.append(current)
                    linear_chromosomes.append(chromosome)
                    chromosome = []

        # find circular chromosomes
        while len(not_telomeres) > 0:
            current = not_telomeres[0]
            not_telomeres.remove(current)
            chromosome.append(current)

            # find next extremity:
            if current[0] % 1 == 0:
                next_extremity = current[0] + 0.5
            else:
                next_extremity = current[0] - 0.5

            # if it is a single gene chromosome:
            if next_extremity == current[1]:
                ordered_circular_chromosome = []

                circular_chromosomes.append(chromosome)
                chromosome = []

            # go find adjacency cycle
            else:
                adjacency_cycle = Node.find_adjacency_cycle(self, next_extremity, chromosome, not_telomeres)
                next_extremity = adjacency_cycle[0]

                # if at end of circular chromosome
                if next_extremity == chromosome[0][1]:
                    circular_chromosomes.append(chromosome)
                    chromosome = []

        return linear_chromosomes, circular_chromosomes

    def get_legal_operations(self, adjacenciesB):
        """
        This method takes a list of adjacencies for genome B and returns a list of legal operations
        to transform the adjacencies of genome A into genome B.
        
        Parameters:
        - adjacencies_genomeB (list): The list of adjacencies for genome B.
        
        Returns:
        - list_of_legal_operations (list): A list of legal operations to transform genome A to genome B.
        """
        list_of_legal_operations = []
        adjacenciesA = self.state
        adjacenciesB = adjacenciesB

        for element in adjacenciesB:
            if element in adjacenciesA:
                pass
            else:

                adjacenciesA_copy = adjacenciesA[:]

                # if element is an adjacency:
                if type(element) is tuple:
                    p = element[0]
                    q = element[1]
                    u = 0
                    v = 0

                    # if elements containing p and q respectively in a are adjacencies
                    for marker in adjacenciesA_copy:
                        if type(marker) is tuple:
                            if marker[0] == p or marker[1] == p:
                                u = marker

                            if marker[0] == q or marker[1] == q:
                                v = marker

                    # element containing p in A is a telomere
                    if u == 0:
                        u = p
                    # element containing q in A is a telomere
                    if v == 0:
                        v = q

                    if u != v:
                        adjacenciesA_copy.append((p, q))
                        adjacenciesA_copy.remove(u)
                        adjacenciesA_copy.remove(v)

                        # if u is an adjacency:
                        if type(u) is tuple:
                            # calcultate u'p
                            if u[0] == p:
                                u_not_p = u[1]
                            else:
                                u_not_p = u[0]

                            # if v is an adjacency:
                            if type(v) is tuple:
                                # calcultate v'q
                                if v[0] == q:
                                    v_not_q = v[1]
                                else:
                                    v_not_q = v[0]

                                adjacenciesA_copy.append((u_not_p, v_not_q))

                                # order operation before appending
                                if u[0] < v[0]:
                                    op_1 = (u, v)
                                else:
                                    op_1 = (v, u)
                                if p < q:
                                    op_2_1 = (p, q)
                                else:
                                    op_2_1 = (q, p)
                                if u_not_p < v_not_q:
                                    op_2_2 = (u_not_p, v_not_q)
                                else:
                                    op_2_2 = (v_not_q, u_not_p)
                                if op_2_1[0] < op_2_2[0]:
                                    op_2 = (op_2_1, op_2_2)
                                else:
                                    op_2 = (op_2_2, op_2_1)
                                ordered_operation = (op_1, op_2)

                                if ordered_operation not in list_of_legal_operations:
                                    list_of_legal_operations.append((ordered_operation))
                                else:
                                    pass

                            # else v is a telomere
                            else:
                                adjacenciesA_copy.append(u_not_p)

                                if p < q:
                                    op_2_1 = (p, q)
                                else:
                                    op_2_1 = (q, p)

                                op_2 = (op_2_1, u_not_p)
                                ordered_operation = ((u, v), op_2)

                                if ordered_operation not in list_of_legal_operations:
                                    list_of_legal_operations.append((ordered_operation))
                                else:
                                    pass


                        # else u is a telomere
                        else:
                            # if v is an adjacency
                            if type(v) is tuple:
                                # calculate v'q
                                if v[0] == q:
                                    v_not_q = v[1]
                                else:
                                    v_not_q = v[0]
                                adjacenciesA_copy.append(v_not_q)

                                if p < q:
                                    op_2_1 = (p, q)
                                else:
                                    op_2_1 = (q, p)

                                ordered_operation = ((v, u), (op_2_1, v_not_q))

                                if ordered_operation not in list_of_legal_operations:
                                    list_of_legal_operations.append((ordered_operation))
                                else:
                                    pass

                            # else v is a telomere
                            else:
                                if p < q:
                                    op_2 = (p, q)
                                else:
                                    op_2 = (q, p)
                                if u < v:
                                    ordered_operation = (u, v, op_2)
                                else:
                                    ordered_operation = (v, u, op_2)

                                if ordered_operation not in list_of_legal_operations:
                                    list_of_legal_operations.append((ordered_operation))
                                else:
                                    pass

                # else if the element is a telomere
                else:
                    u = 0
                    p = element

                    for marker in adjacenciesA_copy:
                        if type(marker) is tuple:
                            if marker[0] == p or marker[1] == p:
                                u = marker
                    if u == 0:
                        u = p

                    # if u is not a telomere:
                    if u != p:
                        adjacenciesA_copy.append(u[0])
                        adjacenciesA_copy.append(u[1])
                        adjacenciesA_copy.remove(u)
                        operation = ((u), (u[0]), (u[1]))
                        if operation not in list_of_legal_operations:
                            list_of_legal_operations.append((operation))
                        else:
                            pass


        return list_of_legal_operations

    def take_action(self, operation):
        '''
        The method performs a series of operations on a given state based on the input operation.
        it handles different types of operations, including fusion, fission, inversions, translocations, and transpositions.

        Parameters:
        operation: A list representing the operation to be performed on the state.

        Returns:
        A tuple containing the ordered and sorted state after the operation and the type of operation performed.

        Raises:
        ValueError: If the provided operation type is invalid.

        Example:
        
        result, operation_type = take_action(some_operation)

        '''
        state_copy = self.state.copy()
        operation_type = None

        # if it is a fusion or fission:
        if len(operation) == 3:

            # fission
            if type(operation[0]) is tuple:

                state_copy.remove(operation[0])
                state_copy.append(operation[1])
                state_copy.append(operation[2])
                operation_type = 'fis'

            # fusion
            else:
                state_copy.remove(operation[0])
                state_copy.remove(operation[1])

                # ensure gene extremities in correct order for downstream comparisions with genome B extremities
                if operation[2][0] < operation[2][1]:
                    state_copy.append(operation[2])
                else:
                    state_copy.append((operation[2][1], operation[2][0]))

                operation_type = 'fus'

        # else it is another rearrangment
        elif len(operation) == 2:
            # inversions, transpositions, balanced translcations :
            if type(operation[0][0]) is tuple and type(operation[0][1]) is tuple:
                state_copy.remove(operation[0][0])
                state_copy.remove(operation[0][1])

                # ensure gene extremities in correct order for downstream comparision with genome B extremities
                if operation[1][0][0] < operation[1][0][1]:
                    state_copy.append(operation[1][0])
                else:
                    state_copy.append((operation[1][0][1], operation[1][0][0]))

                if operation[1][1][0] < operation[1][1][1]:
                    state_copy.append(operation[1][1])
                else:
                    state_copy.append((operation[1][1][1], operation[1][1][0]))

                #transpositions happen in two steps
                #balanced tranlocations - the adjacencies to cute are on different chromosomes
                #inversions - the adjacencies to cut are on the same chromosome

                # transpositions occur in two steps
                chromosomes = self.find_chromosomes(self.state)
                circular_chromosomes = chromosomes[1]

                # transpotion to end of chromosome
                if len(circular_chromosomes) != 0:
                    operation_type = 'trp_reinsertion'

                else:
                    linear_chromosomes = self.find_chromosomes(self.state)[0]


                    for chromosome in linear_chromosomes:

                        if operation[0][0] in chromosome:
                            test_chromosome = chromosome
                    if operation[0][1] in test_chromosome:
                        operation_type = 'inv'
                    else:
                        operation_type = 'b_trl'



            # unbalanced translocations and intrachromosoma transpositions to end of chromosome or inversion at end of chromosome
            elif type(operation[0][0]) is not tuple or type(operation[0][-1]) is not tuple:

                state_copy.remove(operation[0][0])
                state_copy.remove(operation[0][1])

                # ensure gene extremities in correct order for downstream comparisions with genome B extremities
                if operation[1][0][0] < operation[1][0][1]:
                    state_copy.append(operation[1][0])
                else:
                    state_copy.append((operation[1][0][1], operation[1][0][0]))

                state_copy.append(operation[1][1])

                #transpositions occur in two steps
                chromosomes = self.find_chromosomes(self.state)
                circular_chromosomes = chromosomes[1]

                #transpotion to end of chromosome
                if len(circular_chromosomes) != 0:
                    operation_type = 'trp_reinsertion'

                else:

                    linear_chromosomes = chromosomes[0]

                    for element in operation[0]:
                        if type(element) is tuple:
                            adjacency = element
                        else:
                            telomere = element
                    for chromosome in linear_chromosomes:

                        if adjacency in chromosome:
                            test_chromosome = chromosome
                    if telomere in test_chromosome:
                        operation_type = 'inv'
                    else:

                        operation_type = 'u_trl'


        else:
            # RAISE AN ERROR
            print("Error in take_action function")

        # order and sort
        ordered_and_sorted = Node.order_and_sort(self, state_copy)

        return ordered_and_sorted, operation_type


    def adjacencies_equivalent(self, adjacenciesB):
        """
        Checks if the adjacency lists of two genomes are equivalent.

        Parameters:
        - adjacencies_genomeB (list): The adjacency list of the second genome to compare.

        Returns:
        - bool: True if the adjacency lists are equivalent, False otherwise.
        """
        adjacenciesA = self.state.copy()
        adjacenciesB = adjacenciesB

        ordered_adjacenciesA = []
        for element in adjacenciesA:
            if type(element) is tuple:
                if int(element[0]) < int(element[1]):
                    ordered_adjacenciesA.append(element)
                else:
                    ordered_adjacenciesA.append((element[1], element[0]))
            else:
                ordered_adjacenciesA.append(element)

        for element in adjacenciesB:
            if element in ordered_adjacenciesA:
                pass
            else:
                return False
        return True

    def sorted_adjacencies_and_telomeres(self, adjacencies):
        """
        Sorts gene adjacencies and telomeres and returns the sorted list.

        Args:
        - adjacencies (list): A list containing tuples representing gene adjacencies and other elements representing telomeres.

        Returns:
        - list: A sorted list containing telomeres followed by sorted gene adjacencies.

        Example:
        instance = YourClassName()
        result = instance.sorted_adjacencies_and_telomeres([(1, 2), (3, 1), 'telomere'])
        print(result)
        # Output: ['telomere', (1, 2), (1, 3)]
        ```
        """
        telomeres = []
        gene_adjacencies = []
        for element in adjacencies:
            if type(element) is tuple:

                #if it is a single gene adjacency e.g. (4.5, 4.0)
                if int(element[0]) == int(element[1]):
                    if element[0]%1 == 0:
                       gene_adjacencies.append(element)
                    else:
                        gene_adjacencies.append((element[1], element[0]))

                elif int(element[0]) < int(element[1]):
                   gene_adjacencies.append(element)
                else:
                   gene_adjacencies.append((element[1], element[0]))
            else:
                telomeres.append(element)
        telomeres.sort()
        gene_adjacencies.sort()

        sorted_adjacencies = telomeres + gene_adjacencies

        return sorted_adjacencies
    

    def get_decircularization_operations(self, adjacenciesB):
        """
        Retrieves a list of decircularization operations based on the provided adjacencies for Genome B.

        This method analyzes legal operations for adjacencies_genomeB and identifies decircularization operations, 
        which involve removing adjacency connections from circular chromosomes.

        Parameters:
        - adjacencies_genomeB (list of tuples): Adjacency information for Genome B.

        Returns:
        list: A list of decircularization operations, where each operation is represented as a tuple of two elements.

        Example:
        genome_A = [...]  # Adjacency information for Genome A
        genome_B = [...]  # Adjacency information for Genome B
        obj = YourClass(genome_A)
        decircular_ops = obj.get_decircularization_operations(genome_B)
        

        Note:
        Circular chromosomes are identified based on the circular_chromosomes attribute of the object.

        Legal operations are obtained using the get_legal_operations method of the object.

        Decircularization operations are those where at least one of the involved chromosomes is circular, 
        and the adjacency connection is being removed.

        The returned list contains tuples representing the decircularization operations.

        """

        operations = [operation for operation in self.get_legal_operations(adjacenciesB) if len(operation)==2]


        decircularization_operations = []


        for operation in operations:

            if operation[0][0] in self.circular_chromosomes[0] and operation[0][1] in self.circular_chromosomes[0]:
                pass
            elif operation[0][0] in self.circular_chromosomes[0] or operation[0][1] in self.circular_chromosomes[0]:
                decircularization_operations.append(operation)
            else:
                pass

        return decircularization_operations
