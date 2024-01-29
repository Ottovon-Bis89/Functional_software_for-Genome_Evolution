class Node:

    def __init__(self, state=None):
        self.state = state
        self.children = []
        self.children_weights = []
        self.children_operations = []
        self.linear_chromosomes = []
        self.circular_chromosomes = []
        self.next_operation = 0
        self.next_operation_weight = 1
        self.join_adjacency = 0

        # Find chromosomes and store them in instance variables
        get_chromosomes = Node.find_chromosomes(self, self.state)
        self.linear_chromosomes = get_chromosomes[0]
        self.circular_chromosomes = get_chromosomes[1]

    def find_next_extremity(self, current, next_extremity):
         # Determine which element of the current extremity tuple is the next extremity to be reached
        if current[0] == next_extremity:  
        # Determine the value of the next extremity based on whether the current extremity element is an integer or not
            if current[1] % 1 == 0:
                next = current[1] + 0.5  #If current is an integer, set next_extremity as current + 0.5
            else:
                next = current[1] - 0.5  # If current is not an integer, set next_extremity as current - 0.5
         # Check if the first element of current is an integer (has no fractional part)
        else:
            if current[0] % 1 == 0: 
                next = current[0] + 0.5   #If current is an integer, set next_extremity as current + 0.5
            else:
                next = current[0] - 0.5    # If current is not an integer, set next_extremity as current - 0.5

        #return the next extremity
        return next


    def find_next_adjacency(self, next_extremity, chromosome, not_telomeres):
        # iterate over each element in not_telomeres along with its index
        for element in not_telomeres:  
         # if either the start or second element is the next extremity
            if element[0] == next_extremity or element[1] == next_extremity:
                current = element
            # add the current adjacency to the chromosome
                chromosome.append(current)
                not_telomeres.remove(current)  # remove the current element from not_telomeres based on its index
                 # update the next extremity to be the end of the current adjacency
                next_extremity = Node.find_next_extremity(self, current, next_extremity)  

                return next_extremity, chromosome, not_telomeres    # return the updated values of next extremity, chromosome, and not_telomeres
        return [next_extremity]   # if no adjacent element was found, return the current next extremity



    def find_adjacency_cycle(self, next_extremity, chromosome, not_telomeres):
        # Find the next adjacency in the cycle
        next_adjacency = Node.find_next_adjacency(self, next_extremity, chromosome, not_telomeres)

        # Loop until the length of next_adjacency is not equal to 1
        while len(next_adjacency) != 1:

            next_extremity = next_adjacency[0]   # Set next_extremity as the first element of next_adjacency

         # Find the next adjacency based on next_extremity
            next_adjacency = Node.find_next_adjacency(self, next_extremity, chromosome, not_telomeres)

        # If the length of next_adjacency becomes 1
        else:
            next_extremity = next_adjacency[0]   # Set next_extremity as the first element of next_adjacency

            # Return the values of next_extremity, chromosome, and not_telomeres
            return next_extremity, chromosome, not_telomeres 



    def find_chromosomes(self, adjacencies):
         # Separate telomeres and not telomeres
        telomeres = [element for element in adjacencies if type(element) is not tuple]
        not_telomeres = [element for element in adjacencies if type(element) is tuple]

         # Initialize output lists for chromosome, linear chromosome and circular chromosome
        linear_chromosomes = []
        circular_chromosomes = []
        chromosome = []
        i = 0

        # Find linear chromosomes from the telomeres list
        # Loop until the length of telomeres is greater than 0
        while len(telomeres) > 0:

            i += 1    # Increment the counter i
            current = telomeres[0]  # Get the first element from the telomeres list

            telomeres.remove(current)  # Remove the current element from the telomeres list
            chromosome.append(current)  # Append the current element to the chromosome list

            # Get the next extremity
            if current % 1 == 0:   # Check if the current value is an integer (has no fractional part)
                next_extremity = current + 0.5   # If current is an integer, set next_extremity as current + 0.5
            else:
                next_extremity = current - 0.5   # If current is not an integer, set next_extremity as current - 0.5

           # If single gene chromosome, check if its linear or circular chromosome
            if next_extremity in telomeres:  # Check if next_extremity is present in the telomeres list
                current = next_extremity     # Set current as next_extremity

                telomeres.remove(current)    # Remove the current element from the telomeres list
                chromosome.append(current)   # Append the current element to the chromosome list
                linear_chromosomes.append(chromosome)  # Append the current chromosome to the linear_chromosomes list
                chromosome = []  # Reset the chromosome list to an empty list

           # If next_extremity is not present in the telomeres list, find the adjacency cycle
            else:
                adjacency_cycle = Node.find_adjacency_cycle(self, next_extremity, chromosome, not_telomeres)
                next_extremity = adjacency_cycle[0]   # Update next_extremity with the first element of the adjacency cycle

                if next_extremity in telomeres:  # Check if the updated next_extremity is present in the telomeres list
                    current = next_extremity     # Set current as next_extremity
                    telomeres.remove(current)    # Remove the current element from the telomeres list
                    chromosome.append(current)   # Append the current element to the chromosome list
                    linear_chromosomes.append(chromosome)   # Append the current chromosome to the linear_chromosomes list
                    chromosome = []  # Reset the chromosome list to an empty list

        # Find circular chromosomes from the not telomeres list
        while len(not_telomeres) > 0: #Loop until the length of not_telomeres is greater than 0
            current = not_telomeres[0]  # Get the first element from the not_telomeres list
            not_telomeres.remove(current)  # Remove the current element from the not_telomeres list
            chromosome.append(current)     # Append the current element to the chromosome list

          # Check if the first element of current is an integer (has no fractional part)
            if current[0] % 1 == 0:
                next_extremity = current[0] + 0.5   # If the first element is an integer, set next_extremity as current[0] + 0.5
            else:
                next_extremity = current[0] - 0.5    # If the first element is not an integer, set next_extremity as current[0] - 0.5

            # If single gene chromosome, check if it is a circular chromosome.
            if next_extremity == current[1]:   # Check if next_extremity is equal to the second element of current
                circular_chromosomes.append(chromosome)  # Append the current chromosome to the circular_chromosomes list
                chromosome = []  # Reset the chromosome list to an empty list

           # If next_extremity is not equal to the second element of current, find adjacency cycle
            else:
            # Find the adjacency cycle based on next_extremity, chromosome, and not_telomeres
                adjacency_cycle = Node.find_adjacency_cycle(self, next_extremity, chromosome, not_telomeres)
                next_extremity = adjacency_cycle[0]  # Update next_extremity with the first element of the adjacency cycle

                # if at end of circular chromosome, Check if next_extremity is equal to the second element of the first gene in the chromosome
                if next_extremity == chromosome[0][1]:  

                    circular_chromosomes.append(chromosome)  # Append the current chromosome to the circular_chromosomes list
                    chromosome = []  # Reset the chromosome list to an empty list

        # Return the linear_chromosomes and circular_chromosomes lists
        return linear_chromosomes, circular_chromosomes

   

    def get_legal_operations(self, adjacencies_genomeB):
        list_of_legal_operations = []  # Create an empty list to store the legal operations
        adjacencies_genomeA = self.state  # Copy the contents of self.state to adjacencies_genomeA
        adjacencies_genomeB = adjacencies_genomeB # Copy the contents of adjacencies_genomeB to adjacencies_genomeB

        # Iterate over each element in adjacencies_genomeB
        for element in adjacencies_genomeB:
        
        # Check if the element is present in adjacencies_genomeA, If the element is already in adjacenciesA, do nothing
            if element in adjacencies_genomeA:
                pass  # If it is present, do nothing and continue to the next element

            # If the element is not in adjacenciesA, create a copy of adjacencies_genomeA using the slice operator
            else:
            
                adjacencies_genomeA_copy = adjacencies_genomeA[:]

                # If the element is an adjacency
                if type(element) is tuple:
                    p, q = element[0], element[1]  #Extract the values p and q from the adjacency tuple
                    u, v = 0, 0  # Initialize variables u and v

                     # Check if the elements containing p and q respectively in adjacenciesA are adjacencies
                    for marker in adjacencies_genomeA_copy:
                        if type(marker) is tuple:
                            if marker[0] == p or marker[1] == p:   # Check if either marker position matches p
                                u = marker  # Set u to the current marker

                            if marker[0] == q or marker[1] == q:  # Check if either marker position matches q
                                v = marker   # Set v to the current marker

                     # If the element containing p in adjacenciesA is a telomere, set u to p
                    if u == 0:
                        u = p
                    # If the element containing q in adjacenciesA is a telomere, set v to q
                    if v == 0:
                        v = q

                    if u != v:   # If u and v are not equal

                        # Add the adjacency (p,q) to adjacenciesA_copy list
                        adjacencies_genomeA_copy.append((p, q))
                        # Remove u and v from adjacenciesA_copy
                        adjacencies_genomeA_copy.remove(u)
                        
                        adjacencies_genomeA_copy.remove(v)

                         # Check if u is an adjacency
                        if type(u) is tuple:
                           # Calculate u'p based on the position of p in the adjacency tuple
                            if u[0] == p:
                                u_not_p = u[1]
                            else:
                                u_not_p = u[0]

                             # Check if v is an adjacency
                            if type(v) is tuple:

                             #Calculate v'q based on the position of q in the adjacency tuple
                                if v[0] == q:
                                    v_not_q = v[1]
                                else:
                                    v_not_q = v[0]

                            # Add the adjacency (u'p, v'q) to adjacenciesA_copy list
                                adjacencies_genomeA_copy.append((u_not_p, v_not_q))


                               # Order the operations before appending to list_of_legal_operations
                                op_1 = (u, v) if u[0] < v[0] else (v, u)
                                op_2_1 = (p, q) if p < q else (q, p)
                                op_2_2 = (u_not_p, v_not_q) if u_not_p < v_not_q else (v_not_q, u_not_p)
                                op_2 = (op_2_1, op_2_2) if op_2_1[0] < op_2_2[0] else (op_2_2, op_2_1)
                                ordered_operation = (op_1, op_2)

                            # Append the ordered operation to list_of_legal_operations if it's not already in the list
                                if ordered_operation not in list_of_legal_operations:
                                    list_of_legal_operations.append(ordered_operation)
                                else:
                                    pass

                            # else v is a telomere
                            else:
                                adjacencies_genomeA_copy.append(u_not_p)  # Add u'p to the adjacenciesA_copy list

                             # Determine the correct order of p and q based on their values
                                if p < q:
                                    op_2_1 = (p, q)
                                else:
                                    op_2_1 = (q, p)

                                op_2 = (op_2_1, u_not_p)  # Create the operation op_2 as a tuple of (op_2_1, u_not_p)
                                ordered_operation = ((u, v), op_2)   # Create the ordered operation op_2 

                                if ordered_operation not in list_of_legal_operations:  # Check if the ordered_operation is not already in the list_of_legal_operations
                                    list_of_legal_operations.append((ordered_operation))  # Add the ordered_operation to the list_of_legal_operations
                                else:
                                    pass


                         # check if  u is a telomere
                        else:
                            # if v is an adjacency
                            if type(v) is tuple:

                                #Calculate v'q based on the position of q in the adjacency tuple
                                if v[0] == q:
                                    v_not_q = v[1]
                                else:
                                    v_not_q = v[0]
                                adjacencies_genomeA_copy.append(v_not_q)    # Add v'q to the adjacenciesA_copy list

                            # Determine the correct order of p and q based on their values
                                if p < q:
                                    op_2_1 = (p, q)
                                else:
                                    op_2_1 = (q, p)

                                ordered_operation = ((v, u), (op_2_1, v_not_q))  # Create the ordered_operation as a tuple of ((v, u), (op_2_1, v_not_q))

                                if ordered_operation not in list_of_legal_operations:  # Check if the ordered_operation is not already in the list_of_legal_operations
                                    list_of_legal_operations.append(ordered_operation)  # Add the ordered_operation to the list_of_legal_operations
                                else:
                                    pass

                            #check if v is a telomere
                            else:
                             # Determine the correct order of p and q based on their values
                                if p < q:
                                    op_2 = (p, q)
                                else:
                                    op_2 = (q, p)

                                # Determine the correct order of u and v based on their values  
                                if u < v:
                                    ordered_operation = (u, v, op_2)
                                else:
                                    ordered_operation = (v, u, op_2)

                                if ordered_operation not in list_of_legal_operations:   #Check if the ordered_operation is not already in the list_of_legal_operations
                                    list_of_legal_operations.append((ordered_operation))  # Add the ordered_operation to the list_of_legal_operations
                                else:
                                    pass

               # else check if the element is a telomere
                else:
                # Initialize u and p variables  
                    u = 0
                    p = element

                    for marker in adjacencies_genomeA_copy:  # Search for u in adjacencies_genomeA_copy
                     # Check if marker is an adjacency tuple and if it shares a gene with p
                        if type(marker) is tuple: 
                            if marker[0] == p or marker[1] == p:
                                u = marker
                  # If u is still 0, assign u as p                   
                    if u == 0:
                        u = p

                   # Check if u is not a telomere
                    if u != p:
                     #Add u's genes to adjacencies_genomeA_copy and remove u
                        adjacencies_genomeA_copy.append(u[0])
                        adjacencies_genomeA_copy.append(u[1])
                        adjacencies_genomeA_copy.remove(u)

                        operation = ((u), (u[0]), (u[1]))  # Create the operation as a tuple with u, u[0], and u[1]
                        if operation not in list_of_legal_operations: # Check if the operation is not already in the list_of_legal_operations
                            list_of_legal_operations.append((operation)) # Add the operation to the list_of_legal_operations
                        else:
                            pass
     # Return the list_of_legal_operations
        return list_of_legal_operations


    def take_action(self, operation):
    
        # Make a copy of the current state
        state_copy = self.state.copy()
        # Initialize the operation type as None
        operation_type = None

        # if it is a fusion or fission:
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

                # ensure gene extremities in correct order for downstream comparisions with genome B extremities
                if operation[2][0] < operation[2][1]:  # Check the order of the genes in the third element of the operation
                    state_copy.append(operation[2])     # Append the genes as they are to state_copy
                else:
                    state_copy.append((operation[2][1], operation[2][0]))  # Append the genes with reversed order to state_copy


                operation_type = 'fus'   # Set the operation type to 'fus'

         # If the operation is another rearrangement
        elif len(operation) == 2:
             # If it is an inversion, transposition, or balanced translocation
            if type(operation[0][0]) is tuple and type(operation[0][1]) is tuple:
            
              # Remove the first and second tuples from the state
                state_copy.remove(operation[0][0])
                state_copy.remove(operation[0][1])

                # ensure gene extremities in correct order for downstream comparision with genome B extremities
                if operation[1][0][0] < operation[1][0][1]: # Check the order of the first gene in the second element of the operation
                    state_copy.append(operation[1][0])  # Append the first gene as it is to state_copy
                else:
                    state_copy.append((operation[1][0][1], operation[1][0][0]))  # Append the first gene with reversed order to state_copy

                if operation[1][1][0] < operation[1][1][1]: # Check the order of the second gene in the second element of the operation
                    state_copy.append(operation[1][1])  # Append the second gene as it is to state_copy
                else:
                    state_copy.append((operation[1][1][1], operation[1][1][0]))   # Append the second gene with reversed order to state_copy


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
                    linear_chromosomes = self.find_chromosomes(self.state)[0]

                # Find the chromosome that contains the first gene in the first tuple of the operation
                    for chromosome in linear_chromosomes:
                        if operation[0][0] in chromosome:
                            test_chromosome = chromosome

                # If the second gene in the first tuple of the operation is also in the test chromosome,
                    # the operation is an inversion
                    if operation[0][1] in test_chromosome:
                        operation_type = 'inv'
                    else:
                 # Otherwise, it is a balanced translocation
                        operation_type = 'b_trl'

             # check if operation is a translocation or intrachromosomal transposition to end of chromosome or inversion at end of chromosome
            elif type(operation[0][0]) is not tuple or type(operation[0][-1]) is not tuple:   # Check if the type of the first element in the operation is not a tuple or the type of the last element is not a tuple
            
              # remove genes being modified from current state in state_copy
                state_copy.remove(operation[0][0])
                state_copy.remove(operation[0][1])

               # ensure gene extremities in correct order for downstream comparisons with genome B extremities
                if operation[1][0][0] < operation[1][0][1]:
                    state_copy.append(operation[1][0])  # Append the first gene from the second element of the operation as it is to state_copy
                else:
                    state_copy.append((operation[1][0][1], operation[1][0][0]))  # Append the first gene with reversed order to state_copy
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
                        if type(element) is tuple:   # Check if the type of the element is a tuple
                            adjacency = element
                        else:
                            telomere = element

                 # find chromosome containing adjacency
                    for chromosome in linear_chromosomes: # Iterate over the chromosomes in linear_chromosomes

                        if adjacency in chromosome:  # Check if the adjacency is present in the chromosome
                            test_chromosome = chromosome     # Assign the chromosome to the variable "test_chromosome"
                
                # determine if operation is an inversion or unbalanced translocation
                    if telomere in test_chromosome:  # Check if the telomere is present in the test_chromosome
                        operation_type = 'inv'   # Set the operation type as 'inv'
                    else:

                        operation_type = 'u_trl' # Set the operation type as 'u_trl'


        else:
            # raise an error if operation is not valid
            raise ValueError("Invalid operation type")

       # order and sort the modified state of the node
        ordered_and_sorted = Node.sorted_adjacencies_and_telomeres(self, state_copy)

        # return the modified state and the type of operation performed
        return ordered_and_sorted, operation_type

    def adjacencies_equivalent(self, adjacencies_genomeB):
        # create a copy of adjacencies_genomeA (the current node's state) and adjacencies_genomeB (the input state)
        adjacencies_genomeA = self.state.copy()
        adjacencies_genomeB = adjacencies_genomeB

        # order the adjacencies in adjacencies_genomeA and store them in ordered_adjacencies_genomeA
        ordered_adjacencies_genomeA = []
        for element in adjacencies_genomeA:
            if type(element) is tuple:
                # if the adjacency is a tuple, sort the tuple and append it to ordered_adjacencies_genomeA
                if int(element[0]) < int(element[1]):
                    ordered_adjacencies_genomeA.append(element)
                else:
                    ordered_adjacencies_genomeA.append(element[1], element[0])
            else:
                # if the adjacency is not a tuple, append it to ordered_adjacencies_genomeA
                ordered_adjacencies_genomeA.append(element)

        # compare each adjacency in adjacencies_genomeB with ordered_adjacencies_genomeA
        for element in adjacencies_genomeB:
            if element in ordered_adjacencies_genomeA:
                # if the adjacency is in ordered_adjacencies_genomeA, do nothing and continue to the next adjacency
                pass
            else:
                # if the adjacency is not in ordered_adjacencies_genomeA, the states are not equivalent, so return False
                return False
        # if all adjacencies in adjacencies_genomeB are in ordered_adjacencies_genomeA, the states are equivalent, so return True
        return True


    def sorted_adjacencies_and_telomeres(self, adjacencies):

        # initialize empty lists for telomeres and gene adjacencies
        telomeres = []
        gene_adjacencies = []

         # Separate gene adjacencies and telomeres
        for element in adjacencies:
            if type(element) is tuple:

                # if it is a single gene adjacency e.g. (5.5, 5.0)
                if int(element[0]) == int(element[1]):
                    if element[0] % 1 == 0:
                        gene_adjacencies.append(element)
                    else:
                        gene_adjacencies.append((element[1], element[0]))

                 # If it is a regular gene adjacency e.g. (5.0, 6.0)
                elif int(element[0]) < int(element[1]):
                    gene_adjacencies.append(element)
                else:
                    gene_adjacencies.append((element[1], element[0]))
            else:
                telomeres.append(element)
         #Sort telomeres and gene adjacencies
        telomeres.sort()
        gene_adjacencies.sort()

        # Concatenate and return the sorted list
        sorted_adjacencies = telomeres + gene_adjacencies

        return sorted_adjacencies



    def get_decircularization_operations(self, adjacencies_genomeB):
        # get all legal operations
        operations = [operation for operation in self.get_legal_operations(adjacencies_genomeB) if len(operation) == 2]

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
        #Return decircularization operations
        return decircularization_operations
