class Gene_extremities:

    def __init__(self):

        pass

    def gene_extremities(self, genome):
        # Initialize an empty list to store the new genome with gene extremities
        genome_gene_extremities = []
        # Loop over each chromosome in the genome
        for chromosome in genome:
            chromosome_gene_extremities = [] # Initialize an empty list to store the new chromosome with gene extremities
            for marker in chromosome:   # Loop over each marker in the chromosome
                 # If the marker is non-negative, add two new markers: one equal to the original marker, and one equal to the original marker plus 0.5
                if int(marker) >= 0: 
                    chromosome_gene_extremities.append(marker)
                    chromosome_gene_extremities.append(marker + 0.5)
                # If the marker is negative, add two new markers: one equal to the absolute value of the original marker plus 0.5, and one equal to the absolute value of the original marker
                else:
                    chromosome_gene_extremities.append(abs(marker) + 0.5)
                    chromosome_gene_extremities.append(abs(marker))
             # Add the new chromosome with gene extremities to the new genome
            genome_gene_extremities.append(chromosome_gene_extremities)
        # Return the new genome with gene extremities
        return genome_gene_extremities

    def create_adjacency_list(self, genome):
        adjacencies = [] #Initialize an empty list to store the new gene adjacency tuples
        # Call the gene_extremities method to obtain a list of gene extremities for the input genome
        gene_extremities = Gene_extremities.gene_extremities(self, genome)
         # Loop over each chromosome in the gene extremities list
        for chromosome in gene_extremities:
            i = 0    # Initialize the index variable to 0
            while i < len(chromosome):   # Loop over each marker in the chromosome
                # If the marker is at the beginning or end of the chromosome, add a single marker adjacency tuple
                if chromosome[i] == chromosome[0] or chromosome[i] == chromosome[-1]: 
                    adjacencies.append((chromosome[i]))
                    i += 1
                # If the markers are adjacent on the chromosome, add a double marker adjacency tuple
                else:
                    adjacencies.append((chromosome[i], chromosome[i + 1]))
                    i += 2
        # Return the list of adjacency tuples
        return adjacencies


    def ordered_and_sorted_adjacencies(self, genome):
        # Call the create_adjacency_list method to obtain a list of adjacencies for the input genome
        adjacencies = Gene_extremities.create_adjacency_list(self, genome)
        # Initialize empty lists to store sorted adjacencies and telomeres
        sorted_adjacencies = []
        telomeres = []
         # Loop over each element in the adjacencies list
        for element in adjacencies:
          # If the element is a tuple, add it to the adjacencies list after sorting the tuple elements
            if type(element) is tuple:
                if int(element[0]) < int(element[1]):     # Check if the first element of current is an integer (has no fractional part) and greater than the second element
                    sorted_adjacencies.append(element)       #append the element to the sorted adjacencies list
                else:
                    sorted_adjacencies.append((element[1], element[0]))
            # If the element is not a tuple, add it to the telomeres list
            else:
                telomeres.append(element)
         # Sort the adjacency tuples in ascending order and append them to the sorted telomeres list
        sorted_adjacencies.sort()
        telomeres.sort()
        sorted_Adjacencies = telomeres + sorted_adjacencies

        # Return the sorted adjacency list
        return sorted_Adjacencies



    def find_next_extremity(self, current, next_extremity):
         # Determine which element of the current extremity tuple is the next extremity to be reached
        if current[0] == next_extremity:  
        # Determine the value of the next extremity based on whether the current extremity element is an integer or not
            if current[1] % 1 == 0:
                next = current[1] + 0.5  #If current is an integer, set next_extremity as current + 0.5
            else:
                next = current[1] - 0.5  # If current is not an integer, set next_extremity as current - 0.5
         # Check if the first element of current is an integer (has no fractional part)
        else:
            if current[0] % 1 == 0: 
                next = current[0] + 0.5   #If current is an integer, set next_extremity as current + 0.5
            else:
                next = current[0] - 0.5    # If current is not an integer, set next_extremity as current - 0.5

        #return the next extremity
        return next

    def find_next_adjacency(self, next_extremity, chromosome, not_telomeres):
        # iterate over each element in not_telomeres along with its index
        for element in not_telomeres:  
         # if either the start or second element is the next extremity
            if element[0] == next_extremity or element[1] == next_extremity:
                current = element
            # add the current adjacency to the chromosome
                chromosome.append(current)
                not_telomeres.remove(current)  # remove the current element from not_telomeres based on its index
                 # update the next extremity to be the end of the current adjacency
                next_extremity = Gene_extremities.find_next_extremity(self, current, next_extremity)  

                return next_extremity, chromosome, not_telomeres    # return the updated values of next extremity, chromosome, and not_telomeres
        return [next_extremity]   # if no adjacent element was found, return the current next extremity



    def find_adjacency_cycle(self, next_extremity, chromosome, not_telomeres):
        # Find the next adjacency in the cycle
        next_adjacency = Gene_extremities.find_next_adjacency(self, next_extremity, chromosome, not_telomeres)

        # Loop until the length of next_adjacency is not equal to 1
        while len(next_adjacency) != 1:

            next_extremity = next_adjacency[0]   # Set next_extremity as the first element of next_adjacency

         # Find the next adjacency based on next_extremity
            next_adjacency = Gene_extremities.find_next_adjacency(self, next_extremity, chromosome, not_telomeres)

        # If the length of next_adjacency becomes 1
        else:
            next_extremity = next_adjacency[0]   # Set next_extremity as the first element of next_adjacency

            # Return the values of next_extremity, chromosome, and not_telomeres
            return next_extremity, chromosome, not_telomeres 

    def find_chromosomes(self, adjacencies):
         # Separate telomeres and not telomeres
        telomeres = [element for element in adjacencies if type(element) is not tuple]
        not_telomeres = [element for element in adjacencies if type(element) is tuple]

         # Initialize output lists for chromosome, linear chromosome and circular chromosome
        linear_chromosomes = []
        circular_chromosomes = []
        chromosome = []
        i = 0

        # Find linear chromosomes from the telomeres list
        # Loop until the length of telomeres is greater than 0
        while len(telomeres) > 0:

            i += 1    # Increment the counter i
            current = telomeres[0]  # Get the first element from the telomeres list

            telomeres.remove(current)  # Remove the current element from the telomeres list
            chromosome.append(current)  # Append the current element to the chromosome list

            # Get the next extremity
            if current % 1 == 0:   # Check if the current value is an integer (has no fractional part)
                next_extremity = current + 0.5   # If current is an integer, set next_extremity as current + 0.5
            else:
                next_extremity = current - 0.5   # If current is not an integer, set next_extremity as current - 0.5

           # If single gene chromosome, check if its linear or circular chromosome
            if next_extremity in telomeres:  # Check if next_extremity is present in the telomeres list
                current = next_extremity     # Set current as next_extremity

                telomeres.remove(current)    # Remove the current element from the telomeres list
                chromosome.append(current)   # Append the current element to the chromosome list
                linear_chromosomes.append(chromosome)  # Append the current chromosome to the linear_chromosomes list
                chromosome = []  # Reset the chromosome list to an empty list

           # If next_extremity is not present in the telomeres list, find the adjacency cycle
            else:
                adjacency_cycle = Gene_extremities.find_adjacency_cycle(self, next_extremity, chromosome, not_telomeres)
                next_extremity = adjacency_cycle[0]   # Update next_extremity with the first element of the adjacency cycle

                if next_extremity in telomeres:  # Check if the updated next_extremity is present in the telomeres list
                    current = next_extremity     # Set current as next_extremity
                    telomeres.remove(current)    # Remove the current element from the telomeres list
                    chromosome.append(current)   # Append the current element to the chromosome list
                    linear_chromosomes.append(chromosome)   # Append the current chromosome to the linear_chromosomes list
                    chromosome = []  # Reset the chromosome list to an empty list

        # Find circular chromosomes from the not telomeres list
        while len(not_telomeres) > 0: #Loop until the length of not_telomeres is greater than 0
            current = not_telomeres[0]  # Get the first element from the not_telomeres list
            not_telomeres.remove(current)  # Remove the current element from the not_telomeres list
            chromosome.append(current)     # Append the current element to the chromosome list

          # Check if the first element of current is an integer (has no fractional part)
            if current[0] % 1 == 0:
                next_extremity = current[0] + 0.5   # If the first element is an integer, set next_extremity as current[0] + 0.5
            else:
                next_extremity = current[0] - 0.5    # If the first element is not an integer, set next_extremity as current[0] - 0.5

            # If single gene chromosome, check if it is a circular chromosome.
            if next_extremity == current[1]:   # Check if next_extremity is equal to the second element of current
                circular_chromosomes.append(chromosome)  # Append the current chromosome to the circular_chromosomes list
                chromosome = []  # Reset the chromosome list to an empty list

           # If next_extremity is not equal to the second element of current, find adjacency cycle
            else:
            # Find the adjacency cycle based on next_extremity, chromosome, and not_telomeres
                adjacency_cycle = Gene_extremities.find_adjacency_cycle(self, next_extremity, chromosome, not_telomeres)
                next_extremity = adjacency_cycle[0]  # Update next_extremity with the first element of the adjacency cycle

                # if at end of circular chromosome, Check if next_extremity is equal to the second element of the first gene in the chromosome
                if next_extremity == chromosome[0][1]:  

                    circular_chromosomes.append(chromosome)  # Append the current chromosome to the circular_chromosomes list
                    chromosome = []  # Reset the chromosome list to an empty list

        # Return the linear_chromosomes and circular_chromosomes lists
        return linear_chromosomes, circular_chromosomes


    def find_genome(self, adjacencies):
        genome = []   # initialize genome as empty list

        # Find chromosomes using the Extremities_and_adjacencies class and store the results in the 'chromosomes' variable
        chromosomes = Gene_extremities.find_chromosomes(self, adjacencies)

        # Separate the linear_chromosomes and circular_chromosomes from the 'chromosomes' variable
        linear_chromosomes = chromosomes[0]
        circular_chromosomes = chromosomes[1]

        # Iterate over each chromosome in the linear_chromosomes list
        for chromosome in linear_chromosomes:
            chrom = []   # Create an empty list to store the transformed chromosome
            gene = 0     # initialize gene variable as 0
            chromosome_length = len(chromosome)  # get length of chromosome

            for i in range(chromosome_length - 1):  # Iterate over the range of indices from 0 to chromosome_length - 1

                if i == 0:  # Check if the current index is 0
                    gene = chromosome[i]  # Get the gene value from the chromosome at index i

                    if gene % 1 == 0: # Check if the gene is an integer (has no fractional part)
                        chrom.append(int(gene))  # If the gene is an integer, append its integer value to the 'chrom' list
                    
                    # If the gene is not an integer, append its negative integer value to the 'chrom' list
                    else:
                        chrom.append(-int(gene))  

                else:  # If the current index is not 0
                
                    # Check if the integer value of the gene matches the first element of the gene pair at index i in the chromosome
                    if int(gene) == int(chromosome[i][0]):

                        gene = chromosome[i][1]  # If it matches, update the gene with the second element of the gene pair
                    else:
                        gene = chromosome[i][0]   # If it doesn't match, update the gene with the first element of the gene pair

                    
                    # Check if the gene is an integer (has no fractional part)
                    if gene % 1 == 0:
                        chrom.append(int(gene))  # If the gene is an integer, append its integer value to the 'chrom' list
                    else:
                        chrom.append(-int(gene))  # If the gene is not an integer, append its negative integer value to the 'chrom' list

            genome.append(chr)  # Append the 'chrom' list to the 'genome' list

        # Iterate over each chromosome in the circular_chromosomes list
        for chromosome in circular_chromosomes: 
            chrom = []   # Create an empty list to store the transformed chromosome
            gene = []    #Initialize the gene variable as an empty list
            chromosome_length = len(chromosome)  # get length of current chromosome

            # iterate over adjacencies in chromosome
            chr.append('o')  # Append 'o' to represent a circular chromosome
            for i in range(0, chromosome_length):   # Iterate over the range of indices from 0 to chromosome_length

                if i == 0:  # Check if the current index is 0
                    gene = chromosome[i][0]  # Get the first gene from the gene pair at index i in the chromosome
                    if gene % 1 == 0:  # Check if the gene is an integer (has no fractional part)
                        chrom.append(int(gene))   # If the gene is an integer, append its integer value to the 'chrom' list
                    else:
                        chrom.append(-int(gene))

                # Check if the integer value of the gene matches the first element of the gene pair at index i in the chromosome
                else:
                    if int(gene) == int(chromosome[i][0]): 

                        gene = chromosome[i][1]   # If it matches, update the gene with the second element of the gene pair
                    else:
                        gene = chromosome[i][0]  # If it doesn't match, update the gene with the first element of the gene pair

                    if gene % 1 == 0:  # Check if the gene is an integer (has no fractional part)
                        chrom.append(int(gene))  # If the gene is an integer, append its integer value to the 'chrom' list
                    else:
                        chrom.append(-int(gene))   # If the gene is not an integer, append its negative integer value to the 'chrom' list

            genome.append(chrom)   # Append the 'chrom' list to the 'genome' list
            
         # Append the 'chrom' list to the 'genome' list
        return genome
