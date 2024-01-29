
from random import randint
# import Gen_xtremities
from Gen_API import Gen_API

API = Gen_API()
class Node:

    def __init__(self):
        self.state = []
        self.children = []
        self.children_weights = []
        self.next_operation = 0
        self.next_operation_weight = []

    def get_legal_operations(self,source_genome, target_genome):
        list_of_legal_operations = []
        found_solution = False
        insert_fDNA = False

        while found_solution == False:
            if insert_fDNA == False:
                
<<<<<<< HEAD
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
=======
                insert_fDNA = True
>>>>>>> 78426684163234e674593bb0b119ba30b23988bb
            else:
                # Insert Foreign DNA
                source_genome = API.get_foreign_DNA(source_genome)

                #get list of mutations that can occur
                series_of_mutation, mutation_required = self.mutation_legal_operations(source_genome, target_genome)
                print(series_of_mutation)

        return list_of_legal_operations, mutation_required

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
        #1.1 in target and not in source [create in list that contains tuples of (position,gene)]
        in_genome = []
        in_target = []
        
        #Take note of different length of genomes where this condition does not hold
        for j in range(len(target_genome)-1):
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

        for j in range(len(target_genome)-1):
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
                    t_duplication.append([i, API.getIndex(chromosome, chromosome[i]),chromosome[i], type])
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
        do_mutation = API.pick_mutation(duplication_genome,out_genome,in_genome)
    
        #step 3: checking if all these necessary mutations can occur at once
        #First check that insert and del positions dont overlap for same chromosomes, if they do then we won't be able to cause all necessary mutations

        for i in range(len(out_genome)-1):
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
        
        for chromosome in in_genome:
            for i in range(len(chromosome)):
                tup = chromosome[i]
                in_pos.append(tup[0])
            in_pos_genome.append(in_pos)

        # get position indexes [only] from out_genome
        out_pos = []
        out_pos_genome = []
        
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

        return do_mutation
    
    def do_mutation(self, source_genome, mutation_required):
        list_of_mutations = []

        list_of_genes = []
        list_of_genes_genome = []
        list_of_mutation_points = []
        list_of_mutation_points_genome = []

        for genes_with_intergenic_approved in source_genome:
            for i in range(len(genes_with_intergenic_approved)):
                if isinstance(genes_with_intergenic_approved[i], str) and len(genes_with_intergenic_approved[i]) > 1 and '*' in genes_with_intergenic_approved[i]:
                    if i != len(genes_with_intergenic_approved)-2:
                        list_of_mutation_points.append(i+1)
                elif (not isinstance(genes_with_intergenic_approved[i], str)) or (isinstance(genes_with_intergenic_approved[i], str) and '*' not in genes_with_intergenic_approved[i]):
                    list_of_genes.append(genes_with_intergenic_approved[i])

            list_of_genes_genome.append(list_of_genes)
            list_of_mutation_points_genome.append(list_of_mutation_points)

            list_of_mutation_points = []

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

            # check for applicable region at position -1

            if(isinstance(chromosome[position-1], str) and '*' in chromosome[position-1] and len(chromosome[position-1]) > 1):
                mutated_chromosome = API.duplication(chromosome, gene_to_duplicate, position)
                source_genome[chromosome_index] = mutated_chromosome
                # create record
                list_of_mutations = API.create_record(type, chromosome_index, position, type_of_duplication, source_genome, mutated_chromosome, list_of_mutations)

        else:
            position = actual_mutation[0]
            gene = actual_mutation[1]
            chromosome = source_genome[chromosome_index]
            if position > len(chromosome)-1:
                position = len(chromosome)-1
            
            if(isinstance(chromosome[position-1], str) and '*' in chromosome[position-1] and len(chromosome[position-1]) > 1):

                if type == 'ins':
                    mutated_chromosome = API.insertion(chromosome, position, gene)
                    # create record
                    list_of_mutations = API.create_record(type, chromosome_index, position, gene, source_genome, mutated_chromosome, list_of_mutations)


                elif type == 'del':
                    mutated_chromosome = API.deletion(chromosome, position)
                    # create record
                    list_of_mutations = API.create_record(type, chromosome_index, position, gene, source_genome, mutated_chromosome, list_of_mutations)

        return source_genome, list_of_mutations

    