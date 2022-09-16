from random import randint
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

        # get_chromosomes = Node.find_chromosomes(self, self.state)
        gen_x = Gen_xtremities.Xtremities()
        get_chromosomes = gen_x.find_chromosome_type(self.state)
        self.linear_chromosomes = get_chromosomes

    # The function returns a list  of the operations needed to transform the genomes the
    # source  genome to the target genome
    "returns random legal options that can be applied to A, called recursively until A can be transformed to B"

    # TODO:
    # for this to work with foreign dna, this function has to take the source and target genomes
    def get_legal_operations(self, adjacenciesB):
        list_of_legal_operations = []
        adjacenciesA = self.state
        adjacenciesB = adjacenciesB
        switch = False
        loop_counter = 0  # No foreign DNA in first iteration of mutations

        while switch:
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
                        # if the element in the adjacencies is a foreign dna
                        else:
                            for marker in adjacenciesA_copy:
                                if type(marker) is tuple:
                                    if marker[0] != x or marker[1] != x:
                                        fdna = marker
                                    else:
                                        if marker[0] != y or marker[1] != y:
                                            fdna = marker
                                            adjacenciesA_copy.append(fdna[0])
                                            adjacenciesA_copy.append(fdna[1])
                                            operation = (fdna, (fdna[0]), (fdna[1]))
                                            if operation not in list_of_legal_operations:
                                                list_of_legal_operations.append(operation)
                                            else:
                                                pass

            if loop_counter >= 1:
                # randomly choose to insert foreign dna
                choose = randint(0, 1)
                if choose == 0:
                    series_of_mutation = self.mutation_legal_ops(adjacenciesA, adjacenciesB)
                    if series_of_mutation is []:
                        switch = False
                    else:
                        switch = True
                    # mutate without foreign dna
                else:
                    #Here is list of foreign dna where fragments are sublists
                    for_dna = self.foreign_dna_pool(adjacenciesA, adjacenciesB)
                    # Need to randomly choose a foreign dna from pool
                    for_dna_len = len(for_dna)
                    choice_for_dna = randint(0, for_dna_len - 1)
                    chosen = for_dna[choice_for_dna]
                    # TODO:
                    # add foreign dna and then call mutation function
                    # TODO:
                    # create the mutation function that tries to find a series of mutations from A to B
                    series_of_mutation = self.mutation_legal_ops(adjacenciesA, adjacenciesB)
                    if series_of_mutation is []:
                        switch = False
                    else:
                        switch = True
                    # if mutation returns blank then switch is false
                    # if mutation returns list of length greater than 0 then switch needs to be true
            else:
                series_of_mutation = self.mutation_legal_ops(adjacenciesA, adjacenciesB)
                if series_of_mutation is []:
                    switch = False
                    #random mutation
                    #check numbver of applicale region, if 0 then create 
                    
                else:
                    switch = True
                # mutate without foreign dna but still have had done the DCJ (random mutation[do_mutation function])
            loop_counter += 1

        return list_of_legal_operations

    def mutation_legal_ops(self, source_genome, target_genome):
        # This function decides if mutations, any series of mutations, can take genome A to genome B
        # check number of chromosomes -> possibility of chromosome deletion(target chromosmes less than source) or chromosome insertion (source chromosome count less than target)
        # Check number of genes in chromosome for target and source -> indicators for insertion/foreign dna/deletion
        #check signed integers(genes) between target and source
        #Duplication - look at the target; if two of same signed integer next to each other -> tandom duplicatio
        # if two of same signed ints in chromosome but not next to each other then -> transpositional
        
        #step 1, check genes per chromosome between target and source [number of chromosomes should always be the same]
        #1.1 in target and not in source [CREATE in list that contains tuples of (position,gene)]
        in_genome = []
        in_target = []
        for chromosome in source_genome:
            for t_chrom in target_genome:
                for i in range(len(t_chrom)):
                    if t_chrom[i] not in chromosome:
                        in_target.append((i,t_chrom[i]))
            in_genome.append(in_target)

        #1.2 in source and not in target[CREATE out list that contains tuples of (position,gene)]
        out_genome = []
        out_target = []
        for chromosome in source_genome:
            for t_chrom in target_genome:
                for i in range(len(chromosome)):
                    if chromosome[i] not in t_chrom:
                        out_target.append((i,chromosome[i]))
            out_genome.append(out_target)

        #step 2: duplication; check target for duplication [note position, gene and type of duplication]
        duplication_genome = []
        t_duplication = []
        dup_genes = []
        for chromosome in target_genome:
            for i in range(len(chromosome)):
                if chromosome.count(chromosome[i]) > 1 and chromosome[i] not in dup_genes:
                    if chromosome[i] == chromosome[i+1] or chromosome[i] == chromosome[i-1]:
                        type = "tandem"
                    else:
                        type = "transpositional"
                    dup_genes.append(chromosome[i])
                    t_duplication.append([i, self.getIndex(chromosome, chromosome[i]),chromosome[i], type])
            duplication_genome.append(t_duplication)
            dup_genes = []
        
        #step 2.1: check if the duplication is already present in source, if yes remove from list, otherwise cause mutation
        for chromosome in source_genome:
            for sub in duplication_genome:
                for i in range(len(sub)):
                    dup = sub[i]
                    duplicated =  dup[2]
                    #check if gene exists
                    if duplicated in chromosome:
                        occurances = chromosome.count(duplicated)
                        if occurances == 2:
                            #remove from list
                            duplication_genome.remove(dup)
        
        #step 3: checking if all these necessary mutations can occur at once
        #first check that insert and del positions dont overlap for same chromosomes, if they do then we wont be able to cause all mutations necessary
        for i in range(len(out_genome)):
            out_chromosome = out_genome[i]
            in_chromosome = in_genome[i]
            for j in range(len(out_chromosome)):
                tup = out_chromosome[j]
                for tup_in in in_chromosome:
                    if tup_in[0] == tup[0]:
                        return []            
        #Check that intergenic regions exist for insert, del, and dup.
        # get position indexes [only] from in_genome
        in_pos = []
        in_pos_genome = []
        for chromosome in in_genome:
            for i in range(len(chromosome)):
                tup = chromosome[i]
                in_pos.append(tup[0])
            in_pos_genome.append(in_pos)
        # get position indexes [only] from out_genome
        out_pos = []
        out_pos_genome = []
        for chromosome in out_genome:
            for i in range(len(chromosome)):
                tup = chromosome[i]
                out_pos.append(tup[0])
            out_pos_genome.append(out_pos)
        # get position for duplication
        dup_pos = []
        dup_pos_genome = []
        for chromosome in duplication_genome:
            for i in range(len(chromosome)):
                tup = chromosome[i]
                dup_pos.append(tup[1])
            dup_pos_genome.append(dup_pos)
        # get number of applicable intergenic regions
        no_app_region = 0
        app_reg_chrom = []
        app_reg_genome = []
        for chromosome in source_genome:
            for j in range(len(chromosome)):
            # for gene in chromosome:
                if (type(chromosome[j])==str and len(chromosome[j])>1 and '*' in chromosome[j]):
                    no_app_region += 1
                    app_reg_chrom.append(j+1)
                app_reg_genome.append(app_reg_chrom)
        #check number of applicable regions against number of total mutations
        #count positions for each mutation
        insert_count = 0
        for chromosome in in_pos_genome:
            for gene in chromosome:
                insert_count += 1
        del_count = 0
        for chromosome in out_pos_genome:
            for gene in chromosome:
                del_count += 1
        dup_count = 0
        for chromosome in dup_pos_genome:
            for gene in chromosome:
                dup_count += 1
        
        if (no_app_region < (dup_count+insert_count+del_count)):
            return []
        
        #check that the positions for mutations have applicable intergenic regions
        #check insertion
        for i in range(len(app_reg_genome)):
            in_chrom = in_pos_genome[i]
            out_chrom = out_pos_genome[i]
            dup_chrom = dup_pos_genome[i]
            applicable_regions_chrom = app_reg_genome[i]
            total_positions = []
            total_positions = in_chrom+out_chrom+dup_chrom
            for j in range(len(total_positions)):
                if (total_positions[j] not in applicable_regions_chrom):
                    return []
            
            # return list of mutations
            return in_genome, out_genome, duplication_genome


        pass
    

    #Function for finding second occurance of element within list
    def getIndex(self, int_list, num):
        count = 0
        for i, n in enumerate(int_list):
            if n == num:
                count += 1
            if count == 2:
                return i
        else:
            return 0

    def do_mutation(self, source_genome):
        list_of_mutations = []
        # Picks a mutation and calls a functions (delete, duplicate, insert) to act on it
        # uses source_genome with approved intergenic regions

        # Count number of applicable intergenic regions to associate to number of mutations
        count_applicable_regions = 0
        list_of_mutation_points = []
        list_of_mutation_points_genome = []
        for genes_with_intergenic_approved in source_genome:
            for i in genes_with_intergenic_approved:
                if len(i) > 1 and '*' in i:
                    count_applicable_regions += 1
                    list_of_mutation_points.append(i+1)
            list_of_mutation_points_genome.append(list_of_mutation_points)
        
        #get a random int from 0 to count_applicable_regions (how many mutations)
        rand_int_muations = randint(0, count_applicable_regions)
        
        #randomly allocate mutations to the picked applicable regions
        for i in range(rand_int_muations):
            rand_chrom = randint(0,len(list_of_mutation_points_genome))
            position_app_reg_chrom = list_of_mutation_points_genome[rand_chrom]
            source_chrom = source_genome[rand_chrom]

            #randomly pick a position from position_app_reg_chrom to position
            rand_pos = randint(0,len(position_app_reg_chrom))
            position = position_app_reg_chrom[rand_pos]

            #randomly pick a mutation
            mutation_type = randint(0, 2)
            if mutation_type == 0:
                #insertion
                mutated = self.insertion(source_chrom, position)
                list_of_mutations.append("insert", rand_chrom, position)
                #replace orginal with mutated
                source_genome[rand_chrom] = mutated
                pass
            elif mutation_type == 1:
                #deletion
                mutated = self.deletion(source_chrom, position)
                list_of_mutations.append("deletion", rand_chrom, position)
                #replace orginal with mutated
                source_genome[rand_chrom] = mutated
                pass
            else:
                #pick position to insert duplication
                pos = randint(0, len(position_app_reg_chrom))
                pos_f = position_app_reg_chrom[pos]
                if (pos_f+1==position) or (pos_f-1==position):
                    type = 0
                else:
                    type = 1
                #duplicatiom
                mutated = self.duplication(source_chrom, position, pos_f)
                list_of_mutations.append("duplication", rand_chrom, position, pos_f, type)
                #replace orginal with mutated
                source_genome[rand_chrom] = mutated


        #enact mutations and return mutated genome (to enact, need to complete 3 mutation functions)

        return source_genome, list_of_mutations

    def insertion(self, source_chromosome, position_app_region):
        #insertion of gene
        gene = randint(0,99)
        source_chromosome[position_app_region-1] = gene
        
        return source_chromosome

    def deletion(self, source_chromosome, position_app_region):
        #deletion of gene
        del source_chromosome[position_app_region]
        del source_chromosome[position_app_region-1]
        # source_chromosome.pop(position_app_region)
        # source_chromosome.pop(position_app_region-1)
        
        return source_chromosome

    def duplication(self, source_chromosome, position_app_region, insertion_position):
        #duplication of a gene
        gene_to_duplicate = source_chromosome[position_app_region]
        source_chromosome[insertion_position-1] = gene_to_duplicate

        return source_chromosome

    def foreign_dna_pool(self, source, target):
        # Check what genes are not in source that is in target
        source_genome = []
        target_genome = []
        # create master lists

        for chromosome in source:
            for i in range(len(chromosome)):
                if '*' not in chromosome[i]:
                    source_genome.append(int(chromosome[i]))

        for chromosome in target:
            for i in range(len(chromosome)):
                if '*' not in chromosome[i]:
                    target_genome.append(int(chromosome[i]))


        print(source_genome)
        print(target_genome)

        
        # print(source_genome)
        # print(target_genome)


        # Find the difference between source and target
        difference = list(set(target_genome) - set(source_genome))
        # print(difference)
        if len(difference) > 0:
            # define the ratio (1/5)
            number_of_random_ints = (len(difference) * 5) - (len(difference))  # change ratio here (5)

            # create foreign dna
            for_dna = []
            count = 0
            while count < (number_of_random_ints):
                gene = randint(0, 99)
                if len(for_dna) >= 1:
                    if gene not in for_dna:
                        for_dna.append(gene)
                        count += 1
                else:
                    for_dna.append(gene)

            # add difference to foreign dna and check duplicates and add foreign DNA if necessary
            for_dna = difference + for_dna
            for_dna = list(set(for_dna))
            if len(for_dna) < ((len(difference)) * 5):  # change ratio here (5)
                count = len(for_dna)
                while (len(for_dna) < ((len(difference)) * 5)):
                    gene = randint(0, 99)
                    if gene not in for_dna:
                        for_dna.append(gene)
                        count += 1
            
            #Use for_dna list that was created to create foreign dna fragments (random number of frag and random length of fragments)
            number_of_frags = randint(0,99)
            len_frags = (len(difference))+2

            #choose randomly from for_dna list to add to frags
            list_of_frags = []
            frag = []
            for j in range(number_of_frags):
                for i in range(len_frags):
                    choice = randint(0,len(for_dna)-1)
                    frag.append(for_dna[choice])
                #Ensure unique fragments in list
                if j > 0 and frag not in list_of_frags:
                    list_of_frags.append(frag)
                else:
                    j -= 1
                frag = []

            #Check for the difference in genes within atleast one fragment in list
            check = True
            for f in list_of_frags:
                if difference in f:
                    check = False
            print(check)
            if check == True:
                print(difference)
                final_frag = difference[:]
                #add a fragment that does contain the difference
                #Check that the gene does not already exist in the fragment
                while len(final_frag) <= len(difference)+1:
                    c =  for_dna[randint(0, len(for_dna)-1)]
                    if c not in final_frag:
                        final_frag.append(c)
                # print(final_frag)
                list_of_frags.append(final_frag)

            #Tag foreign DNA
            for i in list_of_frags:
                frag = i
                for j in range(len(frag)):
                    frag[j] = str(frag[j])+"_"

            return (list_of_frags)
        else:
            return []

    '''
    Does the mutation
    '''

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
                state_copy.append(operation[0][0] * 2)
                state_copy.append(operation[1][0] * 2)
                operation_type = "dup_"

            elif type(operation[0][0]) is not tuple or type(operation[0][1]) is not tuple:
                state_copy.remove(operation[0][0])
                state_copy.remove(operation[0][1])
                operation_type = "del_"

        elif len(operation) == 3:
            if type(operation[0][1][2]) is tuple and type(operation[1][0][2]) is tuple:
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

    '''
    Checks if the transformed genome A is equal to the target genome B
    '''

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

    '''
    take the source (with transformation) genome and orders and sorts the genes in the source genome for the target genome
    '''

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
