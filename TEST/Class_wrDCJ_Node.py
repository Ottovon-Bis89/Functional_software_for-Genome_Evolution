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
        for element in not_telomeres:
            if element[0] == next_extremity or element[1] == next_extremity:
                current = element
                chromosome.append(current)
                not_telomeres.remove(current)
                next_extremity = Node.find_next_extremity(self, current, next_extremity)
                return next_extremity, chromosome, not_telomeres
        return [next_extremity]

    def find_adjacency_cycle(self, next_extremity, chromosome, not_telomeres):

        next_adjacency = Node.find_next_adjacency(self, next_extremity, chromosome, not_telomeres)

        while len(next_adjacency) != 1:
            next_extremity = next_adjacency[0]
            next_adjacency = Node.find_next_adjacency(self, next_extremity, chromosome, not_telomeres)
        else:
            next_extremity = next_adjacency[0]

            return next_extremity, chromosome, not_telomeres

    def find_chromosomes(self, adjacencies):

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


    def is_equivalent(self, adjacenciesB):
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

    def order_and_sort(self, adjacencies):
        telomeres = []
        adjs = []
        for element in adjacencies:
            if type(element) is tuple:

                #if it is a single gene adjacency e.g. (4.5, 4.0)
                if int(element[0]) == int(element[1]):
                    if element[0]%1 == 0:
                        adjs.append(element)
                    else:
                        adjs.append((element[1], element[0]))

                elif int(element[0]) < int(element[1]):
                    adjs.append(element)
                else:
                    adjs.append((element[1], element[0]))
            else:
                telomeres.append(element)
        telomeres.sort()
        adjs.sort()

        sort = telomeres + adjs


        return sort

    def get_reinsertion_operations(self, adjacenciesB):

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
