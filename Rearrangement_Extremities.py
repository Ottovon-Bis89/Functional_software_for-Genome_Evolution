class Extremities:


    def __init__(self):

        pass


    def gene_extremities(self, genome):
        # Initialize an empty list to store the new genome with gene extremities
        genome_gene_extremities = []
            
        # Loop over each chromosome in the genome
        for chromosome in genome:
            # Initialize an empty list to store the new chromosome with gene extremities
            chromosome_gene_extremities = []
                
            # Loop over each marker in the chromosome
            for marker in chromosome:
                # If the marker is non-negative, add two new markers: one equal to the original marker, and one equal to the original marker plus 0.5
                if marker >= 0:
                    chromosome_gene_extremities.extend([marker, marker + 0.5])
                # If the marker is negative, add two new markers: one equal to the absolute value of the original marker plus 0.5, and one equal to the absolute value of the original marker
                else:
                    chromosome_gene_extremities.extend([abs(marker) + 0.5, abs(marker)])
                
            # Add the new chromosome with gene extremities to the new genome
            genome_gene_extremities.append(chromosome_gene_extremities)
            
        # Return the new genome with gene extremities
        return genome_gene_extremities
    
    def create_adjacency_list(self, genome):
        # Call the gene_extremities method to obtain a list of gene extremities for the input genome
        gene_extremities = self.gene_extremities(genome)
        
        # Initialize an empty list to store the adjacency tuples
        adjacencies = []
        
        # Loop over each chromosome in the gene extremities list
        for chromosome in gene_extremities:
            # Initialize the index variable to 0
            i = 0
            
            # Loop over each marker in the chromosome
            while i < len(chromosome):
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
    
    def adjacencies_ordered_and_sorted(self, genome):
        # Call the create_adjacency_list method to obtain a list of adjacencies for the input genome
        adjacencies = self.create_adjacency_list(genome)
        
        # Initialize empty lists to store sorted adjacencies and telomeres
        sorted_adjacencies = []
        telomeres = []
        
        # Loop over each element in the adjacencies list
        for element in adjacencies:
            # If the element is a tuple, add it to the adjs list after sorting the tuple elements
            if type(element) is tuple:
                if int(element[0]) < int(element[1]):
                    sorted_adjacencies.append(element)
                else:
                    sorted_adjacencies.append((element[1], element[0]))
            # If the element is not a tuple, add it to the telomeres list
            else:
                telomeres.append(element)
        
        # Sort the adjacency tuples in ascending order and append them to the sorted telomeres list
        sorted_adjacencies.sort()
        sorted_adjacencies = telomeres + sorted_adjacencies
        
        # Return the sorted adjacency list
        return sorted_adjacencies
    
    def find_next_extremity(self, current, next_extremity):
        # Determine which element of the current extremity tuple is the next extremity to be reached
        if current[0] == next_extremity:
            next_index = 1
        else:
            next_index = 0
        
        # Determine the value of the next extremity based on whether the current extremity element is an integer or not
        if int(current[next_index]) == current[next_index]:
            next_value = current[next_index] + 0.5
        else:
            next_value = current[next_index] - 0.5
        
        # Return the value of the next extremity
        return next_value

    def find_next_adjacency(self, next_extremity, chromosome, not_telomeres):
        # iterate over each element in not_telomeres along with its index
        for i, element in enumerate(not_telomeres):
            # if either the start or end of the element is the next extremity
            if element[0] == next_extremity or element[1] == next_extremity:
                # set the current adjacency to the element
                current = element
                # add the current adjacency to the chromosome
                chromosome.append(current)
                # remove the current element from not_telomeres based on its index
                not_telomeres.pop(i)
                # update the next extremity to be the end of the current adjacency
                next_extremity = Extremities.find_next_extremity(self, current, next_extremity)
                # return the updated values of next extremity, chromosome, and not_telomeres
                return next_extremity, chromosome, not_telomeres
        # if no adjacent element was found, return the current next extremity
        return next_extremity
    

    def find_adjacency_cycle(self, next_extremity, chromosome, not_telomeres):
        # Find the next adjacency in the cycle
        next_adjacency = Extremities.find_next_adjacency(self, next_extremity, chromosome, not_telomeres)

        # Keep finding adjacencies until there is only one extremity left in the cycle
        while len(next_adjacency) != 1:
            next_extremity = next_adjacency[0]
            next_adjacency = Extremities.find_next_adjacency(self, next_extremity, chromosome, not_telomeres)

        # If there is only one extremity left, return it along with the current chromosome and not_telomeres
        else:
            next_extremity = next_adjacency[0]
            return next_extremity, chromosome, not_telomeres
        

    def find_chromosomes(self, adjacencies):
        # Separate telomeres and not telomeres
        telomeres = [element for element in adjacencies if not isinstance(element, tuple)]
        not_telomeres = [element for element in adjacencies if isinstance(element, tuple)]

        # Initialize output lists
        linear_chromosomes = []
        circular_chromosomes = []

        # Find linear chromosomes
        while telomeres:
            # Initialize a new chromosome
            chromosome = [telomeres.pop(0)]

            # Get the next extremity
            if chromosome[0] % 1 == 0:
                next_extremity = chromosome[0] + 0.5
            else:
                next_extremity = chromosome[0] - 0.5

            # If single gene chromosome, append to the output list
            if next_extremity in telomeres:
                chromosome.append(telomeres.pop(telomeres.index(next_extremity)))
                linear_chromosomes.append(chromosome)

            # Else find adjacency cycle
            else:
                adjacency_cycle = Extremities.find_adjacency_cycle(self, next_extremity, chromosome, not_telomeres)
                next_extremity = adjacency_cycle[0]
                while next_extremity not in telomeres:
                    chromosome.extend(adjacency_cycle[1])
                    adjacency_cycle = Extremities.find_adjacency_cycle(self, next_extremity, chromosome, not_telomeres)
                    next_extremity = adjacency_cycle[0]
                chromosome.extend(adjacency_cycle[1])
                chromosome.append(telomeres.pop(telomeres.index(next_extremity)))
                linear_chromosomes.append(chromosome)

        # Find circular chromosomes
        while not_telomeres:
            # Initialize a new chromosome
            chromosome = [not_telomeres.pop(0)]

            # Get the next extremity
            if chromosome[0][0] % 1 == 0:
                next_extremity = chromosome[0][0] + 0.5
            else:
                next_extremity = chromosome[0][0] - 0.5

            # If single gene chromosome, append to the output list
            if next_extremity == chromosome[0][1]:
                circular_chromosomes.append(chromosome)

            # Else find adjacency cycle
            else:
                adjacency_cycle = Extremities.find_adjacency_cycle(self, next_extremity, chromosome, not_telomeres)
                next_extremity = adjacency_cycle[0]
                while next_extremity != chromosome[0][1]:
                    chromosome.extend(adjacency_cycle[1])
                    adjacency_cycle = Extremities.find_adjacency_cycle(self, next_extremity, chromosome, not_telomeres)
                    next_extremity = adjacency_cycle[0]
                chromosome.extend(adjacency_cycle[1])
                circular_chromosomes.append(chromosome)

        return linear_chromosomes, circular_chromosomes


    def adjacencies_to_genome(self, adjacencies):
        genome = []  # initialize genome as empty list
        chromosomes = Extremities.find_chromosomes(self, adjacencies)  # get list of chromosomes
        linear_chromosomes = chromosomes[0]  # separate linear chromosomes
        circular_chromosomes = chromosomes[1]  # separate circular chromosomes

        # iterate over linear chromosomes
        for chromosome in linear_chromosomes:
            chrom = []  # initialize chromosome as empty list
            gene = 0  # initialize gene as 0
            chromosome_length = len(chromosome)  # get length of chromosome

            # iterate over adjacencies in chromosome
            for i in range(0, chromosome_length - 1):

                if i == 0:  # if first adjacency in chromosome
                    gene = chromosome[i]
                    if gene % 1 == 0:
                        chrom.append(int(gene))  # append gene to chromosome
                    else:
                        chrom.append(-int(gene))  # append negative gene to chromosome

                else:  # if not first adjacency
                    if int(gene) == int(chromosome[i][0]):  # if gene matches first extremity in adjacency
                        gene = chromosome[i][1]  # set gene to second extremity in adjacency
                    else:
                        gene = chromosome[i][0]  # set gene to first extremity in adjacency

                    if gene % 1 == 0:
                        chrom.append(int(gene))  # append gene to chromosome
                    else:
                        chrom.append(-int(gene))  # append negative gene to chromosome

            genome.append(chrom)  # append chromosome to genome

        # iterate over circular chromosomes
        for chromosome in circular_chromosomes:
            chrom = ['o']  # initialize chromosome with origin gene
            gene = []  # initialize gene as empty list
            chromosome_length = len(chromosome)  # get length of chromosome

            # iterate over adjacencies in chromosome
            for i in range(0, chromosome_length):
                if i == 0:  # if first adjacency in chromosome
                    gene = chromosome[i][0]
                    if gene % 1 == 0:
                        chr.append(int(gene))  # append gene to chromosome
                    else:
                        chrom.append(-int(gene))  # append negative gene to chromosome

                else:  # if not first adjacency
                    if int(gene) == int(chromosome[i][0]):  # if gene matches first extremity in adjacency
                        gene = chromosome[i][1]  # set gene to second extremity in adjacency
                    else:
                        gene = chromosome[i][0]  # set gene to first extremity in adjacency

                    if gene % 1 == 0:
                        chrom.append(int(gene))  # append gene
                    else:
                        chrom.append(-int(gene)) # append negative gene to chromosome
            genome.append(chrom) # append chromosome to genome
        return genome # return genome




