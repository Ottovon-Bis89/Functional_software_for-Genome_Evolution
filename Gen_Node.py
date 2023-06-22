
from random import randint
import sys
import Gen_xtremities
import Data_generator


class Node:

    def __init__(self):
        self.state = []
        self.children = []
        self.children_weights = []
        self.next_operation = 0
        self.next_operation_weight = []
        
    """
    The function returns a list  of the operations needed to transform the
    source  genome to the target genome. Itreturns random legal options that can be applied to A,
    called recursively until A can be transformed to B
    It also chooses a fragment of foreign DNA and inserts it into the source genome

    """
    def get_legal_operations(self,source_genome, target_genome):
        list_of_legal_operations = []
        adjacenciesA = source_genome
        adjacenciesB = target_genome
        switch = True
        loop_counter = 0  # No foreign DNA in first iteration of mutations
        for_Dna_counter = 0

        while switch:

            for element in adjacenciesB:
                if element in adjacenciesA:
                    pass
                else:
                    source_genome = adjacenciesA[:]

            #         # if element is an adjacency:
            #         if type(element) is tuple:
            #             x = element[0]
            #             y = element[1]
            #             w = 0
            #             z = 0

            #             # if elements containing x and y respectively  are adjacencies
            #             for marker in adjacenciesA_copy:
            #                 if type(marker) is tuple:
            #                     if marker[0] == x or marker[1] == x:
            #                         w = marker

            #                     if marker[0] == y or marker[1] == y:
            #                         z = marker

            #             # element containing x in adjacenciesA is a telomere
            #             if w == 0:
            #                 w = x
            #             # element containing y in adjacenciesA is a telomere
            #             if z == 0:
            #                 z = y

            #             if w != z:
            #                 adjacenciesA_copy.append((x, y))
            #                 adjacenciesA_copy.remove(w)

            #                 adjacenciesA_copy.remove(z)

            #                 # if w is an adjacency:
            #                 if type(w) is tuple:
            #                     # calculate w'x
            #                     if w[0] == x:
            #                         w_not_x = w[1]
            #                     else:
            #                         w_not_x = w[0]

            #                     # if z is an adjacency:
            #                     if type(z) is tuple:
            #                         # calculate z'y
            #                         if z[0] == y:
            #                             z_not_y = z[1]
            #                         else:
            #                             z_not_y = z[0]

            #                         adjacenciesA_copy.append((w_not_x, z_not_y))

            #                         # order operation before appending
            #                         if w[0] < z[0]:
            #                             op_1 = (w, z)
            #                         else:
            #                             op_1 = (z, w)
            #                         if x < y:
            #                             op_2_1 = (x, y)
            #                         else:
            #                             op_2_1 = (y, x)
            #                         if w_not_x < z_not_y:
            #                             op_2_2 = (w_not_x, z_not_y)
            #                         else:
            #                             op_2_2 = (z_not_y, w_not_x)
            #                         if op_2_1[0] < op_2_2[0]:
            #                             op_2 = (op_2_1, op_2_2)
            #                         else:
            #                             op_2 = (op_2_2, op_2_1)
            #                         ordered_operation = (op_1, op_2)

            #                         if ordered_operation not in list_of_legal_operations:
            #                             list_of_legal_operations.append(ordered_operation)
            #                         else:
            #                             pass

            #                     # else z is a telomere
            #                     else:
            #                         adjacenciesA_copy.append(w_not_x)

            #                         if x < y:
            #                             op_2_1 = (x, y)
            #                         else:
            #                             op_2_1 = (y, x)

            #                         op_2 = (op_2_1, w_not_x)
            #                         ordered_operation = ((w, z), op_2)

            #                         if ordered_operation not in list_of_legal_operations:
            #                             list_of_legal_operations.append(ordered_operation)
            #                         else:
            #                             pass

            #                 # else w is a telomere
            #                 else:
            #                     # if z is an adjacency
            #                     if type(z) is tuple:
            #                         # calculate z'y
            #                         if z[0] == y:
            #                             z_not_y = z[1]
            #                         else:
            #                             z_not_y = z[0]
            #                         adjacenciesA_copy.append(z_not_y)

            #                         if x < y:
            #                             op_2_1 = (x, y)
            #                         else:
            #                             op_2_1 = (y, x)

            #                         ordered_operation = ((z, w), (op_2_1, z_not_y))

            #                         if ordered_operation not in list_of_legal_operations:
            #                             list_of_legal_operations.append(ordered_operation)
            #                         else:
            #                             pass

            #                     # else z is a telomere
            #                     else:
            #                         if x < y:
            #                             op_2 = (x, y)
            #                         else:
            #                             op_2 = (y, x)
            #                         if w < z:
            #                             ordered_operation = (w, z, op_2)
            #                         else:
            #                             ordered_operation = (z, w, op_2)

            #                         if ordered_operation not in list_of_legal_operations:
            #                             list_of_legal_operations.append(ordered_operation)
            #                         else:
            #                             pass

            #         # else if the element is a telomere
            #         else:
            #             w = 0
            #             x = element

            #             for marker in adjacenciesA_copy:
            #                 if type(marker) is tuple:
            #                     if marker[0] == x or marker[1] == x:
            #                         w = marker
            #             if w == 0:
            #                 w = x

            #             # if w is not a telomere:
            #             if w != x:
            #                 adjacenciesA_copy.append(w[0])
            #                 adjacenciesA_copy.append(w[1])
            #                 adjacenciesA_copy.remove(w)
            #                 operation = (w, (w[0]), (w[1]))
            #                 if operation not in list_of_legal_operations:
            #                     list_of_legal_operations.append(operation)
            #                 else:
            #                     pass
            #             # if the element in the adjacencies is a foreign dna
            #             else:
            #                 for marker in adjacenciesA_copy:
            #                     if type(marker) is tuple:
            #                         if marker[0] != x or marker[1] != x:
            #                             fdna = marker
            #                         else:
            #                             if marker[0] != y or marker[1] != y:
            #                                 fdna = marker
            #                                 adjacenciesA_copy.append(fdna[0])
            #                                 adjacenciesA_copy.append(fdna[1])
            #                                 operation = (fdna, (fdna[0]), (fdna[1]))
            #                                 if operation not in list_of_legal_operations:
            #                                     list_of_legal_operations.append(operation)
            #                                 else:
            #                                     pass
    
            if loop_counter > 0 :
                # check number of applicale region, if 0 then create 
                count_app = 0
                for chromosome in adjacenciesA:
                    for i in range(len(chromosome)):
                        if isinstance(chromosome[i], str) and '*' in chromosome[i] and len(chromosome[i]) > 1 :
                            count_app += 1
                
                clean_chrom = []
                clean_genome = []

                if count_app >= 0:
                    #remove all unapplicable intergenic regions and call intergenerator
                    for chromosome in adjacenciesA:
                        for i in range(len(chromosome)):
                            if isinstance(chromosome[i],str) and '*' not in chromosome[i]:
                                clean_chrom.append(chromosome[i])
                            elif isinstance(chromosome[i], int):
                                clean_chrom.append(chromosome[i])
                        clean_genome.append(clean_chrom)
                        clean_chrom = []
                    gen_obj = Data_generator.Data_generator()
                    normal_i_reg = gen_obj.intergenerator(clean_genome)
                    adjacenciesA = gen_obj.intergenic_regions(normal_i_reg)
       
                # randomly choose to insert foreign dna
                choose = randint(0, 1000)
                if (choose <= 1000 and for_Dna_counter != 0) :
                    series_of_mutation,mutation_required = self.mutation_legal_operations(adjacenciesA, adjacenciesB)
                    
                    if series_of_mutation == [] and mutation_required !=():
                        source_genome, mutation_list = self.do_mutation(adjacenciesA, mutation_required)
        
                        adjacenciesA = source_genome[:]

                        list_of_legal_operations.append(mutation_list)
                        switch = True
                    else:
                        while (any(series_of_mutation) and mutation_required !=()) or mutation_required !=():
                            mutations_finale = []
                            for i in range(len(series_of_mutation)):
                                if i == 0:
                                    mutation_type = 'ins'
                                elif i == 1:
                                    mutation_type = 'del'
                                else:
                                    mutation_type = 'dup'
                                mutation = series_of_mutation[i]
                                for chromosome_number in range(len(mutation)):
                                    if mutation[chromosome_number] != []:
                                        chromosome_index = chromosome_number
                                        chrom = mutation[chromosome_number]
                                        for m in range(len(chrom)):
                                            do_mutation = (mutation_type, chromosome_index, chrom[m])
                                            source_genome, mutation_list = self.do_mutation(adjacenciesA, do_mutation)
                                            adjacenciesA = source_genome[:]
                                            mutations_finale.append(mutation_list)
                            list_of_legal_operations.append(mutations_finale)
                            clean_chrom = []
                            clean_genome = []

                            #remove all unapplicable intergenic regions and call intergenerator 
                            # to insert new applicable regions for mutations to occur
                            for chromosome in adjacenciesA:
                                for i in range(len(chromosome)):
                                    if isinstance(chromosome[i],str) and '*' not in chromosome[i]:
                                        clean_chrom.append(chromosome[i])
                                    elif isinstance(chromosome[i], int):
                                        clean_chrom.append(chromosome[i])
                                clean_genome.append(clean_chrom)
                                clean_chrom = []

                            gen_obj = Data_generator.Data_generator()
                            normal_i_reg = gen_obj.intergenerator(clean_genome)
                            adjacenciesA = gen_obj.intergenic_regions(normal_i_reg)
 
                            series_of_mutation,mutation_required = self.mutation_legal_operations(adjacenciesA, adjacenciesB)
                    
                            if mutation_required ==():
                                break
                        switch = False
                elif ((for_Dna_counter < 100 or for_Dna_counter ==0)):
                    print("\tInserted foreign DNA")
                    for_Dna_counter += 1
                    #Here is list of foreign dna where fragments are sublists
                    for_dna = []
                    while for_dna == []:
                        for_dna = self.foreign_dna_pool(adjacenciesA, adjacenciesB)

                    #  Randomly choose a foreign dna from pool
                    for_dna_len = len(for_dna) -1
                    choice_for_dna = randint(0, for_dna_len)
                    chosen = for_dna[choice_for_dna]

                    # add foreign dna 
                    adjacenciesA, list_of_operationss = self.add_for_dna(adjacenciesA, chosen)
                    list_of_legal_operations.append(list_of_operationss)

                    mutation_genome = adjacenciesA.copy()
                    series_of_mutation, mutation_required = self.mutation_legal_operations(mutation_genome, adjacenciesB)
    
                    if series_of_mutation == []:
                        
                        source_genome, mutation_list = self.do_mutation(adjacenciesA, mutation_required)
                        adjacenciesA = source_genome[:]
                        list_of_legal_operations.append(mutation_list)
                        switch = True
        
                    else:
                        while (any(series_of_mutation) and mutation_required ==()) or mutation_required !=():
                            mutations_finale = []
                            for i in range(len(series_of_mutation)):
                                if i == 0:
                                    mutation_type = 'ins'
                                elif i == 1:
                                    mutation_type = 'del'
                                else:
                                    mutation_type = 'dup'

                                mutation = series_of_mutation[i]

                                for chromosome_number in range(len(mutation)):
                                    if mutation[chromosome_number] != []:
                                        chromosome_index = chromosome_number
                                        chrom = mutation[chromosome_number]
                                        for m in range(len(chrom)):
                                            do_mutation = (mutation_type, chromosome_index, chrom[m])
                                            source_genome, mutation_list = self.do_mutation(adjacenciesA, do_mutation)
                                            adjacenciesA = source_genome[:]
                                            mutations_finale.append(mutation_list)
                            
                            list_of_legal_operations.append(mutations_finale)
                            clean_chrom = []
                            clean_genome = []

                            #remove all unapplicable intergenic regions and call intergenerator
                            for chromosome in adjacenciesA:
                                for i in range(len(chromosome)):
                                    if isinstance(chromosome[i],str) and '*' not in chromosome[i]:
                                        clean_chrom.append(chromosome[i])
                                    elif isinstance(chromosome[i], int):
                                        clean_chrom.append(chromosome[i])

                                clean_genome.append(clean_chrom)
                                clean_chrom = []

                            gen_obj = Data_generator.Data_generator()
                            normal_i_reg = gen_obj.intergenerator(clean_genome)
                            adjacenciesA = gen_obj.intergenic_regions(normal_i_reg)

                            series_of_mutation,mutation_required = self.mutation_legal_operations(adjacenciesA, adjacenciesB)
                        
                            if mutation_required ==():
                                break
                        switch = False
                        
            elif loop_counter == 0:
                series_of_mutation, mutation_required = self.mutation_legal_operations(adjacenciesA, adjacenciesB)
                
                if series_of_mutation == [] and mutation_required !=():
                    switch = True

                    #Do random mutation
                    source_genome, mutation_list = self.do_mutation(adjacenciesA, mutation_required)
                    print("Could not find straight path to get to target_genome so randomly mutated")

                    adjacenciesA = source_genome[:]
                    list_of_legal_operations.append(mutation_list)
                    
                    # check number of applicale region, if 0 then create 
                    count_app = 0
                    for chromosome in adjacenciesA:
                        for i in range(len(chromosome)):
                            if isinstance(chromosome[i], str) and '*' in chromosome[i] and len(chromosome[i]) > 1 :
                                count_app += 1
                    print(f"Within first iteration after any and all mutations we check applicable reagions, count is : {str(count_app)}")
                    clean_chrom = []
                    clean_genome = []
               
                    if count_app <= len(adjacenciesA)-1:
                        #remove all unapplicable intergenic regions and call intergenerator
                        for chromosome in adjacenciesA:
                            for i in range(len(chromosome)):
                                if (isinstance(chromosome[i],str) and '*' not in chromosome[i]) or isinstance(chromosome[i],int):
                                    clean_chrom.append(chromosome[i])
                            clean_genome.append(clean_chrom)
                            clean_chrom = []
                        
                        gen_obj = Data_generator.Data_generator()
                        normal_i_reg = gen_obj.intergenerator(clean_genome)
                        adjacenciesA = gen_obj.intergenic_regions(normal_i_reg)
                else:
                        while (any(series_of_mutation) and mutation_required ==()) or mutation_required !=():
                            
                            mutations_finale = []
                            for i in range(len(series_of_mutation)):
                                if i == 0:
                                    mutation_type = 'ins'
                                elif i == 1:
                                    mutation_type = 'del'
                                else:
                                    mutation_type = 'dup'
                                mutation = series_of_mutation[i]
                                for chromosome_number in range(len(mutation)):
                                    if mutation[chromosome_number] != []:
                                        chromosome_index = chromosome_number
                                        chrom = mutation[chromosome_number]
                                        for m in range(len(chrom)):
                                            do_mutation = (mutation_type, chromosome_index, chrom[m])
                                            source_genome, mutation_list = self.do_mutation(adjacenciesA, do_mutation)
                                            adjacenciesA = source_genome[:]
                                            mutations_finale.append(mutation_list)
                            list_of_legal_operations.append(mutations_finale)
                            clean_chrom = []
                            clean_genome = []

                            #remove all unapplicable intergenic regions and call intergenerator
                            for chromosome in adjacenciesA:
                                for i in range(len(chromosome)):
                                    if isinstance(chromosome[i],str) and '*' not in chromosome[i]:
                                        clean_chrom.append(chromosome[i])
                                    elif isinstance(chromosome[i], int):
                                        clean_chrom.append(chromosome[i])
                                clean_genome.append(clean_chrom)
                                clean_chrom = []
                                gen_obj = Data_generator.Data_generator()
                                normal_i_reg = gen_obj.intergenerator(clean_genome)
                                adjacenciesA = gen_obj.intergenic_regions(normal_i_reg)
                                
                            series_of_mutation,mutation_required = self.mutation_legal_ops(adjacenciesA, adjacenciesB)
                            
                            if mutation_required ==():
                                break
                        switch = False                
            else:
                break
            loop_counter += 1

        return list_of_legal_operations
    """
     This function adds a fragment of foreign DNA to the Source genome. The foreign fragment can be identified with an underscore(_) attached to an integer. 
     The path of foreign DNA fragment can be followed through the evolutionary journey of the source genome into 
     the target genome

    """
    def add_for_dna(self, source_genome, frag):
        # Count number of applicable intergenic regions to associate to number of mutations
        list_of_mutation_points = []
        list_of_mutation_points_genome = []

        for genes_with_intergenic_approved in source_genome:
            for i in range(len(genes_with_intergenic_approved)):
                if isinstance(genes_with_intergenic_approved[i], str) and len(genes_with_intergenic_approved[i]) > 1 and '*' in genes_with_intergenic_approved[i]:
                    list_of_mutation_points.append(i+1)

            list_of_mutation_points_genome.append(list_of_mutation_points)
            list_of_mutation_points = []
        
        #insert intergenic regions in foreign dna fragments 
        frag_with_intergenic_regions = []
        length = len(frag)
        for j in range(len(frag)):
            if j == 0 :
                random_bp = randint(5,10)
                region = '*' + str(random_bp)
                frag_with_intergenic_regions.append(region)
            random_bp = randint(5,10)
            start = frag[j]
            region = '*' + str(random_bp)
            frag_with_intergenic_regions.append(start)
            if j != length-1:
                frag_with_intergenic_regions.append(region)

        #find applicable intergenic regions in frag
        for i in range(len(frag_with_intergenic_regions)):
            if i % 2 == 0 or i == 0:
                region = frag_with_intergenic_regions[i]
                if len(region) > 2:
                    value = region[2]+region[2]
                else:
                    value = region[1]
                if int(value) < 5:
                    frag_with_intergenic_regions[i] = '*'


        # Account for chromosomes without intergenic regions
        position_app_reg_chrom = []
        source_chrom = []
        rand_chrom = []

        while len(position_app_reg_chrom) == 0 :
            rand_chrom = randint(0,len(list_of_mutation_points_genome)-1)
            position_app_reg_chrom = list_of_mutation_points_genome[rand_chrom]
            source_chrom = source_genome[rand_chrom]
        
        #randomly pick a position from position_app_reg_chrom to position
        rand_pos = randint(0,len(position_app_reg_chrom)-1)
        position = position_app_reg_chrom[rand_pos]

        mutated = []
        mutated = source_chrom[0:position-1] + frag_with_intergenic_regions + source_chrom[position:]

        source_genome[rand_chrom] = mutated
        return source_genome, ['F_DNA inserted ',rand_chrom, position, frag_with_intergenic_regions]


    """
    This function decides if mutations, any series of mutations, can take genome A to genome B
    check number of chromosomes -> possibility of chromosome deletion(target chromosmes less than source)
     or chromosome insertion (source chromosome count less than target)
    Check number of genes in chromosome for target and source -> indicators for insertion/foreign dna/deletion
    check signed integers(genes) between target and source
    Duplication - look at the target; if two of same signed integer next to each other -> tandom duplicatio
    if two of same signed ints in chromosome but not next to each other then -> transpositional
    source_genome = source[:]remove underscores that identify fragments in source genome
    """

    def mutation_legal_operations(self, source, target_genome):
       
        chromo = []
        source_genome = []

        for chrom in source:
            for i in range(len(chrom)):
                if isinstance(chrom[i], str) and '_' in chrom[i]:
                    if len(chrom[i])==3:
                        gene = chrom[i]
                        chromo.append(int(gene[:2]))
                    elif len(chrom[i])==2:
                        gene = chrom[i]
                        chromo.append(int(gene[:1]))
                elif isinstance(chrom[i], str):
                    chromo.append((chrom[i]))
                elif isinstance(chrom[i], int):
                    chromo.append((chrom[i]))
                elif ((isinstance(chrom[i], str) and '*' in chrom[i])):
                    chromo.append((chrom[i]))
            source_genome.append(chromo)
            chromo = []

        #step 1, check genes per chromosome between target and source [number of chromosomes should always be the same]
        #1.1 in target and not in source [CREATE in list that contains tuples of (position,gene)]
        in_genome = []
        in_target = []
        
        #Take note of different length of genomes where this condition does not hold
        for j in range(len(target_genome)):
            in_target = []
            chromosome = source_genome[j]
            t_chrom = target_genome[j]

            for i in range(len(t_chrom)):
                if '*' not in str(t_chrom[i]) and (t_chrom[i]) not in chromosome:
                    in_target.append((i,t_chrom[i]))
            in_genome.append(in_target)
        
        #1.2 in source genome and not in target genome[Create out list that contains tuples of (position,gene)]
        out_genome = []
        out_target = []
        occurred = []

        for j in range(len(target_genome)):
            chromosome = source_genome[j]
            t_chrom = target_genome[j]

            for i in range(len(chromosome)):
                if ((isinstance(chromosome[i], int) and chromosome[i] not in t_chrom)) or (((isinstance(chromosome[i], str) and '*' not in chromosome[i])) and chromosome[i] not in t_chrom):
                    out_target.append((i,chromosome[i]))
                elif (chromosome.count(chromosome[i])) > t_chrom.count(chromosome[i]) and (isinstance(chromosome[i],str) and '*' not in chromosome[i]) and (chromosome[i] not in occurred):
                    out_target.append((i,chromosome[i]))
                    occurred.append(chromosome[i])
            out_genome.append(out_target)
            out_target = []
        
        #step 2: duplication; check target for duplication [note position, gene and type of duplication]
        #isinstance(chromosome[i], int) and 
        duplication_genome = []
        t_duplication = []
        dup_genes = []

        for chromosome in target_genome:
            for i in range(len(chromosome)):
                if isinstance(chromosome[i], int) and chromosome.count(chromosome[i]) > 1 and chromosome[i] not in dup_genes :
                    if chromosome[i] == chromosome[i+2] or chromosome[i] == chromosome[i-2]:
                        type = "tandem"
                    else:
                        type = "transpositional"
                    dup_genes.append(chromosome[i])
                    t_duplication.append([i, self.getIndex(chromosome, chromosome[i]),chromosome[i], type])
            duplication_genome.append(t_duplication)
            t_duplication = []
            dup_genes = []
      
        #step 2.1: check if the duplication is already present in source, if yes remove from list, otherwise cause mutation
        #Check that duplication genome is not empty
        if any(duplication_genome):
            for j in range(len(source_genome)):
                chromosome = source_genome[j]
                sub = duplication_genome[j]
                for i in range(len(sub)):
                        dup = sub[i]
                        duplicated =  dup[2]
                    
                        #check if gene exists
                        if duplicated in chromosome:
                            occurances = chromosome.count(duplicated)
                            if occurances == 2:
                                if len(sub)>1:
                                    n_sub = sub.remove(dup)
                                    duplication_genome[j] = n_sub
                                else:
                                    n_sub = []
                                    duplication_genome[j] = n_sub

        #check the 3 lists and randomly pick a tuple from one of them
        do_mutation = ()
        d = False
        insert = False
        dup = False

        if any(duplication_genome):
            dup = True
        if any(out_genome):
            d = True
        if any(in_genome):
            insert = True
        
        if insert and d and dup:
            pick = randint(0,2)
            if pick == 0:
                for i in range(len(in_genome)):
                    chromosome = in_genome[i]
                    if chromosome != []:
                        picker = randint(0, len(chromosome)-1)
                        do_mutation = ("ins",i, chromosome[picker])
                        break
            elif pick == 1:
                for i in range(len(out_genome)):
                    chromosome = out_genome[i]
                    if chromosome != []:
                        picker = randint(0, len(chromosome)-1)
                        do_mutation = ("del",i, chromosome[picker])
                        break
            elif pick == 2:
                for i in range(len(duplication_genome)):
                    chromosome = duplication_genome[i]
                    if chromosome != []:
                        picker = randint(0, len(chromosome)-1)
                        do_mutation = ("dup",i, chromosome[picker])
                        break
        elif insert and d:
            pick = randint(0,1)
            if pick == 0:
                for i in range(len(in_genome)):
                    chromosome = in_genome[i]
                    if chromosome != []:
                        picker = randint(0, len(chromosome)-1)
                        do_mutation = ("ins",i, chromosome[picker])
                        break
            elif pick == 1:
                for i in range(len(out_genome)):
                    chromosome = out_genome[i]
                    if chromosome != []:
                        picker = randint(0, len(chromosome)-1)
                        do_mutation = ("del",i, chromosome[picker])
                        break
        elif d and dup:
            pick = randint(0,1)
            if pick == 0:
                for i in range(len(out_genome)):
                    chromosome = out_genome[i]
                    if chromosome != []:
                        picker = randint(0, len(chromosome)-1)
                        do_mutation = ("del",i, chromosome[picker])
                        break
            elif pick == 1:
                for i in range(len(duplication_genome)):
                    chromosome = duplication_genome[i]
                    if chromosome != []:
                        picker = randint(0, len(chromosome)-1)
                        do_mutation = ("dup",i, chromosome[picker])
                        break
        elif insert and dup:
            pick = randint(0,1)
            if pick == 0:
                for i in range(len(in_genome)):
                    chromosome = in_genome[i]
                    if chromosome != []:
                        picker = randint(0, len(chromosome)-1)
                        do_mutation = ("ins",i, chromosome[picker])
                        break
            elif pick == 1:
                for i in range(len(duplication_genome)):
                    chromosome = duplication_genome[i]
                    if chromosome != []:
                        picker = randint(0, len(chromosome)-1)
                        do_mutation = ("dup",i, chromosome[picker])
                        break
        elif insert:
            for i in range(len(in_genome)):
                    chromosome = in_genome[i]
                    if chromosome != []:
                        picker = randint(0, len(chromosome)-1)
                        do_mutation = ("ins",i, chromosome[picker])
                        break
        elif d:
            for i in range(len(out_genome)):
                    chromosome = out_genome[i]
                    if chromosome != []:
                        picker = randint(0, len(chromosome)-1)
                        do_mutation = ("del",i, chromosome[picker])
                        break
        elif dup:
            for i in range(len(duplication_genome)):
                    chromosome = duplication_genome[i]
                    if chromosome != []:
                        picker = randint(0, len(chromosome)-1)
                        do_mutation = ("dup",i, chromosome[picker])
                        break
    
        #step 3: checking if all these necessary mutations can occur at once
        #first check that insert and del positions dont overlap for same chromosomes, if they do then we wont be able to cause all mutations necessary
        for i in range(len(out_genome)):
            out_chromosome = out_genome[i]
            in_chromosome = in_genome[i]
            for j in range(len(out_chromosome)):
                tup = out_chromosome[j]
                for tup_in in in_chromosome:
                    if tup_in[0] == tup[0]:
                        return [], do_mutation            
        #Check that intergenic regions exist for insert, del, and dup.
        # get position indexes [only] from in_genome
        in_pos = []
        in_pos_genome = []
        # if any(in_genome):
        for chromosome in in_genome:
            for i in range(len(chromosome)):
                tup = chromosome[i]
                in_pos.append(tup[0])
            in_pos_genome.append(in_pos)
        # get position indexes [only] from out_genome
        out_pos = []
        out_pos_genome = []
        # if any(out_genome):
        for chromosome in out_genome:
            if len(chromosome)!= 0:
                for i in range(len(chromosome)):
                    tup = chromosome[i]
                    if len(chromosome)>1 and i < len(chromosome)-1:
                        check = chromosome[i+1]
                        if check[0] == tup[0]+1:
                            out_pos.append(tup[0])
                            i += 1
                out_pos_genome.append(out_pos)
            else: 
                out_pos_genome.append([])
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
                if (isinstance(chromosome[j],str) and len(chromosome[j])>1 and '*' in chromosome[j]):
                    no_app_region += 1
                    app_reg_chrom.append(j)
            app_reg_genome.append(app_reg_chrom)
            app_reg_chrom = []

        #check number of applicable regions against number of total mutations
        #count positions for each mutation
        insert_count = 0
        for chromosome in in_pos_genome:
            for gene in chromosome:
                insert_count += 1
        del_count = 0


        # check counting in pairs as well
        for chromosome in out_pos_genome:
            for gene in chromosome:
                del_count += 1
        dup_count = 0
        for chromosome in dup_pos_genome:
            for gene in chromosome:
                dup_count += 1
        if (no_app_region < (dup_count+insert_count+del_count)):
            return [], do_mutation
        
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
                if (total_positions[j]+1 not in applicable_regions_chrom) or app_reg_chrom == []:
                    return [], do_mutation

            mutation_insert = {}
            
            # code to take elements of lists and place in dictionary [for loop]
            for i in range(len(in_genome)):
                if len(in_genome[i]) > 0:
                    mutation_insert["insertion chromosome"] = i+1
                    chrom_interest =in_genome[i]
                    for i in range(len(chrom_interest)):
                        instance = chrom_interest[i]
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
    """
    This fuction picks a type of mutation and calls different functions (delete, duplicate, insert) to act on it
    It uses source_genome with approved intergenic regions
    It counts number of applicable intergenic regions to associate to number of mutations
    """
    def do_mutation(self, source_genome, mutation_required):
        list_of_mutations = []
        
        list_of_genes = []
        list_of_genes_genome = []
        list_of_mutation_points = []
        list_of_mutation_points_genome = []

        for genes_with_intergenic_approved in source_genome:
            for i in range(len(genes_with_intergenic_approved)):
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

        if type == 'dup':
            position = actual_mutation[1]
            gene_to_duplicate = actual_mutation[2]
            type_of_duplication = actual_mutation[3]
            chromosome = source_genome[chromosome_index]
            if position > len(chromosome)-1:
                position = len(chromosome)-1
            #check for applicable region at position -1 
    
            if(isinstance(chromosome[position-1], str) and '*' in chromosome[position-1] and len(chromosome[position-1])>1):
                mutated_chromosome = self.duplication(chromosome, gene_to_duplicate, position)
                source_genome[chromosome_index] = mutated_chromosome
                #create record
                operation = {}
                operation['Type'] = type
                operation['Chr'] = chromosome_index + 1
                operation['Pos'] = position
                operation['Type of dup'] = type_of_duplication
    #            operation['Genome before mutation'] = source_genome
                operation['Genome after mutation'] = source_genome
                list_of_mutations.append(operation)
                
        elif type == 'ins':
            position = actual_mutation[0]
            gene_to_insert = actual_mutation[1]
            chromosome = source_genome[chromosome_index]

            if position > len(chromosome)-1:
                position = len(chromosome)-1
           
            if(isinstance(chromosome[position-1], str) and '*' in chromosome[position-1] and len(chromosome[position-1])>1):
                mutated_chromosome = self.insertion(chromosome, position, gene_to_insert)
                #create record
                operation = {}
                operation['Type'] = type
                operation['Chr'] = chromosome_index + 1
                operation['Pos'] = position
                operation['Gene'] = gene_to_insert
    #            operation['Genome before mutation'] = source_genome
                source_genome[chromosome_index] = mutated_chromosome
                operation['Genome after mutation'] = source_genome
                list_of_mutations.append(operation)

        elif type == 'del':
            position = actual_mutation[0]
            gene_to_delete = actual_mutation[1]
            chromosome = source_genome[chromosome_index]
            if position > len(chromosome)-1:
                position = len(chromosome)-1
       
            if(isinstance(chromosome[position-1], str) and '*' in chromosome[position-1] and len(chromosome[position-1])>1):
                mutated_chromosome = self.deletion(chromosome, position)
                #create record
                operation = {}
                operation['Type'] = type
                operation['Chr'] = chromosome_index + 1
                operation['Pos'] = position
                operation['Gene'] = gene_to_delete
    #            operation['Genome before mutation'] = source_genome
                source_genome[chromosome_index] = mutated_chromosome
                operation['Genome after mutation'] = source_genome
                list_of_mutations.append(operation)

        return source_genome, list_of_mutations

    """
     This function inserts series of genes required(sequence block) in the source genome in order 
     to get to the target genome
    """

    def insertion(self, source_chromosome, position_app_region, gene):
        
        source_chromosome[position_app_region-1] = gene
     
        return source_chromosome

    """
    This function deletes genes that are in the source genome but not in the target genome, so that
    the source genome can be the same as the target genome at the end of the evolutionary process.
    """

    # def deletion(self, source_chromosome, position_app_region):
    #     if isinstance(source_chromosome[position_app_region], int) and '_' not in str(source_chromosome[position_app_region]):
    #         del source_chromosome[position_app_region]
    #     if position_app_region > 0 and isinstance(source_chromosome[position_app_region-1], int) and '_' not in str(source_chromosome[position_app_region-1]):
    #         del source_chromosome[position_app_region-1]

    #     return source_chromosome

    def deletion(self, source_chromosome, position_app_region):

            del source_chromosome[position_app_region]
            if position_app_region > 0 :
                del source_chromosome[position_app_region-1]
            return source_chromosome
        

    """
     This function duplicates genes required in the source genome so they can compare with 
     the duplicates in the target genome.The duplication could be tandem or transpositional
    """    
    def duplication(self, source_chromosome, gene, insertion_position):
        
        source_chromosome[insertion_position-1] = gene

        return source_chromosome


    def foreign_dna_pool(self, source, target):
        # Check what genes are not in source genome but are in target genome
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
        
        for chromosome in target:
            for i in range(len(chromosome)):
                if isinstance(chromosome[i],int):
                    target_genome.append(int(chromosome[i]))

        # Find the difference between source genome and target genome
        difference = list(set(target_genome) - set(source_genome))

        if len(difference) > 0:
            # define the ratio (1/5)
            number_of_random_ints = (len(difference) * 3) - (len(difference))  # change ratio here (5)

            # create foreign dna
            for_dna = []
            count = 0
            while count < (number_of_random_ints):
                gene = randint(1, 40)
                if len(for_dna) >= 1:
                    if gene not in for_dna:
                        for_dna.append(gene)
                        count += 1
                else:
                    for_dna.append(gene)

            # add difference to foreign dna and check duplicates and add foreign DNA if necessary
            for_dna = difference + for_dna
            for_dna = list(set(for_dna))
            if len(for_dna) < ((len(difference)) * 3):  # change ratio here (5)
                count = len(for_dna)
                while (len(for_dna) < ((len(difference)) * 3)):
                    gene = randint(1, 40)
                    if gene not in for_dna:
                        for_dna.append(gene)
                        count += 1
            
            #Use for_dna list that was created to create foreign dna fragments (random number of frag and random length of fragments)
            number_of_frags = randint(1,99)
            len_frags = 1
            
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

            #Check for the difference in genes within at least one fragment in list
            check = True
            for f in list_of_frags:
                if difference in f:
                    check = False
            if check == True:
                final_frag = difference[:]
            #add a fragment that does contain the difference
            #Check that the gene does not already exist in the fragment
                while len(final_frag) <= len(difference)+1:
                    c =  for_dna[randint(0, len(for_dna)-1)]
                    if c not in final_frag:
                        final_frag.append(c)
                list_of_frags.append(final_frag)

            #Tag foreign DNA
            for i in list_of_frags:
                frag = i
                for j in range(len(frag)):
                    frag[j] = str(frag[j])+"_"
            return list_of_frags

        else:
            # define the ratio (1/5)
            number_of_random_ints = randint(1,5)

            # create foreign dna
            for_dna = []
            count = 0
            while count < (number_of_random_ints):
                gene = randint(1, 40)
                if len(for_dna) >= 1:
                    if gene not in for_dna:
                        for_dna.append(gene)
                        count += 1
                else:
                    for_dna.append(gene)
            
            #Use for_dna list that was created to create foreign dna fragments (random number of frag and random length of fragments)
            number_of_frags = randint(1,99)
            len_frags = 1
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

            #Tag foreign DNA
            for i in list_of_frags:
                frag = i
                for j in range(len(frag)):
                    frag[j] = str(frag[j])+"_"

            return list_of_frags

    



