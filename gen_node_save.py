
from random import randint
import sys
# import Gen_xtremities
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

    def get_legal_operations(self, source_genome, target_genome):

        list_of_legal_operations = []
        loop_counter = 0  # No foreign DNA in first iteration of mutations
        foreign_Dna_counter = 0
        switch = True

        while switch:

            for element in target_genome:
                if element in source_genome:
                    pass
                else:
                    source_genome = source_genome[:]

            if loop_counter >= 0:
                # check number of applicale region, if 0 then create
                count_applicable = 0
                for chromosome in source_genome:
                    for i in range(len(chromosome)):
                        if isinstance(chromosome[i], str) and '*' in chromosome[i] and len(chromosome[i]) > 1:
                            count_applicable += 1

                clean_chromosome = []
                clean_genome = []

                if count_applicable >= 0:
                    # remove all unapplicable intergenic regions and call intergenerator
                    for chromosome in source_genome:
                        for i in range(len(chromosome)):
                            if isinstance(chromosome[i], str) and '*' not in chromosome[i]:
                                clean_chromosome.append(chromosome[i])
                            elif isinstance(chromosome[i], int):
                                clean_chromosome.append(chromosome[i])
                        clean_genome.append(clean_chromosome)
                        clean_chromosome = []

                gen_obj = Data_generator.Data_generator()
                normal_intergenic_region = gen_obj.generate_integenic_regions(clean_genome)
                source_genome = gen_obj.generate_integenic_regions(normal_intergenic_region)

                # randomly choose to insert foreign dna into the source genome
                choose = randint(0, 10)
                if (choose <= 5 and foreign_Dna_counter != 0):
                    mutations, required_mutations = self.mutation_legal_operations(source_genome, target_genome)
                    if mutations == [] and required_mutations != ():
                        source_genome, *mutation_list = self.do_mutation(source_genome, required_mutations)
                        print(mutation_list)

                        list_of_legal_operations.append(mutation_list)
                        switch = True
                    else:
                        while (any(mutation_list) and required_mutations != ()) or required_mutations != ():
                            final_mutation= []
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
                                            do_mutation = (
                                                mutation_type, chromosome_index, chromosome[m])
                                            source_genome, mutation_list = self.do_mutation(source_genome, do_mutation)
                                            final_mutation.append(mutation_list)
                            list_of_legal_operations.append(final_mutation)
                            clean_chromosome = []
                            clean_genome = []

                            # remove all unapplicable intergenic regions and call intergenerator
                            # to insert new applicable regions for mutations to occur
                            for chromosome in source_genome:
                                for i in range(len(chromosome)):
                                    if isinstance(chromosome[i], str) and '*' not in chromosome[i]:
                                        clean_chromosome.append(chromosome[i])
                                    elif isinstance(chromosome[i], int):
                                        clean_chromosome.append(chromosome[i])
                                clean_genome.append(clean_chromosome)
                                clean_chromosome = []

                            gen_obj = Data_generator.Data_generator()
                            normal_intergenic_region = gen_obj.generate_integenic_regions(clean_genome)
                            source_genome = gen_obj.generate_integenic_regions(normal_intergenic_region)

                            mutations, required_mutations = self.mutation_legal_operations(source_genome, target_genome)

                            if required_mutations == ():
                                break
                        switch = True
                elif ((foreign_Dna_counter < 10 or foreign_Dna_counter == 0)):
                    print("\tInserted foreign DNA")
                    foreign_Dna_counter += 1
                    # Here is list of foreign dna where fragments are sublists
                    foreign_dna = []
                    while foreign_dna == []:
                        foreign_dna = self.get_foreign_dna_fragment(source_genome, target_genome)
                        # print(len(foreign_dna))
                    #  Randomly choose a foreign dna from pool
                    foreign_dna_length = len(foreign_dna) - 1
                    choice_foreign_dna = randint(0, foreign_dna_length)
                    chosen_fragment = foreign_dna[choice_foreign_dna]
                    
                    # add foreign dna to the source genome
                    source_genome, list_of_operationss = self.insert_foreign_dna(source_genome, chosen_fragment)
                     
                    list_of_legal_operations.append(list_of_operationss)
                    print("problem starts here.........................")
                    print("problem starts hereeeeeeeeeeeeeeeeeeeeeee.........................")
                    if mutations == []:
                        
                        source_genome, mutation_list = self.do_mutation(source_genome, required_mutations)
                        list_of_legal_operations.append(mutation_list)
                        switch = True
                        print("waaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaat")
                    else:
                        while (any(mutations) and required_mutations == ()) or required_mutations != ():
                            final_mutation = []
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
                                            final_mutation.append(mutation_list)

                            list_of_legal_operations.append(final_mutation)
                            clean_chromosome = []
                            clean_genome = []

                            # remove all unapplicable intergenic regions and call intergenerator
                            for chromosome in source_genome:
                                for i in range(len(chromosome)):
                                    if isinstance(chromosome[i], str) and '*' not in chromosome[i]:
                                        clean_chromosome.append(chromosome[i])
                                    elif isinstance(chromosome[i], int):
                                        clean_chromosome.append(chromosome[i])
                                        

                                clean_genome.append(clean_chromosome)
                                clean_chromosome = []

                            gen_obj = Data_generator.Data_generator()
                            normal_intergenic_region = gen_obj.generate_integenic_regions(clean_genome)
                            source_genome = gen_obj.generate_integenic_regions(normal_intergenic_region)

                            mutations, required_mutations = self.mutation_legal_operations(source_genome, target_genome)

                            if required_mutations == ():
                                break
                        switch = False

            elif loop_counter == 0:
                mutations, required_mutations = self.mutation_legal_operations(source_genome, target_genome)

                if mutations == [] and required_mutations != ():
                    switch = True

                    # Do random mutation
                    source_genome, mutation_list = self.do_mutation(source_genome, required_mutations)
                    print("Could not find straight path to get to target_genome so randomly mutated")

                    list_of_legal_operations.append(mutation_list)

                    # check number of applicale region, if 0 then create
                    count_applicable = 0
                    for chromosome in source_genome:
                        for i in range(len(chromosome)):
                            if isinstance(chromosome[i], str) and '*' in chromosome[i] and len(chromosome[i]) > 1:
                                count_applicable += 1
                    print(f"Within first iteration after any and all mutations we check applicable reagions, count is : {str(count_applicable)}")
                    clean_chromosome = []
                    clean_genome = []

                    if count_applicable <= len(source_genome)-1:
                        # remove all unapplicable intergenic regions and call intergenerator
                        for chromosome in source_genome:
                            for i in range(len(chromosome)):
                                if (isinstance(chromosome[i], str) and '*' not in chromosome[i]) or isinstance(chromosome[i], int):
                                    clean_chromosome.append(chromosome[i])
                            clean_genome.append(clean_chromosome)
                            clean_chromosome = []

                        gen_obj = Data_generator.Data_generator()
                        normal_intergenic_region = gen_obj.generate_integenic_regions(clean_genome)
                        source_genome = gen_obj.generate_integenic_regions(normal_intergenic_region)
                else:
                    while (any(mutations) and required_mutations == ()) or required_mutations != ():

                        final_mutation = []
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
                                        do_mutation = (
                                            mutation_type, chromosome_index, chromosome[m])
                                        source_genome, mutation_list = self.do_mutation(source_genome, do_mutation)
                                        final_mutation.append(mutation_list)
                        list_of_legal_operations.append(final_mutation)
                        clean_chromosome = []
                        clean_genome = []

                        # remove all unapplicable intergenic regions and call intergenerator
                        for chromosome in source_genome:
                            for i in range(len(chromosome)):
                                if isinstance(chromosome[i], str) and '*' not in chromosome[i]:
                                    clean_chromosome.append(chromosome[i])
                                elif isinstance(chromosome[i], int):
                                    clean_chromosome.append(chromosome[i])
                            clean_genome.append(clean_chromosome)
                            clean_chromosome = []
                            gen_obj = Data_generator.Data_generator()
                            normal_intergenic_region = gen_obj.generate_integenic_regions(clean_genome)
                            source_genome = gen_obj.generate_integenic_regions(normal_intergenic_region)

                        mutations, required_mutations = self.mutation_legal_operations(source_genome, target_genome)

                        if required_mutations == ():
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

    def insert_foreign_dna(self, source_genome, chosen_fragment):
        # Count number of applicable intergenic regions to correspond with number of mutations
        list_of_mutation_points = []
        list_of_mutation_points_genome = []

        for genes_with_intergenic_approved in source_genome:
            for i in range(len(genes_with_intergenic_approved)):
                if isinstance(genes_with_intergenic_approved[i], str) and len(genes_with_intergenic_approved[i]) > 1 and '*' in genes_with_intergenic_approved[i]:
                    list_of_mutation_points.append(i+1)

            list_of_mutation_points_genome.append(list_of_mutation_points)
            list_of_mutation_points = []

        # insert intergenic regions in foreign dna fragments as these intergenic regions would be used for mutations to occur.
        fragment_with_intergenic_regions = []
        length = len(chosen_fragment)
        for j in range(len(chosen_fragment)):
            if j == 0:
                random_bp = randint(6, 10)
                region = '*' + str(random_bp)
                fragment_with_intergenic_regions.append(region)
            random_bp = randint(6, 10)
            start = chosen_fragment[j]
            region = '*' + str(random_bp)
            fragment_with_intergenic_regions.append(start)
            if j != length-1:
                fragment_with_intergenic_regions.append(region)

        # find applicable intergenic regions in fragments
        for i in range(len(fragment_with_intergenic_regions)):
            if i % 2 == 0 or i == 0:
                region = fragment_with_intergenic_regions[i]
                if len(region) > 2:
                    value = region[2]+region[2]
                else:
                    value = region[1]
                if int(value) <= 5:
                    fragment_with_intergenic_regions[i] = '*'

        # Account for chromosomes without intergenic regions
        position_applicable_region_chromosome = []
        source_chromosome = []
        random_chromosome = []

        while len(position_applicable_region_chromosome) == 0:
            random_chromosome = randint(0, len(list_of_mutation_points_genome)-1)
            position_applicable_region_chromosome = list_of_mutation_points_genome[random_chromosome]
            source_chromosome = source_genome[random_chromosome]

        # randomly pick a position from position of applicable region in chromosome to random position in chromosome
        random_position = randint(0, len(position_applicable_region_chromosome)-1)
        position = position_applicable_region_chromosome[random_position]

        mutated = []
        mutated = source_chromosome[0:position-1] + fragment_with_intergenic_regions + source_chromosome[position:]
        source_genome[random_chromosome] = mutated
        return source_genome, ['F_DNA inserted ', random_chromosome, position, fragment_with_intergenic_regions]

    """
    This function decides if any series of mutations, can take genome A(soure genome) to genome B(target genome)
    checks number of chromosomes -> possibility of chromosome deletion(target chromosmes less than source)
     or chromosome insertion (source chromosome count less than target)
    Checks number of genes in chromosome for target and source -> indicators for insertion/foreign dna/deletion
    checks signed integers(genes) between target and source
    Duplication - look at the target; if two of same signed integer next to each other -> tandom duplicatio
    if two of same signed ints in chromosome but not next to each other then -> transpositional
    source_genome = source[:]remove underscores that identify fragments in source genome
    """

    def mutation_legal_operations(self, source_genome, target_genome):

        for chromosome in source_genome:
            for i in range(len(chromosome)):
                if isinstance(chromosome[i], str) and '_' in chromosome[i]:
                    if len(chromosome[i]) == 3:
                        gene = chromosome[i]
                        chromosome.append(int(gene[:2]))
                    elif len(chromosome[i]) == 2:
                        gene = chromosome[i]
                        chromosome.append(int(gene[:1]))
                elif isinstance(chromosome[i], str):
                    chromosome.append((chromosome[i]))
                elif isinstance(chromosome[i], int):
                    chromosome.append((chromosome[i]))
                elif ((isinstance(chromosome[i], str) and '*' in chromosome[i])):
                    chromosome.append((chromosome[i]))
            source_genome.append(chromosome)
            chromosome = []

        # step 1, check genes per chromosome between target and source [number of chromosomes should always be the same]
        # 1.1 in target and not in source [create in list that contains tuples of (position,gene)]
        in_genome = []
        in_target = []

        # Take note of different length of genomes where this condition does not hold
        # print('source_genome:', source_genome)
        # print('target_genome:', target_genome)
        for j in range(len(target_genome)):
            in_target = []
            chromosome = source_genome[j]
            target_chromosome = target_genome[j]
            # print('j:', j)
            # print('chromosome:', chromosome)
            # print('target_chromosome:', target_chromosome)
            for i in range(len(target_chromosome)):
                if '*' not in str(target_chromosome[i]) and (target_chromosome[i]) not in chromosome:
                    in_target.append((i, target_chromosome[i]))
            in_genome.append(in_target)

        # 1.2 in source genome and not in target genome[Create out list that contains tuples of (position,gene)]
        out_genome = []
        out_target = []
        occurred = []

        for j in range(len(target_genome)):
            chromosome = source_genome[j]
            target_chromosome = target_genome[j]

            for i in range(len(chromosome)):
                if ((isinstance(chromosome[i], int) and chromosome[i] not in target_chromosome)) or (((isinstance(chromosome[i], str) and '*' not in chromosome[i])) and chromosome[i] not in target_chromosome):
                    out_target.append((i, chromosome[i]))
                elif (chromosome.count(chromosome[i])) > target_chromosome.count(chromosome[i]) and (isinstance(chromosome[i], str) and '*' not in chromosome[i]) and (chromosome[i] not in occurred):
                    out_target.append((i, chromosome[i]))
                    occurred.append(chromosome[i])
            out_genome.append(out_target)
            out_target = []

        # step 2: duplication; check target for duplication [note position, gene and type of duplication]
        # isinstance(chromosome[i], int) and
        duplication_genome = []
        target_duplication = []
        duplicated_genes = []

        for chromosome in target_genome:
            for i in range(len(chromosome)):
                if isinstance(chromosome[i], int) and chromosome.count(chromosome[i]) > 1 and chromosome[i] not in duplicated_genes:
                    if chromosome[i] == chromosome[i+2] or chromosome[i] == chromosome[i-2]:
                        type = "tandem"
                    else:
                        type = "transpositional"
                    duplicated_genes.append(chromosome[i])
                    target_duplication.append(
                        [i, self.get_second_index(chromosome, chromosome[i]), chromosome[i], type])
            duplication_genome.append(target_duplication)
            target_duplication = []
            duplicated_genes = []

        # step 2.1: check if the duplication is already present in source, if yes remove from list, otherwise cause mutation
        # Check that duplication genome is not empty
        if any(duplication_genome):
            for j in range(len(source_genome)):
                chromosome = source_genome[j]
                sub = duplication_genome[j]
                for i in range(len(sub)):
                    dup = sub[i]
                    duplicated = dup[2]

                    # check if gene exists
                    if duplicated in chromosome:
                        occurances = chromosome.count(duplicated)
                        if occurances == 2:
                            if len(sub) > 1:
                                n_sub = sub.remove(dup)
                                duplication_genome[j] = n_sub
                            else:
                                n_sub = []
                                duplication_genome[j] = n_sub

        # check the 3 lists and randomly pick a tuple from one of them
        do_mutation = ()
        delete = False
        insert = False
        duplicate = False

        if any(duplication_genome):
            duplicate = True
        if any(out_genome):
            delete = True
        if any(in_genome):
            insert = True

        if insert and delete and duplicate:
            pick = randint(0, 2)
            if pick == 0:
                for i in range(len(in_genome)):
                    chromosome = in_genome[i]
                    if chromosome != []:
                        picker = randint(0, len(chromosome)-1)
                        do_mutation = ("ins", i, chromosome[picker])
                        break
            elif pick == 1:
                for i in range(len(out_genome)):
                    chromosome = out_genome[i]
                    if chromosome != []:
                        picker = randint(0, len(chromosome)-1)
                        do_mutation = ("del", i, chromosome[picker])
                        break
            elif pick == 2:
                for i in range(len(duplication_genome)):
                    chromosome = duplication_genome[i]
                    if chromosome != []:
                        picker = randint(0, len(chromosome)-1)
                        do_mutation = ("dup", i, chromosome[picker])
                        break
        elif insert and delete:
            pick = randint(0, 1)
            if pick == 0:
                for i in range(len(in_genome)):
                    chromosome = in_genome[i]
                    if chromosome != []:
                        picker = randint(0, len(chromosome)-1)
                        do_mutation = ("ins", i, chromosome[picker])
                        break
            elif pick == 1:
                for i in range(len(out_genome)):
                    chromosome = out_genome[i]
                    if chromosome != []:
                        picker = randint(0, len(chromosome)-1)
                        do_mutation = ("del", i, chromosome[picker])
                        break
        elif delete and duplicate:
            pick = randint(0, 1)
            if pick == 0:
                for i in range(len(out_genome)):
                    chromosome = out_genome[i]
                    if chromosome != []:
                        picker = randint(0, len(chromosome)-1)
                        do_mutation = ("del", i, chromosome[picker])
                        break
            elif pick == 1:
                for i in range(len(duplication_genome)):
                    chromosome = duplication_genome[i]
                    if chromosome != []:
                        picker = randint(0, len(chromosome)-1)
                        do_mutation = ("dup", i, chromosome[picker])
                        break
        elif insert and duplicate:
            pick = randint(0, 1)
            if pick == 0:
                for i in range(len(in_genome)):
                    chromosome = in_genome[i]
                    if chromosome != []:
                        picker = randint(0, len(chromosome)-1)
                        do_mutation = ("ins", i, chromosome[picker])
                        break
            elif pick == 1:
                for i in range(len(duplication_genome)):
                    chromosome = duplication_genome[i]
                    if chromosome != []:
                        picker = randint(0, len(chromosome)-1)
                        do_mutation = ("dup", i, chromosome[picker])
                        break
        elif insert:
            for i in range(len(in_genome)):
                chromosome = in_genome[i]
                if chromosome != []:
                    picker = randint(0, len(chromosome)-1)
                    do_mutation = ("ins", i, chromosome[picker])
                    break
        elif delete:
            for i in range(len(out_genome)):
                chromosome = out_genome[i]
                if chromosome != []:
                    picker = randint(0, len(chromosome)-1)
                    do_mutation = ("del", i, chromosome[picker])
                    break
        elif duplicate:
            for i in range(len(duplication_genome)):
                chromosome = duplication_genome[i]
                if chromosome != []:
                    picker = randint(0, len(chromosome)-1)
                    do_mutation = ("dup", i, chromosome[picker])
                    break

        # step 3: checking if all these necessary mutations can occur at once
        # First check that insert and del positions dont overlap for same chromosomes, if they do then we won't be able to cause all necessary mutations

        for i in range(len(out_genome)):
            out_chromosome = out_genome[i]
            in_chromosome = in_genome[i]
            for j in range(len(out_chromosome)):
                tup = out_chromosome[j]
                for tup_in in in_chromosome:
                   # print(tup_in)
                    if tup_in[0] == tup[0]:
                        # print(tup[0])
                        return [], do_mutation
        # Check that intergenic regions exist for ins, del, and dup.
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
            if len(chromosome) != 0:
                for i in range(len(chromosome)):
                    tup = chromosome[i]
                    if len(chromosome) > 1 and i < len(chromosome)-1:
                        check = chromosome[i+1]
                        if check[0] == tup[0]+1:
                            out_position.append(tup[0])
                            i += 1
                out_position_genome.append(out_position)
            else:
                out_position_genome.append([])
        # get position for duplication
        dup_position = []
        dup_position_genome = []

        for chromosome in duplication_genome:
            for i in range(len(chromosome)):
                tup = chromosome[i]
                dup_position.append(tup[1])
            dup_position_genome.append(dup_position)

        # get number of applicable intergenic regions
        number_applicable_region = 0
        applicable_region_chromosome = []
        applicable_region_genome = []

        for chromosome in source_genome:
            for j in range(len(chromosome)):
                # for gene in chromosome:
                if (isinstance(chromosome[j], str) and len(chromosome[j]) > 1 and '*' in chromosome[j]):
                    number_applicable_region += 1
                    applicable_region_chromosome.append(j)
            applicable_region_genome.append(applicable_region_chromosome)
            applicable_region_chromosome = []

        # check number of applicable regions against number of total mutations
        # count positions for each mutation
        insert_count = 0
        for chromosome in in_position_genome:
            for gene in chromosome:
                insert_count += 1
        del_count = 0

        # check counting in pairs as well
        for chromosome in out_position_genome:
            for gene in chromosome:
                del_count += 1
        dup_count = 0
        for chromosome in dup_position_genome:
            for gene in chromosome:
                dup_count += 1
        if (number_applicable_region < (dup_count+insert_count+del_count)):
            return [], do_mutation

        # check that the positions for mutations have applicable intergenic regions
        # check insertion
        for i in range(len(applicable_region_genome)):
            in_chromosome = in_position_genome[i]
            out_chromosome = out_position_genome[i]
            dup_chromosome = dup_position_genome[i]
            applicable_regions_chrom = applicable_region_genome[i]

            total_positions = []
            total_positions = in_chromosome+out_chromosome+dup_chromosome

            for j in range(len(total_positions)):
                if (total_positions[j]+1 not in applicable_regions_chrom) or applicable_region_chromosome == []:
                    return [], do_mutation

            mutation_insert = {}

            # code to take elements of lists and place in dictionary [for loop]
            for i in range(len(in_genome)):
                if len(in_genome[i]) > 0:
                    mutation_insert["insertion chromosome"] = i+1
                    chromosome_interest = in_genome[i]
                    for i in range(len(chromosome_interest)):
                        instance = chromosome_interest[i]
                        mutation_insert["insertion position"] = instance[0]
                        mutation_insert["insertion gene"] = instance[1]

            # return list of mutations
            return [in_genome, out_genome, duplication_genome], do_mutation

        return do_mutation

    # Function for finding second occurance of element within list

    def get_second_index(self, int_list, num):
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

    def do_mutation(self, source_genome, required_mutations):
        list_of_mutations = []

        list_of_genes = []
        list_of_genes_genome = []
        list_of_mutation_points = []
        list_of_mutation_points_genome = []

        for genes_with_intergenic_approved in source_genome:
            for i in range(len(genes_with_intergenic_approved)):
                if isinstance(genes_with_intergenic_approved[i], str) and len(genes_with_intergenic_approved[i]) > 1 and '*' in genes_with_intergenic_approved[i]:
                    # count_applicable_regions += 1
                    if i != len(genes_with_intergenic_approved)-2:
                        list_of_mutation_points.append(i+1)
                elif (not isinstance(genes_with_intergenic_approved[i], str)) or (isinstance(genes_with_intergenic_approved[i], str) and '*' not in genes_with_intergenic_approved[i]):
                    list_of_genes.append(genes_with_intergenic_approved[i])

            list_of_genes_genome.append(list_of_genes)
            list_of_mutation_points_genome.append(list_of_mutation_points)

            list_of_mutation_points = []

        type = required_mutations[0]
        chromosome_index = required_mutations[1]
        print(str(required_mutations[0])+"++++++"+str(required_mutations[1])+"+++++"+str(required_mutations[2])+"This is what is stored in mutation required")
        actual_mutation = required_mutations[2]

        if type == 'dup':
            position = actual_mutation[1]
            gene_to_duplicate = actual_mutation[2]
            type_of_duplication = actual_mutation[3]
            chromosome = source_genome[chromosome_index]

            if position > len(chromosome)-1:
                position = len(chromosome)-1

            # check for applicable region at position -1

            if (isinstance(chromosome[position-1], str) and '*' in chromosome[position-1] and len(chromosome[position-1]) > 1):
                mutated_chromosome = self.duplication(
                    chromosome, gene_to_duplicate, position)
                source_genome[chromosome_index] = mutated_chromosome
                # create record
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
            # print(str(chromosome_index)+"((((((((((((((((((((((((- This is the index of the chromosome")
            chromosome = source_genome[chromosome_index]
            # print(str(chromosome)+ "%%%%%%%%%%%%%%%%%%%3")
            # print(str(source_genome)+"||||||||||||||||||||||- THIS IS the source chromosome")
            if position > len(chromosome)-1:
                position = len(chromosome)-1

            if (isinstance(chromosome[position-1], str) and '*' in chromosome[position-1] and len(chromosome[position-1]) > 1):
                mutated_chromosome = self.Insertion(
                    chromosome, position, gene_to_insert)
                # create record
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
            # print(str(chromosome))
            if position > len(chromosome)-1:
                position = len(chromosome)-1

            if (isinstance(chromosome[position-1], str) and '*' in chromosome[position-1] and len(chromosome[position-1]) > 1):
                mutated_chromosome = self.Deletion(chromosome, position)
                # create record
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
     This function inserts series of genes(sequence blocks) required in the source genome in order 
     to get to the target genome
    """

    def insertion(self, source_chromosome, position_applicable_region, gene):

        source_chromosome[position_applicable_region-1] = gene

        return source_chromosome

    """
    This function deletes genes that are in the source genome but not in the target genome, so that
    the source genome can be the same as the target genome at the end of the evolutionary process.
    However, it does not delete the inserted foreign DNA fragments.
    """

    def deletion(self, source_chromosome, position_applicable_region):
        position_a = False
        position_b = False
        deletion_region = source_chromosome[position_applicable_region]
        new_source_chromosome = []

        # print(deletion_region+"OOI - This is what the program wants to delete")
        if "_" not in deletion_region:
            position_a = True
            # print(str(deletion_region)+ "HERE A - This is what the program actually deletes")
            if position_applicable_region > 0 and source_chromosome[position_applicable_region-1] == deletion_region:
                position_b = True
                # print(str(deletion_region)+ "HERE B - This is what the program actually deletes")

        if position_a and position_b:
            for i in range(0, position_applicable_region-1):
                new_source_chromosome.append(source_chromosome[i])
            for i in range(position_applicable_region+1, len(source_chromosome)):
                new_source_chromosome.append(source_chromosome[i])
        elif position_a:
            for i in range(0, position_applicable_region):
                new_source_chromosome.append(source_chromosome[i])
            for i in range(position_applicable_region+1, len(source_chromosome)):
                new_source_chromosome.append(source_chromosome[i])
        elif position_a == False:
            return source_chromosome

        # print(f"{source_chromosome}***************** - Source chromosome")
        # print(f"{new_source_chromosome}_______________ - New source chromosome after deletions")
        return new_source_chromosome

    """
     This function duplicates genes required in the source genome so they can compare with 
     the duplicates in the target genome.The duplication could be tandem or transpositional
    """

    def duplication(self, source_chromosome, gene, insertion_position):

        source_chromosome[insertion_position-1] = gene

        return source_chromosome

    def get_foreign_dna_fragment(self, source_genome, target_genome):
        # Check what genes are not in source genome but are in target genome
        source_genome = []
        target_genome = []

        # create master lists

        for chromosome in source_genome:
            for i in range(len(chromosome)):
                if isinstance(chromosome[i], int):
                    source_genome.append(int(chromosome[i]))
                elif isinstance(chromosome[i], str) and "_" in chromosome[i]:
                    if len(chromosome[i]) == 2:
                        gene = chromosome[i]
                        source_genome.append(int(gene[:1]))
                    elif len(chromosome[i]) == 3:
                        gene = chromosome[i]
                        source_genome.append(int(gene[:2]))

        for chromosome in target_genome:
            for i in range(len(chromosome)):
                if isinstance(chromosome[i], int):
                    target_genome.append(int(chromosome[i]))

        # Find the difference between source genome and target genome
        difference = list(set(target_genome) - set(source_genome))

        if len(difference) > 0:
            # define the ratio (1/5)
            # change ratio here (5)
            number_of_random_ints = (len(difference) * 3) - (len(difference))

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

            # Use for_dna list that was created to create foreign dna fragments (random number of frag and random length of fragments)
            number_of_fragments = randint(1, 99)
            len_fragments = 1

            # choose randomly from for_dna list to add to frags
            list_of_fragments = []
            fragment = []
            for j in range(number_of_fragments):
                for i in range(len_fragments):
                    choice = randint(0, len(foreign_dna)-1)
                    fragment.append(foreign_dna[choice])
                # Ensure unique fragments in list
                if j > 0 and fragment not in list_of_fragments:
                    list_of_fragments.append(fragment)
                else:
                    j -= 1
                fragment = []

            # Check for the difference in genes within at least one fragment in list
            check = True
            for f in list_of_fragments:
                if difference in f:
                    check = False
            if check == True:
                final_fragment = difference[:]
            # add a fragment that does contain the difference
            # Check that the gene does not already exist in the fragment
                while len(final_fragment) <= len(difference)+1:
                    c = foreign_dna[randint(0, len(foreign_dna)-1)]
                    if c not in final_fragment:
                        final_fragment.append(c)
                list_of_fragments.append(final_fragment)

            # Tag foreign DNA
            for i in list_of_fragments:
                fragment = i
                for j in range(len(fragment)):
                    fragment[j] = str(fragment[j])+"_"
            return list_of_fragments

        else:
            # define the ratio (1/5)
            number_of_random_ints = randint(1, 5)

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

            # Use for_dna list that was created to create foreign dna fragments (random number of frag and random length of fragments)
            number_of_fragments = randint(1, 99)
            len_fragments = 1
            # choose randomly from for_dna list to add to frags
            list_of_fragments = []
            fragment = []
            for j in range(number_of_fragments):
                for i in range(len_fragments):
                    choice = randint(0, len(foreign_dna)-1)
                    fragment.append(foreign_dna[choice])
                # Ensure unique fragments in list
                if j > 0 and fragment not in list_of_fragments:
                    list_of_fragments.append(fragment)
                else:
                    j -= 1
                fragment = []

            # Tag foreign DNA
            for i in list_of_fragments:
                fragment = i
                for j in range(len(fragment)):
                    fragment[j] = str(fragment[j])+"_"

            return list_of_fragments
            
