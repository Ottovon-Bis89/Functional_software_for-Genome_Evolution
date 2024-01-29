from random import randint
import sys
import Data_generator
import random



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
    def Get_legal_operations(self,source_genome, target_genome):
        list_of_legal_operations = []
        adjacenciesA = source_genome
        adjacenciesB = target_genome
        switch = True
        loop_counter = 0  # No foreign DNA in first iteration of mutations
        foreign_Dna_counter = 0
       

        while switch:

            for element in adjacenciesB:
                if element in adjacenciesA:
                    pass
                else:
                    source_genome = adjacenciesA[:]

                    if loop_counter >= 0:
                # count the number of applicable regions
                            count_applicable = sum(isinstance(gene, str) and '*' in gene and len(gene) > 1 for chromosome in adjacenciesA for gene in chromosome)

                    if count_applicable > 0:
                        # remove unapplicable intergenic regions and create cleaned genome
                            clean_genome = []
                            for chromosome in adjacenciesA:
                                clean_chromosome = [gene for gene in chromosome if isinstance(gene, int) or ('*' not in gene)]
                                clean_genome.append(clean_chromosome)

                    gen_obj = Data_generator.Data_generator()
                    normal_intergenic_region = gen_obj.Generate_integenic_regions(clean_genome)
                    adjacenciesA = gen_obj.Generate_integenic_regions(normal_intergenic_region)

                    # randomly choose to insert foreign dna


                    if foreign_Dna_counter > 0 and randint(0, 10) >= 5:
                        series_of_mutation, mutation_required = self.Mutation_legal_operations(adjacenciesA, adjacenciesB)

                        if series_of_mutation and mutation_required:
                            source_genome, *mutation_list = self.Do_mutation(adjacenciesA, mutation_required)
                            adjacenciesA = source_genome[:]
                        list_of_legal_operations.append(mutation_list)
                        switch = True

                    elif series_of_mutation:
                        mutations_finale = []
                        for mutation_type, mutation in zip(['ins', 'del', 'dup'], series_of_mutation):
                            for chromosome_number, chromosome in enumerate(mutation):
                                if chromosome:
                                    for breakpoint in chromosome:
                                        do_mutation = (mutation_type, chromosome_number, breakpoint)
                                        source_genome, mutation_list = self.Do_mutation(adjacenciesA, do_mutation)
                                        adjacenciesA = source_genome[:]
                                        mutations_finale.append(mutation_list)
                        if mutations_finale:
                            list_of_legal_operations.append(mutations_finale)
                            switch = True


                            # Remove all unapplicable intergenic regions and generate new ones for mutations
                            clean_genome = []
                            for chromosome in adjacenciesA:
                                clean_chromosome = [x for x in chromosome if isinstance(x, (str, int)) and '*' not in str(x)]
                                clean_genome.append(clean_chromosome)

                            gen_obj = Data_generator.Data_generator()
                            normal_intergenic_region = gen_obj.Generate_integenic_regions(clean_genome)
                            adjacenciesA = gen_obj.Generate_integenic_regions(normal_intergenic_region)

                            # Find applicable mutations
                            while True:
                                series_of_mutation, mutation_required = self.Mutation_legal_operations(adjacenciesA, adjacenciesB)
                                if mutation_required == ():
                                    break
                                
                                # Perform mutations and update genome
                                source_genome, *mutation_list = self.Do_mutation(adjacenciesA, mutation_required)
                                adjacenciesA = source_genome[:]
                                list_of_legal_operations.append(mutation_list)

                            switch = False
                            
                    elif foreign_Dna_counter < 10 or foreign_Dna_counter == 0:
                        print("\tInserted foreign DNA")
                        foreign_Dna_counter += 1
                
                        # Select foreign DNA fragment to insert
                        foreign_dna = self.Get_foreign_dna_fragment(adjacenciesA, adjacenciesB)
                        
                        # Insert foreign DNA fragment into genome
                        adjacenciesA, list_of_operations = self.Insert_foreign_dna(adjacenciesA, foreign_dna)
                        list_of_legal_operations.append(list_of_operations)

                        # Perform mutation on genome
                        mutation_results = self.Mutation_legal_operations(adjacenciesA, adjacenciesB)
                        print(len(mutation_results))
                        print(mutation_results)
                        series_of_mutation = mutation_results[0]
                        mutation_required = mutation_results[1]
                        if series_of_mutation == []:
                            source_genome, mutation_list = self.Do_mutation(adjacenciesA, mutation_required)
                            adjacenciesA = source_genome[:]
                            list_of_legal_operations.append(mutation_list)
                            switch = True


                        else:
                            while any(series_of_mutation) or mutation_required:
                                mutations_finale = []
                                for i, mutation_type in enumerate(['ins', 'del', 'dup']):
                                    if mutation := series_of_mutation[i]:
                                        for chromosome_number, chromosome in enumerate(mutation):
                                            if chromosome:
                                                chromosome_index = chromosome_number
                                                for m in chromosome:
                                                    do_mutation = (mutation_type, chromosome_index, m)
                                                    source_genome, mutation_list = self.Do_mutation(adjacenciesA, do_mutation)
                                                    adjacenciesA = source_genome[:]
                                                    mutations_finale.append(mutation_list)
                                list_of_legal_operations.append(mutations_finale)
                                clean_chromosome = []
                                clean_genome = []
                            # Remove all inapplicable intergenic regions and call Data_generator
                            clean_genome = []
                            for chromosome in adjacenciesA:
                                clean_chromosome = []
                                for i in range(len(chromosome)):
                                    if isinstance(chromosome[i], str) and '*' not in chromosome[i]:
                                        clean_chromosome.append(chromosome[i])
                                    elif isinstance(chromosome[i], int):
                                        clean_chromosome.append(chromosome[i])
                                clean_genome.append(clean_chromosome)
                                
                            # Generate normal intergenic regions and update adjacenciesA
                            gen_obj = Data_generator.Data_generator()
                            normal_intergenic_region = gen_obj.Generate_integenic_regions(clean_genome)
                            adjacenciesA = gen_obj.Generate_integenic_regions(normal_intergenic_region)

                            # Obtain mutation series and required mutations
                            series_of_mutation, mutation_required = self.Mutation_legal_operations(adjacenciesA, adjacenciesB)

                            # If no mutations are required, exit the loop
                            if mutation_required == ():
                                break
                                
                            switch = False
                # Check if this is the first iteration
            if loop_counter == 0:
                # Check if there are any legal operations to reach the target genome
                series_of_mutation, mutation_required = self.Mutation_legal_operations(adjacenciesA, adjacenciesB)
                
                # If there are no legal operations and mutation is required
                if series_of_mutation == [] and mutation_required !=():
                    switch = True
                    
                    # Do a random mutation
                    source_genome, mutation_list = self.Do_mutation(adjacenciesA, mutation_required)
                    print("Could not find a straight path to get to target genome so randomly mutated")

                    # Append the mutation list to the list of legal operations
                    list_of_legal_operations.append(mutation_list)
                    
                    # Check the number of applicable regions, if 0 then create them
                    count_applicable = 0
                    for chromosome in adjacenciesA:
                        for i in range(len(chromosome)):
                            if isinstance(chromosome[i], str) and '*' in chromosome[i] and len(chromosome[i]) > 1 :
                                count_applicable += 1
                    print(f"Within the first iteration after any and all mutations, we check applicable regions, count is: {str(count_applicable)}")
                    clean_chromosome = []
                    clean_genome = []
                    # If the number of applicable regions is less than or equal to the number of chromosomes in the genome
                    if count_applicable <= len(adjacenciesA) - 1:
                        # Remove all unapplicable intergenic regions and call intergenerator
                        for chromosome in adjacenciesA:
                            for i in range(len(chromosome)):
                                # If the intergenic region is a string and does not contain an asterisk, or if it is an integer
                                if (isinstance(chromosome[i], str) and '*' not in chromosome[i]) or isinstance(chromosome[i], int):
                                    clean_chromosome.append(chromosome[i])
                            clean_genome.append(clean_chromosome)
                            clean_chromosome = []

                        gen_obj = Data_generator.Data_generator()
                        normal_intergenic_region = gen_obj.Generate_integenic_regions(clean_genome)
                        adjacenciesA = gen_obj.Generate_integenic_regions(normal_intergenic_region)
                    else:
                        # If there are more applicable regions than the number of chromosomes, perform mutation operations
                        while (any(series_of_mutation) and mutation_required == ()) or mutation_required != ():
                            mutations_finale = []
                            for i in range(len(series_of_mutation)):
                                # Determine the type of mutation based on the index of the series of mutations
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
                                        chromosome = mutation[chromosome_number]
                                        for m in range(len(chromosome)):
                                            # Perform the mutation and add the mutation list to the mutations finale list
                                            do_mutation = (mutation_type, chromosome_index, chromosome[m])
                                            source_genome, mutation_list = self.Do_mutation(adjacenciesA, do_mutation)
                                            adjacenciesA = source_genome[:]
                                            mutations_finale.append(mutation_list)
                            list_of_legal_operations.append(mutations_finale)
                            clean_chromosome = []
                            clean_genome = []
                        # Create a function to clean the chromosomes and generate intergenic regions
    
                            clean_chromosome = []
                            for element in chromosome:
                                if isinstance(element, str) and '*' not in element:
                                    clean_chromosome.append(element)
                                elif isinstance(element, int):
                                    clean_chromosome.append(element)
                            clean_genome.append(clean_chromosome)
                            gen_obj = Data_generator.Data_generator()
                            normal_intergenic_region = gen_obj.Generate_integenic_regions(clean_genome)
                            adjacenciesA = gen_obj.Generate_integenic_regions(normal_intergenic_region)
                            return adjacenciesA

                        # Initialize variables and start the loop
                        max_loops = 10000000
                        clean_genome = []
                        adjacenciesA = [...]
                        adjacenciesB = [...]
                        list_of_legal_operations = []
                        loop_counter = 0
                        while True:
                            if loop_counter > max_loops:
                                raise ValueError('Exceeded maximum number of loops')
                            
                            # Clean the genome and generate intergenic regions
                            adjacenciesA = gen_obj.Generate_integenic_regions(adjacenciesA)
                            
                            # Check for mutations
                            series_of_mutation, mutation_required = self.Mutation_legal_operations(
                                adjacenciesA, adjacenciesB)
                            
                            # Add legal operations to the list
                            list_of_legal_operations.extend(series_of_mutation)
                            
                            # Exit the loop if no more mutations are required
                            if not mutation_required:
                                break
                            
                            # # Switch the genomes and continue the loop
                            # adjacenciesA, adjacenciesB = adjacenciesB, adjacenciesA
                            loop_counter += 1

        return list_of_legal_operations



    def Insert_foreign_dna(self, source_genome, fragment):
        # Collect applicable intergenic regions in the source genome
        list_of_mutation_points_genome = []
        for genes_with_intergenic_approved in source_genome:
            mutation_points = [
                i+1 for i, gene in enumerate(genes_with_intergenic_approved)
                if isinstance(gene, str) and len(gene) > 1 and '*' in gene
            ]
            list_of_mutation_points_genome.append(mutation_points)

        # Insert intergenic regions in foreign DNA fragments
        fragment_with_intergenic_regions = []
        for i, gene in enumerate(fragment):
            if i == 0:
                region = '*' + str(randint(6, 10))
                fragment_with_intergenic_regions.append(region)
            region = '*' + str(randint(6, 10))
            fragment_with_intergenic_regions.extend([gene, region] if i < len(fragment)-1 else [gene])

        # Collect applicable intergenic regions in the foreign DNA fragment
        positions_applicable_region_fragment = [
            i for i, gene in enumerate(fragment_with_intergenic_regions)
            if i % 2 == 0 and len(gene) > 2 and int(gene[2:]) <= 5
        ]

        # Account for chromosomes without intergenic regions
        random_chromosome = randint(0, len(list_of_mutation_points_genome)-1)
        position_applicable_region_chromosome = list_of_mutation_points_genome[random_chromosome]
        while not position_applicable_region_chromosome:
            random_chromosome = randint(0, len(list_of_mutation_points_genome)-1)
            position_applicable_region_chromosome = list_of_mutation_points_genome[random_chromosome]

        # Randomly pick an applicable intergenic region in the foreign DNA fragment and a chromosome in the source genome
        random_position = positions_applicable_region_fragment[randint(0, len(positions_applicable_region_fragment)-1)]
        position = position_applicable_region_chromosome[randint(0, len(position_applicable_region_chromosome)-1)]
        mutated_chromosome = source_genome[random_chromosome][:position-1] + fragment_with_intergenic_regions[random_position:random_position+2] + source_genome[random_chromosome][position:]

        source_genome[random_chromosome] = mutated_chromosome
        return source_genome, ['F_DNA inserted ', random_chromosome, position, fragment_with_intergenic_regions[random_position:random_position+2]]

        
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

    def Mutation_legal_operations(self, source_genome, target_genome):
        in_genome = []
        out_genome = []
        duplicated_genes = []
        target_duplication = []
        do_mutation = ()

        for j in range(len(source_genome)):
            chromosome = source_genome[j]
            target_chromosome = target_genome[j]
            in_target = []
            out_target = []

            for i in range(len(target_chromosome)):
                target_gene = target_chromosome[i]

                if target_gene not in chromosome:
                    if isinstance(target_gene, int):
                        in_target.append((i, target_gene))
                    elif isinstance(target_gene, str) and '*' not in target_gene:
                        out_target.append((i, target_gene))

                elif isinstance(target_gene, int) and chromosome.count(target_gene) > 1 and target_gene not in duplicated_genes:
                    if target_gene == chromosome[i-2] or target_gene == chromosome[i+2]:
                        duplication_type = 'tandem'
                    else:
                        duplication_type = 'transpositional'
                    duplicated_genes.append(target_gene)
                    target_duplication.append([i, self.Get_second_index(chromosome, target_gene), target_gene, duplication_type])

            in_genome.append(in_target)
            out_genome.append(out_target)

        # check if the duplication is already present in source, if yes remove from list, otherwise cause mutation
        if any(target_duplication):
            for j in range(len(source_genome)):
                chromosome = source_genome[j]
                sub = target_duplication[j]
                for i in range(len(sub)):
                    dup = sub[i]
                    duplicated = dup[2]

                    if duplicated in chromosome:
                        occurrences = chromosome.count(duplicated)
                        if occurrences == 2:
                            if len(sub) > 1:
                                n_sub = sub.remove(dup)
                                target_duplication[j] = n_sub
                            else:
                                n_sub = []
                                target_duplication[j] = n_sub

        # randomly pick a mutation from the available options

            options = [('ins', in_genome), ('del', out_genome), ('dup', target_duplication)]
            available_options = [opt for opt in options if any(opt[1])]

            if available_options:
                op, op_genome = random.choice(available_options)
                chromosome_index = random.choice([i for i in range(len(op_genome)) if op_genome[i]])
                gene_index = random.choice([i for i, gene in op_genome[chromosome_index]])
                gene = op_genome[chromosome_index][gene_index][1]
                do_mutation = (op, chromosome_index, gene)

        return do_mutation


                
            # code to create mutations
            # options = [('ins', in_genome), ('del', out_genome), ('dup', target_duplication)]
            # available_options = [opt for opt in options if any(opt[1])]

            # if available_options:
            #     op, op_genome = random.choice(available_options)
            #     chromosome_index = random.choice([i for i in range(len(op_genome)) if op_genome[i]])
            #     genes = [(i, gene) for i, gene in enumerate(op_genome[chromosome_index]) if gene]
            #     if genes:
            #         gene_index, gene = random.choice(genes)
            #         do_mutation = (op, chromosome_index, gene)
            #     else:
            #         # no non-None genes found, try another operation
            #         return self.mutation_legal_operations(source_genome, target_genome)
            # else:
            #     # no available options found, return None
            #     do_mutation = None

            # return do_mutation


        


    # def get_index(self, chromosome, gene):
    #     for i in range(len(chromosome)):
    #         if chromosome[i] == gene:
    #             return i
    #     return -1

    def Get_second_index(int_list, num):
        count = 0
        for i, n in enumerate(int_list):
            if n == num:
                count += 1
                if count == 2:
                    return i
        return -1

    """
    This fuction picks a type of mutation and calls different functions (delete, duplicate, insert) to act on it
    It uses source_genome with approved intergenic regions
    It counts number of applicable intergenic regions to associate to number of mutations
    """
    def Do_mutation(self, source_genome, mutation_required):
        list_of_mutations = []

        for chromosome_index, chromosome in enumerate(source_genome):
            list_of_genes = []
            list_of_mutation_points = []
            list_of_mutation_points_genome = []
            list_of_genes_genome = []
            
            for i, gene in enumerate(chromosome):
                if isinstance(gene, str) and len(gene) > 1 and '*' in gene:
                    if i != len(chromosome) - 2:
                        list_of_mutation_points.append(i + 1)
                elif not isinstance(gene, str) or ('*' not in gene):
                    list_of_genes.append(gene)

            list_of_mutation_points_genome.append(list_of_mutation_points)
            list_of_genes_genome.append(list_of_genes)

        mutation_type, chromosome_index, actual_mutation = mutation_required
        chromosome = source_genome[chromosome_index]

        if mutation_type == 'dup':
            position, gene_to_duplicate, type_of_duplication = actual_mutation[1:]
            if position > len(chromosome) - 1:
                position = len(chromosome) - 1
                

            if isinstance(chromosome[position-1], str) and '*' in chromosome[position-1] and len(chromosome[position-1]) > 1:
                mutated_chromosome = self.Duplication(chromosome, gene_to_duplicate, position)
                source_genome[chromosome_index] = mutated_chromosome
                
                operation = {'Type': mutation_type,
                            'Chr': chromosome_index + 1,
                            'Pos': position,
                            'Type of dup': type_of_duplication,
                            'Genome after mutation': source_genome}
                list_of_mutations.append(operation)

        elif mutation_type == 'ins':
            position = actual_mutation[0]
            gene_to_insert = actual_mutation[1]
            actual_mutation = self.Insertion(chromosome, position, gene_to_insert)
            position, gene_to_insert = actual_mutation
            if position > len(chromosome) - 1:
                position = len(chromosome) - 1


            if isinstance(chromosome[position-1], str) and '*' in chromosome[position-1] and len(chromosome[position-1]) > 1:
                mutated_chromosome = self.Insertion(chromosome, position, gene_to_insert)
                source_genome[chromosome_index] = mutated_chromosome

                operation = {'Type': mutation_type,
                            'Chr': chromosome_index + 1,
                            'Pos': position,
                            'Gene': gene_to_insert,
                            'Genome after mutation': source_genome}
                list_of_mutations.append(operation)

        elif mutation_type == 'del':
            
            position, gene_to_delete = actual_mutation
            if position > len(chromosome) - 1:
                position = len(chromosome) - 1
                
            if isinstance(chromosome[position-1], str) and '*' in chromosome[position-1] and len(chromosome[position-1]) > 1:
                mutated_chromosome = self.Deletion(chromosome, position)
                source_genome[chromosome_index] = mutated_chromosome

                operation = {'Type': mutation_type,
                            'Chr': chromosome_index + 1,
                            'Pos': position,
                            'Gene': gene_to_delete,
                            'Genome after mutation': source_genome}
                list_of_mutations.append(operation)

        return source_genome, list_of_mutations
    

    """
     This function inserts series of genes(sequence blocks) required in the source genome in order 
     to get to the target genome
     """
    def Insertion(self, source_chromosome, position_applicable_region, gene):
            mutated_chromosome = source_chromosome[:]
            mutated_chromosome[position_applicable_region-1] = gene

            return mutated_chromosome
    

    """
    This function deletes genes that are in the source genome but not in the target genome, so that
    the source genome can be the same as the target genome at the end of the evolutionary process.
    However, it does not delete the inserted foreign DNA fragments.
    """

    def Deletion(self, source_chromosome, position_applicable_region):
        deletion_region = source_chromosome[position_applicable_region]
        if "_" not in deletion_region and position_applicable_region > 0 and source_chromosome[position_applicable_region-1] == deletion_region:
            return source_chromosome[:position_applicable_region-1] + source_chromosome[position_applicable_region+1:]
        else:
            return source_chromosome


    """
     This function duplicates genes required in the source genome so they can compare with 
     the duplicates in the target genome.The duplication could be tandem or transpositional
    """
    def Duplication(self, source_chromosome, gene, insertion_position):

        source_chromosome[insertion_position-1] = gene

        return source_chromosome

    

    def Get_foreign_dna_fragment(self, source_genome, target_genome):
        # Create a set of genes from source genome
        source_genes = set()
        for chromosome in source_genome:
            for gene in chromosome:
                if isinstance(gene, int):
                    source_genes.add(gene)
                elif isinstance(gene, str) and "_" in gene:
                    gene_num = int(gene.split("_")[0])
                    source_genes.add(gene_num)

        # Find the difference between source genome and target genome
        difference = set()
        for chromosome in target_genome:
            for gene in chromosome:
                if isinstance(gene, int) and gene not in source_genes:
                    difference.add(gene)

        if len(difference) > 0:
            # Define the ratio (1/5)
            ratio = 5
            # Calculate the number of random ints to generate
            number_of_random_ints = (len(difference) * (ratio - 1)) // ratio

            # Generate a set of random ints
            random_ints = set()
            while len(random_ints) < number_of_random_ints:
                random_ints.add(randint(1, 40))

            # Create a list of foreign dna fragments
            fragments = []
            for i in range(randint(1, 99)):
                fragment_length = randint(1, 10)
                fragment = set()
                while len(fragment) < fragment_length:
                    gene = difference if len(fragment) == 0 else random_ints
                    fragment.add(randint(1, 40) if gene == random_ints else next(iter(gene)))
                fragments.append(fragment)

            # Ensure unique fragments in list
            unique_fragments = []
            for fragment in fragments:
                if fragment not in unique_fragments:
                    unique_fragments.append(fragment)

            # Check for the difference in genes within at least one fragment in list
            check = True
            for f in unique_fragments:
                if difference.issubset(f):
                    check = False
            if check:
                unique_fragments.append(difference | set([randint(1, 40)]))

            # Tag foreign DNA
            tagged_fragments = []
            for fragment in unique_fragments:
                tagged_fragments.append([str(gene) + "_" for gene in fragment])

            return tagged_fragments

        else:
            # Define the ratio (1/5)
            ratio = 5
            # Calculate the number of random ints to generate
            number_of_random_ints = (len(difference) * (ratio - 1)) // ratio

            # Generate a set of random ints
            random_ints = set()
            while len(random_ints) < number_of_random_ints:
                random_ints.add(randint(1, 40))

            # Create a list of foreign dna fragments
            fragments = []
            for i in range(randint(1, 99)):
                fragment_length = randint(1, 10)
                fragment = set()
                while len(fragment) < fragment_length:
                    fragment.add(randint(1, 40))
                fragments.append(fragment)

            # Ensure unique fragments in list
            unique_fragments = []
            for fragment in fragments:
                if fragment not in unique_fragments:
                    unique_fragments.append(fragment)

            # Tag foreign DNA
            tagged_fragments = []
            for fragment in unique_fragments:
                tagged_fragments.append([str(gene) + "_" for gene in fragment])

            return tagged_fragments

        

