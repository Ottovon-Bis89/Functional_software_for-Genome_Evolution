from random import randint
from Data_generator import DataGenerator
import Intergenic_region_generator
import ForeignDNA
from LegalOperations import MutationOperations
import Helper_Methods as PF
from logger import log


class Node:
    def __init__(self):
        self.state = []

    def get_operations(self, source_genome, target_genome):
        # log.debug(f"get_operations")

        '''
         Get the operations required to transform the source genome into the target genome.
        The function follows these steps:
        Initialize an empty list to store legal operations
        Set the switch variable to True, indicating the loop should start
        Initialize the foreign DNA counter to 0, counting occurrences of foreign DNA insertion
        Start a while loop that continues until the switch is turned off
        Iterate over each element in the target genome
        If the element is present at the same index, do nothing and continue to the next element
        Create a copy of source_genome to ensure it remains unchanged
        Check the number of applicable intergenic regions, if 0 then create more intergenic regions
        Initialize a variable to count the applicable regions
        Iterate over each chromosome in the source genome
        Iterate over each element in the chromosome
        Check if the element is a string, contains '*', and has length greater than 1
        Increment the count of applicable regions
        Initialize an empty list to store clean chromosomes
        Remove all unapplicable intergenic regions and call the intergenic regions generator
        Iterate over each chromosome in the source genome
        Iterate over each element in the chromosome
        Check if the element is a string and does not contain '*', which indicates a gene(sequence block)
        Append the element to the clean chromosome list
        Check if the element is an integer
        Append the element to the clean chromosome list
        Reset the clean chromosome list for the next iteration
        Call the inter_generator method of the gen_obj instance, passing the clean genome as an argument and assign the result to the insert_intergenic_region variable.
        This will populate the chromosome with intergenic regions, necessary for mutations to occur
        Generate a random number between 0 and 5 and assign it to 'choose'
        Check if 'choose' is less than 5 and 'foreign_Dna_counter' is not equal to 0 and assign the returned values to 'mutations' and 'required_mutation'
        Check if there are no mutations and if 'required_mutation' is not an empty tuple
        Call the 'do_mutation' method with 'source_genome' and 'required_mutation' as arguments, and assign the returned values to 'source_genome' and 'mutation_list'
        Append 'mutation_list' to 'list_of_legal_operations'
        Enter a while loop that continues while there are mutations or 'required_mutation' is not an empty tuple
        Initialize an empty list to hold 'final_mutations'
        Iterate over the indices of 'mutations'
        Set 'mutation_type' to 'del' if the index is 1
        Set 'mutation_type' to 'dup' for any other index
        Get the mutation at the current index
        Iterate over the indices of the 'mutation' list
        Check if the element at the current index is not an empty list
        Assign the current index to 'chromosome_index'
        Assign the element at the current index to 'chromosome'
        Iterate over the indices of the 'chromosome' list
        Create a tuple 'do_mutation' with 'mutation_type', 'chromosome_index', and the element at the current index
        Call the 'do_mutation' method with 'source_genome' and 'do_mutation' as arguments, and assign the returned values to 'source_genome' and 'mutation_list'
        Append 'mutation_list' to 'final_mutations'
        Append 'final_mutations' to 'list_of_legal_operations'
        Remove all unapplicable intergenic regions and call intergenerator
        Call the 'mutation_legal_operations' method with 'source_genome' and 'target_genome' as arguments, and assign the returned value to 'required_mutation'
        Check if there are not any required mutations'
        Set 'switch' to False for the loop to terminate
        Check if the 'foreign_Dna_counter' is greater than or equal to 0
        Increment the 'foreign_Dna_counter' by 1 after each insertion
        Here is a list of foreign DNAs where fragments are sublists
        Create an instance of the 'Foreign_DNA' class
        Initialize an empty list 'foreign_dna' to hold foreign DNA fragments
        Enter a while loop that continues as long as 'foreign_dna' is an empty list
        Call the 'foreign_dna_pool' method of the 'foreign_obj' instance with 'source_genome' and 'target_genome' as arguments, and assign the returned value to 'foreign_dna'
        Get the length of the 'foreign_dna' list and subtract 1 to account for zero-based indexing
        Generate a random integer between 0 and 'foreign_dna_len' and assign the random integer to 'choice_foreign_dna'
        Get the element at the index of the choice of foreign of dna' from the 'foreign_dna' list, and Assign the element to 'chosen'add foreign DNA to the source genome
        Call the 'insert_foreign_dna' method of the 'foreign_obj' instance with 'source_genome' and 'chosen' as arguments and Assign the returned values to 'source_genome' and 'list_of_operationss'
        mutation_genome = source_genome.copy()  // Create a copy of 'source_genome' and assign it to 'mutation_genome'
        Call the 'mutation_legal_operations' method with 'mutation_genome' and 'target_genome' as arguments. Assign the returned values to 'mutations' and 'required_mutation'
        Check if 'mutations' is an empty list
        Call the 'do_mutation' method with 'source_genome' and 'required_mutation' as arguments and Assign the returned values to 'source_genome' and 'mutation_list'
        Enter a while loop that continues while either there are mutations and 'required_mutation' is not an empty tuple, or 'required_mutation' is not an empty tuple
        Initialize an empty list 'final_mutations'
        Iterate over the indices of 'non_empty_mutations'. Determine the 'mutation_type' based on the current index 'i'
        Iterate over the indices of 'mutation' and Check if the element at the current index is not an empty list
        Assign the current index to 'chromosome_index'. Assign the element at the current index to 'chromosome'
        Iterate over the indices of 'chromosome'. Create a tuple 'do_mutation' with 'mutation_type', 'chromosome_index', and the element at the current index
        Call the 'do_mutation' method with 'source_genome' and 'do_mutation' as arguments. Assign the returned values to 'source_genome' and 'mutation_list'
        Remove all unapplicable intergenic regions and call intergenerator
        Call the 'mutation_legal_operations' method with 'source_genome' and 'target_genome' as arguments and Assign the returned values to 'mutations' and 'required_mutation'
        If a required mutation is not found, exit the loop
        @param source_genome The source genome to transform.
        @param target_genome The target genome to transform into.
        @return A list of operations needed for the transformation.
        '''

        list_of_operations = []  
        switch = (True  )
        foreign_Dna_counter = 0  

        while (switch): 
            for i, element in enumerate(target_genome):
                if i < len(source_genome) and element == source_genome[i]:
                    pass 
                else:
                    source_genome = source_genome[:] 

            gen_obj = Intergenic_region_generator.IntergenicGenerator()
            legalOps = MutationOperations()
            data_generator = DataGenerator()
            source_genome = data_generator.check_genes(source_genome)
            target_genome = data_generator.check_genes(target_genome)
            source_genome = data_generator.generate_intergenic_regions(source_genome)
            target_genome = data_generator.generate_intergenic_regions(target_genome)

           
            count_applicable_region = 0
            for chromosome in source_genome:  
                for i in range(len(chromosome)):  
                    
                    if (isinstance(chromosome[i], str) and "*" in chromosome[i]) and len(chromosome[i]) > 1:
                        count_applicable_region += 1 
                    
            if count_applicable_region > 0:
                clean_chromosome = []
                clean_genome = []  

                for chromosome in source_genome:  
                    for i in range(len(chromosome)):  
                        if isinstance(chromosome[i], str) and "*" not in chromosome[i]:
                            clean_chromosome.append(chromosome[i])  
                        elif isinstance(chromosome[i], int): 
                            clean_chromosome.append(chromosome[i])  
                    clean_genome.append(clean_chromosome)  
                    clean_chromosome = []
                    

                insert_intergenic_region = gen_obj.inter_generator(clean_genome)
                source_genome = gen_obj.intergenic_regions(insert_intergenic_region)

                num_FDNA = randint(0, 3) 
                if (num_FDNA <= 2 and foreign_Dna_counter != 0):  
                    mutations, required_mutation = legalOps.mutation_legal_operations(source_genome, target_genome)
                    if (required_mutation):  
                        source_genome, mutation_list = self.do_mutation(source_genome, required_mutation)
                        if mutation_list != []:
                            list_of_operations.append(mutation_list)  
                        switch = True  
                    else:
                       
                        while (any(mutations)) and required_mutation:

                            final_mutations = []

                            for i in range(len(mutations)):
                                if i == 0:
                                    mutation_type = "ins"  
                                elif i == 1:
                                    mutation_type = "del"  
                                else:
                                    mutation_type = "dup" 

                                mutation = mutations[i] 

                                for chromosome_number in range(len(mutation)):
                                    if mutation[chromosome_number]:  
                                        chromosome_index = chromosome_number  
                                        chromosome = mutation[chromosome_number]  

                                        for m in range(len(chromosome)): 
                                            
                                            do_mutation = (mutation_type,chromosome_index,chromosome[m])

                                            source_genome,mutation_list,= self.do_mutation(source_genome, do_mutation)
                                            source_genome = source_genome[:]

                                            final_mutations.append(mutation_list)  

                            list_of_operations.append(final_mutations)

                            
                            clean_chromosome = []
                            clean_genome = []
                            for chromosome in source_genome:
                                for i in range(len(chromosome)):
                                    if (isinstance(chromosome[i], str)and "*" not in chromosome[i]):
                                        clean_chromosome.append(chromosome[i])
                                    elif isinstance(chromosome[i], int):
                                        clean_chromosome.append(chromosome[i])
                                clean_genome.append(clean_chromosome)
                                clean_chromosome = []

                            gen_obj = Intergenic_region_generator.IntergenicGenerator()
                            insert_intergenic_region = gen_obj.inter_generator(clean_genome)
                            source_genome = gen_obj.intergenic_regions(insert_intergenic_region)

                            mutations,required_mutation = legalOps.mutation_legal_operations(source_genome, target_genome)
                            if ( not required_mutation): 
                                break
                            switch = (False)
                elif (foreign_Dna_counter <= 2 or foreign_Dna_counter != 0):  
                    foreign_Dna_counter += 1  
        
                    foreign_obj = (ForeignDNA.Foreign_DNA())  
                    foreign_dna = []
                    while foreign_dna == []: 
                        foreign_dna = foreign_obj.foreign_dna_pool(source_genome, target_genome)

                    foreign_dna_len = len(foreign_dna) - 1

                    choice_foreign_dna = randint(0, foreign_dna_len)

                    chosen = foreign_dna[choice_foreign_dna]

                    source_genome, f_dna_mutation = foreign_obj.insert_foreign_dna(source_genome, chosen)

                    
                    mutations, required_mutation = legalOps.mutation_legal_operations(source_genome, target_genome)

                    if required_mutation:  
                        
                        source_genome, mutation_list = self.do_mutation(source_genome, required_mutation)

                        if mutation_list != []:
                            list_of_operations.append(mutation_list) 
                        switch = True

                    else:
                        
                        while any(mutations) and required_mutation:
                            final_mutations = []
                            for i in range(len(mutations)):  
                                if i == 0:
                                    mutation_type = "ins"
                                elif i == 1:
                                    mutation_type = "del"
                                else:
                                    mutation_type = "dup"

                                mutation = mutations[i]  

                                for chromosome_number in range(len(mutation)):  
                                    if mutation[chromosome_number]:  
                                        chromosome_index = chromosome_number  
                                        chromosome = mutation[chromosome_number]  

                                        for m in range(len(chromosome)):  
                                            do_mutation = (mutation_type,chromosome_index,chromosome[m])

                                            source_genome,mutation_list, = self.do_mutation(source_genome, do_mutation)

                          
                            clean_chromosome = []
                            clean_genome = []
                            for chromosome in source_genome:
                                for i in range(len(chromosome)):
                                    if (isinstance(chromosome[i], str) and "*" not in chromosome[i]):
                                        clean_chromosome.append(chromosome[i])
                                    elif isinstance(chromosome[i], int):
                                        clean_chromosome.append(chromosome[i])

                                clean_genome.append(clean_chromosome)
                                clean_chromosome = []

                            gen_obj = Intergenic_region_generator.IntergenicGenerator()
                            insert_intergenic_region = gen_obj.inter_generator(
                                clean_genome)
                            source_genome = gen_obj.intergenic_regions(insert_intergenic_region)

                            
                            mutations,required_mutation, = legalOps.mutation_legal_operations(source_genome, target_genome)

                            if (not required_mutation):  
                                break
                        switch = False

        return list_of_operations
    

    def do_mutation(self, source_genome, required_mutation):
        """
        Performs a specified mutation on the source genome with approved intergenic regions.
        The function interprets the required mutation and calls appropriate sub-functions
        (delete, duplicate, insert) to execute the mutation operation.
        The function follows these steps:
        1. Iterates over genes with approved intergenic regions in the source genome.
            - Identifies mutation points marked with '*' in the gene strings.
            - Stores genes and mutation points for each gene in their respective lists.
            - Appends the gene and mutation point lists to their respective genome lists.
        2. Extracts mutation type, chromosome index, and actual mutation details from the required mutation list.
        3. Performs the specified mutation operation:
            - For duplication, adjusts the position, checks for applicable regions, and updates the source genome.
            - For insertion, inserts genes at the specified position and updates the source genome.
            - For deletion, deletes genes at the specified position and updates the source genome.
        4. Records each mutation operation and appends it to the list of mutations.
        @param sourceGenome A list representing the source genome with approved intergenic regions.
        @param requiredMutation A list representing the required mutation with details such as type, chromosome index, and mutation data.
        @return A tuple containing the updated source genome and a list of mutation records.
        """

        # log.debug("do mutation")
        

        list_of_mutations = []
        list_of_genes = []
        list_of_genes_genome = []
        list_of_mutation_points = []
        list_of_mutation_points_genome = []

        for genes_with_intergenic_approved in source_genome:
            for i in range(len(genes_with_intergenic_approved)):
                if (
                    isinstance(genes_with_intergenic_approved[i], str)
                    and len(genes_with_intergenic_approved[i]) > 1
                ) and "*" in genes_with_intergenic_approved[i]:
                    if i != len(genes_with_intergenic_approved) - 2:
                        list_of_mutation_points.append(i + 1)
                elif (not isinstance(genes_with_intergenic_approved[i], str)) or (
                    isinstance(genes_with_intergenic_approved[i], str)
                    and "*" not in genes_with_intergenic_approved[i]
                ):
                    list_of_genes.append(genes_with_intergenic_approved[i])
            list_of_genes_genome.append(list_of_genes)
            list_of_mutation_points_genome.append(list_of_mutation_points)

            list_of_genes = []
            list_of_mutation_points = []

        mutation_type = required_mutation[0]
        chromosome_index = required_mutation[1]
        actual_mutation = required_mutation[2]

        if mutation_type == "dup":
            position = actual_mutation[1]
            gene_to_duplicate = actual_mutation[2]
            type_of_duplication = actual_mutation[3]

            chromosome = source_genome[chromosome_index]
            if position > len(chromosome) - 1:
                position = len(chromosome) - 1

            if (
                isinstance(chromosome[position - 1], str)
                and "*" in chromosome[position - 1]
            ) and len(chromosome[position - 1]) > 1:
                mutated_chromosome = self.duplication(
                    chromosome, gene_to_duplicate, position
                )
                source_genome[chromosome_index] = mutated_chromosome

                operation = {
                    "Mut_Type": mutation_type,
                    "Chr": chromosome_index + 1,
                    "Gene": gene_to_duplicate,
                    "Pos": position,
                    "Type of dup": type_of_duplication,
                    "Genome after mutation": source_genome,
                }

                list_of_mutations.append(operation)

        elif mutation_type == "ins":
            position = actual_mutation[0]
            gene_to_insert = actual_mutation[1]

            while chromosome_index >= len(source_genome):
                source_genome.append([])
            chromosome = source_genome[chromosome_index]

            if (
                position > len(chromosome) - 1
                or "_" in str(chromosome[position])
                or len(chromosome) == 0
            ):
                mutated_chromosome = self.insertion(
                    chromosome, position, gene_to_insert, True
                )

                operation = {
                    "Mut_Type": mutation_type,
                    "Chr": chromosome_index + 1,
                    "Pos": len(chromosome) + 1,
                    "Gene": gene_to_insert,
                    "Genome after mutation": source_genome,
                }

                list_of_mutations.append(operation)

            elif (
                isinstance(chromosome[position - 1], str)
                and "*" in chromosome[position - 1]
            ) and len(chromosome[position - 1]) > 1:
                mutated_chromosome = self.insertion(
                    chromosome, position, gene_to_insert
                )

                operation = {
                    "Mut_Type": mutation_type,
                    "Chr": chromosome_index + 1,
                    "Pos": position,
                    "Gene": gene_to_insert,
                    "Genome after mutation": source_genome,
                }

                list_of_mutations.append(operation)

        elif mutation_type == "del":
            position = actual_mutation[0]

            gene_to_delete = actual_mutation[1]

            if chromosome_index < len(source_genome):
                chromosome = source_genome[chromosome_index]

            if position > len(chromosome) - 1 :
                position = len(chromosome) - 1

            if (
                isinstance(chromosome[position - 1], str)
                and "*" in chromosome[position - 1]
            ) and len(chromosome[position - 1]) > 1:
                mutated_chromosome = self.deletion(chromosome, position)

                operation = {
                    "Mut_Type": mutation_type,
                    "Chr": chromosome_index + 1,
                    "Pos": position,
                    "Gene": gene_to_delete,
                    "Genome after mutation": source_genome,
                }

                list_of_mutations.append(operation)

        return source_genome, list_of_mutations

    def insertion( self, source_chromosome, position_applicable_region, gene, larger_length=False):
        # log.debug("insertion")
        """
        This function performs an insertion operation in the source genome by inserting a gene at the specified position.
        
        Parameters:
        - source_chromosome: The source chromosome (list) where the insertion will be performed.
        - position_applicable_region: The position within the chromosome where the insertion is applicable.
        - gene: The gene to be inserted at the specified position.
        - larger_length: A boolean flag indicating if the insertion should be performed at a position beyond the current length of the chromosome.
        Returns:
        - The updated source chromosome after the insertion operation.
        """
        
        print("sourve before")
        print(source_chromosome)
        print("----------")
        if larger_length:
            insertion_index = 0
            while (insertion_index < len(source_chromosome) and gene > source_chromosome[insertion_index]):
                print("check1")
                print(insertion_index)
                print(len(source_chromosome))
                print(insertion_index < len(source_chromosome))
                print("-------------------")
                print(gene)
                print(source_chromosome[insertion_index])
                print(gene > source_chromosome[insertion_index])
                print("check2")
                insertion_index += 1


            if insertion_index >= len(source_chromosome):
                source_chromosome.append(gene)  # Insert gene at the end of the chromosome
                print("greater")
                print(source_chromosome)
            else:
                source_chromosome.insert(insertion_index, gene)
                print("less")
                print(source_chromosome)
        else:
            source_chromosome[position_applicable_region] = gene

        return source_chromosome
    

    def deletion(self, source_chromosome, position_applicable_region):
        # log.debug("deletion")
        """
        Delete genes from the source chromosome that are not present in the target genome.

        This function deletes genes from the source chromosome that are not found in the target genome.
        The goal is to make the source chromosome the same as the target chromosome at the end of the evolutionary process.

        :param source_chromosome: The source chromosome from which genes will be deleted.
        :param position_applicable_region: The index of the gene to be checked for deletion.
        :return: The modified source chromosome with genes deleted as necessary.
        """
        if (
            "_" not in source_chromosome[position_applicable_region]
            or "*" not in source_chromosome[position_applicable_region]
        ):
            del source_chromosome[position_applicable_region]
        return source_chromosome
    

    def duplication(self, source_chromosome, gene_to_duplicate, insertion_position):
        # log.debug("duplication")
        """
        This function performs a duplication operation in the source genome by duplicating a gene at the specified position.
        # Check if the specified position is not marked with '_' or does not contain '*'
            # This condition ensures that the duplication does not occur in regions already marked for other purposes
            # Insert the gene to be duplicated at the position before the insertion_position
        Parameters:
        - source_chromosome: The source chromosome (list) where the duplication will be performed.
        - gene_to_duplicate: The gene to be duplicated.
        - insertion_position: The position in the chromosome where the duplication will be inserted.
        Returns:
        - The updated source chromosome after the duplication operation.
        """

        if (
            "_" not in source_chromosome[insertion_position]
            or "*" not in source_chromosome[insertion_position]
        ):
            source_chromosome.insert(insertion_position - 1, gene_to_duplicate)

        return source_chromosome
