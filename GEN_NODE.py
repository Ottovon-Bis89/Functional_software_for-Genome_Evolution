
from random import randint
import Intergenic_region_generator
import ForeignDNA


class Node:

    def __init__(self):
        self.state = []
        
    """
    The function returns a list  of the operations needed to transform the
    source  genome to the target genome. Itreturns random legal options that can be applied to A,
    called recursively until A can be transformed to B
    It also chooses a fragment of foreign DNA and inserts it into the source genome

    """
    def get_legal_operations(self,source_genome, target_genome):

        list_of_legal_operations = []
        switch = True
        loop_counter = 0  # No foreign DNA in first iteration of mutations
        foreign_Dna_counter = 0

        while switch:

            for element in target_genome:
                if element in source_genome:
                    pass
                else:
                    source_genome = source_genome[:]
    
            if loop_counter > 0 :
                gen_obj = Intergenic_region_generator.Intergenic_generator()
                # check number of applicale intergenic regions, if 0 then create more intergenic regions
                #gen_obj = Intergenic_region_generator.Intergenic_generator()
                count_applicable_region = 0
                for chromosome in source_genome:
                    for i in range(len(chromosome)):
                        if isinstance(chromosome[i], str) and '*' in chromosome[i] and len(chromosome[i]) > 1 :
                            count_applicable_region += 1
                
                clean_chromosome = []
                clean_genome = []

                if count_applicable_region > 0:
                    #remove all unapplicable intergenic regions and call intergenic regions generator
                    for chromosome in source_genome:
                        for i in range(len(chromosome)):
                            if isinstance(chromosome[i],str) and '*' not in chromosome[i]:
                                clean_chromosome.append(chromosome[i])
                            elif isinstance(chromosome[i], int):
                                clean_chromosome.append(chromosome[i])
                        clean_genome.append(clean_chromosome)
                        clean_chromosome = []
                    #gen_obj = Intergenic_region_generator.Intergenic_generator()
                    insert_intergenic_region = gen_obj.inter_generator(clean_genome)
                    source_genome = gen_obj.intergenic_regions(insert_intergenic_region)
       
                # randomly choose to insert foreign dna
                choose = randint(0, 100)
                if (choose >= 10 and foreign_Dna_counter != 0) :
                    mutations, required_mutation = self.mutation_legal_operations(source_genome, target_genome)
                    print("muta1", mutations)
                    
                    if mutations ==[] or required_mutation ==():
                        print("muta2", mutations)
                        source_genome, mutation_list = self.do_mutation(source_genome, required_mutation)
        

                        list_of_legal_operations.append(mutation_list)
                        switch = True
                    else:
                        while (any(mutations) and required_mutation ==()) or required_mutation ==():
                            print("muta3", mutations)
                            final_mutations = []
                            for i in range(len(mutations)):
                                print("muta4", mutations)
                                if i == 0:
                                    mutation_type = 'ins'
                                elif i == 1:
                                    mutation_type = 'del'
                                else:
                                    mutation_type = 'dup'
                                mutation = mutations[i]
                                # print("muta5", mutations)
                                for chromosome_number in range(len(mutation)):
                                    if mutation[chromosome_number] != []:
                                        chromosome_index = chromosome_number
                                        chromosome = mutation[chromosome_number]

                                        for m in range(len(chromosome)):
                                            do_mutation = (mutation_type, chromosome_index, chromosome[m])
                                            source_genome, mutation_list = self.do_mutation(source_genome, do_mutation)

                                            final_mutations.append(mutation_list)
                            list_of_legal_operations.append(final_mutations)
                            clean_chromosome = []
                            clean_genome = []

                            #remove all unapplicable intergenic regions and call intergenerator 
                            # to insert new applicable regions for mutations to occur
                            for chromosome in source_genome:
                                for i in range(len(chromosome)):
                                    if isinstance(chromosome[i],str) and '*' not in chromosome[i]:
                                        clean_chromosome.append(chromosome[i])
                                    elif isinstance(chromosome[i], int):
                                        clean_chromosome.append(chromosome[i])
                                clean_genome.append(clean_chromosome)
                                clean_chromosome = []

                            #gen_obj = Intergenic_region_generator.Intergenic_generator()
                            insert_intergenic_region = gen_obj.inter_generator(clean_genome)
                            source_genome = gen_obj.intergenic_regions(insert_intergenic_region)
 
                            mutations,required_mutation = self.mutation_legal_operations(source_genome, target_genome)
                            # print("muta6", mutations)
                            if required_mutation ==():
                                break
                        switch = False
                elif ((foreign_Dna_counter < 10 or foreign_Dna_counter ==0)):
                    print("\tInserted foreign DNA")
                    foreign_Dna_counter += 1
                    #Here is list of foreign DNAs where fragments are sublists
                    foreign_obj = ForeignDNA.Foreign_DNA()
                    foreign_dna = []
                    while foreign_dna == []:
                        foreign_dna = foreign_obj.foreign_dna_pool(source_genome, target_genome)

                    # Randomly choose a foreign dna from the foreign DNA pool
                    foreign_dna_len = len(foreign_dna) -1
                    choice_foreign_dna = randint(0, foreign_dna_len)
                    chosen = foreign_dna[choice_foreign_dna]

                    # add foreign DNA to the source genome
                    source_genome, list_of_operationss = foreign_obj.insert_foreign_dna(source_genome, chosen)
                    # print(list_of_operationss)
                    # list_of_legal_operations.append(list_of_operationss)

                    mutation_genome = source_genome.copy()
                    mutations, required_mutation = self.mutation_legal_operations(mutation_genome, target_genome)
                    # print("muta7", mutations)
                    if mutations == []:
                        # print("muta8", mutations)
                        
                        source_genome, mutation_list = self.do_mutation(source_genome, required_mutation)
                       
                        list_of_legal_operations.append(mutation_list)
                        switch = True
        
                    else:
                        while (any(mutations) and required_mutation !=()) or required_mutation !=():
                            # print("muta9", mutations)
                            final_mutations = []
                            for i in range(len(mutations)):
                                if i == 0:
                                    mutation_type = 'ins'
                                elif i == 1:
                                    mutation_type = 'del'
                                else:
                                    mutation_type = 'dup'

                                mutation = mutations[i]
                                # print("muta10", mutations)

                                for chromosome_number in range(len(mutation)):
                                    if mutation[chromosome_number] != []:
                                        chromosome_index = chromosome_number
                                        chromosome = mutation[chromosome_number]
                                       
                                        for m in range(len(chromosome)):
                                            do_mutation = (mutation_type, chromosome_index, chromosome[m])
                                            source_genome, mutation_list = self.do_mutation(source_genome, do_mutation)
                                           
                                            final_mutations.append(mutation_list)
                            
                            list_of_legal_operations.append(final_mutations)
                            clean_chromosome = []
                            clean_genome = []

                            #remove all unapplicable intergenic regions and call intergenerator
                            for chromosome in source_genome:
                                for i in range(len(chromosome)):
                                    if isinstance(chromosome[i],str) and '*' not in chromosome[i]:
                                        clean_chromosome.append(chromosome[i])
                                    elif isinstance(chromosome[i], int):
                                        clean_chromosome.append(chromosome[i])

                                clean_genome.append(clean_chromosome)
                                clean_chromosome = []

                            #gen_obj = Intergenic_region_generator.Intergenic_generator()
                            insert_intergenic_region = gen_obj.inter_generator(clean_genome)
                            source_genome = gen_obj.intergenic_regions(insert_intergenic_region)

                            mutations ,required_mutation = self.mutation_legal_operations(source_genome, target_genome)
                            # print("muta11",)
                            
                            
                            if required_mutation !=():
                                break
                        switch = False
                        
            elif loop_counter == 0:
            # # elif loop_counter == 0:
            #     self.handle_no_legal_mutations(source_genome, target_genome, list_of_legal_operations)

                mutations, required_mutation = self.mutation_legal_operations(source_genome, target_genome)
                
                if mutations == [] and required_mutation !=():
                    switch = True
                    # print("mutations:", mutations)
                    # print("required mutations:", required_mutation)

                    #Do random mutation
                    source_genome, mutation_list = self.do_mutation(source_genome, required_mutation)
                    #print("Could not find straight path to get to target_genome so randomly mutated")

                    list_of_legal_operations.append(mutation_list)
                    
                    # check number of applicale region, if 0 then create new intergenic regions 
                    count_applicable_region = 0
                    for chromosome in source_genome:
                        for i in range(len(chromosome)):
                            # print(len(chromosome))
                            if isinstance(chromosome[i], str) and '*' in chromosome[i] and len(chromosome[i]) > 1 :
                                count_applicable_region += 1
                    #print(f"Within first iteration after any and all mutations we check applicable reagions, count is : {str(count_applicable_region)}")
                    clean_chromosome = []
                    clean_genome = []
               
                    if count_applicable_region <= len(source_genome)-1:
                        #remove all unapplicable intergenic regions and call intergenerator
                        for chromosome in source_genome:
                            for i in range(len(chromosome)):
                                if (isinstance(chromosome[i],str) and '*' not in chromosome[i]) or isinstance(chromosome[i],int):
                                    clean_chromosome.append(chromosome[i])
                            clean_genome.append(clean_chromosome)
                            clean_chromosome = []
                        
                        gen_obj = Intergenic_region_generator.Intergenic_generator()
                        insert_intergenic_region = gen_obj.inter_generator(clean_genome)
                        source_genome = gen_obj.intergenic_regions(insert_intergenic_region)
                else:
                        while (any(mutations) and required_mutation !=()) or required_mutation !=():
                            
                            final_mutations = []
                            for i in range(len(mutations)):
                                if i == 0:
                                    mutation_type = 'ins'
                                elif i == 1:
                                    mutation_type = 'del'
                                else:
                                    mutation_type = 'dup'
                                mutation = mutations[i]
                                for chromosome_number in range(len(mutation)):
                                    if mutation[chromosome_number] != []:
                                        chromosome_index = chromosome_number
                                        chromosome = mutation[chromosome_number]
                                        for m in range(len(chromosome)):
                                            do_mutation = (mutation_type, chromosome_index, chromosome[m])
                                            source_genome, mutation_list = self.do_mutation(source_genome, do_mutation)
                                            # adjacenciesA = source_genome[:]
                                            final_mutations.append(mutation_list)
                            list_of_legal_operations.append(final_mutations)
                            clean_chromosome = []
                            clean_genome = []

                            #remove all unapplicable intergenic regions and call intergenerator
                            for chromosome in source_genome:
                                for i in range(len(chromosome)):
                                    if isinstance(chromosome[i],str) and '*' not in chromosome[i]:
                                        clean_chromosome.append(chromosome[i])
                                    elif isinstance(chromosome[i], int):
                                        clean_chromosome.append(chromosome[i])
                                clean_genome.append(clean_chromosome)
                                clean_chromosome = []
                                gen_obj = Intergenic_region_generator.Intergenic_generator()
                                insert_intergenic_region = gen_obj.inter_generator(clean_genome)
                                source_genome = gen_obj.intergenic_regions(insert_intergenic_region)
                                
                            mutations ,required_mutation = self.mutation_legal_operations(source_genome, target_genome)
                            
                            
                            if required_mutation ==():
                                break
                        switch = False                
            else:
                break
            loop_counter += 1

        return list_of_legal_operations
    
    """
    This function decides if mutations, any mutations, can take genome A to genome B
    check number of chromosomes -> possibility of chromosome deletion(target chromosmes less than source)
     or chromosome insertion (source chromosome count less than target)
    Check number of genes in chromosome for target and source -> indicators for insertion/foreign dna/deletion
    check signed integers(genes) between target and source
    Duplication - look at the target; if two of same signed integer next to each other -> tandom duplicatio
    if two of same signed ints in chromosome but not next to each other then -> transpositional
    source_genome = source[:]remove underscores that identify fragments in source genome
    """

    def mutation_legal_operations(self, source_genome, target_genome):
        # new_source_genome = []

        # for chromosome in source_genome:
        #     new_chromosome = []
        #     for gene in chromosome:
               
        #         if isinstance(gene, str) and '_' in gene:
        #             if len(gene) == 3:
        #                 new_chromosome.append(int(gene[:2]))
        #             elif len(gene) == 2:
        #                 new_chromosome.append(int(gene[:1]))
        #         else:
        #             new_chromosome.append(gene)
        #     new_source_genome.append(new_chromosome)
        new_source_genome = []

        for chromosome in source_genome:
            new_chromosome = []
            for gene in chromosome:
                if isinstance(gene, str) and '_' in gene:
                    new_chromosome.append(gene)
                else:
                    new_chromosome.append(gene)
            new_source_genome.append(new_chromosome)


        #step 1, check genes per chromosome between target and source genomes[number of chromosomes should always be the same]
        #1.1 find genes in target and not in source [CREATE in list that contains tuples of (position,gene)]
        insertion_genome = []
        insertion_target = []
        
        #Take note of different length of genomes where this condition does not hold
        for j in range(len(target_genome)):
            insertion_target = []
            new_chromosome = new_source_genome[j]
            target_chromosome = target_genome[j]

            for i in range(len(target_chromosome)):
                if '*' not in str(target_chromosome[i]) and (target_chromosome[i]) not in new_chromosome:
                    insertion_target.append((i,target_chromosome[i]))
            insertion_genome.append(insertion_target)
        
        #1.2 find genes in source genome and not in target genome[Create out list that contains tuples of (position,gene)]
        # deletion_genome = []
        # deletion_target = []
        # occurred = []

        # for j in range(len(target_genome)):
        #     new_chromosome = new_source_genome[j]
        #     target_chromosome = target_genome[j]

        #     for i in range(len(new_chromosome)):
        #         if ((isinstance(new_chromosome[i], int) and new_chromosome[i] not in target_chromosome)) or \
        #         (((isinstance(new_chromosome[i], str) and '*' not in new_chromosome[i]) and '_' not in new_chromosome[i])) and \
        #         (new_chromosome[i] not in target_chromosome):
        #             deletion_target.append((i, new_chromosome[i]))
        #         elif (new_chromosome.count(new_chromosome[i])) > target_chromosome.count(new_chromosome[i]) and \
        #         (isinstance(new_chromosome[i], str) and '*' not in new_chromosome[i]) and \
        #         (new_chromosome[i] not in occurred) and ('_' not in new_chromosome[i]):
        #             deletion_target.append((i, new_chromosome[i]))
        #             occurred.append(new_chromosome[i])
        # deletion_genome.append(deletion_target)
        # deletion_target = []

        deletion_genome = []
        deletion_target = []
        occurred = []

        for j in range(len(target_genome)):
            new_chromosome = new_source_genome[j]
            target_chromosome = target_genome[j]

            for i in range(len(new_chromosome)):
                if ((isinstance(new_chromosome[i], int) and new_chromosome[i] not in target_chromosome)) or (((isinstance(new_chromosome[i], str) and '*' not in new_chromosome[i])) and new_chromosome[i] not in target_chromosome):
                    deletion_target.append((i,new_chromosome[i]))
                elif (new_chromosome.count(new_chromosome[i])) > target_chromosome.count(new_chromosome[i]) and (isinstance(new_chromosome[i],str) and '*' not in new_chromosome[i]) and (new_chromosome[i] not in occurred):
                    deletion_target.append((i,new_chromosome[i]))
                    occurred.append(new_chromosome[i])
            deletion_genome.append(deletion_target)
            deletion_target = []
        
        #step 2: duplication; check target for duplication [note position, gene and type of duplication]
       

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
                    target_duplication.append([i, self.get_second_index(chromosome, chromosome[i]),chromosome[i], type])
            duplication_genome.append(target_duplication)
            target_duplication = []
            duplicated_genes = []
      
        #step 2.1: check if the duplication is already present in source, if yes remove from list, otherwise cause mutation
        #Check that duplication genome is not empty
        if any(duplication_genome):
            for j in range(len(new_source_genome)):
                new_chromosome = new_source_genome[j]
               
                sub = duplication_genome[j]
                for i in range(len(sub)):
                        duplicate = sub[i]
                        duplicated =  duplicate[2]
                    
                        #check if gene exists
                        if duplicated in new_chromosome:
                            occurances = new_chromosome.count(duplicated)
                            
                            if occurances == 2:
                                if len(sub)>1:
                                    n_sub = sub.remove(duplicate)
                                    duplication_genome[j] = n_sub
                                else:
                                    n_sub = []
                                    duplication_genome[j] = n_sub

        #check the 3 lists and randomly pick a tuple from one of them
        do_mutation = ()
        deletion = False
        insertion = False
        duplication = False

        if any(duplication_genome):
            duplication = True
        if any(deletion_genome):
            deletion = True
        if any(insertion_genome):
            insertion = True
        
        if insertion and deletion and duplication:
            pick = randint(0,2)
            if pick == 0:
                for i in range(len(insertion_genome)):
                    new_chromosome = insertion_genome[i]
                    if new_chromosome != []:
                        picker = randint(0, len(new_chromosome)-1)
                        do_mutation = ("ins",i, new_chromosome[picker])
                        break
            elif pick == 1:
                for i in range(len(deletion_genome)):
                    new_chromosome = deletion_genome[i]
                    if new_chromosome != []:
                        picker = randint(0, len(new_chromosome)-1)
                        do_mutation = ("del",i, new_chromosome[picker])
                        break
            elif pick == 2:
                for i in range(len(duplication_genome)):
                    new_chromosome = duplication_genome[i]
                    if new_chromosome != []:
                        picker = randint(0, len(new_chromosome)-1)
                        do_mutation = ("dup",i, new_chromosome[picker])
                        break
        elif insertion and deletion:
            pick = randint(0,1)
            if pick == 0:
                for i in range(len(insertion_genome)):
                    new_chromosome = insertion_genome[i]
                    if new_chromosome != []:
                        picker = randint(0, len(new_chromosome)-1)
                        do_mutation = ("ins",i, new_chromosome[picker])
                        break
            elif pick == 1:
                for i in range(len(deletion_genome)):
                    new_chromosome = deletion_genome[i]
                    if new_chromosome != []:
                        picker = randint(0, len(new_chromosome)-1)
                        do_mutation = ("del",i, new_chromosome[picker])
                        break
        elif deletion and duplication:
            pick = randint(0,1)
            if pick == 0:
                for i in range(len(deletion_genome)):
                    new_chromosome = deletion_genome[i]
                    if new_chromosome != []:
                        picker = randint(0, len(new_chromosome)-1)
                        do_mutation = ("del",i, new_chromosome[picker])
                        break
            elif pick == 1:
                for i in range(len(duplication_genome)):
                    new_chromosome = duplication_genome[i]
                    if new_chromosome != []:
                        picker = randint(0, len(new_chromosome)-1)
                        do_mutation = ("dup",i, new_chromosome[picker])
                        break
        elif insertion and duplication:
            pick = randint(0,1)
            if pick == 0:
                for i in range(len(insertion_genome)):
                    new_chromosome = insertion_genome[i]
                    if chromosome != []:
                        picker = randint(0, len(new_chromosome)-1)
                        do_mutation = ("ins",i, new_chromosome[picker])
                        break
            elif pick == 1:
                for i in range(len(duplication_genome)):
                    new_chromosome = duplication_genome[i]
                    if new_chromosome != []:
                        picker = randint(0, len(new_chromosome)-1)
                        do_mutation = ("dup",i, new_chromosome[picker])
                        break
        elif insertion:
            for i in range(len(insertion_genome)):
                    new_chromosome = insertion_genome[i]
                    if new_chromosome != []:
                        picker = randint(0, len(new_chromosome)-1)
                        do_mutation = ("ins",i, new_chromosome[picker])
                        break
        elif deletion:
            for i in range(len(deletion_genome)):
                    new_chromosome = deletion_genome[i]
                    if new_chromosome != []:
                        picker = randint(0, len(new_chromosome)-1)
                        do_mutation = ("del",i, new_chromosome[picker])
                        break
        elif duplication:
            for i in range(len(duplication_genome)):
                    new_chromosome = duplication_genome[i]
                    if new_chromosome != []:
                        picker = randint(0, len(new_chromosome)-1)
                        do_mutation = ("dup",i, new_chromosome[picker])
                        break
    
        #step 3: checking if all these necessary mutations can occur at once
        #first check that insert and deletion positions dont overlap for same chromosomes, if they do then we wont be able to cause all mutations necessary
        for i in range(len(deletion_genome)):
            deletion_chromosome = deletion_genome[i]
            insertion_chromosome = insertion_genome[i]
            for j in range(len(deletion_chromosome)):
                tup = deletion_chromosome[j]
                for tup_in in insertion_chromosome:
                    if tup_in[0] == tup[0]:
                        return [], do_mutation
                    #    continue           
        #Check that intergenic regions exist for insertion, deletion, and duplication.
        # get position indexes [only] from in_genome(insertion in genome)
        insertion_position = []
        insertion_position_genome = []
        
        for new_chromosome in insertion_genome:
            for i in range(len(new_chromosome)):
                tup = new_chromosome[i]
                insertion_position.append(tup[0])
            insertion_position_genome.append(insertion_position)
        # get position indexes [only] from out_genome(deletion in genome)
        deletion_position = []
        deletion_position_genome = []
        
        for new_chromosome in deletion_genome:
            if len(new_chromosome)!= 0:
                for i in range(len(new_chromosome)):
                    tup = new_chromosome[i]
                    if len(new_chromosome)>1 and i < len(new_chromosome)-1:
                        check = new_chromosome[i+1]
                        if check[0] == tup[0]+1:
                            deletion_position.append(tup[0])
                            i += 1
                deletion_position_genome.append(deletion_position)
            else: 
                deletion_position_genome.append([])
        # get position for duplication
        duplication_position = []
        duplication_position_genome = []

        for new_chromosome in duplication_genome:
            for i in range(len(new_chromosome)):
                tup = new_chromosome[i]
                duplication_position.append(tup[1])
            duplication_position_genome.append(duplication_position)

        # get the number of applicable intergenic regions
        num_applicable_regions = 0
        applicable_region_chromosome = []
        applicable_region_genome = []

        for new_chromosome in source_genome:
            for j in range(len(new_chromosome)):
           
                if (isinstance(new_chromosome[j],str) and len(new_chromosome[j])>1 and '*' in new_chromosome[j]):
                    num_applicable_regions += 1
                    applicable_region_chromosome.append(j)
            applicable_region_genome.append(applicable_region_chromosome)
            applicable_region_chromosome = []

        #check number of applicable regions against number of total mutations and
        #count positions for each mutation
       

        insertion_count = 0

        for new_chromosome in insertion_position_genome:
            for gene in new_chromosome:
                insertion_count += 1

        deletion_count = 0


        # check counting in pairs as well
        for new_chromosome in deletion_position_genome:
            for gene in new_chromosome:
                deletion_count += 1

        duplication_count = 0
        for new_chromosome in duplication_position_genome:
            for gene in new_chromosome:
                duplication_count += 1

        # if (num_applicable_regions < (duplication_count+insertion_count+deletion_count)):

            # return do_mutation

            # raise ValueError("Number of applicable regions cannot be less than the total number of insertions, deletions, and duplications.")

            

         # insertion_count = sum(len(new_chromosome) for new_chromosome in insertion_position_genome)
        # deletion_count = sum(len(new_chromosome) for new_chromosome in deletion_position_genome)
        # duplication_count = sum(len(new_chromosome) for new_chromosome in duplication_position_genome)
        # total_mutation_count = deletion_count + duplication_count + insertion_count
        # if num_applicable_regions >= total_mutation_count:
        #     return do_mutation

        # else:
        #     return None
        
        #check that the positions for mutations have applicable intergenic regions
        #check insertion

        # for i in range(len(applicable_region_genome)):
        #     insertion_chromosome = insertion_position_genome[i]
        #     deletion_chromosome = deletion_position_genome[i]
        #     duplication_chromosome = duplication_position_genome[i]
        #     applicable_regions_chromosome = applicable_region_genome[i]
     
        #     total_positions = insertion_chromosome + deletion_chromosome + duplication_chromosome
        
        #     for j in range(len(total_positions)):
        #         if total_positions[j] + 1 not in applicable_regions_chromosome or not applicable_regions_chromosome:
        #             return do_mutation

        # Return something else if the condition is not met
        # return None

        # for i in range(len(applicable_region_genome)):
        #     insertion_chromosome = insertion_position_genome[i]
        #     deletion_chromosome = deletion_position_genome[i]
        #     duplication_chromosome = duplication_position_genome[i]
        #     applicable_regions_chromosome = applicable_region_genome[i]
         
        #     total_positions = []
        #     total_positions = insertion_chromosome+deletion_chromosome+duplication_chromosome
            
        #     for j in range(len(total_positions)):
        #         if total_positions[j]+1 not in applicable_regions_chromosome or not applicable_region_chromosome:
                    
        #             return [], do_mutation

           
            
            # code to take elements of lists and place in dictionary [for loop]
            # mutation_insert = {}
            # for i in range(len(insertion_genome)):
            #     if len(insertion_genome[i]) > 0:
            #         mutation_insert["insertion chromosome"] = i+1
            #         chromosome_interest =insertion_genome[i]
            #         for i in range(len(chromosome_interest)):
            #             instance = chromosome_interest[j]
            #             mutation_insert["insertion position"] = instance[0]
            #             mutation_insert["insertion gene"] = instance[1]


            # # return list of mutations
        if all(len(genome) > 0 for genome in [insertion_genome, deletion_genome, duplication_genome]):
            return [insertion_genome, deletion_genome, duplication_genome], do_mutation
        else:
            return do_mutation

        #     return [insertion_genome, deletion_genome, duplication_genome], do_mutation

        # return do_mutation
    

    #Function for finding second occurance of element within list
    def get_second_index(self, int_list, num):
        count = 0
        for i, n in enumerate(int_list):
            if n == num:
                count += 1
            if count == 2:
                return i
        else:
            return -1


    """
    This fuction picks a type of mutation and calls different functions (delete, duplicate, insert) to act on it
    It uses source_genome with approved intergenic regions
    It counts number of applicable intergenic regions to associate to number of mutations
    """
    def do_mutation(self, source_genome, required_mutation):
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

        type = required_mutation[0]
        chromosome_index = required_mutation[1]
        # print(str(required_mutation[0])+"++++++"+str(required_mutation[1])+"+++++"+str(required_mutation[2])+"This is what is stored in required mutation")
        actual_mutation = required_mutation[2]

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
                #create record to keep each type of mutation/operation
                operation = {'Mut_Type': type,
                            'Chr': chromosome_index + 1,
                            'Pos': position,
                            'Type of dup': type_of_duplication,
                            'Genome after mutation': source_genome}
                list_of_mutations.append(operation)
              
                
        elif type == 'ins':
            position = actual_mutation[0]
            gene_to_insert = actual_mutation[1]
            # print(str(chromosome_index)+"((((((((((((((((((((((((- This is the index of the chromosome")
            chromosome = source_genome[chromosome_index]
            # print(str(chromosome)+ "%%%%%%%%%%%%%%%%%%%3")
            # print(str(source_genome)+"||||||||||||||||||||||- THIS IS the source chromosome")

            if position > len(chromosome)-1:
                position = len(chromosome)-1
           
            if(isinstance(chromosome[position-1], str) and '*' in chromosome[position-1] and len(chromosome[position-1])>1):
                mutated_chromosome = self.insertion(chromosome, position, gene_to_insert)
                #create record
                operation = {'Mut_Type': type,
                            'Chr': chromosome_index + 1,
                            'Pos': position,
                            'Gene': gene_to_insert,
                            'Genome after mutation': source_genome}
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
                operation = {'Mut_Type': type,
                            'Chr': chromosome_index + 1,
                            'Pos': position,
                            'Gene': gene_to_delete,
                            'Genome after mutation': source_genome}
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

    # def deletion(self, source_chromosome, position_applicable_region):
    #     if isinstance(source_chromosome[position_applicable_region], int) and '_' not in str(source_chromosome[position_applicable_region]):
    #         del source_chromosome[position_applicable_region]
    #     if position_applicable_region > 0 and isinstance(source_chromosome[position_applicable_region-1], int) and '_' not in str(source_chromosome[position_applicable_region-1]):
    #         del source_chromosome[position_applicable_region-1]

    #     return source_chromosome

    

    def deletion(self, source_chromosome, position_applicable_region):

            del source_chromosome[position_applicable_region]
            if position_applicable_region > 0 :
                del source_chromosome[position_applicable_region-1]
            return source_chromosome

    # def deletion(self, source_chromosome, position_applicable_region):
    #     if '_' not in source_chromosome[position_applicable_region]:
    #         del source_chromosome[position_applicable_region]
    #         if position_applicable_region > 0:
    #             if '_' not in source_chromosome[position_applicable_region-1]:
    #                 del source_chromosome[position_applicable_region-1]
    #     return source_chromosome

    
    # def deletion(self, source_chromosome, position_applicable_region):
    #     position_a = False
    #     position_b = False
    #     deletion_region = source_chromosome[position_applicable_region]
    #     new_source_chromosome = []

    #     # print(deletion_region+"OOI - This is what the program wants to delete")
    #     if "_" not in deletion_region:
    #         position_a = True
    #         # print(str(deletion_region)+ "HERE A - This is what the program actually deletes")
    #         if position_applicable_region > 0 and source_chromosome[position_applicable_region-1] == deletion_region:
    #             position_b = True
    #             # print(str(deletion_region)+ "HERE B - This is what the program actually deletes")

    #     if position_a and position_b:
    #         for i in range(0, position_applicable_region-1):
    #             new_source_chromosome.append(source_chromosome[i])
    #         for i in range(position_applicable_region+1, len(source_chromosome)):
    #             new_source_chromosome.append(source_chromosome[i])
    #     elif position_a:
    #         for i in range(0, position_applicable_region):
    #             new_source_chromosome.append(source_chromosome[i])
    #         for i in range(position_applicable_region+1, len(source_chromosome)):
    #             new_source_chromosome.append(source_chromosome[i])
    #     elif position_a == False:
    #         return source_chromosome

    #     # print(f"{source_chromosome}***************** - Source chromosome")
    #     # print(f"{new_source_chromosome}_______________ - New source chromosome after deletions")
    #     return new_source_chromosome


    """
     This function duplicates genes required in the source genome so they can compare with 
     the duplicates in the target genome.The duplication could be tandem or transpositional
    """    
    def duplication(self, source_chromosome, gene, insertion_position):
        
        source_chromosome[insertion_position-1] = gene

        return source_chromosome


    # def handle_no_legal_mutations(self, source_genome, target_genome, list_of_legal_operations):
    #     mutations, required_mutation = self.mutation_legal_operations(source_genome, target_genome)
                
    #     if mutations == [] and required_mutation !=():
    #         switch = True
    #         source_genome, mutation_list = self.do_mutation(source_genome, required_mutation)
    #         list_of_legal_operations.append(mutation_list)
                    
    #         count_applicable_region = 0
    #         for chromosome in source_genome:
    #             for i in range(len(chromosome)):
    #                 if isinstance(chromosome[i], str) and '*' in chromosome[i] and len(chromosome[i]) > 1 :
    #                     count_applicable_region += 1
    #         clean_chromosome = []
    #         clean_genome = []


    

