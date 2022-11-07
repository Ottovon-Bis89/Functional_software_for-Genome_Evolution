from doctest import master
import Data_generator
import sys
from random import randint

class Eve:
    def __init__(self):
        pass
         
         #This function determines all the possible events(operations) that can be will executed or need to be executed to transform the source genome into
         #the target genome. The function returns operations such as insertions, deletions, duplications
    def get_legal_operations(self, src, adjacenciesB):
        print("enter get legal ops")
        list_of_legal_operations = []
        adjacenciesA = src
        adjacenciesB = adjacenciesB
        switch = True
        print(src)
        print(adjacenciesB)
        

        #accomodate more than one solution -> modify while loop
        #incorporate master list [([f_src,[list_of_operations],[()].....])]
        #check where len(src/trgt) is used due to possibly differing lengths.
        master_list = []
        repeat_counter = 0

        while repeat_counter <= 100:
            print("enter outer while")
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
            clean_src, clean_trgt = self.genome_cleaner(adjacenciesA, adjacenciesB)
            print(clean_src, clean_trgt)
            
            while list(map(sorted,clean_src)) != list(map(sorted,clean_trgt)):
                print("enter solution creation while")
                #TODO: check number of applicale region, if 0 then create 
                count_app = 0
                for chromosome in adjacenciesA:
                    for i in range(len(chromosome)):
                        if isinstance(chromosome[i], str) and '*' in chromosome[i] and len(chromosome[i]) > 1 :
                            count_app += 1
                
                clean_chrom = []
                clean_genome = []
                print("count of applicable regions is: " + str(count_app))
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
                    print(adjacenciesA)
                series_of_mutation,mutation_required = self.mutation_legal_ops(adjacenciesA, adjacenciesB)
                if series_of_mutation == []:
                    src_genome, mutation_list = self.do_mutation(adjacenciesA, mutation_required)
                    adjacenciesA = src_genome[:]
                    list_of_legal_operations.append(mutation_list)
                else:
                    while (any(series_of_mutation) and mutation_required !=()) or mutation_required !=():
                        mutations_finale = []
                        for i in range(len(series_of_mutation)):
                            if i == 0:
                                mutation_type = 'insert'
                            elif i == 1:
                                mutation_type = 'delete'
                            else:
                                mutation_type = 'duplication'
                            mutation = series_of_mutation[i]
                            for chromosome_number in range(len(mutation)):
                                if mutation[chromosome_number] != []:
                                    chromosome_index = chromosome_number
                                    chrom = mutation[chromosome_number]
                                    for m in range(len(chrom)):
                                        do_mutation = (mutation_type, chromosome_index, chrom[m])
                                        src_genome, mutation_list = self.do_mutation(adjacenciesA, do_mutation)
                                        adjacenciesA = src_genome[:]
                                        mutations_finale.append(mutation_list)
                        list_of_legal_operations.append(mutations_finale)
                        clean_chrom = []
                        clean_genome = []

                        #remove all unapplicable intergenic regions and call intergenerator
                        for chromosome in adjacenciesA:
                            for i in range(len(chromosome)):
                                if isinstance(chromosome[i],str) and '*' not in chromosome[i]:
                                    # print(chromosome[i])
                                    clean_chrom.append(chromosome[i])
                                elif isinstance(chromosome[i], int):
                                    clean_chrom.append(chromosome[i])
                            clean_genome.append(clean_chrom)
                            clean_chrom = []
                        gen_obj = Data_generator.Data_generator()
                        normal_i_reg = gen_obj.intergenerator(clean_genome)
                        adjacenciesA = gen_obj.intergenic_regions(normal_i_reg)
                        print("src before mutation legal ops")
                        #print(adjacenciesA)  
                        series_of_mutation,mutation_required = self.mutation_legal_ops(adjacenciesA, adjacenciesB)
                        #print("within while loop and series of mutation checks")
                        print(series_of_mutation,mutation_required)
                        print(any(series_of_mutation))
                        #print(adjacenciesA)  
                        if mutation_required ==():
                            break

                clean_src, clean_trgt = self.genome_cleaner(adjacenciesA, adjacenciesB)
                print(list(map(sorted,clean_src)))
                print(list(map(sorted,clean_trgt)))
                # sys.exit(0)       
                        # print(src_genome)
                    #print(adjacenciesA) 
            #at the end clean for check
            #TODO: Check against master and increment(or not) the repeat_counter and if not present append to master
            solution = [adjacenciesA, list_of_legal_operations]
            print(solution)
            
            if len(master_list)>0:
                if solution in master_list:
                    repeat_counter += 1
                else:
                    master_list.append(solution)
                    print("master here")
            else:
                master_list.append(solution)
            list_of_legal_operations = []
        print(repeat_counter)
        return master_list
        

    def genome_cleaner(self, src, target):
        print("enter genome_cleaner")
        new_src_chrom = []
        new_src = []
        new_trgt_chrom = []
        new_trgt = []

        for chrom in src:
            for ele in chrom:
                if isinstance(ele,str) and '*' not in ele:
                    if '_' in ele and len(ele) == 3:
                        new_src_chrom.append(ele[:2])
                    elif '_' in ele and len(ele) == 2:
                        new_src_chrom.append(ele[:1])
                    else:
                        new_src_chrom.append(ele)
            new_src.append(new_src_chrom)
            new_src_chrom = []
        
        for chrom in target:
            for ele in chrom:
                if isinstance(ele,str) and '*' not in ele:
                    if '_' in ele and len(ele) == 3:
                        new_trgt_chrom.append(ele[:2])
                    elif '_' in ele and len(ele) == 2:
                        new_trgt_chrom.append(ele[:1])
                    else:
                        new_trgt_chrom.append(ele)
            new_trgt.append(new_trgt_chrom)
            new_trgt_chrom = []
        
        return new_src, new_trgt
        
    def mutation_legal_ops(self, source, target):
        # This function decides if mutations, any series of mutations, can take genome A to genome B
        # check number of chromosomes -> possibility of chromosome deletion(target chromosmes less than source) or chromosome insertion (source chromosome count less than target)
        # Check number of genes in chromosome for target and source -> indicators for insertion/foreign dna/deletion
        # check signed integers(genes) between target and source
        # Duplication - look at the target; if two of same signed integer next to each other -> tandom duplicatio
        # if two of same signed ints in chromosome but not next to each other then -> transpositional
        # source_genome = source[:]
        #remove underscores from target
        chromo = []
        target_genome = []
        for chrom in target:
            for i in range(len(chrom)):
                if isinstance(chrom[i], str) and '_' in chrom[i]:
                    if len(chrom[i])==3:
                        gene = chrom[i]
                        chromo.append(int(gene[:1]))
                    elif len(chrom[i])==2:
                        gene = chrom[i]
                        # print((gene[:1]))
                        chromo.append(int(gene[:1]))
                elif isinstance(chrom[i], str):
                    chromo.append((chrom[i]))
                elif isinstance(chrom[i], int):
                    chromo.append((chrom[i]))
                elif ((isinstance(chrom[i], str) and '*' in chrom[i])):
                    chromo.append((chrom[i]))
            target_genome.append(chromo)
            chromo = []

        #remove underscores that identify fragments in source genome
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
                        # print((gene[:1]))
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

        #print(len(source_genome))
        #print(len(target_genome))

        #Take note o differing length of genomes where this condition does not hold
        # for k in range(len(target_genome)):

        for j in range(len(target_genome)):
            in_target = []
            chromosome = source_genome[j]
            t_chrom = target_genome[j]

            for i in range(len(t_chrom)):
                if '*' not in str(t_chrom[i]) and (t_chrom[i]) not in chromosome:
                    in_target.append((i,t_chrom[i]))
            in_genome.append(in_target)

        #1.2 in source and not in target[CREATE out list that contains tuples of (position,gene)]
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
        duplications_to_remove = []
        empty_dup_genome = False
        #Check that duplication genome is not empty
        if any(duplication_genome):
            print("elements exist")
            for j in range(len(source_genome)):
                chromosome = source_genome[j]
                sub = duplication_genome[j]
                for i in range(len(sub)):
                        dup = sub[i]
                        duplicated =  dup[2]
                        print(duplicated)
                        print(chromosome)
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
        print("duplication_genome:  "+str(duplication_genome))

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
        print(insert, d, dup)
        if insert and d and dup:
            pick = randint(0,2)
            if pick == 0:
                for i in range(len(in_genome)):
                    chromosome = in_genome[i]
                    if chromosome != []:
                        print('inside mutation_legal_ops insert_1')
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
        elif insert and d:
            pick = randint(0,1)
            if pick == 0:
                for i in range(len(in_genome)):
                    chromosome = in_genome[i]
                    if chromosome != []:
                        print('inside mutation_legal_ops insert_2')
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
        elif d and dup:
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
        elif insert and dup:
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
        elif insert:
            for i in range(len(in_genome)):
                    chromosome = in_genome[i]
                    if chromosome != []:
                        print('inside mutation_legal_ops insert_4')
                        # print(chromosome[i])
                        picker = randint(0, len(chromosome)-1)
                        do_mutation = ("insert",i, chromosome[picker])
                        break
        elif d:
            for i in range(len(out_genome)):
                    chromosome = out_genome[i]
                    if chromosome != []:
                        picker = randint(0, len(chromosome)-1)
                        do_mutation = ("delete",i, chromosome[picker])
                        break
        elif dup:
            for i in range(len(duplication_genome)):
                    chromosome = duplication_genome[i]
                    if chromosome != []:
                        picker = randint(0, len(chromosome)-1)
                        do_mutation = ("duplication",i, chromosome[picker])
                        break
        print('mutation get_leg_op return for do mutation')
        print(do_mutation)
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
        # if any(duplication_genome):
            # print(duplication_genome)
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


        #TODO check counting in pairs as well
        for chromosome in out_pos_genome:
            for gene in chromosome:
                del_count += 1
        dup_count = 0
        for chromosome in dup_pos_genome:
            for gene in chromosome:
                dup_count += 1
        if (no_app_region < (dup_count+insert_count+del_count)):
            #print("returned at line 481")
            return [], do_mutation
        
        #check that the positions for mutations have applicable intergenic regions
        #check insertion
        for i in range(len(app_reg_genome)):
            in_chrom = in_pos_genome[i]
            out_chrom = out_pos_genome[i]
            dup_chrom = dup_pos_genome[i]
            applicable_regions_chrom = app_reg_genome[i]
            # print(applicable_regions_chrom)
            total_positions = []
            total_positions = in_chrom+out_chrom+dup_chrom
            # print("tot_pos")
            # print(total_positions)
            for j in range(len(total_positions)):
                #print("final resting place")
                #print(total_positions)
                #print(app_reg_chrom)
                if (total_positions[j]+1 not in applicable_regions_chrom) or app_reg_chrom == []:
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
        elif type == 'insert':
            position = actual_mutation[0]
            gene_to_insert = actual_mutation[1]
            chromosome = source_genome[chromosome_index]
            if position > len(chromosome)-1:
                print("changed pos")
                position = len(chromosome)-1
            mutation_point_chromosome = list_of_mutation_points_genome[chromosome_index]
            print("error line 1030")
            print(position)
            print(len(chromosome))
            print(source_genome)
            print(chromosome_index)
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

        elif type == 'delete':
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
        return source_genome, list_of_mutations

    def insertion(self, source_chromosome, position_app_region, gene):
        source_chromosome[position_app_region-1] = gene
        return source_chromosome

    def deletion(self, source_chromosome, position_app_region):
        del source_chromosome[position_app_region]
        if position_app_region > 0 :
            del source_chromosome[position_app_region-1]
        
        return source_chromosome

    def duplication(self, source_chromosome, gene, insertion_position):
        source_chromosome[insertion_position-1] = gene
        return source_chromosome