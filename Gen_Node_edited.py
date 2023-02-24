
from random import randint
import Gen_xtremities
import Data_generator
import random


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

        gen_x = Gen_xtremities.Xtremities()
        get_chromosomes = gen_x.find_chromosome_type(self.state)
        self.linear_chromosomes = get_chromosomes

    # The function returns a list  of the operations needed to transform the genomes the
    # source  genome to the target genome
    "returns random legal options that can be applied to A, called recursively until A can be transformed to B"

    def get_legal_operations(self,source_genome, adjacenciesB):
        list_of_legal_operations = []
        adjacenciesA = source_genome
        adjacenciesB = adjacenciesB
        switch = True
        loop_counter = 0  # No foreign DNA in first iteration of mutations

        #accomodate more than one solution -> modify while loop
        while switch:
            print("loop counter: " +str(loop_counter))
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

                        # if elements containing x and y respectively are adjacencies
                        for marker in adjacenciesA_copy:
                            #if type(marker) is tuple:
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
    
            if loop_counter > 0 :
                #print(adjacenciesA)
                #TODO: check number of applicale region, if 0 then create 
                count_applicable = 0
                for chromosome in adjacenciesA:
                    for i in range(len(chromosome)):
                        if isinstance(chromosome[i], str) and '*' in chromosome[i] and len(chromosome[i]) > 1 :
                            count_applicable += 1
                
                clean_chromosome = []
                clean_genome = []

                print("count of applicable regions is: " + str(count_applicable))
                if count_applicable >= 0:
                    #remove all unapplicable intergenic regions and call intergenerator
                    for chromosome in adjacenciesA:
                        for i in range(len(chromosome)):
                            if isinstance(chromosome[i],str) and '*' not in chromosome[i]:
                                # print(chromosome[i])
                                clean_chromosome.append(chromosome[i])
                            elif isinstance(chromosome[i], int):
                                clean_chromosome.append(chromosome[i])
                        clean_genome.append(clean_chromosome)
                        clean_chromosome = []

                    gen_obj = Data_generator.Data_generator()
                    normal_intergenic_region = gen_obj.intergenerator(clean_genome)
                    adjacenciesA = gen_obj.intergenic_regions(normal_intergenic_region)
                    #print(adjacenciesA)
                # randomly choose to insert foreign dna
                #randint(0, 10)
                
                choose = randint(0, 30)
                if choose >= 3:
                    print("chosen not to insert foreign dna")
                    series_of_mutation,mutation_required = self.mutation_legal_operations(adjacenciesA, adjacenciesB)
                    print("series of mutation_legal_operations is: " + str(series_of_mutation))
                    if series_of_mutation == [] and mutation_required !=():
                        source_genome, *mutation_list = self.do_mutation(adjacenciesA, mutation_required)
                        #print("could not find mutation to get to B so randomly mutated")
                        #print(mutation_list)
                        #print("source genome after random mutations" + str(source_genome))
                        adjacenciesA = source_genome[:]

                        list_of_legal_operations.append(mutation_list)
                        switch = True
                    else:
                        while (any(series_of_mutation) and mutation_required !=()) or mutation_required !=():
                            mutations_finale = []
                            for i in range(len(series_of_mutation)):
                                if i == 0:
                                    mutation_type = 'insertion'
                                elif i == 1:
                                    mutation_type = 'deletion'
                                else:
                                    mutation_type = 'duplication'
                                mutation = series_of_mutation[i]
                                for chromosome_number in range(len(mutation)):
                                    if mutation[chromosome_number] != []:
                                        chromosome_index = chromosome_number
                                        chromosome = mutation[chromosome_number]
                                        for m in range(len(chromosome)):
                                            do_mutation = (mutation_type, chromosome_index, chromosome[m])
                                            source_genome, mutation_list = self.do_mutation(adjacenciesA, do_mutation)
                                            adjacenciesA = source_genome[:]
                                            mutations_finale.append(mutation_list)
                            list_of_legal_operations.append(mutations_finale)
                            clean_chromosome = []
                            clean_genome = []

                            #remove all unapplicable intergenic regions and call intergenerator
                            for chromosome in adjacenciesA:
                                for i in range(len(chromosome)):
                                    if isinstance(chromosome[i],str) and '*' not in chromosome[i]:
                                        # print(chromosome[i])
                                        clean_chromosome.append(chromosome[i])
                                    elif isinstance(chromosome[i], int):
                                        clean_chromosome.append(chromosome[i])
                                clean_genome.append(clean_chromosome)
                                clean_chromosome = []
                            gen_obj = Data_generator.Data_generator()
                            normal_intergenic_region = gen_obj.intergenerator(clean_genome)
                            adjacenciesA = gen_obj.intergenic_regions(normal_intergenic_region)
                            print("source before mutation legal operations")
                            print(adjacenciesA)  
                            series_of_mutation,mutation_required = self.mutation_legal_operations(adjacenciesA, adjacenciesB)
                            #print("within while loop and series of mutation checks")
                            #print(series_of_mutation,mutation_required)
                            #print(any(series_of_mutation))
                            #print(adjacenciesA)  
                            if mutation_required ==():
                                break
                        switch = False
                        #print(adjacenciesA)  
                        #print(series_of_mutation)
                        # src_genome, mutation_list = self.do_mutation(adjacenciesA, mutation_required)
                        # list_of_legal_operations.append(series_of_mutation)
                        # print(src_genome)
                        # switch = False
                    # mutate without foreign dna
                else:
                    print("chose to insert foreign dna")
                    #Here is list of foreign dna where fragments are sublists
                    foreign_dna = []
                    while foreign_dna == []:
                        foreign_dna = self.foreign_dna_pool(adjacenciesA, adjacenciesB)
                    print("found foreign dna from pool")
                    # Need to randomly choose a foreign dna from pool
                    foreign_dna_len = len(foreign_dna) -1
                    choice_foreign_dna = randint(0, foreign_dna_len)
                    chosen = foreign_dna[choice_foreign_dna]
                    # add foreign dna 
                    adjacenciesA, list_of_operationz = self.add_foreign_dna(adjacenciesA, chosen)
                    list_of_legal_operations.append(list_of_operationz)

                    #record addition of foreign dna
                    #list_of_legal_operations.append([include what happened, chrom_no, frag])

                    #print("added for_dna")
                    print("source after add_for_dna:  "+str(adjacenciesA))
                    mutation_genome = adjacenciesA.copy()
                    #print("mutation_genome: "+str(mutation_genome))
                    series_of_mutation, mutation_required = self.mutation_legal_operations(mutation_genome, adjacenciesB)
                    print("series of mutation_legal_operations is: " + str(series_of_mutation))
                    if series_of_mutation == []:
                        #print("mutation_genome: "+str(mutation_genome))
                        #print("adjacencies A before do mutation"+ str(adjacenciesA))
                        source_genome, *mutation_list = self.do_mutation(adjacenciesA, mutation_required)
                        #print("could not find mutation to get to B so randomly mutated")
                        #print(mutation_list)
                        #print(source_genome)

                        adjacenciesA = source_genome[:]
                        list_of_legal_operations.append(mutation_list)
                        switch = True
        
                    else:
                        while (any(series_of_mutation) and mutation_required ==()) or mutation_required !=():
                            mutations_finale = []
                            for i in range(len(series_of_mutation)):
                                if i == 0:
                                    mutation_type = 'insertion'
                                elif i == 1:
                                    mutation_type = 'deletion'
                                else:
                                    mutation_type = 'duplication'
                                mutation = series_of_mutation[i]
                                for chromosome_number in range(len(mutation)):
                                    if mutation[chromosome_number] != []:
                                        chromosome_index = chromosome_number
                                        chromosome = mutation[chromosome_number]
                                        for m in range(len(chromosome)):
                                            do_mutation = (mutation_type, chromosome_index, chromosome[m])
                                            source_genome, mutation_list = self.do_mutation(adjacenciesA, do_mutation)
                                            adjacenciesA = source_genome[:]
                                            mutations_finale.append(mutation_list)
                            
                            list_of_legal_operations.append(mutations_finale)
                            clean_chromosome = []
                            clean_genome = []

                            #remove all unapplicable intergenic regions and call intergenerator
                            for chromosome in adjacenciesA:
                                for i in range(len(chromosome)):
                                    if isinstance(chromosome[i],str) and '*' not in chromosome[i]:
                                        # print(chromosome[i])
                                        clean_chromosome.append(chromosome[i])
                                    elif isinstance(chromosome[i], int):
                                        clean_chromosome.append(chromosome[i])
                                clean_genome.append(clean_chromosome)
                                clean_chromosome = []
                            gen_obj = Data_generator.Data_generator()
                            normal_intergenic_region = gen_obj.intergenerator(clean_genome)
                            adjacenciesA = gen_obj.intergenic_regions(normal_intergenic_region)
                            #print("source before mutation legal operations")
                            #print(adjacenciesA)
                            series_of_mutation,mutation_required = self.mutation_legal_operations(adjacenciesA, adjacenciesB)
                            #print("within while loop and series of mutation checks")
                            #print(series_of_mutation,mutation_required)
                            #print(any(series_of_mutation))
                            #print(adjacenciesA)  
                            if mutation_required ==():
                                break
                        switch = False
                        #print(adjacenciesA)  
                        # print("could find solution")
                        #print(series_of_mutation)
                        # src_genome, mutation_list = self.do_mutation(adjacenciesA, mutation_required)
                        # list_of_legal_operations.append(series_of_mutation)
                        # print(src_genome)
                        # switch = False
            elif loop_counter == 0:
                #print("first Iteration")
                series_of_mutation, mutation_required = self.mutation_legal_operations(adjacenciesA, adjacenciesB)
                print("series of mutation_legal_operations is: " + str(series_of_mutation))
                # sys.exit(0)
                #print(series_of_mutation)
                if series_of_mutation == [] and mutation_required !=():
                    #print("loop counter 0 and cannot get to target")
                    switch = True

                    #TODO random mutation
                    source_genome, *mutation_list = self.do_mutation(adjacenciesA, mutation_required)
                
                    #print("could not find mutation to get to target_genome so randomly mutated")
                    #print(mutation_list)
                    adjacenciesA = source_genome[:]
                    list_of_legal_operations.append(mutation_list)
                    
                    #TODO: check number of applicale region, if 0 then create 
                    count_applicable = 0
                    for chromosome in adjacenciesA:
                        for i in range(len(chromosome)):
                            if isinstance(chromosome[i], str) and '*' in chromosome[i] and len(chromosome[i]) > 1 :
                                count_applicable += 1
                    print("within first iteration after any and all mutations we check applicable reagions, count is : "+str(count_applicable))
                    clean_chromosome = []
                    clean_genome = []
                    # source = []
                    if count_applicable <= len(adjacenciesA)-1:
                        #remove all unapplicable intergenic regions and call intergenerator
                        for chromosome in adjacenciesA:
                            for i in range(len(chromosome)):
                                if (isinstance(chromosome[i],str) and '*' not in chromosome[i]) or isinstance(chromosome[i],int):
                                    clean_chromosome.append(chromosome[i])
                            clean_genome.append(clean_chromosome)
                            clean_chromosome = []
                        
                        gen_obj = Data_generator.Data_generator()
                        normal_intergenic_region = gen_obj.intergenerator(clean_genome)
                        adjacenciesA = gen_obj.intergenic_regions(normal_intergenic_region)
                        # print("first iteration update app_reg so source is :  "+str(adjacenciesA))
                else:
                        while (any(series_of_mutation) and mutation_required ==()) or mutation_required !=():
                            
                            mutations_finale = []
                            for i in range(len(series_of_mutation)):
                                if i == 0:
                                    mutation_type = 'insertion'
                                elif i == 1:
                                    mutation_type = 'deletion'
                                else:
                                    mutation_type = 'duplication'
                                mutation = series_of_mutation[i]
                                for chromosome_number in range(len(mutation)):
                                    if mutation[chromosome_number] != []:
                                        chromosome_index = chromosome_number
                                        chrom = mutation[chromosome_number]
                                        for m in range(len(chromosome)):
                                            do_mutation = (mutation_type, chromosome_index, chromosome[m])
                                            source_genome, mutation_list = self.do_mutation(adjacenciesA, do_mutation)
                                            adjacenciesA = source_genome[:]
                                            mutations_finale.append(mutation_list)
                            list_of_legal_operations.append(mutations_finale)
                            clean_chromosome = []
                            clean_genome = []

                            #remove all unapplicable intergenic regions and call intergenerator
                            for chromosome in adjacenciesA:
                                for i in range(len(chromosome)):
                                    if isinstance(chromosome[i],str) and '*' not in chromosome[i]:
                                        # print(chromosome[i])
                                        clean_chromosome.append(chromosome[i])
                                    elif isinstance(chromosome[i], int):
                                        clean_chromosome.append(chromosome[i])
                                clean_genome.append(clean_chromosome)
                                clean_chromosome = []
                                gen_obj = Data_generator.Data_generator()
                                normal_intergenic_region = gen_obj.intergenerator(clean_genome)
                                adjacenciesA = gen_obj.intergenic_regions(normal_intergenic_region)
                            #print("\n source_genome before mutation legal operations")
                            #print(adjacenciesA)  
                            series_of_mutation,mutation_required = self.mutation_legal_operations(adjacenciesA, adjacenciesB)
                            #print("within while loop and series of mutation checks")
                            #print(series_of_mutation,mutation_required)
                            #print(any(series_of_mutation))
                            #print(adjacenciesA)  
                            # print(src_genome)
                            if mutation_required ==():
                                break
                        switch = False 
                        #print(adjacenciesA)                  
            else:
                break
            loop_counter += 1
     
            # shuffle the list of list_legal_operations to get different sets of solutions
            # create a master list to hold  shuffled list_of legal_operations
            #master_list = []

            # loop through the list_of_legal_of_operations and shuffle each operation randomly
            #for operation in list_of_legal_operations:
                #shuffled_operations = random.shuffle(operation)
                #master_list.append(shuffled_operations)
            
        return list_of_legal_operations

    


    # change to new fdna func
    def add_foreign_dna(self, source_genome, fragment):

        # Count number of applicable intergenic regions to associate with number of mutations
        list_of_mutation_points = []
        list_of_mutation_points_genome = []
        for genes_with_intergenic_approved in source_genome:
            for i in range(len(genes_with_intergenic_approved)):
                if isinstance(genes_with_intergenic_approved[i], str) and len(genes_with_intergenic_approved[i]) > 1 and '*' in genes_with_intergenic_approved[i]:
                    list_of_mutation_points.append(i+1)
                    # print(genes_with_intergenic_approved[i])
            list_of_mutation_points_genome.append(list_of_mutation_points)
            list_of_mutation_points = []
        
        #insert intergenic regions in foreign dna fragments 
        fragment_with_intergenic_regions = []
        length = len(fragment)
        for j in range(len(fragment)):
            if j == 0 :
                random_bp = randint(0,10)
                region = '*' + str(random_bp)
                fragment_with_intergenic_regions.append(region)
            random_bp = randint(0,10)
            start = fragment[j]
            region = '*' + str(random_bp)
            fragment_with_intergenic_regions.append(start)
            if j != length-1:
                fragment_with_intergenic_regions.append(region)
        #find applicable inergenic regions in fragment
        for i in range(len(fragment_with_intergenic_regions)):
            if i % 2 == 0 or i == 0:
                region = fragment_with_intergenic_regions[i]
                # print(region)
                if len(region) > 2:
                    value = region[2]+region[2]
                else:
                    value = region[1]
                if int(value) < 5:
                    fragment_with_intergenic_regions[i] = '*'


        #TODO: ACCOUNT FOR CHROMOSOMES WITHOUT INTERGENIC REGIONS
        position_applicable_region_chromosome = []
        source_chromosome = []
        rand_chromosome = []
        while len(position_applicable_region_chromosome) == 0 :
            # print(source_genome)
            # print((list_of_mutation_points_genome))
            rand_chromosome = randint(0,len(list_of_mutation_points_genome)-1)
            # print(rand_chrom)
            position_applicable_region_chromosome = list_of_mutation_points_genome[rand_chromosome]
            source_chromosome = source_genome[rand_chromosome]
        
        #randomly pick a position from position_app_reg_chrom to position
        #print(position_app_reg_chrom)
        rand_position = randint(0,len(position_applicable_region_chromosome)-1)
        position = position_applicable_region_chromosome[rand_position]
        # print(position)
        # print(position_app_reg_chrom)

        mutated = []
        mutated = source_chromosome[0:position-1] + fragment_with_intergenic_regions + source_chromosome[position:]

        source_genome[rand_chromosome] = mutated
        print("mutated chromosome with frag inserted :  " +str(mutated))
        print("mutated genome with frag inserted :  " +str(source_genome))
        return source_genome, ['F_DNA inserted ',rand_chromosome, position, fragment_with_intergenic_regions]

    def mutation_legal_operations(self, source_genome, target_genome):
        # This function decides if mutations, any series of mutations, can take genome A to genome B
        # check number of chromosomes -> possibility of chromosome deletion(target chromosmes less than source) or chromosome insertion (source chromosome count less than target)
        # Check number of genes in chromosome for target and source -> indicators for insertion/foreign dna/deletion
        # check signed integers(genes) between target and source
        # Duplication - look at the target; if two of same signed integer next to each other -> tandom duplicatio
        # if two of same signed ints in chromosome but not next to each other then -> transpositional
        # source_genome = source[:]

        #remove underscores that identify fragments in source genome
        chromosome = []
        source_genome = []
        for chromosome in source_genome:
            for i in range(len(chromosome)):
                if isinstance(chromosome[i], str) and '_' in chromosome[i]:
                    if len(chromosome[i])==3:
                        gene = chromosome[i]
                        chromosome.append(int(gene[:2]))
                    elif len(chromosome[i])==2:
                        gene = chromosome[i]
                        # print((gene[:1]))
                        chromosome.append(int(gene[:1]))
                elif isinstance(chromosome[i], str):
                    chromosome.append((chromosome[i]))
                elif isinstance(chromosome[i], int):
                    chromosome.append((chromosome[i]))
                elif ((isinstance(chromosome[i], str) and '*' in chromosome[i])):
                    chromosome.append((chromosome[i]))
            source_genome.append(chromosome)
            chromosome = []

        # sys.exit(0)
        #step 1, check genes per chromosome between target and source [number of chromosomes should always be the same]
        #1.1 in target and not in source [CREATE in list that contains tuples of (position,gene)]
        in_genome = []
        in_target = []

        # for chromosome in source_genome:
        #     for t_chrom in target_genome:
        print(len(source_genome))
        #print(len(target_genome))
        #Take note of differing length of genomes where this condition does not hold

        for j in range(len(target_genome)):
            chromosome1 = source_genome[j]
            target_chromosome = target_genome[j]

            for i in range(len(target_chromosome)):
                if '*' not in str(target_chromosome[i]) and (target_chromosome[i]) not in chromosome1:
                    in_target.append((i,target_chromosome[i]))
            in_genome.append(in_target)
        
        #print("in_genome")
        #print(in_genome)
        #1.2 in source and not in target[CREATE out list that contains tuples of (position,gene)]
        out_genome = []
        out_target = []
        occurred = []
        for j in range(len(target_genome)):
            chromosome = source_genome[j]
            target_chromosome = target_genome[j]
            for i in range(len(chromosome)):
                if ((isinstance(chromosome[i], int) and chromosome[i] not in target_chromosome)) or (((isinstance(chromosome[i], str) and '*' not in chromosome[i])) and chromosome[i] not in target_chromosome):
                    out_target.append((i,chromosome[i]))
                elif (chromosome.count(chromosome[i])) > target_chromosome.count(chromosome[i]) and (isinstance(chromosome[i],str) and '*' not in chromosome[i]) and (chromosome[i] not in occurred):
                    out_target.append((i,chromosome[i]))
                    occurred.append(chromosome[i])
            out_genome.append(out_target)
            out_target = []
        #print("out_genome")
        #print(out_genome)
        #step 2: duplication; check target for duplication [note position, gene and type of duplication]
        #isinstance(chromosome[i], int) and 
        duplication_genome = []
        target_duplication = []
        duplicated_genes = []
        for chromosome in target_genome:
            for i in range(len(chromosome)):
                if isinstance(chromosome[i], int) and chromosome.count(chromosome[i]) > 1 and chromosome[i] not in duplicated_genes :
                    if chromosome[i] == chromosome[i+2] or chromosome[i] == chromosome[i-2]:
                        type = "tandem"
                    else:
                        type = "transpositional"
                    duplicated_genes.append(chromosome[i])
                    target_duplication.append([i, self.getIndex(chromosome, chromosome[i]),chromosome[i], type])
            duplication_genome.append(target_duplication)
            target_duplication = []
            duplicated_genes = []
        # print("dup")
        # print(duplication_genome)
        #step 2.1: check if the duplication is already present in source, if yes remove from list, otherwise cause mutation
        duplications_to_remove = []
        empty_duplication_genome = False
        #Check that duplication genome is not empty
        if any(duplication_genome):
            #print("elements exist")
            for j in range(len(source_genome)):
                chromosome = source_genome[j]
                sub = duplication_genome[j]
                for i in range(len(sub)):
                        dup = sub[i]
                        duplicated =  dup[2]
                        #print(duplicated)
                        #print(chromosome)
                        #check if gene exists
                        if duplicated in chromosome:
                            print("Duplicated gene: " + str(duplicated))
                            occurances = chromosome.count(duplicated)
                            print("occurances: "+ str(occurances))
                            if occurances == 2:
                                if len(sub)>1:
                                    n_sub = sub.remove(dup)
                                    duplication_genome[j] = n_sub
                                else:
                                    n_sub = []
                                    duplication_genome[j] = n_sub
        #print("duplication_genome:  "+str(duplication_genome))
        #print(duplications_to_remove)

        # for chromosome in source_genome:
        #     for sub in duplication_genome:
        #         for i in range(len(sub)):
        #             dup = sub[i]
        #             duplicated =  dup[2]
        #             print(dup)
        #             #check if gene exists
        #             if duplicated in chromosome:
        #                 occurances = chromosome.count(duplicated)
        #                 if occurances == 2:
        #                     #remove from list
        #                     for i in range(len(duplication_genome)):
        #                         if dup in duplication_genome[i]:
        #                             duplications_to_remove.append((i, dup))
                                    # chrom = duplication_genome[i]
                                    # chrom.remove(dup)
                                    # sub = chrom[:]
                                    # duplication_genome[i] = chrom
                            # print(dup)
                            # print(duplication_genome)
                            # duplication_genome.remove(dup)
        # print(duplications_to_remove)

        # for i in range(len(duplications_to_remove)):
        #     duplication = duplications_to_remove[i]
        #     chrom_index = duplication[0]
        #     match = duplication[1]
        #     target_chrom = duplication_genome[chrom_index]
        #     print(target_chrom)
        #     print(match)
        #     if match != None and match in target_chrom:
        #         final_chrom = target_chrom.remove(match)
        #         duplication_genome[chrom_index] = final_chrom

        #remove tuples from out_list that contain intergenic regions and does not contain the gene tuple
        #out_c = []
        #out_g = []
        #print("out_genome before suspicious activity with intergenic regions")
        #print(out_genome)
        '''
        for k in range(len(out_genome)):
            # print("len of out_genome is : "+ str(len(out_genome)))
            # print("k variable is : " +str(k))
            chromosome_o = out_genome[k]
            print(chromosome_o)
            l = len(chromosome_o)
            print(l)
            for i in range(l):
                tuple_to_remove = chromosome_o[i]
                position = tuple_to_remove[0]
                item = tuple_to_remove[1]
                if (len(chromosome_o)>1 and i < len(chromosome_o)-1):
                    consecutive_tuple = chromosome_o[i+1]
                    position_c = consecutive_tuple[0]
                    item_c = consecutive_tuple[1]
                    # print("pos = " + str(position))
                    # print("pos_c = " + str(position_c))
                    if position + 1 == position_c:
                        #we know its not consecutive
                        if (isinstance(item_c, int) or '*' not in item_c) and (isinstance(item_c, str) and '*' in item):
                            # print("we here")
                            # print(tuple_to_remove)
                            out_c.append(tuple_to_remove)
                            # print("here" + str(i))
                            if i == len(chromosome_o)-2:
                                # print("here is out_c")
                                # print(out_c)
                                out_c.append(chromosome_o[l-1])
                                # print("final out_c")
                                # print(out_c)
                                # print("out_g")
                                # print(out_g)
                            # out_genome[k] = chromosome_o.remove(tuple_to_remove)
                            # print(out_genome)
                elif (len(chromosome_o) == 1 and isinstance(item, str) and '*' in item ):
                    out_genome[k] = []
            # print(out_c)
            out_g.append(out_c)
            out_c = []
        # print("last instance of out_g")
        # print(out_g)
        out_genome = out_g[:]
        '''
        #print("out_genome after suspicious activity with intergenic regions")
        #print(out_genome)

        #check in list with out list and remove overlaps where an insertion will occur
        # out_g = []
        # out_c = []

        # for c in range(len(out_genome)):
        #     in_chrom = in_genome[c]
        #     for tuple in out_genome[c]:
        #         pos = tuple[0]
        #         print(pos)
        #         if len(in_chrom)==0:
        #             out_c.append(tuple)
        #         else:
        #             for t in in_chrom:
        #                 if t[0]!= pos:
        #                     out_c.append(tuple)
        #                     print(tuple)
        #     out_g.append(out_c)
        #     out_c =[]

        # out_genome = out_g[:]
        #print(in_genome)
        #print(out_genome)

        #check the 3 lists and randomly pick a tuple from one of them
        do_mutation = ()
        deletion = False
        insertion = False
        duplication = False
        if any(duplication_genome):
            duplication = True
        if any(out_genome):
            deletion = True
        if any(in_genome):
            insertion = True
        print(insertion, deletion, duplication)
        if insertion and deletion and duplication:
            pick = randint(0,2)
            if pick == 0:
                for i in range(len(in_genome)):
                    chromosome = in_genome[i]
                    if chromosome != []:
                        #print('inside mutation_legal_ops insert_1')
                        # print(chromosome[i])
                        picker = randint(0, len(chromosome)-1)
                        do_mutation = ("insert",i, chromosome[picker])
                        break
            elif pick == 1:
                for i in range(len(out_genome)):
                    chromosome = out_genome[i]
                    if chromosome != []:
                        picker = randint(0, len(chromosome)-1)
                        do_mutation = ("delete",i, chromosome[picker])
                        break
            elif pick == 2:
                for i in range(len(duplication_genome)):
                    chromosome = duplication_genome[i]
                    if chromosome != []:
                        picker = randint(0, len(chromosome)-1)
                        do_mutation = ("duplication",i, chromosome[picker])
                        break
        elif insertion and deletion:
            pick = randint(0,1)
            if pick == 0:
                for i in range(len(in_genome)):
                    chromosome = in_genome[i]
                    if chromosome != []:
                        #print('inside mutation_legal_ops insert_2')
                        # print(chromosome[i])
                        picker = randint(0, len(chromosome)-1)
                        do_mutation = ("insert",i, chromosome[picker])
                        break
            elif pick == 1:
                for i in range(len(out_genome)):
                    chromosome = out_genome[i]
                    if chromosome != []:
                        picker = randint(0, len(chromosome)-1)
                        do_mutation = ("delete",i, chromosome[picker])
                        break
        elif deletion and duplication:
            pick = randint(0,1)
            if pick == 0:
                for i in range(len(out_genome)):
                    chromosome = out_genome[i]
                    if chromosome != []:
                        picker = randint(0, len(chromosome)-1)
                        do_mutation = ("delete",i, chromosome[picker])
                        break
            elif pick == 1:
                for i in range(len(duplication_genome)):
                    chromosome = duplication_genome[i]
                    if chromosome != []:
                        picker = randint(0, len(chromosome)-1)
                        do_mutation = ("duplication",i, chromosome[picker])
                        break
        elif insertion and duplication:
            pick = randint(0,1)
            if pick == 0:
                for i in range(len(in_genome)):
                    chromosome = in_genome[i]
                    if chromosome != []:
                        #print('inside mutation_legal_ops insert_3')
                        # print(chromosome[i])
                        picker = randint(0, len(chromosome)-1)
                        do_mutation = ("insert",i, chromosome[picker])
                        break
            elif pick == 1:
                for i in range(len(duplication_genome)):
                    chromosome = duplication_genome[i]
                    if chromosome != []:
                        picker = randint(0, len(chromosome)-1)
                        do_mutation = ("duplication",i, chromosome[picker])
                        break
        elif insertion:
            for i in range(len(in_genome)):
                    chromosome = in_genome[i]
                    if chromosome != []:
                        #print('inside mutation_legal_ops insert_4')
                        # print(chromosome[i])
                        picker = randint(0, len(chromosome)-1)
                        do_mutation = ("insert",i, chromosome[picker])
                        break
        elif deletion:
            for i in range(len(out_genome)):
                    chromosome = out_genome[i]
                    if chromosome != []:
                        picker = randint(0, len(chromosome)-1)
                        do_mutation = ("delete",i, chromosome[picker])
                        break
        elif duplication:
            for i in range(len(duplication_genome)):
                    chromosome = duplication_genome[i]
                    if chromosome != []:
                        picker = randint(0, len(chromosome)-1)
                        do_mutation = ("duplication",i, chromosome[picker])
                        break
        #print('mutation get_legal_operation return for do mutation')
        #print(do_mutation)

        #step 3: checking if all these necessary mutations can occur at once
        #first check that insert and del positions dont overlap for same chromosomes, if they do then we wont be able to cause all mutations necessary
        for i in range(len(out_genome)):
            out_chromosome = out_genome[i]
            in_chromosome = in_genome[i]
            for j in range(len(out_chromosome)):
                tup = out_chromosome[j]
                for tup_in in in_chromosome:
                    if tup_in[0] == tup[0]:
                        #print("returned because overlap")
                        return [], do_mutation            
        #Check that intergenic regions exist for insertion, deletion, and duplication.
        # get position indexes [only] from in_genome
        in_position = []
        in_position_genome = []
        # if any(in_genome):
        for chromosome in in_genome:
            for i in range(len(chromosome)):
                tup = chromosome[i]
                in_position.append(tup[0])
            in_position_genome.append(in_position)
        # get position indexes [only] from out_genome
        out_position = []
        out_position_genome = []
        # if any(out_genome):
        for chromosome in out_genome:
            if len(chromosome)!= 0:
                for i in range(len(chromosome)):
                    tup = chromosome[i]
                    if len(chromosome)>1 and i < len(chromosome)-1:
                        check = chromosome[i+1]
                        if check[0] == tup[0]+1:
                            out_position.append(tup[0])
                            i += 1
                out_position_genome.append(out_position)
            else: 
                out_position_genome.append([])
        # get position for duplication
        duplication_position = []
        duplication_position_genome = []
        # if any(duplication_genome):
            # print(duplication_genome)
        for chromosome in duplication_genome:
            for i in range(len(chromosome)):
                tup = chromosome[i]
                duplication_position.append(tup[1])
            duplication_position_genome.append(duplication_position)
        # get number of applicable intergenic regions
        number_applicable_region = 0
        applicable_region_chromosome = []
        applicable_region_genome = []
        for chromosome in source_genome:
            for j in range(len(chromosome)):
            # for gene in chromosome:
                if (isinstance(chromosome[j],str) and len(chromosome[j])>1 and '*' in chromosome[j]):
                    number_applicable_region += 1
                    applicable_region_chromosome.append(j)
            applicable_region_genome.append(applicable_region_chromosome)
            applicable_region_chromosome = []
        #check number of applicable regions against number of total mutations
        #count positions for each mutation
        insertion_count = 0
        for chromosome in in_position_genome:
            for gene in chromosome:
                insertion_count += 1
        deletion_count = 0


        #TODO check counting in pairs as well
        for chromosome in out_position_genome:
            for gene in chromosome:
                deletion_count += 1
        duplication_count = 0
        for chromosome in duplication_position_genome:
            for gene in chromosome:
                duplication_count += 1
        if (number_applicable_region < (duplication_count+insertion_count+deletion_count)):
            #print("returned at line 481")
            return [], do_mutation
        
        #check that the positions for mutations have applicable intergenic regions
        #check insertion
        for i in range(len(applicable_region_genome)):
            in_chromosome = in_position_genome[i]
            out_chromosome = out_position_genome[i]
            duplication_chromosome = duplication_position_genome[i]
            applicable_regions_chrom = applicable_region_genome[i]
            # print(applicable_regions_chrom)
            total_positions = []
            total_positions = in_chromosome+out_chromosome+duplication_chromosome
            # print("tot_pos")
            # print(total_positions)
            for j in range(len(total_positions)):
                #print("final resting place")
                #print(total_positions)
                #print(app_reg_chrom)
                if (total_positions[j]+1 not in applicable_region_chromosome) or applicable_region_chromosome == []:
                    #print("final resting place")
                    #print(total_positions)
                    #print(app_reg_chrom)
                    return [], do_mutation

            mutation_insert = {}
            #TODO: COMPLETE FORMAT CHANGE FOR MUTATION DISPLAY
            #write code to take elements of lists and place in dictionary [for loop]
            for i in range(len(in_genome)):
                if len(in_genome[i]) > 0:
                    mutation_insert["insertion chromosome"] = i+1
                    chromosome_interest =in_genome[i]
                    for i in range(len(chromosome_interest)):
                        instance = chromosome_interest[i]
                        mutation_insert["insertion position"] = instance[0]
                        mutation_insert["insertion gene"] = instance[1]


            # return list of mutations
            return [in_genome, out_genome, duplication_genome], do_mutation

        return [], do_mutation
    

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

    def do_mutation(self, source_genome, mutation_required):
        list_of_mutations = []
        # Picks a mutation and calls a functions (delete, duplicate, insert) to act on it
        # uses source_genome with approved intergenic regions

        # Count number of applicable intergenic regions to associate to number of mutations
        # count_applicable_regions = 0
        list_of_genes = []
        list_of_genes_genome = []
        list_of_mutation_points = []
        list_of_mutation_points_genome = []
        mutation_point_chromosome = []
        for genes_with_intergenic_approved in source_genome:
            for i in range(len(genes_with_intergenic_approved)):
                # print(genes_with_intergenic_approved)
                if isinstance(genes_with_intergenic_approved[i],str) and len(genes_with_intergenic_approved[i]) > 1 and '*' in genes_with_intergenic_approved[i]:
                    # count_applicable_regions += 1
                    if i != len(genes_with_intergenic_approved)-2:
                        list_of_mutation_points.append(i+1)
                elif (not isinstance(genes_with_intergenic_approved[i],str)) or (isinstance(genes_with_intergenic_approved[i],str) and '*' not in genes_with_intergenic_approved[i]):
                    list_of_genes.append(genes_with_intergenic_approved[i])
            list_of_genes_genome.append(list_of_genes)
            list_of_mutation_points_genome.append(list_of_mutation_points)
            list_of_mutation_points =[]

        type = mutation_required[0]
        chromosome_index = mutation_required[1]
        actual_mutation = mutation_required[2]

        if type == 'duplication':
            position = actual_mutation[1]
            gene_to_duplicate = actual_mutation[2]
            type_of_duplication = actual_mutation[3]
            chromosome = source_genome[chromosome_index]
            if position > len(chromosome)-1:
                position = len(chromosome)-1
            #check for applicable region at position -1 
            mutation_point_chromosome = list_of_mutation_points_genome[chromosome_index]
            if(isinstance(chromosome[position-1], str) and '*' in chromosome[position-1] and len(chromosome[position-1])>1):
                mutated_chromosome = self.duplication(chromosome, gene_to_duplicate, position)
                source_genome[chromosome_index] = mutated_chromosome
                #create record
                operation = {}
                operation['Type'] = type
                operation['Chromosome'] = chromosome_index + 1
                operation['Position of mutation in chromosome'] = position
                operation['Type of mutation'] = type_of_duplication
                operation['Genome before mutation'] = source_genome
                operation['Genome after mutation'] = source_genome
                list_of_mutations.append(operation)
        elif type == 'insertion':
            position = actual_mutation[0]
            # print('position value within do mutation')
            # print(position)
            gene_to_insert = actual_mutation[1]
            # print("insertion_chromosome index")
            # print(chromosome_index)
            # print(source_genome)
            chromosome = source_genome[chromosome_index]
            # print("insertion chromosome")
            # print(chromosome)
            if position > len(chromosome)-1:
                #print("changed pos")
                position = len(chromosome)-1
            mutation_point_chromosome = list_of_mutation_points_genome[chromosome_index]
            #print("error line 1030")
            #print(position)
            #print(len(chromosome))
            #print(source_genome)
            #print(chromosome_index)
            if(isinstance(chromosome[position-1], str) and '*' in chromosome[position-1] and len(chromosome[position-1])>1):
                mutated_chromosome = self.insertion(chromosome,position,gene_to_insert)
                #create record
                operation = {}
                operation['Type'] = type
                operation['Chromosome'] = chromosome_index + 1
                operation['Position of mutation in chromosome'] = position
                operation['Gene to insert'] = gene_to_insert
                operation['Genome before mutation'] = source_genome
                source_genome[chromosome_index] = mutated_chromosome
                operation['Genome after mutation'] = source_genome
                list_of_mutations.append(operation)

        elif type == 'deletion':
            position = actual_mutation[0]
            gene_to_delete = actual_mutation[1]
            chromosome = source_genome[chromosome_index]
            if position > len(chromosome)-1:
                position = len(chromosome)-1
            print("do_mutation deletion : pos : " + str(position))
            mutation_point_chromosome = list_of_mutation_points_genome[chromosome_index]
            if(isinstance(chromosome[position-1], str) and '*' in chromosome[position-1] and len(chromosome[position-1])>1):
                mutated_chromosome = self.deletion(chromosome, position)
                #create record
                operation = {}
                operation['Type'] = type
                operation['Chromosome'] = chromosome_index + 1
                operation['Position of mutation in chromosome'] = position
                operation['Gene to delete'] = gene_to_delete
                operation['Genome before mutation'] = source_genome
                source_genome[chromosome_index] = mutated_chromosome
                operation['Genome after mutation'] = source_genome
                list_of_mutations.append(operation)

        
        # #Create a list of applicable cromosomes
        # list_app_chrom = []
        # for c in range(len(list_of_mutation_points_genome)):
        #     chromsome = list_of_mutation_points_genome[c]
        #     if chromsome != []:
        #         list_app_chrom.append(c)
        # #randomly pick applicable chromosome
        # rand_chrom = randint(0, len(list_app_chrom)-1)
        # rand_chrom = list_app_chrom[rand_chrom]
        # #pick number of mutations within that chromosome
        # picked_chrom = source_genome[rand_chrom]
        # picked_chrom_app_intergenic_regions = list_of_mutation_points_genome[rand_chrom]
        # # print(picked_chrom_app_intergenic_regions)
        # rand_number_mutations_within_chrom = randint(0, len(picked_chrom_app_intergenic_regions)-1)
        # len_genes_in_picked_chrom = len(list_of_genes_genome[rand_chrom])
        # for r in range(rand_number_mutations_within_chrom):

        #     #recheck mutation points within genome
        #     list_of_genes = []
        #     list_of_genes_genome = []
        #     list_of_mutation_points = []
        #     list_of_mutation_points_genome = []
        #     for genes_with_intergenic_approved in source_genome:
        #         for i in range(len(genes_with_intergenic_approved)):
        #             # print(genes_with_intergenic_approved)
        #             if isinstance(genes_with_intergenic_approved[i],str) and len(genes_with_intergenic_approved[i]) > 1 and '*' in genes_with_intergenic_approved[i]:
        #                 # count_applicable_regions += 1
        #                 if i != len(genes_with_intergenic_approved)-2:
        #                     list_of_mutation_points.append(i+1)
        #             elif (not isinstance(genes_with_intergenic_approved[i],str)) or (isinstance(genes_with_intergenic_approved[i],str) and '*' not in genes_with_intergenic_approved[i]):
        #                 list_of_genes.append(genes_with_intergenic_approved[i])
        #         list_of_genes_genome.append(list_of_genes)
        #         list_of_mutation_points_genome.append(list_of_mutation_points)
        #         list_of_mutation_points =[]

        #     picked_chrom = source_genome[rand_chrom]
        #     picked_chrom_app_intergenic_regions = list_of_mutation_points_genome[rand_chrom]
        #     print(rand_chrom)
        #     print(picked_chrom_app_intergenic_regions)
        #     print(list_of_mutation_points_genome)
        #     print(picked_chrom)
        #     position_mutation = randint(0, len(picked_chrom_app_intergenic_regions)-1)
        #     len_genes_in_picked_chrom = len(list_of_genes_genome[rand_chrom])
        #     #randomly pick a mutation
        #     mutation_type = randint(0, 11)
            
        #     if mutation_type <= 2:
        #         #insertion
        #         mutated = self.insertion(picked_chrom, position_mutation)
        #         list_of_mutations.append(["insert", rand_chrom, position_mutation])
        #         #replace orginal with mutated
        #         source_genome[rand_chrom] = mutated
        #     elif (mutation_type > 2 or mutation_type <= 8) and len_genes_in_picked_chrom > 2:
        #         #deletion
        #         mutated = self.deletion(picked_chrom, position_mutation)
        #         list_of_mutations.append(["deletion", rand_chrom, position_mutation])
        #         #replace orginal with mutated
        #         source_genome[rand_chrom] = mutated
        #     else:
        #         #pick position to insert duplication
        #         pos = randint(0, len(picked_chrom_app_intergenic_regions)-1)
        #         pos_f = picked_chrom_app_intergenic_regions[pos]
        #         if (pos_f+2==position_mutation) or (pos_f==position_mutation):
        #             type = 0
        #         else:
        #             type = 1
        #         #duplicatiom
        #         mutated = self.duplication(picked_chrom, position_mutation, pos_f)
        #         list_of_mutations.append(["duplication", rand_chrom, position_mutation, pos_f, type])
        #         #replace orginal with mutated
        #         source_genome[rand_chrom] = mutated




        
        
        
        
        
        
        
        # print(list_of_mutation_points_genome)
        
        #get a random int from 0 to count_applicable_regions (how many mutations)
        # print(count_applicable_regions)
        # rand_int_muations = 0
        # if count_applicable_regions%2==0:
        #     half = count_applicable_regions/2
        #     rand_int_muations = randint(0, half)
        # else:
        #     half = (count_applicable_regions-1)/2
        #     rand_int_muations = randint(0, half)
        # rand_int_muations = randint(0, count_applicable_regions)
        # print("number of random mutations: " + str(rand_int_muations))
        #randomly allocate mutations to the picked applicable regions
        # for i in range(rand_int_muations):
        #     if i > 0 :
        #         list_of_mutation_points_genome = []
        #         for genes_with_intergenic_approved in source_genome:
        #             for i in range(len(genes_with_intergenic_approved)):
        #                 if isinstance(genes_with_intergenic_approved[i], str)==True and len(genes_with_intergenic_approved[i]) > 1 and '*' in genes_with_intergenic_approved[i]:
        #                     if i != len(genes_with_intergenic_approved):
        #                         list_of_mutation_points.append(i+1)
        #             list_of_mutation_points_genome.append(list_of_mutation_points)
        #             list_of_mutation_points =[]

        #     position_app_reg_chrom =[]
        #     rand_chrom = 0
        #     source_chrom = []
            # loop = 0
            # print(list_of_mutation_points_genome)
            # while(len(position_app_reg_chrom) == 0):
                # print("stuck in do mutations in while loop for app regions in chrom")
                # print(position_app_reg_chrom)
                # rand_chrom = randint(0,len(source_genome)-1)
                # print(rand_chrom)
                # print(list_of_mutation_points_genome)
                # position_app_reg_chrom = list_of_mutation_points_genome[rand_chrom]
                # print(rand_chrom)
                # print(len(source_genome))
                # source_chrom = source_genome[rand_chrom]
                # loop += 1
            # sys.exit(0)

            #edited
            #randomly pick a position from position_app_reg_chrom to position
            # if len(position_app_reg_chrom) > 1:
                # rand_pos = randint(0,len(position_app_reg_chrom)-1)
            # else:
            #     rand_pos = 0

                # position = position_app_reg_chrom[rand_pos]

                #randomly pick a mutation
                # mutation_type = randint(0, 11)
                
                # if mutation_type <= 2:
                #     #insertion
                #     mutated = self.insertion(source_chrom, position)
                #     list_of_mutations.append(["insert", rand_chrom, position])
                #     #replace orginal with mutated
                #     source_genome[rand_chrom] = mutated
                # elif mutation_type > 2 or mutation_type <= 8:
                #     #deletion
                #     mutated = self.deletion(source_chrom, position)
                #     list_of_mutations.append(["deletion", rand_chrom, position])
                #     #replace orginal with mutated
                #     source_genome[rand_chrom] = mutated
                # else:
                #     #pick position to insert duplication
                #     pos = randint(0, len(position_app_reg_chrom)-1)
                #     pos_f = position_app_reg_chrom[pos]
                #     if (pos_f+2==position) or (pos_f==position):
                #         type = 0
                #     else:
                #         type = 1
                #     #duplicatiom
                #     mutated = self.duplication(source_chrom, position, pos_f)
                #     list_of_mutations.append(["duplication", rand_chrom, position, pos_f, type])
                #     #replace orginal with mutated
                #     source_genome[rand_chrom] = mutated


        #enact mutations and return mutated genome (to enact, need to complete 3 mutation functions)
        # print("source genome after random mutation" + str(source_genome))
        return source_genome, list_of_mutations, mutation_point_chromosome

    def insertion(self, source_chromosome, position_applicable_region, gene):
        #insertion of gene
        # gene = randint(1,40)
        # print("in insert")
        # print(position_app_region)
        # print(len(source_chromosome))
        source_chromosome[position_applicable_region-1] = gene
        # print('end insert')
        return source_chromosome

    def deletion(self, source_chromosome, position_applicable_region):
        #deletion of gene
        # print("start deletion")
        #print((source_chromosome))
        #print(len(source_chromosome))
        #print(position_app_region)
        # print("end deletion")
        del source_chromosome[position_applicable_region]
        if position_applicable_region > 0 :
            del source_chromosome[position_applicable_region-1]
        # source_chromosome.pop(position_app_region)
        # source_chromosome.pop(position_app_region-1)
        
        return source_chromosome

    def duplication(self, source_chromosome, gene, insertion_position):
        #duplication of a gene
        # print("start dup")
        # print(position_app_region)
        # print(len(source_chromosome))
        # print("end dup")
        # gene_to_duplicate = source_chromosome[position_app_region]
        source_chromosome[insertion_position-1] = gene

        return source_chromosome


    #TODO CHECK THIS OUT
    def foreign_dna_pool(self, source, target):
        # Check what genes are not in source that is in target
        source_genome = []
        target_genome = []
        # create master lists

        for chromosome in source:
            for i in range(len(chromosome)):
                if isinstance(chromosome[i],int):
                    source_genome.append(int(chromosome[i]))
                elif isinstance(chromosome[i],str) and "_" in chromosome[i]:
                    if len(chromosome[i])==2:
                        gene = chromosome[i]
                        source_genome.append(int(gene[:1]))
                    elif len(chromosome[i])==3:
                        gene = chromosome[i]
                        source_genome.append(int(gene[:2]))
        # and '*' not in chromosome[i]
        for chromosome in target:
            for i in range(len(chromosome)):
                if isinstance(chromosome[i],int):
                    target_genome.append(int(chromosome[i]))


        # Find the difference between source and target
        difference = list(set(target_genome) - set(source_genome))
        # print(difference)
        if len(difference) > 0:
            # define the ratio (1/5)
            number_of_random_ints = (len(difference) * 3) - (len(difference))  # change ratio here (5)

            # create foreign dna
            foreign_dna = []
            count = 0
            while count < (number_of_random_ints):
                gene = randint(1, 40)
                if len(foreign_dna) >= 1:
                    if gene not in foreign_dna:
                        foreign_dna.append(gene)
                        count += 1
                else:
                    foreign_dna.append(gene)

            # add difference to foreign dna and check duplicates and add foreign DNA if necessary
            foreign_dna = difference + foreign_dna
            foreign_dna = list(set(foreign_dna))
            if len(foreign_dna) < ((len(difference)) * 3):  # change ratio here (5)
                count = len(foreign_dna)
                while (len(foreign_dna) < ((len(difference)) * 3)):
                    gene = randint(1, 40)
                    if gene not in foreign_dna:
                        foreign_dna.append(gene)
                        count += 1
            
            #Use for_dna list that was created to create foreign dna fragments (random number of frag and random length of fragments)
            number_of_fragments = randint(1,99)
            len_fragments = 1
            #(len(difference))+2
            #choose randomly from foreign_dna list to add to frags
            list_of_fragments = []
            fragment = []
            for j in range(number_of_fragments):
                for i in range(len_fragments):
                    choice = randint(0,len(foreign_dna)-1)
                    fragment.append(foreign_dna[choice])
                #Ensure unique fragments in list
                if j > 0 and fragment not in list_of_fragments:
                    list_of_fragments.append(fragment)
                else:
                    j -= 1
                fragment = []

            #Check for the difference in genes within atleast one fragment in list
            check = True
            for f in list_of_fragments:
                if difference in f:
                    check = False
            print(check)
            if check == True:
                print(difference)
                final_fragment = difference[:]
                #add a fragment that does contain the difference
                #Check that the gene does not already exist in the fragment
                while len(final_fragment) <= len(difference)+1:
                    unique_fragment =  foreign_dna[randint(0, len(foreign_dna)-1)]
                    if unique_fragment not in final_fragment:
                        final_fragment.append(unique_fragment)
                # print(final_fragment)
                list_of_fragments.append(final_fragment)

            #Tag foreign DNA
            for i in list_of_fragments:
                fragment = i
                for j in range(len(fragment)):
                    fragment[j] = str(fragment[j])+"_"
            print("list of frags when there is differenct")
            print(list_of_fragments)
            return list_of_fragments
        else:
            # define the ratio (1/5)
            number_of_random_ints = randint(1,5)

            # create foreign dna
            foreign_dna = []
            count = 0
            while count < (number_of_random_ints):
                gene = randint(1, 40)
                if len(foreign_dna) >= 1:
                    if gene not in foreign_dna:
                        foreign_dna.append(gene)
                        count += 1
                else:
                    foreign_dna.append(gene)
            
            #Use foreign_dna list that was created to create foreign dna fragments (random number of fragment and random length of fragments)
            number_of_fragments = randint(1,99)
            len_fragments = 1
            #randint(1,5)
            #choose randomly from for_dna list to add to frags
            list_of_fragments = []
            fragment = []
            for j in range(number_of_fragments):
                for i in range(len_fragments):
                    choice = randint(0,len(foreign_dna)-1)
                    fragment.append(foreign_dna[choice])
                #Ensure unique fragments in list
                if j > 0 and fragment not in list_of_fragments:
                    list_of_fragments.append(fragment)
                else:
                    j -= 1
                fragment = []

            #Tag foreign DNA
            for i in list_of_fragments:
                fragment = i
                for j in range(len(fragment)):
                    fragment[j] = str(fragment[j])+"_"
            print("list of frags when no differenct")
            print(list_of_fragments)
            return list_of_fragments

    '''
    Does the mutation
    '''

    #def take_action(self, operation):
    #    state_copy = self.state.copy()
    #    operation_type = []

        # if it is an insertion or deletion:
    #    if len(operation) == 1:

            # insertion
    #        if type(operation[0]) is tuple:

    #            state_copy.append(operation[0])
    #            operation_type = 'ins'

    #        else:
    #            state_copy.remove(operation[0])
    #            operation_type = "del_"

            # else it is another structural event
    #    elif len(operation) == 2:
    #        if type(operation[0][1]) is tuple and type(operation[1][0]) is tuple:
    #            state_copy.append(operation[0][1] * 2)
    #            state_copy.append(operation[1][0] * 2)
    #            operation_type = "dup_"

    #        elif type(operation[0][1]) is not tuple or type(operation[1][0]) is not tuple:
    #            state_copy.remove(operation[0][1])
    #            state_copy.remove(operation[1][0])
    #            operation_type = "del_"

    #    elif len(operation) == 3:
    #        if type(operation[0][1][2]) is tuple and type(operation[0][2][1]) is tuple:
    #            state_copy.append(operation[0][2])
    #            state_copy.append(operation[2][1])
    #            state_copy.remove(operation[0][1])
    #            state_copy.remove(operation[0][0])
    #            operation_type = "fDNA"

    #    else:
            # RAISE AN ERROR
    #        print("Error in take_action function")

        # order and sort
    #    ordered_and_sorted = Node.order_and_sort(self, state_copy)

    #    return ordered_and_sorted, operation_type

    '''
    Checks if the transformed genome A is equal to the target genome B
    '''

    #def is_equivalent(self, adjacenciesB):
    #    adjacenciesA = self.state.copy()
    #    adjacenciesB = adjacenciesB

    #    ordered_adjacenciesA = []
    #    for element in adjacenciesA:
    #        if type(element) is tuple:
    #            if int(element[0]) < int(element[1]):
    #                ordered_adjacenciesA.append(element)
    #            else:
    #                ordered_adjacenciesA.append((element[1], element[0]))
    #        else:
    #            ordered_adjacenciesA.append(element)

    #    for element in adjacenciesB:
    #        if element in ordered_adjacenciesA:
    #            pass
    #        else:
    #            return False
    #    return True

    '''
    take the source (with transformation) genome and orders and sorts the genes in the source genome for the target genome
    '''

    #def order_and_sort(self, adjacencies):
    #    telomers = []
    #    adjs = []
    #    for element in adjacencies:
    #        if type(element) is tuple:

                # if it is a single gene adjacency
    #            if int(element[0]) == int(element[1]):
    #                if element[0] % 1 == 0:
    #                    adjs.append(element)
    #                else:
    #                    adjs.append((element[1], element[0]))

    #            elif int(element[0]) < int(element[1]):
    #                adjs.append(element)
    #            else:
    #                adjs.append((element[1], element[0]))
    #        else:
    #            telomers.append(element)
    #    telomers.sort()
    #    adjs.sort()

    #    sort = telomers + adjs

    #    return sort, telomers, adjs

# if __name__ == '__main__':
#     gen_ex_obj = Gen_xtremities.Xtremities()
#     genome_gene_extremities = gen_ex_obj.gene_extremity()




    # def foreign_dna_pool(self, source, target):
    #     # Check what genes are not in source genome but are in target genome
    #     source_genome = []
    #     target_genome = []

    #     # create master lists

    #     for chromosome in source:
    #         for i in range(len(chromosome)):
    #             if isinstance(chromosome[i], int):
    #                 source_genome.append(int(chromosome[i]))
    #             elif isinstance(chromosome[i], str) and "_" in chromosome[i]:
    #                 if len(chromosome[i]) == 2:
    #                     gene = chromosome[i]
    #                     source_genome.append(int(gene[:1]))
    #                 elif len(chromosome[i]) == 3:
    #                     gene = chromosome[i]
    #                     source_genome.append(int(gene[:2]))

    #     for chromosome in target:
    #         for i in range(len(chromosome)):
    #             if isinstance(chromosome[i], int):
    #                 target_genome.append(int(chromosome[i]))

    #     # Find the difference between source genome and target genome
    #     difference = list(set(target_genome) - set(source_genome))

    #     if len(difference) > 0:
    #         # define the ratio (1/5)
    #         # change ratio here (5)
    #         number_of_random_ints = (len(difference) * 3) - (len(difference))

    #         # create foreign dna
    #         for_dna = []
    #         count = 0
    #         while count < (number_of_random_ints):
    #             gene = random.randint(1, 40)
    #             if len(for_dna) >= 1:
    #                 if gene not in for_dna:
    #                     for_dna.append(gene)
    #                     count += 1
    #             else:
    #                 for_dna.append(gene)

    #         # add difference to foreign dna and check duplicates and add foreign DNA if necessary
    #         for_dna = difference + for_dna
    #         for_dna = list(set(for_dna))
    #         if len(for_dna) < ((len(difference)) * 3):  # change ratio here (5)
    #             count = len(for_dna)
    #             while (len(for_dna) < ((len(difference)) * 3)):
    #                 gene = random.randint(1, 40)
    #                 if gene not in for_dna:
    #                     for_dna.append(gene)
    #                     count += 1

    #         # Use for_dna list that was created to create foreign dna fragments (random number of frag and random length of fragments)
    #         number_of_frags = random.randint(1, 99)
    #         len_frags = 1

    #         # choose randomly from for_dna list to add to frags
    #         list_of_frags = []
    #         frag = []
    #         for j in range(number_of_frags):
    #             for i in range(len_frags):
    #                 choice = random.randint(0, len(for_dna)-1)
    #                 frag.append(for_dna[choice])
    #             # Ensure unique fragments in list
    #             if j > 0 and frag not in list_of_frags:
    #                 list_of_frags.append(frag)
    #             else:
    #                 j -= 1
    #             frag = []

    #         # Check for the difference in genes within at least one fragment in list
    #         check = True
    #         for f in list_of_frags:
    #             if difference in f:
    #                 check = False
    #         if check == True:
    #             final_frag = difference[:]
    #         # add a fragment that does contain the difference
    #         # Check that the gene does not already exist in the fragment
    #             while len(final_frag) <= len(difference)+1:
    #                 c = for_dna[random.randint(0, len(for_dna)-1)]
    #                 if c not in final_frag:
    #                     final_frag.append(c)
    #             list_of_frags.append(final_frag)

    #         # Tag foreign DNA
    #         for i in list_of_frags:
    #             frag = i
    #             for j in range(len(frag)):
    #                 frag[j] = str(frag[j])+"_"
    #         return list_of_frags

    #     else:
    #         # define the ratio (1/5)
    #         number_of_random_ints = random.randint(1, 5)

    #         # create foreign dna
    #         for_dna = []
    #         count = 0
    #         while count < (number_of_random_ints):
    #             gene = random.randint(1, 40)
    #             if len(for_dna) >= 1:
    #                 if gene not in for_dna:
    #                     for_dna.append(gene)
    #                     count += 1
    #             else:
    #                 for_dna.append(gene)

    #         # Use for_dna list that was created to create foreign dna fragments (random number of frag and random length of fragments)
    #         number_of_frags = random.randint(1, 99)
    #         len_frags = 1
    #         # choose randomly from for_dna list to add to frags
    #         list_of_frags = []
    #         frag = []
    #         for j in range(number_of_frags):
    #             for i in range(len_frags):
    #                 choice = random.randint(0, len(for_dna)-1)
    #                 frag.append(for_dna[choice])
    #             # Ensure unique fragments in list
    #             if j > 0 and frag not in list_of_frags:
    #                 list_of_frags.append(frag)
    #             else:
    #                 j -= 1
    #             frag = []

    #         # Tag foreign DNA
    #         for i in list_of_frags:
    #             frag = i
    #             for j in range(len(frag)):
    #                 frag[j] = str(frag[j])+"_"

    #         print(f'{list_of_frags}__________________________')
    #         return list_of_frags


    # def intergenic_regions(self,genes_with_intergenic_genome):
        
    #     for genes_with_intergenic in genes_with_intergenic_genome:
    #         for i in range(len(genes_with_intergenic)):
    #             if i % 2 == 0 or i == 0:
    #                 region = genes_with_intergenic[i]
                
    #                 if len(region) > 2:
    #                     value = region[2]+region[2]
    #                 else:
    #                     value = region[1]
    #                 if int(value) < 5:
    #                     genes_with_intergenic[i] = '*'
    #     return genes_with_intergenic_genome


      # def intergenerator(self,numbered_genes_list):
    #     genes_with_intergenic_chrom = []
    #     genes_with_intergenic = []
    #     for i in range(len(numbered_genes_list)):
    #         chrom = numbered_genes_list[i]
    #         length = len(chrom)
          
        #         ntergenic_chrom.append(start)
    #             if j != length-1:
    #                 genes_with_intergenic_chrom.append(region)
    #         genes_with_intergenic.append(genes_with_intergenic_chrom)
    #         genes_with_intergenic_chrom = []
      
    #     return genes_with_intergenic