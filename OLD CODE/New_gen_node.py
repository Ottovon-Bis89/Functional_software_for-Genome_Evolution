from random import choice
from random import randint
import Data_generator



class Node:
    def __init__(self):
        self.state = []
        self.children = []
        self.children_weights = []
        self.next_operation = 0
        self.next_operation_weight = []


    """
    The function returns a list of the operations needed to transform the
    source genome to the target genome. It returns random legal options that can be applied to A,
    called recursively until A can be transformed to B
    It also chooses a fragment of foreign DNA and inserts it into the source genome
    """
    
    def get_legal_operations(self, source_genome, target_genome):
        list_of_legal_operations = []
        series_of_mutation = []
        mutation_required = []
        switch = True
        loop_counter = 0
        for_Dna_counter = 0

        while switch:
            for element in target_genome:
                if element in source_genome:
                   
                    pass
                else:
                    source_genome = source_genome[:]
    
            if loop_counter > 0:
                count_app = sum(1 for chromosome in source_genome for i in range(len(chromosome)) 
                                if isinstance(chromosome[i], str) and '*' in chromosome[i] and len(chromosome[i]) > 1)
                
                if count_app > 0:
                    clean_genome = []
                    for chromosome in source_genome:
                        
                        clean_chrom = [x for x in chromosome if isinstance(x, int) or ('*' not in x)]
                        clean_genome.append(clean_chrom)
                    
                    gen_obj = Data_generator.Data_generator()
                    normal_i_reg = gen_obj.generate_integenic_regions(clean_genome)
                    source_genome = gen_obj.generate_integenic_regions(normal_i_reg)

                choose = randint(0, 10)
                if choose <= 5 and for_Dna_counter == 0:
                    series_of_mutation, *mutation_required = self.mutation_legal_operations(source_genome, target_genome)

                    if series_of_mutation == [] and mutation_required !=():
                        source_genome, mutation_list = self.do_mutation(source_genome, mutation_required)

                        list_of_legal_operations.append(mutation_list)
                        switch = True

                    else:
                        mutations_finale = []
                        for i in range(len(series_of_mutation)):
                            print(series_of_mutation)
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
                                        source_genome, *mutation_list = self.do_mutation(source_genome, do_mutation)
                                        
                                        mutations_finale.append(mutation_list)
                        list_of_legal_operations.append(mutations_finale)
                        
            else:
                break
            loop_counter += 1
            for_Dna_counter += 1
            switch = False
        
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

        # insert intergenic regions in foreign dna fragments
        frag_with_intergenic_regions = []
        length = len(frag)
        for j in range(length):
            if j == 0:
                random_bp = randint(6, 10)
                region = '*' + str(random_bp)
                frag_with_intergenic_regions.append(region)
            random_bp = randint(6, 10)
            start = frag[j]
            region = '*' + str(random_bp)
            frag_with_intergenic_regions.append(start)
            if j != length - 1:
                frag_with_intergenic_regions.append(region)

        # find applicable intergenic regions in frag
        for i in range(len(frag_with_intergenic_regions)):
            if i % 2 == 0 or i == 0:
                region = frag_with_intergenic_regions[i]
                if len(region) > 2:
                    value = region[1:3]
                else:
                    value = region[1]
                if int(value) <= 5:
                    frag_with_intergenic_regions[i] = '*'

        # Account for chromosomes without intergenic regions
        position_app_reg_chrom = []
        source_chrom = []
        rand_chrom = []

        while len(position_app_reg_chrom) == 0:
            rand_chrom = randint(0, len(list_of_mutation_points_genome) - 1)
            position_app_reg_chrom = list_of_mutation_points_genome[rand_chrom]
            source_chrom = source_genome[rand_chrom]

        # randomly pick a position from position_app_reg_chrom to position
        rand_pos = randint(0, len(position_app_reg_chrom) - 1)
        position = position_app_reg_chrom[rand_pos]

        mutated = []
        mutated = source_chrom[0:position - 1] + frag_with_intergenic_regions + source_chrom[position:]

        source_genome[rand_chrom] = mutated
        return source_genome, ['F_DNA inserted ', rand_chrom, position, frag_with_intergenic_regions]





    def mutation_legal_operations(self, source_genome, target_genome):

        for chrom in source_genome:
            chromo = []
            for elem in chrom:
                try:
                    value = int(elem.split('_')[0])
                    chromo.append(value)
                except ValueError:
                    chromo.append(elem)
            source_genome.append(chromo)
            return source_genome
        
        

# Step 1: Check genes per chromosome between target and source, where number of chromosomes should always be the same
# 1.1 In target and not in source (create a list that contains tuples of (position, gene))
        
        in_genome = []

        for j in range(len(target_genome)):
            in_target = []
            chromosome = source_genome[j]
            
            t_chrom = target_genome[j]

            for i in range(len(t_chrom)):
                if '*' not in str(t_chrom[i]) and i < len(chromosome) and t_chrom[i] not in chromosome:
                    in_target.append((i, t_chrom[i]))

            in_genome.append(in_target)
            
            
       


    # 1.2 In source genome and not in target genome (create a list that contains tuples of (position, gene))
        out_genome = []

        for j in range(len(target_genome)):
            out_target = []
            chromosome = source_genome[j]
            t_chrom = target_genome[j]
            occurred = []

        for i in range(len(chromosome)):
            if isinstance(chromosome[i], int) and chromosome[i] not in t_chrom:
                out_target.append((i, chromosome[i]))
            elif isinstance(chromosome[i], str) and '*' not in chromosome[i]:
                if chromosome[i] not in t_chrom and chromosome.count(chromosome[i]) > t_chrom.count(chromosome[i]) and chromosome[i] not in occurred:
                    out_target.append((i, chromosome[i]))
                    occurred.append(chromosome[i])

        out_genome.append(out_target)

        out_genome = []

        # for j in range(len(target_genome)):
        #     out_target = []
        #     if j < len(source_genome):
        #         chromosome = source_genome[j]
        #     else:
        #         chromosome = []

        #     t_chrom = target_genome[j]
        #     occurred = []

        #     for i in range(len(chromosome)):
        #         if isinstance(chromosome[i], int) and chromosome[i] not in t_chrom:
        #             out_target.append((i, chromosome[i]))
        #         elif isinstance(chromosome[i], str) and '*' not in chromosome[i]:
        #             if chromosome[i] not in t_chrom and chromosome.count(chromosome[i]) > t_chrom.count(chromosome[i]) and chromosome[i] not in occurred:
        #                 out_target.append((i, chromosome[i]))
        #                 occurred.append(chromosome[i])

        # out_genome.append(out_target)




        # Step 2: Check target for duplications and note position, gene, and type of duplication
        duplication_genome = []
        for chromosome in target_genome:
            t_duplication = []
            last_positions = {}
            for i, gene in enumerate(chromosome):
                if isinstance(gene, int) and chromosome.count(gene) > 1 and gene not in last_positions:
                    if i - last_positions.get(gene, i-1) == 1:
                        dup_type = "tandem"
                    else:
                        dup_type = "transpositional"
                    last_positions[gene] = i
                    t_duplication.append([i, self.get_second_index(chromosome, gene), gene, dup_type])
            duplication_genome.append(t_duplication)

        # Step 2.1: Check if the duplication is already present in source, if yes remove from list, otherwise cause mutation
        for j, chromosome in enumerate(source_genome):
            sub = duplication_genome[j]
            new_sub = []
            dup_genes = set()
            for i, dup in enumerate(sub):
                duplicated = dup[2]
                if duplicated in chromosome:
                    occurances = chromosome.count(duplicated)
                    if occurances == 2:
                        if len(sub) > 1:
                            new_sub = sub[:i] + sub[i+1:]
                        break
                else:
                    new_sub.append(dup)
                    dup_genes.add(duplicated)
            duplication_genome[j] = new_sub



        #check the 3 lists and randomly pick a tuple from one of them

        mutation_genomes = [in_genome, out_genome, duplication_genome]
        mutation_types = ["ins", "del", "dup"]
        do_mutation = ()

        # Check if there is any non-empty list
        if any(mutation_genomes):
            # Randomly pick a non-empty list and a mutation type
            genome = choice([g for g in mutation_genomes if g])
            mutation_type = choice(mutation_types)
            # Find a non-empty chromosome and pick a random element
            for i, chromosome in enumerate(genome):
                if chromosome:
                    picker = choice(range(len(chromosome)))
                    do_mutation = (mutation_type, i, chromosome[picker])
                    break


    def check_mutations(in_genome, out_genome, duplication_genome, source_genome):
        # Step 1: check for empty inputs
        if not in_genome or not out_genome or not duplication_genome:
            return [], False

        # Step 2: check for overlapping positions
        for i in range(len(out_genome)):
            out_chromosome = out_genome[i]
            in_chromosome = in_genome[i]
            for j in range(len(out_chromosome)):
                tup = out_chromosome[j]
                for tup_in in in_chromosome:
                    if tup_in[0] == tup[0]:
                        return [], False

        # Step 3: check that intergenic regions exist for insert, del, and dup
        in_pos = set(tup[0] for chromosome in in_genome for tup in chromosome)
        out_pos = set(tup[0] for chromosome in out_genome for tup in chromosome)
        dup_pos = set(tup[1] for chromosome in duplication_genome for tup in chromosome)
        app_reg_pos = set()
        for chromosome in source_genome:
            for j in range(len(chromosome)):
                if isinstance(chromosome[j], str) and len(chromosome[j]) > 1 and '*' in chromosome[j]:
                    app_reg_pos.add(j + 1)

        # Step 4: check that the positions for mutations have applicable intergenic regions
        total_positions = in_pos | out_pos | dup_pos
        if not app_reg_pos.issuperset(p + 1 for p in total_positions):
            return [], False

        # Step 5: create dictionary of mutations and return list of mutations
        mutations = {'insertion': [], 'deletion': [], 'duplication': []}
        for i, chromosome in enumerate(in_genome):
            for pos, gene in chromosome:
                mutations['insertion'].append({'chromosome': i+1, 'position': pos, 'gene': gene})
        for chromosome in out_genome:
            for i in range(len(chromosome)-1):
                pos, gene = chromosome[i]
                next_pos, next_gene = chromosome[i+1]
                if next_pos == pos + 1:
                    mutations['deletion'].append({'chromosome': i+1, 'position': pos, 'gene': gene})
        for i, chromosome in enumerate(duplication_genome):
            for pos, gene in chromosome:
                mutations['duplication'].append({'chromosome': i+1, 'position': pos, 'gene': gene})

        return mutations, True


    def get_second_index(int_list, num):
        """
        Returns the index of the second occurrence of num in int_list.
        If num does not occur twice in the list, returns -1.
        """
        first_index = -1
        for i, n in enumerate(int_list):
            if n == num:
                if first_index == -1:
                    first_index = i
                else:
                    return i
        return -1


    def do_mutation(self, source_genome, mutation_required):
        """
        This function picks a type of mutation and calls different functions (delete, duplicate, insert) to act on it.
        It uses source_genome with approved intergenic regions
        It counts the number of applicable intergenic regions to associate with the number of mutations
        """

        list_of_mutations = []
        list_of_genes_genome = []
        list_of_mutation_points_genome = []

        # Loop over each chromosome in the source genome
        for genes_with_intergenic_approved in source_genome:
            list_of_genes = []
            list_of_mutation_points = []

            # Loop over each gene and intergenic region
            for i in range(len(genes_with_intergenic_approved)):
                # Check if the current element is an intergenic region and contains an asterisk
                if isinstance(genes_with_intergenic_approved[i], str) and len(genes_with_intergenic_approved[i]) > 1 and '*' in genes_with_intergenic_approved[i]:
                    # Check if the intergenic region is not the last element
                    if i != len(genes_with_intergenic_approved)-2:
                        list_of_mutation_points.append(i+1)
                # If the current element is not an intergenic region, append it to the list of genes
                elif not isinstance(genes_with_intergenic_approved[i], str) or (isinstance(genes_with_intergenic_approved[i], str) and '*' not in genes_with_intergenic_approved[i]):
                    list_of_genes.append(genes_with_intergenic_approved[i])

            # Append the list of genes and mutation points to the corresponding genome lists
            list_of_genes_genome.append(list_of_genes)
            list_of_mutation_points_genome.append(list_of_mutation_points)

        # Get the mutation type, chromosome index, and actual mutation from the mutation_required argument
        mutation_type = mutation_required[0]
        chromosome_index = mutation_required[1]
        actual_mutation = mutation_required[2]
        # print(len(actual_mutation))

        # Perform the appropriate mutation based on the mutation type
        if mutation_type == 'dup':
            position = actual_mutation[1]
            gene_to_duplicate = actual_mutation[2]
            type_of_duplication = actual_mutation[3]
            chromosome = source_genome[chromosome_index]

            # Check if the position is greater than the length of the chromosome and adjust it accordingly
            if position > len(chromosome)-1:
                position = len(chromosome)-1

            # Check if an applicable intergenic region exists at position-1
            if isinstance(chromosome[position-1], str) and '*' in chromosome[position-1] and len(chromosome[position-1]) > 1:
                # Perform duplication and update the source genome
                mutated_chromosome = self.duplication(chromosome, gene_to_duplicate, position)
                source_genome[chromosome_index] = mutated_chromosome

                # Create a record of the mutation and append it to the list of mutations

                operation = {'Type': type, 'Chr': chromosome_index + 1, 'Pos': position, 'Type of dup': type_of_duplication,
                                'Genome after mutation': source_genome}
                source_genome[chromosome_index] = mutated_chromosome
                list_of_mutations.append(operation)
                

        elif mutation_type == 'ins':
            # print(len(actual_mutation))
            # print(actual_mutation)
            if len(actual_mutation) < 2:
                raise ValueError('actual_mutation must have at least two elements')
            position = actual_mutation[0]
            gene_to_insert = actual_mutation[1]
            chromosome = source_genome[chromosome_index]

            if position > len(chromosome)-1:
                    position = len(chromosome)

            if position == 0 or not isinstance(chromosome[position-1], str):
                    mutated_chromosome = chromosome[:position] + [gene_to_insert] + chromosome[position:]
                    # create record
                    operation = {'Type': type, 'Chr': chromosome_index + 1, 'Pos': position, 'Gene': gene_to_insert,
                                'Genome after mutation': source_genome}
                    source_genome[chromosome_index] = mutated_chromosome
                    list_of_mutations.append(operation)
        
        elif type == 'del':
                position = actual_mutation[0]
                gene_to_delete = actual_mutation[1]
                chromosome = source_genome[chromosome_index]
                if position > len(chromosome)-1:
                    position = len(chromosome)-1

                if(isinstance(chromosome[position], str) and '*' in chromosome[position] and len(chromosome[position])>1):
                    mutated_chromosome = chromosome[:position] + chromosome[position+1:]
                    # create record
                    operation = {'Type': type, 'Chr': chromosome_index + 1, 'Pos': position, 'Gene': gene_to_delete,
                                'Genome after mutation': source_genome}
                    source_genome[chromosome_index] = mutated_chromosome
                    list_of_mutations.append(operation)

        return source_genome, list_of_mutations


    # This function inserts a sequence of genes into a source genome at a specific position to get to the target genome.
    def insertion(source_chromosome, position_app_region, gene):
        source_chromosome[position_app_region - 1] = gene
        return source_chromosome

    # This function deletes genes from the source genome that are not in the target genome, leaving the inserted foreign DNA fragments intact.
    def deletion(source_chromosome, position_app_region):
        deletion_region = source_chromosome[position_app_region]
        if "_" not in deletion_region:
            if position_app_region > 0 and source_chromosome[position_app_region - 1] == deletion_region:
                new_source_chromosome = source_chromosome[:position_app_region-1] + source_chromosome[position_app_region+1:]
            else:
                new_source_chromosome = source_chromosome[:position_app_region] + source_chromosome[position_app_region+1:]
        else:
            new_source_chromosome = source_chromosome
        return new_source_chromosome

    # This function duplicates genes required in the source genome so they can compare with the duplicates in the target genome.
    # The duplication could be tandem or transpositional.
    def duplication(source_chromosome, gene, insertion_position):
        source_chromosome.insert(insertion_position - 1, gene)
        return source_chromosome




    def foreign_dna_pool(source, target):
        # Create empty lists to store genes in source and target genomes
        source_genome = []
        target_genome = []
        
        # Extract genes from source genome
        for chromosome in source:
            for i in range(len(chromosome)):
                if isinstance(chromosome[i], int):
                    source_genome.append(int(chromosome[i]))
                elif isinstance(chromosome[i], str) and "_" in chromosome[i]:
                    # Extract gene from gene tag
                    gene = chromosome[i][:chromosome[i].index("_")]
                    source_genome.append(int(gene))
        
        # Extract genes from target genome
        for chromosome in target:
            for i in range(len(chromosome)):
                if isinstance(chromosome[i], int):
                    target_genome.append(int(chromosome[i]))
        
        # Find the difference between source and target genomes
        difference = list(set(target_genome) - set(source_genome))
        
        if len(difference) > 0:
            # Define the ratio of foreign DNA fragments to difference genes
            ratio = 3  # change ratio here
            
            # Create foreign DNA list
            for_dna = []
            count = 0
            while count < len(difference) * ratio:
                gene = randint(1, 40)
                if gene not in for_dna:
                    for_dna.append(gene)
                    count += 1
            
            # Combine foreign DNA with difference genes and remove duplicates
            for_dna = difference + for_dna
            for_dna = list(set(for_dna))
            
            # Add more genes if necessary to meet the ratio
            if len(for_dna) < len(difference) * ratio:
                count = len(for_dna)
                while len(for_dna) < len(difference) * ratio:
                    gene = randint(1, 40)
                    if gene not in for_dna:
                        for_dna.append(gene)
                        count += 1
            
            # Create foreign DNA fragments
            number_of_frags = randint(1, 99)
            len_frags = 1
            list_of_frags = []
            for j in range(number_of_frags):
                frag = []
                for i in range(len_frags):
                    choice = randint(0, len(for_dna)-1)
                    frag.append(for_dna[choice])
                # Ensure unique fragments in list
                if j > 0 and frag not in list_of_frags:
                    list_of_frags.append(frag)
                else:
                    j -= 1
            
            # Check for the presence of difference genes in the fragments
            check = True
            for f in list_of_frags:
                if any(gene in f for gene in difference):
                    check = False
            if check:
                # Add a fragment that contains the difference genes
                final_frag = difference[:]
                while len(final_frag) <= len(difference)+1:
                    c =  for_dna[randint(0, len(for_dna)-1)]
                    if c not in final_frag:
                        final_frag.append(c)
                list_of_frags.append(final_frag)
            
            # Tag foreign DNA fragments
            for frag in list_of_frags:
                for i in range(len(frag)):
                    frag[i] = str(frag[i])+"_"

           
        
