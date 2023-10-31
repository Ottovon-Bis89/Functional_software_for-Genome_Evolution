
from random import randint
import Intergenic_region_generator
import ForeignDNA
import Helper_Methods as PF


class Node:

    def __init__(self):
        self.state = []
   
    def get_operations(self,source_genome, target_genome):
             
        """
        The function returns a list  of the operations that are needed to transform the
        source  genome to the target genome. It returns a random list of legal operations that can be applied to A,
        sequentially until the source genome (genomeA) can be transformed to the target genome (genomeB)
        It also chooses and inserts fragments of foreign DNA into the source genome as it is transformed into the target genome
        """
       
        list_of_operations = []   # Initialize an empty list to store legal operations
        switch = True    # Set the switch variable to True, indicating the loop should start
        loop_counter = 0 # Initialize the loop counter to 0, representing the number of iterations
        foreign_Dna_counter = 0  # Initialize the foreign DNA counter to 0, counting occurrences of foreign DNA insertion

        while switch:  # Start a while loop that continues until the switch is turned off
            # print(f"{switch=}")
            # Iterate over each element in the target genome
            for i, element in enumerate(target_genome):
                if i < len(source_genome) and element == source_genome[i]:
                    pass  # If the element is present at the same index, do nothing and continue to the next element
                else:
                    source_genome = source_genome[:]  # Create a copy of source_genome to ensure it remains unchanged

            gen_obj = Intergenic_region_generator.Intergenic_generator()
            # check number of applicale intergenic regions, if 0 then create more intergenic regions
            count_applicable_region = 0  # Initialize a variable to count the applicable regions
            for chromosome in source_genome: # Iterate over each chromosome in the source genome
                for i in range(len(chromosome)): # Iterate over each element in the chromosome
                        # Check if the element is a string, contains '*', and has length greater than 1
                    if (isinstance(chromosome[i], str) and '*' in chromosome[i]) and len(chromosome[i]) > 1:
                        count_applicable_region += 1 # Increment the count of applicable regions
            
            if count_applicable_region > 0:
                clean_chromosome = [] # Initialize an empty list to store clean chromosomes
                clean_genome = []  # Initialize an empty list to store clean genomes

                #remove all unapplicable intergenic regions and call intergenic regions generator
                for chromosome in source_genome: # Iterate over each chromosome in the source genome
                    for i in range(len(chromosome)):  # Iterate over each element in the chromosome
                        # Check if the element is a string and does not contain '*', which indicates a gene(sequence block)
                        if isinstance(chromosome[i],str) and '*' not in chromosome[i]: 
                            clean_chromosome.append(chromosome[i])# Append the element to the clean chromosome list
                        elif isinstance(chromosome[i], int): # Check if the element is an integer
                            clean_chromosome.append(chromosome[i])  # Append the element to the clean chromosome list
                    clean_genome.append(clean_chromosome)  # Append the clean chromosome to the clean genome list
                    clean_chromosome = []   # Reset the clean chromosome list for the next iteration
                
                # Call the inter_generator method of the gen_obj instance, passing the clean genome as an argument and assign the result to insert_intergenic_region variable.
                # This will popular the chromosome with intergenic regions, necessary for mutations to occur
    
                insert_intergenic_region = gen_obj.inter_generator(clean_genome)
                source_genome = gen_obj.intergenic_regions(insert_intergenic_region)
                
                # randomly choose to insert foreign dna
                choose = randint(0, 5)  # Generate a random number between 0 and 5 and assign it to 'choose'
                
                if (choose < 4 and foreign_Dna_counter != 0):  # Check if 'choose' is less than 5 and 'foreign_Dna_counter' is not equal to 0
                    
                    # Call the 'mutation_legal_operations' method with 'source_genome' and 'target_genome' as arguments to determine the operations required for transforming A into B,
                    # and assign the returned values to 'mutations' and 'required_mutation'
                    mutations, required_mutation = self.mutation_legal_operations(source_genome, target_genome)
                    # print("req muts        "+str(required_mutation))
                    if required_mutation: # Check if there are no mutations and if 'required_mutation' is not an empty tuple
                    # Call the 'do_mutation' method with 'source_genome' and 'required_mutation' as arguments,
                    # and assign the returned values to 'source_genome' and 'mutation_list'
                    
                        source_genome, mutation_list = self.do_mutation(source_genome, required_mutation)


                        list_of_operations.append(mutation_list)   # Append 'mutation_list' to 'list_of_legal_operations'
                        
                        switch = True  # Set 'switch' to True to continue the loop
                    else:   
                        # print("ent")
                        # print(str(mutations))
                        if all([not sublist for sublist in mutations[0]]):
                            mutation = False
                            # print("mut True")
                        else:
                            # print("mut true")
                            mutation = True
                        # print(mut and required_mutation == False)
                        # Enter a while loop that continues while there are  mutations or 'required_mutation' is not an empty tuple
                        # while (any(mutations) and required_mutation !=()) or required_mutation !=():
                        while mutation == True and required_mutation == True:
                         
                            final_mutations = []   # Initialize an empty list to hold 'final_mutations'

                            for i in range(len(mutations)): # Iterate over the indices of 'mutations'
                                # print(mutations)
                               
                                if i == 0:
                                    mutation_type = 'ins'   # Set 'mutation_type' to 'ins' if the index is 0
                                elif i == 1: 
                                    mutation_type = 'del'   # Set 'mutation_type' to 'del' if the index is 1
                                else:
                                    mutation_type = 'dup'   # Set 'mutation_type' to 'dup' for any other index

                                mutation = mutations[i]     # Get the mutation at the current index


                                # Iterate over the indices of the 'mutation' list
                                for chromosome_number in range(len(mutation)):
            
                                    if mutation[chromosome_number]:       # Check if the element at the current index is not an empty list   
                                        chromosome_index = chromosome_number    # Assign the current index to 'chromosome_index'
                                        chromosome = mutation[chromosome_number]   # Assign the element at the current index to 'chromosome'

                                        for m in range(len(chromosome)):   # Iterate over the indices of the 'chromosome' list
                                             # Create a tuple 'do_mutation' with 'mutation_type', 'chromosome_index', and the element at the current index
                                            do_mutation = (mutation_type, chromosome_index, chromosome[m])

                                            # Call the 'do_mutation' method with 'source_genome' and 'do_mutation' as arguments,
                                            # and assign the returned values to 'source_genome' and 'mutation_list'
                                            source_genome, mutation_list = self.do_mutation(source_genome, do_mutation)
                                            source_genome = source_genome[:]

                                            final_mutations.append(mutation_list)  # Append 'mutation_list' to 'final_mutations'

                             # Append 'final_mutations' to 'list_of_legal_operations'
                            list_of_operations.append(final_mutations)

                            # #remove all unapplicable intergenic regions and call intergenerator 
                            # # to insert new applicable regions for mutations to occur
                            clean_chromosome = []
                            clean_genome = []
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

                            #Call the 'mutation_legal_operations' method with 'source_genome' and 'target_genome' as arguments,
                            # and assign the returned value to 'required_mutation'
 
                            mutations, required_mutation = self.mutation_legal_operations(source_genome, target_genome)
                            if not required_mutation: # Check if there are not any required mutations'
                                break
                            switch = False  # Set 'switch' to False for the loop to terminate
                        switch = False  # Set 'switch' to False for the loop to terminate
                elif foreign_Dna_counter <= 5 or foreign_Dna_counter == 0:  # Check if the 'foreign_Dna_counter' is equal to 0
                    foreign_Dna_counter += 1   # Increment the 'foreign_Dna_counter' by 1 after each insertion
                    #Here is list of foreign DNAs where fragments are sublists
                    foreign_obj = ForeignDNA.Foreign_DNA()   # Create an instance of the 'Foreign_DNA' class
                    foreign_dna = []  # Initialize an empty list 'foreign_dna' to hold foreign DNA fragments
                    while foreign_dna == []: # Enter a while loop that continues as long as 'foreign_dna' is an empty list

                        # Call the 'foreign_dna_pool' method of the 'foreign_obj' instance with 'source_genome' and 'target_genome' as arguments,
                        # and assign the returned value to 'foreign_dna'
                        foreign_dna = foreign_obj.foreign_dna_pool(source_genome, target_genome)

                    # Get the length of the 'foreign_dna' list and subtract 1 to account for zero-based indexing
                    # Assign the result to 'foreign_dna_len'
                    foreign_dna_len = len(foreign_dna) -1

                    # Generate a random integer between 0 and 'foreign_dna_len'
                    # Assign the random integer to 'choice_foreign_dna'
                    choice_foreign_dna = randint(0, foreign_dna_len)

                    # Get the element at the index of the choice of foreign of dna' from the 'foreign_dna' list, and
                    # Assign the element to 'chosen'
                    chosen = foreign_dna[choice_foreign_dna]

                    # add foreign DNA to the source genome
                    # Call the 'insert_foreign_dna' method of the 'foreign_obj' instance with 'source_genome' and 'chosen' as arguments
                    # Assign the returned values to 'source_genome' and 'list_of_operationss'
                    source_genome, list_of_operationss = foreign_obj.insert_foreign_dna(source_genome, chosen)

                    mutation_genome = source_genome.copy()  # Create a copy of 'source_genome' and assign it to 'mutation_genome'

                    # Call the 'mutation_legal_operations' method with 'mutation_genome' and 'target_genome' as arguments
                    # Assign the returned values to 'mutations' and 'required_mutation'
                    mutations, required_mutation = self.mutation_legal_operations(mutation_genome, target_genome)
                    # print(f"REQUIRED MUTATION: {required_mutation}")
                    # if required_mutation:
                        # print("THIS HAPPPNENENNSNSNS")
                    if required_mutation:  # Check if 'mutations' is an empty list
                       
                        # Call the 'do_mutation' method with 'source_genome' and 'required_mutation' as arguments
                        # Assign the returned values to 'source_genome' and 'mutation_list'
                        source_genome, mutation_list = self.do_mutation(mutation_genome, required_mutation)
                        list_of_operations.append(mutation_list)  # Append 'mutation_list' to 'list_of_legal_operations'
                        switch = True
                        
                    else:
                        # Enter a while loop that continues while either there are mutations and 'required_mutation' is not an empty tuple,
                        # or 'required_mutation' is not an empty tuple
                        while any(mutations) and required_mutation:
                            final_mutations = []   # Initialize an empty list 'final_mutations'
                            for i in range(len(mutations)):  # Iterate over the indices of 'non_empty_mutations'
                            # Determine the 'mutation_type' based on the current index 'i'
                                if i == 0:
                                    mutation_type = 'ins'
                                elif i == 1:
                                    mutation_type = 'del'
                                else:
                                    mutation_type = 'dup'

                                mutation = mutations[i]   # Get the mutation at the current index
                               
                                for chromosome_number in range(len(mutation)):  # Iterate over the indices of 'mutation'
                                    if mutation[chromosome_number]:  # Check if the element at the current index is not an empty list
                                        chromosome_index = chromosome_number  # Assign the current index to 'chromosome_index'
                                        chromosome = mutation[chromosome_number]  # Assign the element at the current index to 'chromosome'
                                       
                                        for m in range(len(chromosome)):   # Iterate over the indices of 'chromosome'
                                        
                                        # Create a tuple 'do_mutation' with 'mutation_type', 'chromosome_index', and the element at the current index
                                            do_mutation = (mutation_type, chromosome_index, chromosome[m]) 

                                            # Call the 'do_mutation' method with 'source_genome' and 'do_mutation' as arguments
                                            # Assign the returned values to 'source_genome' and 'mutation_list'
                                            source_genome, mutation_list = self.do_mutation(mutation_genome, do_mutation)
                          
                            #remove all unapplicable intergenic regions and call intergenerator
                            clean_chromosome = []
                            clean_genome = []
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

                            # Call the 'mutation_legal_operations' method with 'source_genome' and 'target_genome' as arguments
                            # Assign the returned values to 'mutations' and 'required_mutation'
                            mutations, required_mutation = self.mutation_legal_operations(source_genome, target_genome)
                            
                            if not required_mutation:  # If a required mutation is not found, exit the loop
                                break
                        switch = False

        return list_of_operations
    
    def mutation_legal_operations(self, source_genome, target_genome):
        """
        This function decides if mutations, any mutations, or required mutations can take genome A to genome B
        checks number of chromosomes -> possibility of chromosome deletion(target chromosmes less than source)
        or chromosome insertion (source chromosome count less than target)
        Checks number of genes in chromosome for target and source -> indicators for insertion/foreign dna/deletion
        checks signed integers(genes) between target and source
        Duplication - look at the target; if two of same signed integer next to each other -> tandom duplicatio
        if two of same signed ints in chromosome but not next to each other then -> transpositional
        """
        # Create empty lists to store the modified source genome and source genome with positions
        new_source_genome = []
        new_source_genome_with_positions = []

        # Iterate over each chromosome in the source genome
        for chromosome in source_genome:
        
         # Create empty lists to store the positions with genes and the modified chromosome
            new_chromosome_positions_with_genes = []
            new_chromosome = []
            for i in range(len(chromosome)):  # Iterate over each element in the chromosome
                gene = chromosome[i]   # Get the gene at the current position
                if isinstance(gene, str) and '_' not in gene and '*' not in gene:  # Check if the gene is a string and does not contain '_' or '*'

                    new_chromosome_positions_with_genes.append((i,gene))   # Append the position and gene as a tuple to the list

            for gene in chromosome:   # Iterate over each gene in the chromosome again
                if isinstance(gene, str) and '_' not in gene and '*' not in gene: # Check if the gene is a string and does not contain '_' or '*'

                    new_chromosome.append(gene)  # Append the gene to the modified chromosome
                else:
                    new_chromosome.append(gene)

            new_source_genome.append(new_chromosome)   # Append the modified chromosome to the new_source_genome
            new_source_genome_with_positions.append(new_chromosome_positions_with_genes)  # Append the positions with genes to the new_source_genome_with_positions


        # Perform step 1: Checking genes per chromosome between the target and source genomes
        # 1.1 Find genes in the target and not in the source genome [Create a list that contains tuples of (position, gene)]

        # initialize empty list to hold insertion operations in the genome
        insertion_genome = []
        insertion_target = []
   
        for j in range(len(target_genome)): # Iterate over each chromosome in the target genome
            
            insertion_target = []   # Reset the insertion_target list for each chromosome
            if j < len(new_source_genome):
                target_chromosome = target_genome[j]
                new_chromosome = new_source_genome[j]  # Get the corresponding modified chromosome from the new_source_genome
            else:
                new_chromosome = []

                # target_chromosome = []
            # target_chromosome = target_genome[j]    # Get the chromosome from the target genome


            # Iterate over each element in the target chromosome
            for i in range(len(target_chromosome)):
                # Check if the element does not contain the character '*' and is not present in the modified chromosome 
                if ('*' not in str(target_chromosome[i])) and ((target_chromosome[i]) not in new_chromosome):
                    insertion_target.append((i,target_chromosome[i])) # Append the position and gene as a tuple to the insertion_target list
                    # print(insertion_target)
            
            insertion_genome.append(insertion_target)    # Append the insertion_target to the insertion_genome list
            print("ins:" ,insertion_genome)
            insertion_target = []
        
        #create the missing chromosomes in the source genome
        if len(target_genome) > len(source_genome):
            for m in range(len(source_genome), len(target_genome)):
                new_chromosome = target_genome[m]
                new_source_genome.append(new_chromosome)
       
        #1.2 find genes in source genome and not in target genome[Create out list that contains tuples of (position,gene)]

       
        # Create empty lists to store the deletion genome, deletion target, and occurred genes
        deletion_genome = []
        deletion_target = []

        # Check if the new_source_genome_with_positions has the same length as target_genome
        if len(target_genome) > len(new_source_genome_with_positions):
            # Append empty lists as placeholders for missing chromosomes
            diff = len(target_genome) - len(new_source_genome_with_positions)
            new_source_genome_with_positions.extend([[]] * diff)
  

        for j in range(len(target_genome)): # Iterate over each chromosome in the target genome
            new_chromosome_with_positions_source = new_source_genome_with_positions[j] # Get the chromosome with positions from the modified source genome
            if j < len(new_source_genome_with_positions):
                target_chromosome = target_genome[j]   # Get the chromosome from the target genome
            else:
                target_chromosome = []


             # Iterate over each gene with position in the modified source chromosome
            for i in range(len(new_chromosome_with_positions_source)): 
                gene_with_position = new_chromosome_with_positions_source[i]

                # Get the gene with its position
                position = gene_with_position[0]
                gene = gene_with_position[1]
                  
            # Check if the gene is not present in the target chromosome or present but at different index in the source chromosome
                if gene not in target_chromosome:
                    deletion_target.append((position, gene)) # Append the position and gene as a tuple to the deletion_target list

            # deletion_target = [(position - len([gene for _, gene in deletion_target if _ < position]), gene) for position, gene in deletion_target]
            # print(f"Deleting >>>>>> {deletion_genome} +-> {deletion_target}")
            deletion_genome.append(deletion_target)  # Append the deletion_target to the deletion_genome list
            print("del:", deletion_genome)
            deletion_target = []    # Reset the deletion_target list for the next chromosome
            
        #create chromosomes with genes from the target genome if it has more chromosomes than the source genome
        if len(target_genome) > len(new_source_genome_with_positions):
            for g in range(len(new_source_genome_with_positions), len(target_genome)):
                target_chromosome = target_genome[g]
                deletion_target = [(pos, gene) for pos, gene in enumerate(target_chromosome)]  # Add all genes in the target chromosome as deletions
                deletion_genome.append(deletion_target)  # Append the deletion_target to the deletion_genome list

        
        #step 2: duplication; check target for duplication [note position, gene and type of duplication]
       
         # Create empty lists to store the duplication genome, target duplication, and duplicated genes
        duplication_genome = []
        target_duplication = []
        duplicated_genes = []

        # Iterate over each new_chromosome in the target_genome
        for new_chromosome in target_genome: 
             # Iterate over each element in the new_chromosome
            for i in range(len(new_chromosome)): 
            # Check if the element is a string, occurs more than once in the chromosome, does not contain '*', and is not already in duplicated_genes list    
                if (isinstance(new_chromosome[i], str) and new_chromosome.count(new_chromosome[i]) > 1) and ("*" not in new_chromosome[i] and new_chromosome[i] not in duplicated_genes):
              # Check if the current gene has a tandem or transpositional duplication
                    if new_chromosome[i] == new_chromosome[i+2] or new_chromosome[i] == new_chromosome[i-2]:
                        type = "tandem"
                    else:
                        type = "transpositional"
                    
                    duplicated_genes.append(new_chromosome[i])    # Add the gene to duplicated_genes list to avoid duplication

                     # Append the information of the duplicated gene to target_duplication list
                    target_duplication.append([i, self.get_second_index(new_chromosome, new_chromosome[i]),new_chromosome[i], type]) 
                    
            duplication_genome.append(target_duplication) # Append the target duplication list to the duplication genome
            target_duplication = [] #Reset the target duplication list for the next chromosome
            duplicated_genes = [] #Reset the duplicated genes list for the next chromosome
      
        #step 2.1: check if the duplication is already present in source, if yes remove from list, otherwise cause mutation
       # Check if there are any elements in duplication_genome list
        if any(duplication_genome):
           
           # Iterate over each new_chromosome in the new_source_genome
            for j in range(len(new_source_genome)):
                new_chromosome = new_source_genome[j]
                sub = duplication_genome[j]

                # Iterate over each duplicated gene in the sub-list of duplication_genome
                for i in range(len(sub)):
                        duplicate = sub[i]
                        duplicated =  duplicate[2]
                    
                        # Check if the duplicated gene exists in the new_chromosome
                        if duplicated in new_chromosome:
                            occurances = new_chromosome.count(duplicated)

                     # Check if the duplicated gene occurs exactly twice       
                            if occurances == 2:
                                if len(sub)>1:
                    # Remove the current duplicated gene from the sub-list
                                    n_sub = sub.remove(duplicate)
                                    duplication_genome[j] = n_sub
                                else:
                     # If there is only one duplicated gene, replace the sub-list with an empty list
                                    n_sub = []
                                    duplication_genome[j] = n_sub

        #check the 3 lists and randomly pick a tuple from one of them
        do_mutation = ()
        deletion = False
        insertion = False
        duplication = False

    # Check if there are any elements in duplication_genome, deletion_genome, and insertion_genome lists
        if any(duplication_genome):
            duplication = True
        if any(deletion_genome):
            deletion = True
        if any(insertion_genome):
            insertion = True

    # Determine the mutation type based on the presence of different types of mutations
        if insertion and deletion and duplication:
        # If all three types of mutations are present
            pick = randint(0,2)
            if pick == 0:
        # Choose insertion mutation
                for i in range(len(insertion_genome)):
                    new_chromosome = insertion_genome[i]
                    if new_chromosome != []:
                        picker = randint(0, len(new_chromosome)-1)
                        do_mutation = ("ins",i, new_chromosome[picker])
                        break
            elif pick == 1:
            # Choose deletion mutation
                for i in range(len(deletion_genome)):
                    new_chromosome = deletion_genome[i]
                    if new_chromosome != []:
                        picker = randint(0, len(new_chromosome)-1)
                        do_mutation = ("del",i, new_chromosome[picker])
                        break
            elif pick == 2:
            # Choose duplication mutation
                for i in range(len(duplication_genome)):
                    new_chromosome = duplication_genome[i]
                    if new_chromosome != []:
                        picker = randint(0, len(new_chromosome)-1)
                        do_mutation = ("dup",i, new_chromosome[picker])
                        break

        elif insertion and deletion:
        # If insertion and deletion mutations are present
            pick = randint(0,1)
            if pick == 0:
            # Choose insertion mutation
                for i in range(len(insertion_genome)):
                    new_chromosome = insertion_genome[i]
                    if new_chromosome != []:
                        picker = randint(0, len(new_chromosome)-1)
                       
                        do_mutation = ("ins",i, new_chromosome[picker])
                        break
            elif pick == 1:
            # Choose deletion mutation
                for i in range(len(deletion_genome)):
                    new_chromosome = deletion_genome[i]
                    if new_chromosome != []:
                        picker = randint(0, len(new_chromosome)-1)
                      
                        do_mutation = ("del",i, new_chromosome[picker])
                        break
        
        elif deletion and duplication:
        # If deletion and duplication mutations are present
            pick = randint(0,1)
            if pick == 0:
            # Choose deletion mutation
                for i in range(len(deletion_genome)):
                    new_chromosome = deletion_genome[i]
                    if new_chromosome != []:
                        picker = randint(0, len(new_chromosome)-1)
                       
                        do_mutation = ("del",i, new_chromosome[picker])
                        break
            elif pick == 1:
            # Choose duplication mutation
                for i in range(len(duplication_genome)):
                    new_chromosome = duplication_genome[i]
                    if new_chromosome != []:
                        picker = randint(0, len(new_chromosome)-1)
                        do_mutation = ("dup",i, new_chromosome[picker])
                        break
        elif insertion and duplication:
        # If insertion and duplication mutations are present
            pick = randint(0,1)
            if pick == 0:
            # Choose insertion mutation
                for i in range(len(insertion_genome)):
                    new_chromosome = insertion_genome[i]
                    if new_chromosome != []:
                        picker = randint(0, len(new_chromosome)-1)
                      
                        do_mutation = ("ins",i, new_chromosome[picker])
                        break
            elif pick == 1:
            #If no insertion mutation was performed, move to duplication mutation
                # if "do_mutation" not in locals():
                for i in range(len(duplication_genome)):
                    new_chromosome = duplication_genome[i]
                    if new_chromosome != []:
                        picker = randint(0, len(new_chromosome)-1)
                        do_mutation = ("dup",i, new_chromosome[picker])
                        break
        elif insertion:
        # If only insertion mutation is present
            for i in range(len(insertion_genome)):
                    new_chromosome = insertion_genome[i]
                    if new_chromosome != []:
                        picker = randint(0, len(new_chromosome)-1)
                        
                        do_mutation = ("ins",i, new_chromosome[picker])
                        
                        break
    
        elif deletion:
        # If only deletion mutation is present
            for i in range(len(deletion_genome)):
                    new_chromosome = deletion_genome[i]
                    if new_chromosome != []:
                        picker = randint(0, len(new_chromosome)-1)
                        
                        do_mutation = ("del",i, new_chromosome[picker])
                        break
        elif duplication:
         # If only duplication mutation is present
            for i in range(len(duplication_genome)):
                    new_chromosome = duplication_genome[i]
                    if new_chromosome != []:
                        picker = randint(0, len(new_chromosome)-1)
                        do_mutation = ("dup",i, new_chromosome[picker])
                        break
    
        #step 3: checking if all these necessary mutations can occur at once
        #first check that insert and deletion positions dont overlap for same chromosomes, if they do then we wont be able to cause all mutations necessary
        # print("THIS COMPLETED")
        # Iterate over the deletion_genome
        for i in range(len(deletion_genome)):
            deletion_chromosome = deletion_genome[i]
            insertion_chromosome = insertion_genome[i]

             # Iterate over the deletion_chromosome
            for j in range(len(deletion_chromosome)):
                tup = deletion_chromosome[j]
                # Iterate over the insertion_chromosome
                for tup_in in insertion_chromosome:
                  # Check if the first element of the inserted tuple matches the first element of the deleted tuple
                    if tup_in[0] == tup[0]:
                     # If there is a match, return an empty list and perform the mutation
                        return [], do_mutation
                    continue 
                    #           
        #Check that intergenic regions exist for insertion, deletion, and duplication.
        # get position indexes [only] from in_genome(insertion in genome)
        #initialize empty list to hold insertion position and insertion genome
        insertion_position = []
        insertion_position_genome = []
        
        # Iterate over each new_chromosome in the insertion_genome
        for new_chromosome in insertion_genome:

        # Iterate over the elements within the new_chromosome
            for i in range(len(new_chromosome)):
                tup = new_chromosome[i]
            # Extract the first element of the tuple and add it to the insertion_position list
                insertion_position.append(tup[0])
             # Add the insertion_position list to the insertion_position_genome
            insertion_position_genome.append(insertion_position)
        
        # get position indexes [only] from out_genome(deletion in genome)
        # Initialize empty lists for deletion positions
        deletion_position_genome = []
        
        # Iterate over each new_chromosome in the deletion_genome
        for new_chromosome in deletion_genome:
         # Check if the new_chromosome is not empty
            if len(new_chromosome)> 0:
                deletion_position = []

                 # Iterate over the elements within the new_chromosome
                for i in range(len(new_chromosome)):
                    tup = new_chromosome[i]
                # Check if the length of the new_chromosome is greater than 1 and if there are more elements to compare
                    if len(new_chromosome)>1 and i < len(new_chromosome)-1:
                    # Check if the next element has a value that is one greater than the current element
                        check = new_chromosome[i+1]
                        if check[0] == tup[0]+1:
                        # If the condition is satisfied, add the current element to the deletion_position list
                            deletion_position.append(tup[0])
                            i += 1
                deletion_position_genome.append(deletion_position)  # Add the deletion_position list to the deletion_position_genome
            
        # Initialize empty lists for duplication positions
        duplication_position = []
        duplication_position_genome = []

        # Iterate over each new_chromosome in the duplication_genome
        for new_chromosome in duplication_genome:

            # Iterate over the elements within the new_chromosome
            for i in range(len(new_chromosome)):
                tup = new_chromosome[i]
            # Append the second element of the tuple to the duplication_position list
                duplication_position.append(tup[1])
            
            # Add the duplication_position list to the duplication_position_genome
            duplication_position_genome.append(duplication_position)

        # Calculate the number of applicable intergenic regions
        num_applicable_regions = 0
        applicable_region_chromosome = []
        applicable_region_genome = []

        # Iterate over each new_chromosome in the new_source_genome
        for new_chromosome in new_source_genome:
        # Iterate over the elements within the new_chromosome
            for j in range(len(new_chromosome)):

                # Check if the element is a string, its length is greater than 1, and it contains the '*' character
                if (isinstance(new_chromosome[j],str) and len(new_chromosome[j])>1 and '*' in new_chromosome[j]):
                # If the conditions are satisfied, increment the num_applicable_regions count
                    num_applicable_regions += 1
                     # Append the current position (j) to the applicable_region_chromosome
                    applicable_region_chromosome.append(j)

            # Add the applicable_region_chromosome to the applicable_region_genome
            applicable_region_genome.append(applicable_region_chromosome)
            # Reset the applicable_region_chromosome for the next new_chromosome
            applicable_region_chromosome = []

        #check number of applicable regions against number of total mutations and
        #count positions for each mutation
        insertion_count = 0
        # Iterate over each new_chromosome in the insertion_position_genome
        for new_chromosome in insertion_position_genome:
        # Iterate over the genes in the new_chromosome
            for gene in new_chromosome:
            # Increment the insertion_count for each gene
                insertion_count += 1

    
       # Count the number of deletions
        deletion_count = 0
        # Iterate over each new_chromosome in the deletion_position_genome
        for new_chromosome in deletion_position_genome:
             # Iterate over the genes in the new_chromosome
            for gene in new_chromosome:
            # Increment the deletion_count for each gene
                deletion_count += 1

        duplication_count = 0
        # Count the number of duplications
        for new_chromosome in duplication_position_genome:
        # Iterate over each new_chromosome in the duplication_position_genome
            for gene in new_chromosome:
                # Iterate over the genes in the new_chromosome
                duplication_count += 1  # Increment the duplication_count for each gene


            # Check if all the mutation lists (insertion_genome, deletion_genome, duplication_genome) have at least one element
            # If all lists have at least one element, return the mutation lists and perform the mutation
        if all(len(new_source_genome) > 0 for new_source_genome in [insertion_genome, deletion_genome, duplication_genome]):
            return [insertion_genome, deletion_genome, duplication_genome], do_mutation
        else:
            # If any of the mutation lists is empty, only perform the mutation
            return do_mutation
    
    #Function for finding second occurance of element within list
    def get_second_index(self, int_list, num):
        count = 0
         # Iterate over the elements and their indices in the int_list
        for i, n in enumerate(int_list):
        # Check if the current element is equal to the target number
            if n == num:
                count += 1
        # Check if the count is equal to 2
            if count == 2:
         # Return the index of the second occurrence of the target number
                return i
        # If the loop completes without finding the second occurrence, return -1
        else:
            return -1

    def do_mutation(self, source_genome, required_mutation):

        """
        This fuction picks a type of mutation and calls different functions (delete, duplicate, insert) to act on it
        It uses source_genome with approved intergenic regions
        It counts number of applicable intergenic regions to associate to number of mutations
        """
        # Initialize empty lists for storing mutations, genes, mutation points, and their respective genomes
        list_of_mutations = []
        list_of_genes = []
        list_of_genes_genome = []
        list_of_mutation_points = []
        list_of_mutation_points_genome = []

        # Iterate over the genes_with_intergenic_approved in the source_genome
        for genes_with_intergenic_approved in source_genome:
        # Iterate over the elements and their indices in genes_with_intergenic_approved

            for i in range(len(genes_with_intergenic_approved)):
            # Check if the current element is a string, its length is greater than 1, and it contains the '*' character
                if (isinstance(genes_with_intergenic_approved[i],str) and len(genes_with_intergenic_approved[i]) > 1) and '*' in genes_with_intergenic_approved[i]:
            # If the condition is true, append the index of the mutation point (i+1) to the list_of_mutation_points
                    if i != len(genes_with_intergenic_approved)-2:
                        list_of_mutation_points.append(i+1)
                # Check if the current element is not a string or if it is a string without the '*' character
                elif (not isinstance(genes_with_intergenic_approved[i],str)) or (isinstance(genes_with_intergenic_approved[i],str) and '*' not in genes_with_intergenic_approved[i]):
                
                 # If the condition is true, append the current element to the list_of_genes
                    list_of_genes.append(genes_with_intergenic_approved[i])
            # Append the list_of_genes and list_of_mutation_points to their respective genome lists
            list_of_genes_genome.append(list_of_genes)
            list_of_mutation_points_genome.append(list_of_mutation_points)

            # Reset the list_of_genes and list_of_mutation_points for the next iteration of genes_with_intergenic_approved
            list_of_genes = []
            list_of_mutation_points =[]

        # Extract the mutation type and chromosome index from the required_mutation list
        type = required_mutation[0]
        chromosome_index = required_mutation[1]
        actual_mutation = required_mutation[2]

        # Extract the actual_mutation from the required_mutation list
        if type == 'dup':
            position = actual_mutation[1]
            # Extract the position of the duplication from the actual_mutation
            gene_to_duplicate = actual_mutation[2]
            # Extract the gene to be duplicated from the actual_mutation
            type_of_duplication = actual_mutation[3]

             # Extract the type of duplication from the actual_mutation
            chromosome = source_genome[chromosome_index]
            # Access the chromosome in the source_genome based on the chromosome_index
            if position > len(chromosome)-1:
                position = len(chromosome)-1

            # Adjust the position if it exceeds the chromosome length, ensuring it is within bounds
            # Check for an applicable region at position -1
            if(isinstance(chromosome[position-1], str) and '*' in chromosome[position-1]) and len(chromosome[position-1])>1:
            # If the condition is true, perform the duplication operation
                mutated_chromosome = self.duplication(chromosome, gene_to_duplicate, position)
                source_genome[chromosome_index] = mutated_chromosome
                #Update the source_genome with the mutated chromosome
                #create record to keep each type of mutation/operation
                operation = {'Mut_Type': type, 'Chr': chromosome_index + 1,'Gene': gene_to_duplicate,'Pos': position,'Type of dup': type_of_duplication,'Genome after mutation': source_genome}

                # operation_str = str(operation).replace("\n", "")

                list_of_mutations.append(operation) # Append the operation to the list_of_mutations
              
                
        elif type == 'ins':
            position = actual_mutation[0]
            gene_to_insert = actual_mutation[1]

            while chromosome_index  >= len(source_genome):
                source_genome.append([])
            chromosome = source_genome[chromosome_index]   # Access the chromosome in the source_genome based on the chromosome_index
        
            # print(str(position) +"    "+str(len(chromosome))+"      " +str(chromosome)+"          "+str(chromosome_index))
            # If the position exceeds the chromosome length or the position contains '_', perform insertion at the end of the chromosome
            if position > len(chromosome)-1 or '_' in str(chromosome[position]):
                # print(str(position) +"    "+str(len(chromosome))+"      " +str(chromosome)+"          "+str(chromosome_index))
                # print("condition met")
                # sys.exit("...") 
                mutated_chromosome = self.insertion(chromosome, position, gene_to_insert, True)

                 # Perform the insertion operation and obtain the mutated chromosome
                # Create a record to keep track of the mutation operation
                operation = {'Mut_Type': type,'Chr': chromosome_index + 1,'Pos': len(chromosome)+1,'Gene': gene_to_insert,'Genome after mutation': source_genome}
                
                list_of_mutations.append(operation)   # Append the operation to the list_of_mutations
    

            elif (isinstance(chromosome[position-1], str) and '*' in chromosome[position-1]) and len(chromosome[position-1])>1:
                # print(str(position) +"    "+str(len(chromosome))+"      " +str(chromosome)+"          "+str(chromosome_index))
                # print("condition met")
                # sys.exit("...") 
                # If the condition is true, perform the insertion operation
                mutated_chromosome = self.insertion(chromosome, position-1, gene_to_insert)
                #Create a record to keep track of the mutation operation
                operation = {'Mut_Type': type,'Chr': chromosome_index + 1,'Pos': position,'Gene': gene_to_insert,'Genome after mutation': source_genome}

                list_of_mutations.append(operation)   # Append the operation to the list_of_mutations


                
               

        elif type == 'del':
          
            position = actual_mutation[0]
            gene_to_delete = actual_mutation[1]

            if chromosome_index < len(source_genome): #if the chromosome index is less than the source genome, do the deletion at the specified position
                chromosome = source_genome[chromosome_index]  # Access the chromosome in the source_genome based on the chromosome_index
           
            if position > len(chromosome)-1:
                position = len(chromosome)-1
       
            if(isinstance(chromosome[position-1], str) and '*' in chromosome[position-1]) and len(chromosome[position-1])>1:
                # If the condition is true, perform the deletion operation, and obtain the mutated chromosome.
                mutated_chromosome = self.deletion(chromosome, position)
              
               # Create a record to keep track of the mutation operation
                operation = {'Mut_Type': type,'Chr': chromosome_index + 1,'Pos': position,'Gene': gene_to_delete,'Genome after mutation': source_genome}

                # operation_str = str(operation).replace("\n", "")

                list_of_mutations.append(operation)   # Append the operation to the list_of_mutations
                    
        # Return the updated source_genome and the list_of_mutations
        return source_genome, list_of_mutations

    def insertion(self, source_chromosome, position_applicable_region, gene, larger_length=False):
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
        # if larger_length:
        #     # If larger_length is True, append the gene to the end of the chromosome
        #     source_chromosome.append(gene)
        # else:
        #     # Otherwise, replace the gene at the specified position with the new gene
        #     source_chromosome[position_applicable_region] = gene
        
        # return source_chromosome

        if larger_length:
            insertion_index = 0
            while insertion_index < len(source_chromosome) and gene > source_chromosome[insertion_index]:
                insertion_index += 1
        
            # source_chromosome.insert(insertion_index, gene)

            if insertion_index < len(source_chromosome) and gene < source_chromosome[insertion_index]:
                insertion_index += 1
                source_chromosome.insert(insertion_index, gene)
            else:
                source_chromosome.append(gene)
    

        else:
            source_chromosome[position_applicable_region] = gene
        return source_chromosome

    def deletion(self, source_chromosome, position_applicable_region):
        """
        This function deletes genes that are in the source genome but not in the target genome, so that
        the source genome can be the same as the target genome at the end of the evolutionary process.
        """
        if "_" not in source_chromosome[position_applicable_region] or '*' not in source_chromosome[position_applicable_region]:
            del source_chromosome[position_applicable_region]
            del source_chromosome[position_applicable_region-1:position_applicable_region+1]
        return source_chromosome

    def duplication(self, source_chromosome, gene_to_duplicate, insertion_position):
        """
        This function performs a duplication operation in the source genome by duplicating a gene at the specified position.
        
        Parameters:
        - source_chromosome: The source chromosome (list) where the duplication will be performed.
        - gene_to_duplicate: The gene to be duplicated.
        - insertion_position: The position in the chromosome where the duplication will be inserted.
        Returns:
        - The updated source chromosome after the duplication operation.
        """
        if "_" not in source_chromosome[insertion_position] or '*' not in source_chromosome[insertion_position]:
            # Check if the specified position is not marked with '_' or does not contain '*'
            # This condition ensures that the duplication does not occur in regions already marked for other purposes
            # Insert the gene to be duplicated at the position before the insertion_position
            source_chromosome.insert(insertion_position - 1, gene_to_duplicate)
        
        return source_chromosome



    

