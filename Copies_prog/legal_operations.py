from random import randint
import sys
import math 
class MutationOperations:

    def __init__(self):

        self.state = []
        

    def mutation_legal_operations(self, source_genome, target_genome):
        """
        This function decides if a series of different mutations can take genome A to genome B.

        Args:
        source_genome (list): The source genome.
        target_genome (list): The target genome.

        Returns:
        tuple: A tuple containing either lists of mutation data (insertion, deletion, duplication) or a single mutation operation.
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
                new_chromosome = new_source_genome[j]  # Get the corresponding chromosome (that is cleaned of intergenic regions) from the new_source_genome
            else:
                new_chromosome = []
                # target_chromosome = []
            target_chromosome = target_genome[j]    # Get the chromosome from the target genome


            # Iterate over each element in the target chromosome
            for i in range(len(target_chromosome)):
                # Check if the element does not contain the character '*' and is not present in the modified chromosome 
                if ('*' not in str(target_chromosome[i])) and ((target_chromosome[i]) not in new_chromosome):
                    insertion_target.append((i,target_chromosome[i])) # Append the position and gene as a tuple to the insertion_target list
            
            insertion_genome.append(insertion_target)    # Append the insertion_target to the insertion_genome list
            # print("ins:" ,insertion_genome)
            insertion_target = []
        
        #create the missing chromosomes in the source genome
        if len(target_genome) > len(source_genome):
            for missing_chromosome in range(len(source_genome), len(target_genome)):
                new_chromosome = target_genome[missing_chromosome]
                new_source_genome.append(new_chromosome)
       
        #1.2 find genes in source genome and not in target genome[Create out list that contains tuples of (position,gene)]

       
        # Create empty lists to store the deletion genome, deletion target, and occurred genes
        deletion_genome = []
        deletion_target = []

        # Check if the new_source_genome_with_positions has the same length as target_genome
        if len(target_genome) > len(new_source_genome_with_positions):
            # Append empty lists as placeholders for missing chromosomes
            difference = len(target_genome) - len(new_source_genome_with_positions)
            new_source_genome_with_positions.extend([[]] * difference)
  

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
                 # Append the position and gene as a tuple to the deletion_target list
                if gene not in target_chromosome:
                    deletion_target.append((position, gene))
                # elif position != target_chromosome.index(gene):
                #     deletion_target.append((position, gene))

            
            deletion_genome.append(deletion_target)  # Append the deletion_target to the deletion_genome list
                # print("del:" ,deletion_genome)
            deletion_target = []    # Reset the deletion_target list for the next chromosome
                
        #create chromosomes with genes from the target genome if it has more chromosomes than the source genome
        if len(target_genome) > len(new_source_genome_with_positions):
            for gene_target in range(len(new_source_genome_with_positions), len(target_genome)):
                target_chromosome = target_genome[gene_target]
                deletion_target = [(position, gene) for position, gene in enumerate(target_chromosome)]  # Add all genes in the target chromosome as deletions
                deletion_genome.append(deletion_target)  # Append the deletion_target to the deletion_genome list

        
        #step 2: duplication; check target for duplication [note position, gene and type of duplication]
       
         #Create empty lists to store the duplication genome, target duplication, and duplicated genes
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
        
    def get_second_index(self, int_list, num):

        #Function for finding second occurance of element within list
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
        
    