import Gen_xtremities


class Node:

    def __init__(self, state=None):
        self.state = []
        self.children = []
        self.children_weights = []
        self.children_operations = []
        self.linear_chromosomes = []
        self.next_operation = 0
        self.next_operation_weight = 1
        self.join_adjacency = 0

        get_chromosomes = Node.find_chromosomes(self, self.state)
        self.linear_chromosomes = get_chromosomes


    # The function returns a list  of the operations needed to transform the genomes the
    # source  genome to the target genome

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
                    x = element[0]
                    y = element[1]
                    w = 0
                    z = 0

                    # if elements containing x and y respectively  are adjacencies
                    for marker in adjacenciesA_copy:
                        if type(marker) is tuple:
                            if marker[0] == x or marker[1] == x:
                                w = marker

                            if marker[0] == y or marker[1] == y:
                                z = marker

                    # element containing x in adjacenciesA is a telomere
                    if w == 0:
                        w = x
                    # element containing y in adjacenciesA is a telomere
                    if z == 0:
                        z = y

                    if w != z:
                        adjacenciesA_copy.append((x, y))
                        adjacenciesA_copy.remove(w)

                        adjacenciesA_copy.remove(z)

                        # if w is an adjacency:
                        if type(w) is tuple:
                            # calculate w'x
                            if w[0] == x:
                                w_not_x = w[1]
                            else:
                                w_not_x = w[0]

                            # if z is an adjacency:
                            if type(z) is tuple:
                                # calculate z'y
                                if z[0] == y:
                                    z_not_y = z[1]
                                else:
                                    z_not_y = z[0]

                                adjacenciesA_copy.append((w_not_x, z_not_y))

                                # order operation before appending
                                if w[0] < z[0]:
                                    op_1 = (w, z)
                                else:
                                    op_1 = (z, w)
                                if x < y:
                                    op_2_1 = (x, y)
                                else:
                                    op_2_1 = (y, x)
                                if w_not_x < z_not_y:
                                    op_2_2 = (w_not_x, z_not_y)
                                else:
                                    op_2_2 = (z_not_y, w_not_x)
                                if op_2_1[0] < op_2_2[0]:
                                    op_2 = (op_2_1, op_2_2)
                                else:
                                    op_2 = (op_2_2, op_2_1)
                                ordered_operation = (op_1, op_2)

                                if ordered_operation not in list_of_legal_operations:
                                    list_of_legal_operations.append(ordered_operation)
                                else:
                                    pass

                            # else z is a telomere
                            else:
                                adjacenciesA_copy.append(w_not_x)

                                if x < y:
                                    op_2_1 = (x, y)
                                else:
                                    op_2_1 = (y, x)

                                op_2 = (op_2_1, w_not_x)
                                ordered_operation = ((w, z), op_2)

                                if ordered_operation not in list_of_legal_operations:
                                    list_of_legal_operations.append(ordered_operation)
                                else:
                                    pass

                        # else w is a telomere
                        else:
                            # if z is an adjacency
                            if type(z) is tuple:
                                # calculate z'y
                                if z[0] == y:
                                    z_not_y = z[1]
                                else:
                                    z_not_y = z[0]
                                adjacenciesA_copy.append(z_not_y)

                                if x < y:
                                    op_2_1 = (x, y)
                                else:
                                    op_2_1 = (y, x)

                                ordered_operation = ((z, w), (op_2_1, z_not_y))

                                if ordered_operation not in list_of_legal_operations:
                                    list_of_legal_operations.append(ordered_operation)
                                else:
                                    pass

                            # else z is a telomere
                            else:
                                if x < y:
                                    op_2 = (x, y)
                                else:
                                    op_2 = (y, x)
                                if w < z:
                                    ordered_operation = (w, z, op_2)
                                else:
                                    ordered_operation = (z, w, op_2)

                                if ordered_operation not in list_of_legal_operations:
                                    list_of_legal_operations.append(ordered_operation)
                                else:
                                    pass

                # else if the element is a telomere
                else:
                    w = 0
                    x = element

                    for marker in adjacenciesA_copy:
                        if type(marker) is tuple:
                            if marker[0] == x or marker[1] == x:
                                w = marker
                    if w == 0:
                        w = x

                    # if w is not a telomere:
                    if w != x:
                        adjacenciesA_copy.append(w[0])
                        adjacenciesA_copy.append(w[1])
                        adjacenciesA_copy.remove(w)
                        operation = (w, (w[0]), (w[1]))
                        if operation not in list_of_legal_operations:
                            list_of_legal_operations.append(operation)
                        else:
                            pass
                    else:
                        #incomplete
                        pass
                        

        return list_of_legal_operations

    def take_action(self, operation):
        state_copy = self.state.copy()
        operation_type = []

        # if it is an insertion or deletion:
        if len(operation) == 1:

            # insertion
            if type(operation[0]) is tuple:

                state_copy.append(operation[0])
                operation_type = 'ins'

            else:
                state_copy.remove(operation[0])
                operation_type = "del_"

            # else it is another structural event
        elif len(operation) == 2:
            if type(operation[0][0]) is tuple and type(operation[0][1]) is tuple:
                state_copy.append(operation[0][0])
                state_copy.append(operation[1][0])
                operation_type = "dup_"

            elif type(operation[0][0]) is not tuple or type(operation[0][1]) is not tuple:
                state_copy.remove(operation[0][0])
                state_copy.remove(operation[0][1])
                operation_type = "del_"

        elif len(operation) == 3:
            if type(operation[0][1][2]) is tuple and type(operation[1][0[2]]) is tuple:
                state_copy.append(operation[0][2])
                state_copy.append(operation[2][2])
                state_copy.remove(operation[0][1])
                state_copy.remove(operation[0][0])
                operation_type = "fDNA"

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
        telomers = []
        adjs = []
        for element in adjacencies:
            if type(element) is tuple:

                # if it is a single gene adjacency
                if int(element[0]) == int(element[1]):
                    if element[0] % 1 == 0:
                        adjs.append(element)
                    else:
                        adjs.append((element[1], element[0]))

                elif int(element[0]) < int(element[1]):
                    adjs.append(element)
                else:
                    adjs.append((element[1], element[0]))
            else:
                telomers.append(element)
        telomers.sort()
        adjs.sort()

        sort = telomers + adjs

        return sort, telomers, adjs


# if __name__ == '__main__':
#     gen_ex_obj = Gen_xtremities.Xtremities()
#     genome_gene_extremities = gen_ex_obj.gene_extremity()
