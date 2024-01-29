import random
from Class_extremities_and_adjacencies import Extremities_and_adjacencies
import time

class Evolve:

    def __init__(self, target_genome):
        get_adjacencies_and_chromosomes = Extremities_and_adjacencies()
        self.state = get_adjacencies_and_chromosomes.create_adjacency_list(target_genome)


    def evolve_with_random_rearrangements(self, number_of_rearrangements):
        rearrangements = ['inv', 'trp', 'b_trl', 'u_trl', 'fus', 'fis']
        get_adjacencies_and_chromosomes = Extremities_and_adjacencies()
        #genome_adjacencies = get_adjacencies_and_chromosomes.create_adjacency_list(target_genome)

        rearrangement_series = []

        while number_of_rearrangements>0:
            #print('NUMBER OF REARRANGEMENTS: ', number_of_rearrangements)
            chromosomes = get_adjacencies_and_chromosomes.find_chromosomes(self.state)

            linear_chromosomes = chromosomes[0]
            if len(chromosomes[0]) < 2: #if it is a single chromosome genome
                if len(chromosomes[0][0]) < 5:
                    operation = 'inv'

                else:
                    chr_lens = [len(x) for x in linear_chromosomes]

                    if max(chr_lens) < 4:
                        operation = 'inv'
                    else:
                        operation = random.choice(['inv', 'trp'])

           # elif len(chromosomes[0]) == 2 and (len(chromosomes[0][0])==2 or len(chromosomes[0][1])==2): # if the genome consists of two chromosomes but one chromosomes is a single gene chromosome
            #    operation = random.choice(['inv', 'trp', 'u_trl', 'fis', 'fus'])
            else:
                chr_lens = [len(x) for x in linear_chromosomes]
                chrm_longer_than_2_SB = [x for x in chr_lens if x > 3]
                chrm_longer_than_1_SB = [x for x in chr_lens if x > 2]

                if len(chrm_longer_than_2_SB) < 2: #cannot be trp
                    if len(chrm_longer_than_1_SB) < 2: #cannot be b_trl:
                        if len(chrm_longer_than_1_SB) < 1: #cannot be u_trl, fis, inv
                            operation = 'fus'
                        else:
                            operation = random.choice(['inv', 'u_trl', 'fus', 'fis'])
                    else:
                        operation = random.choice(['inv', 'b_trl', 'u_trl', 'fus', 'fis'])
                else:
                   operation = random.choice(rearrangements)



                # if max(chr_lens) < 4: #cannot be trp
                #     number_of_chromosomes_with_more_than_one_sequence_block = 0
                #     for element in chr_lens:
                #         if element > 2:
                #             number_of_chromosomes_with_more_than_one_sequence_block+=1
                #     if number_of_chromosomes_with_more_than_one_sequence_block >= 2:
                #         operation = random.choice(['inv', 'b_trl' ,'u_trl', 'fis', 'fus'])
                #     else:
                #         operation = random.choice(['inv', 'u_trl', 'fis', 'fus'])
                # else:
                #     number_of_chromosomes_with_more_than_one_sequence_block = 0
                #     for element in chr_lens:
                #         if element > 2:
                #             number_of_chromosomes_with_more_than_one_sequence_block += 1
                #     if number_of_chromosomes_with_more_than_one_sequence_block >= 2:
                #         operation = random.choice(['inv', 'trp','b_trl', 'u_trl', 'fis', 'fus'])
                #     else:
                #         operation = random.choice(['inv', 'trp','u_trl', 'fis', 'fus'])
                #





                # number_of_chromosomes_with_more_than_one_sequence_block = 0
                #
                # for element in chromosomes[0]:
                #     if len(element) > 2:
                #         number_of_chromosomes_with_more_than_one_sequence_block+=1
                # if number_of_chromosomes_with_more_than_one_sequence_block >= 2:
                #     operation = random.choice(rearrangements)
                # else:
                #     operation = random.choice(['inv', 'trp', 'u_trl', 'fis', 'fus'])

            if operation == 'inv':
                execution = self.inversion(linear_chromosomes)
                #print('REACHES THIS POINT')
                rearrangement_series.append(execution)
                number_of_rearrangements -= 1
                #print('NUMBER OF REARRANGEMENTS after: ', number_of_rearrangements)

            elif operation == 'trp':
                execution = self.transposition(linear_chromosomes)
                for element in execution:
                    rearrangement_series.append(element)
                number_of_rearrangements -=1

            elif operation == 'b_trl':
                execution = self.balanced_translocation(linear_chromosomes)
                rearrangement_series.append(execution)
                number_of_rearrangements -=1

            elif operation == 'u_trl':
                execution = self.unbalanced_translocation(linear_chromosomes)
                rearrangement_series.append(execution)
                number_of_rearrangements -=1

            elif operation == 'fus':
                execution = self.fusion(linear_chromosomes)
                rearrangement_series.append(execution)
                number_of_rearrangements -=1

            elif operation == 'fis':
                execution = self.fission(linear_chromosomes)
                rearrangement_series.append(execution)
                number_of_rearrangements -=1

        return rearrangement_series

    def evolve_with_set_rearrangments(self, target_genome, inv, trp, b_trl, u_trl, fus, fis):
        pass

    def inversion(self, linear_chromosomes):




        get_adjacencies_and_chromosomes = Extremities_and_adjacencies()

        chromosome_number = random.randint(0, len(linear_chromosomes) - 1)
        chromosome = linear_chromosomes[chromosome_number]
        #print('the chromosome: ', chromosome)
        chromosome_length = len(chromosome)
        #print('chromosome length: ', chromosome_length)


        to_exclude = []

       # print('CHROMOSOMES Before Inversion: ', get_adjacencies_and_chromosomes.find_chromosomes(self.state))

        while chromosome_length < 3:


            to_exclude.append(linear_chromosomes.index(chromosome))
         #   print('Inversion')
         #   print('THE LIST: ', [i for i in range(0, len(linear_chromosomes)) if i not in to_exclude])
         #   print(linear_chromosomes)
            chromosome_number = random.choice([i for i in range(0, len(linear_chromosomes)) if i not in to_exclude])
            chromosome = linear_chromosomes[chromosome_number]
            chromosome_length = len(chromosome)

        if chromosome_length == 3:
            #print('is executing')

            adjacencies = [element for element in chromosome if type(element) is tuple]
            telomeres = [element for element in chromosome if type(element) is not tuple]

            adj = adjacencies[0]
            telo = random.choice(telomeres)
            if int(telo) == int(adj[0]):
                if telo < adj[1]:
                    new_adj = (telo, adj[1])
                else:
                    new_adj = (adj[1], telo)
                new_telo = adj[0]

            else:
                if telo < adj[0]:
                    new_adj = (telo, adj[0])
                else:
                    new_adj = (adj[0], telo)
                new_telo = adj[1]
            operationA = (adj, telo)
            operationB = (new_adj, new_telo)

            self.state.remove(adj)
            self.state.remove(telo)
            self.state.append(new_adj)
            self.state.append(new_telo)

            operation = (operationA, operationB, 'inv')
            intermediate = self.state
           # print('operation: ', operation)
           ## print('done')

        else:

            try:
                adjacencies = [element for element in chromosome if type(element) is tuple]
            except:
                print('There were not any chromosomes with more than 2 sequence blocks')

            adj1_num = random.randint(0, len(adjacencies) - 1)
            adj2_num = random.randint(0, len(adjacencies) - 1)

            while adj1_num == adj2_num:
                adj2_num = random.randint(0, len(adjacencies) - 1)

            adj1 = adjacencies[adj1_num]
            adj2 = adjacencies[adj2_num]

            #order extremities in the adjacency tuple
            if adj1[0] < adj2[0]:
                new_adj1 = (adj1[0], adj2[0])
            else:
                new_adj1 = (adj2[0], adj1[0])

            if adj1[1] < adj2[1]:
                new_adj2 = (adj1[1], adj2[1])
            else:
                new_adj2 = (adj2[1], adj1[1])

            #perform_operation
            self.state.remove(adj1)
            self.state.remove(adj2)
            self.state.append(new_adj1)
            self.state.append(new_adj2)

            chromosomes = get_adjacencies_and_chromosomes.find_chromosomes(self.state)
            if len(chromosomes[1]) != 0:

                #reverse operation
                self.state.append(adj1)
                self.state.append(adj2)
                self.state.remove(new_adj1)
                self.state.remove(new_adj2)

                # order extremities in the adjacency tuple
                if adj1[0] < adj2[1]:
                    new_adj1 = (adj1[0], adj2[1])
                else:
                    new_adj1 = (adj2[1], adj1[0])

                if adj1[1] < adj2[0]:
                    new_adj2 = (adj1[1], adj2[0])
                else:
                    new_adj2 = (adj2[0], adj1[1])

                # perform_operation
                self.state.remove(adj1)
                self.state.remove(adj2)
                self.state.append(new_adj1)
                self.state.append(new_adj2)

            # get operation notation
            if adj1[0] < adj2[0]:
                operationA = (adj1, adj2)
            else:
                operationA = (adj2, adj1)

            if new_adj1[0] < new_adj2[0]:
                operationB = (new_adj1, new_adj2)
            else:
                operationB = (new_adj2, new_adj1)

            operation = ((operationA, operationB), 'inv')
            intermediate = self.state[:]


      #  print('CHROMOSOMES After: ', get_adjacencies_and_chromosomes.find_chromosomes(self.state))
      #  print('operation: ',operation)
        return (operation, intermediate)

    def transposition(self, linear_chromosomes):
        get_adjacencies_and_chromosomes = Extremities_and_adjacencies()
      #  print('CHROMOSOMES Before transposition 1: ', get_adjacencies_and_chromosomes.find_chromosomes(self.state))
        get_adjacencies_and_chromosomes = Extremities_and_adjacencies()

        chromosome_number = random.randint(0, len(linear_chromosomes) - 1)
        chromosome = linear_chromosomes[chromosome_number]
        chromosome_length = len(chromosome)
        to_exclude = []

        while chromosome_length < 4:
            to_exclude.append(linear_chromosomes.index(chromosome))
           # print('Transposition a')
          #  print('THE LIST: ', [i for i in range(0, len(linear_chromosomes)) if i not in to_exclude])
          #  print(linear_chromosomes)
            chromosome_number = random.choice([i for i in range(0, len(linear_chromosomes)) if i not in to_exclude])

            chromosome = linear_chromosomes[chromosome_number]
            chromosome_length = len(chromosome)

        try:
            adjacencies = [element for element in chromosome if type(element) is tuple]

        except:
            print('There were not any chromosomes with more than 2 sequence blocks')

        adj1_num = random.randint(0, len(adjacencies) - 1)
        adj2_num = random.randint(0, len(adjacencies) - 1)

        while adj1_num == adj2_num:
            adj2_num = random.randint(0, len(adjacencies) - 1)

        adj1 = adjacencies[adj1_num]
        adj2 = adjacencies[adj2_num]

        # order extremities in the adjacency tuple
        if adj1[0] < adj2[0]:
            new_adj1 = (adj1[0], adj2[0])
        else:
            new_adj1 = (adj2[0], adj1[0])

        if adj1[1] < adj2[1]:
            new_adj2 = (adj1[1], adj2[1])
        else:
            new_adj2 = (adj2[1], adj1[1])

        # perform_operation
        self.state.remove(adj1)
        self.state.remove(adj2)
        self.state.append(new_adj1)
        self.state.append(new_adj2)

        chromosomes = get_adjacencies_and_chromosomes.find_chromosomes(self.state)
        if len(chromosomes[1]) == 0:

            # reverse operation
            self.state.append(adj1)
            self.state.append(adj2)
            self.state.remove(new_adj1)
            self.state.remove(new_adj2)

            # order extremities in the adjacency tuple
            if adj1[0] < adj2[1]:
                new_adj1 = (adj1[0], adj2[1])
            else:
                new_adj1 = (adj2[1], adj1[0])

            if adj1[1] < adj2[0]:
                new_adj2 = (adj1[1], adj2[0])
            else:
                new_adj2 = (adj2[0], adj1[1])

            # perform_operation
            self.state.remove(adj1)
            self.state.remove(adj2)
            self.state.append(new_adj1)
            self.state.append(new_adj2)

        # get operation notation
        if adj1[0] < adj2[0]:
            operationA = (adj1, adj2)
        else:
            operationA = (adj2, adj1)

        if new_adj1[0] < new_adj2[0]:
            operationB = (new_adj1, new_adj2)
        else:
            operationB = (new_adj2, new_adj1)

        chromosomes = get_adjacencies_and_chromosomes.find_chromosomes(self.state)
        if new_adj1 in chromosomes[1][0]:
            circular_adjacency = new_adj1
            exsision_adjacency = new_adj2
        else:
            circular_adjacency = new_adj2
            exsision_adjacency = new_adj1

        operation1 = ((operationA, operationB), 'trp0')
        intermediate1 = self.state[:]


        ###############
        # Reinsertion DCJ
        adj1 = circular_adjacency
        adj2 = exsision_adjacency


        counter = 0
        while adj2 == exsision_adjacency:
            if counter > 2:
                adj2 = chromosomes[0][0][0]
            else:
                chromosome_number = random.randint(0, len(chromosomes[0]) - 1)
                chromosome = chromosomes[0][chromosome_number]
                chromosome_length = len(chromosome)
                to_exclude = []
                while chromosome_length < 3:
                    to_exclude.append(linear_chromosomes.index(chromosome))
                  #  print('Transposition b')
                  ##  print('THE LIST: ', [i for i in range(0, len(linear_chromosomes)) if i not in to_exclude])
                  #  print(linear_chromosomes)
                    chromosome_number = random.choice( [i for i in range(0, len(linear_chromosomes)) if i not in to_exclude])
                    chromosome =chromosomes[0][chromosome_number]
                    chromosome_length = len(chromosome)



                adjacencies = [element for element in chromosome if type(element) is tuple]

                adj2_num = random.randint(0, len(adjacencies) - 1)
                adj2 = adjacencies[adj2_num]
                counter += 1


        # order extremities in adjacency tuple
        if type(adj2) is not tuple:
            if adj1[0] < adj2:
                new_adj1 = (adj1[0], adj2)
            else:
                new_adj1 = (adj2, adj1[0])
            new_adj2 = adj1[1]
            # perfrom operation
            self.state.remove(adj1)
            self.state.remove(adj2)
            self.state.append(new_adj1)
            self.state.append(new_adj2)

            if adj1[0] < adj2:
                operationA = (adj1, adj2)
            else:
                operationA = (adj2, adj1)

            if new_adj1[0] < new_adj2:
                operationB = (new_adj1, new_adj2)
            else:
                operationB = (new_adj2, new_adj1)

            operation2 = ((operationA, operationB), 'trp1')
            intermediate2 = self.state[:]

        else:
            try:
                if adj1[0] < adj2[0]:
                    new_adj1 = (adj1[0], adj2[0])
                else:
                    new_adj1 = (adj2[0], adj1[0])
            except TypeError:
                print("transcroption problem in line 293")
                print('adj1: ', adj1 )
                print('adj2: ', adj2)

            if adj1[1] < adj2[1]:
                new_adj2 = (adj1[1], adj2[1])
            else:
                new_adj2 = (adj2[1], adj1[1])

            # perfrom operation
            self.state.remove(adj1)
            self.state.remove(adj2)
            self.state.append(new_adj1)
            self.state.append(new_adj2)

            if adj1[0] < adj2[0]:
                operationA = (adj1, adj2)
            else:
                operationA = (adj2, adj1)

            if new_adj1[0] < new_adj2[0]:
                operationB = (new_adj1, new_adj2)
            else:
                operationB = (new_adj2, new_adj1)

            operation2 = ((operationA, operationB), 'trp1')
            intermediate2 = self.state[:]

        return [(operation1, intermediate1), (operation2, intermediate2)]

    def balanced_translocation(self, linear_chromosomes):

        chromosome1_number = random.randint(0, len(linear_chromosomes)-1)
        chromosome1 = linear_chromosomes[chromosome1_number]
        chromosome1_length = len(chromosome1)
        to_exclude = []
        while chromosome1_length < 3:
            to_exclude.append(linear_chromosomes.index(chromosome1))
          #  print('Balanced translocations a')
          #  print('THE LIST: ', [i for i in range(0, len(linear_chromosomes)) if i not in to_exclude])
          #  print(linear_chromosomes)
            chromosome1_number = random.choice([i for i in range(0, len(linear_chromosomes)) if i not in to_exclude])
            chromosome1 = linear_chromosomes[chromosome1_number]
            chromosome1_length = len(chromosome1)

        try:
            chromosome2_number = chromosome1_number
        except:
            print('There were not any non-single sequence block chromosomes')

        to_exclude = []

        while chromosome2_number == chromosome1_number:
            to_exclude.append(chromosome2_number)
            chromosome2_number = random.randint(0, len(linear_chromosomes)-1)
            chromosome2 = linear_chromosomes[chromosome2_number]
            chromosome2_length = len(chromosome2)


            while chromosome2_length < 3:

                to_exclude.append(linear_chromosomes.index(chromosome2))
             #   print('Balanced translocations b')
             #   print('THE LIST: ', [i for i in range(0, len(linear_chromosomes)) if i not in to_exclude])
             #   print(linear_chromosomes)
                chromosome2_number = random.choice([i for i in range(0, len(linear_chromosomes)) if i not in to_exclude])
                chromosome2 = linear_chromosomes[chromosome2_number]
                chromosome2_length = len(chromosome2)


        try:
            adjacencies1 = [element for element in chromosome1 if type(element) is tuple]
            adjacencies2 = [element for element in chromosome2 if type(element) is tuple]
        except:
            print('There were not any non-single sequence block chromosomes')

        adj1_num = random.randint(0, len(adjacencies1) - 1)
        adj2_num = random.randint(0, len(adjacencies2) - 1)

        adj1 = adjacencies1[adj1_num]
        adj2 = adjacencies2[adj2_num]

        # order extremities in the adjacency tuple
        if adj1[0] < adj2[1]:
            new_adj1 = (adj1[0], adj2[1])
        else:
            new_adj1 = (adj2[1], adj1[0])

        if adj1[1] < adj2[0]:
            new_adj2 = (adj1[1], adj2[0])
        else:
            new_adj2 = (adj2[0], adj1[1])


        # perfrom operation
        self.state.remove(adj1)
        self.state.remove(adj2)
        self.state.append(new_adj1)
        self.state.append(new_adj2)

        if adj1[0] < adj2[0]:
            operationA = (adj1, adj2)
        else:
            operationA = (adj2, adj1)

        if new_adj1[0] < new_adj2[0]:
            operationB = (new_adj1, new_adj2)
        else:
            operationB = (new_adj2, new_adj1)

        operation = ((operationA, operationB), 'b_trl')
        intermediate = self.state[:]

        return (operation, intermediate)

    def unbalanced_translocation(self, linear_chromosomes):  # linear_chromosomes

        chromosome1_number = random.randint(0, len(linear_chromosomes)-1)
        chromosome1 = linear_chromosomes[chromosome1_number]
        chromosome1_length = len(chromosome1)
        to_exclude =[]

        while chromosome1_length < 3:
            to_exclude.append(linear_chromosomes.index(chromosome1))
         #   print('Unbalanced translocation a')
         #   print('THE LIST: ', [i for i in range(0, len(linear_chromosomes)) if i not in to_exclude])
         #   print(linear_chromosomes)
            chromosome1_number = random.choice([i for i in range(0, len(linear_chromosomes)) if i not in to_exclude])

            chromosome1 = linear_chromosomes[chromosome1_number]
            chromosome1_length = len(chromosome1)

        try:
            chromosome2_number = chromosome1_number
        except:
            print('There were not any non-single sequence block chromosomes')

        to_exclude = []
        while chromosome2_number == chromosome1_number:
            to_exclude.append(chromosome2_number)
        #    print('Unbalanced translocations b')
        #    print('THE LIST: ', [i for i in range(0, len(linear_chromosomes)) if i not in to_exclude])
        #    print(linear_chromosomes)
            chromosome2_number = random.choice([i for i in range(0, len(linear_chromosomes)) if i not in to_exclude])

        chromosome2 = linear_chromosomes[chromosome2_number]

        adjacencies = [element for element in chromosome1 if type(element) is tuple]
        telomeres = [element for element in chromosome2 if type(element) is not tuple]

        adj_num = random.randint(0, len(adjacencies) - 1)
        telo_num = random.randint(0, 1)

        adj = adjacencies[adj_num]
        telo = telomeres[telo_num]

        # order extremities in the adjacency tuple
        if adj[0] < telo:
            new_adj = (adj[0], telo)
        else:
            new_adj = (telo, adj[0])

        new_telo = adj[1]


        # perfrom operation
        self.state.remove(adj)
        self.state.remove(telo)
        self.state.append(new_adj)
        self.state.append(new_telo)

        operationA = (adj, telo)
        operationB = (new_adj, new_telo)

        operation = ((operationA, operationB), 'u_trl')
        intermediate = self.state[:]

        return (operation, intermediate)

    def fusion(self, linear_chromosomes):

        chromosome1_number = random.randint(0, len(linear_chromosomes)-1)
        chromosome1 = linear_chromosomes[chromosome1_number]

        chromosome2_number = chromosome1_number
        to_exclude = []
        while chromosome2_number == chromosome1_number:

            to_exclude.append(chromosome2_number)
        #    print('Fusion a')
        #    print('THE LIST: ', [i for i in range(0, len(linear_chromosomes)) if i not in to_exclude])
        #    print(linear_chromosomes)
            chromosome2_number = random.choice([i for i in range(0, len(linear_chromosomes)) if i not in to_exclude])


        chromosome2 = linear_chromosomes[chromosome2_number]


        telomeres1 = [element for element in chromosome1 if type(element) is not tuple]
        telomeres2 = [element for element in chromosome2 if type(element) is not tuple]

        telo1_num = random.randint(0, 1)
        telo2_num = random.randint(0, 1)

        telo1 = telomeres1[telo1_num]
        telo2 = telomeres2[telo2_num]

        # order extremities in the adjacency tuple
        if telo1 < telo2:
            new_adj = (telo1, telo2)
            operation = ((telo1, telo2, new_adj),'fus')
        else:
            new_adj = (telo2, telo1)
            operation = ((telo2, telo1, new_adj), 'fus')

        # perfrom operation
        self.state.remove(telo1)
        self.state.remove(telo2)
        self.state.append(new_adj)

        intermediate = self.state[:]

        return (operation, intermediate)

    def fission(self, linear_chromosomes):  # linear_chromosomes

        chromosome_number = random.randint(0, len(linear_chromosomes)-1)
        chromosome = linear_chromosomes[chromosome_number]
        chromosome_length = len(chromosome)
        to_exclude = []
        while chromosome_length < 3:
            to_exclude.append(linear_chromosomes.index(chromosome))
         #   print('Fission')
         #   print('THE LIST: ', [i for i in range(0, len(linear_chromosomes)) if i not in to_exclude])
         #   print(linear_chromosomes)
            chromosome_number = random.choice([i for i in range(0, len(linear_chromosomes)) if i not in to_exclude])
            chromosome = linear_chromosomes[chromosome_number]
            chromosome_length = len(chromosome)


        adjacencies = [element for element in chromosome if type(element) is tuple]
        adj_num = random.randint(0, len(adjacencies) - 1)
        adj = adjacencies[adj_num]

        new_telo1 = adj[0]
        new_telo2 = adj[1]

        # perfrom operation
        self.state.remove(adj)
        self.state.append(new_telo1)
        self.state.append(new_telo2)

        operation = ((adj, new_telo1, new_telo2), 'fis')
        intermediate = self.state[:]

        return (operation, intermediate)

