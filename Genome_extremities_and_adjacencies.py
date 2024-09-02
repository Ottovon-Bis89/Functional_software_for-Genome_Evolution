class Extremities_and_adjacencies:
    
    def __init__(self):
        pass

    def gene_extremities(self, genome):
        """
        Generates a list of gene extremities for each chromosome in the given genome.

        Parameters:
        - genome (list): A list of chromosomes, where each chromosome is represented as a list of markers.

        Returns:
        - list: A list of gene extremities for each chromosome in the genome. 
                Each chromosome's gene extremities are represented as a list of numeric values.
        """
        genome_gene_extremities = []
        
        # Iterate over each chromosome in the genome
        for chromosome in genome:
            chromosome_gene_extremities = []

            # Process each marker in the chromosome
            for marker in chromosome:
                if isinstance(marker, str) and '_' in marker:  # Skip special string markers
                    continue
                try:
                    # Convert marker to integer
                    marker_int = int(marker)
                    if marker_int >= 0:
                        chromosome_gene_extremities.append(marker_int)
                        chromosome_gene_extremities.append(marker_int + 0.5)
                    else:
                        chromosome_gene_extremities.append(abs(marker_int) + 0.5)
                        chromosome_gene_extremities.append(abs(marker_int))
                except ValueError:
                    # Handle cases where the marker cannot be converted to an integer
                    print(f"Marker cannot be converted to int: {marker}")
                    continue
            
            # Append the gene extremities for this chromosome
            genome_gene_extremities.append(chromosome_gene_extremities)
        
        return genome_gene_extremities

    def create_adjacency_list(self, genome):
        """
        Creates an adjacency list based on the given genome.

        Parameters:
        - genome (list): A list representing the genome.

        Returns:
        - list: An adjacency list representing the relationships between elements in the genome.
        """
        adjacencies = []
        
        # Get gene extremities for the genome
        gene_extremities = self.gene_extremities(genome)

        # Iterate over each chromosome's gene extremities
        for chromosome in gene_extremities:
            i = 0
            while i < len(chromosome):
                # If element is the first or last in the chromosome, it is a telomere
                if i == 0 or i == len(chromosome) - 1:
                    adjacencies.append(chromosome[i])
                    i += 1
                else:
                    # Otherwise, add adjacent pairs as tuples
                    adjacencies.append((chromosome[i], chromosome[i + 1]))
                    i += 2
        
        return adjacencies

    def ordered_and_sorted_adjacencies(self, genome):
        """
        Retrieves the ordered and sorted list of adjacencies from the given genome.

        Parameters:
        - genome (list): The genome for which adjacencies are to be retrieved.

        Returns:
        - list: A sorted list of adjacencies, including telomeres.
        """
        adjacencies = self.create_adjacency_list(genome)
        adjacency_list = []
        telomeres = []
        
        # Separate telomeres and adjacencies
        for element in adjacencies:
            if isinstance(element, tuple):
                adjacency_list.append((min(element), max(element)))
            else:
                telomeres.append(element)

        # Sort both lists and combine
        adjacency_list.sort()
        telomeres.sort()

        # Return the combined sorted list of telomeres and adjacencies
        return telomeres + adjacency_list

    def find_next_extremity(self, current, next_extremity):
        """
        Finds the next extremity based on the current extremity and a specified next extremity.

        Parameters:
        - current (tuple): The current extremity represented as a tuple (x, y).
        - next_extremity: The specified next extremity.

        Returns:
        - next_extremity: The next extremity calculated based on the input parameters.
        """
        # Check the next extremity based on current extremity's first or second element
        if current[0] == next_extremity:
            return current[1] + 0.5 if current[1] % 1 == 0 else current[1] - 0.5
        else:
            return current[0] + 0.5 if current[0] % 1 == 0 else current[0] - 0.5

    def find_next_adjacency(self, next_extremity, chromosome, not_telomeres):
        """
        Find the next adjacency based on the next extremity in the 'not_telomeres' list.

        Parameters:
        - next_extremity: The current extremity.
        - chromosome: The current chromosome list.
        - not_telomeres: The list of non-telomeric adjacencies.

        Returns:
        - tuple: Updated next_extremity, chromosome, and not_telomeres.
        """
        for element in not_telomeres:
            if element[0] == next_extremity or element[1] == next_extremity:
                chromosome.append(element)
                not_telomeres.remove(element)
                next_extremity = self.find_next_extremity(element, next_extremity)
                return next_extremity, chromosome, not_telomeres
        return next_extremity,

    def find_adjacency_cycle(self, next_extremity, chromosome, not_telomeres):
        """
        Find an adjacency cycle starting from the given 'next_extremity'.

        Parameters:
        - next_extremity: The starting extremity.
        - chromosome: The current chromosome list.
        - not_telomeres: List of non-telomeric adjacencies.

        Returns:
        - tuple: Updated next_extremity, chromosome, and not_telomeres.
        """
        while True:
            result = self.find_next_adjacency(next_extremity, chromosome, not_telomeres)
            if len(result) == 1:
                return result[0], chromosome, not_telomeres
            next_extremity = result[0]

    def find_chromosomes(self, adjacencies):
        """
        Find linear and circular chromosomes from a list of adjacencies.

        Parameters:
        - adjacencies (list): A list of adjacencies representing chromosomes.

        Returns:
        - tuple: Two lists: linear_chromosomes and circular_chromosomes.
        """
        telomeres = [element for element in adjacencies if not isinstance(element, tuple)]
        not_telomeres = [element for element in adjacencies if isinstance(element, tuple)]

        linear_chromosomes, circular_chromosomes = [], []
        chromosome = []

        # Handle linear chromosomes
        while telomeres:
            current = telomeres.pop(0)
            chromosome.append(current)
            next_extremity = current + 0.5 if current % 1 == 0 else current - 0.5

            if next_extremity in telomeres:
                telomeres.remove(next_extremity)
                chromosome.append(next_extremity)
                linear_chromosomes.append(chromosome)
            else:
                next_extremity, chromosome, not_telomeres = self.find_adjacency_cycle(next_extremity, chromosome, not_telomeres)
                if next_extremity in telomeres:
                    telomeres.remove(next_extremity)
                    chromosome.append(next_extremity)
                    linear_chromosomes.append(chromosome)
            chromosome = []

        # Handle circular chromosomes
        while not_telomeres:
            current = not_telomeres.pop(0)
            chromosome.append(current)
            next_extremity = current[0] + 0.5 if current[0] % 1 == 0 else current[0] - 0.5

            if next_extremity == current[1]:
                circular_chromosomes.append(chromosome)
            else:
                next_extremity, chromosome, not_telomeres = self.find_adjacency_cycle(next_extremity, chromosome, not_telomeres)
                if next_extremity == chromosome[0][1]:
                    circular_chromosomes.append(chromosome)
            chromosome = []

        return linear_chromosomes, circular_chromosomes

    def find_genome(self, adjacencies):
        """
        Finds the genome from the given adjacencies.

        Parameters:
        - adjacencies (list): A list of adjacencies representing chromosomes.

        Returns:
        - list: The reconstructed genome.
        """
        genome = []
        linear_chromosomes, circular_chromosomes = self.find_chromosomes(adjacencies)

        # Process linear chromosomes
        for chromosome in linear_chromosomes:
            chrom = []
            gene=0
            chromosome_length = len(chromosome)

            for i in range(0, chromosome_length-1):

                if i==0:
                    gene = chromosome[i]
                    if gene%1 == 0:
                        chrom.append(int(gene))
                    else:
                        chrom.append(-int(gene))
                # Handling the tuple case for gene selection
                else:
                    if int(gene) == int(chromosome[i][0]):
                        gene=chromosome[i][1]
                    else:
                        gene = chromosome[i][0]

                if isinstance(gene, (int, float)):
                    if gene % 1 == 0:
                        chrom.append(int(gene))
                    else:
                        chrom.append(-int(gene))
                else:
                    # Handle unexpected non-numeric gene values (e.g., error handling, logging, etc.)
                    raise ValueError(f"Unexpected gene type: {type(gene)} in chromosome {chromosome}")

            genome.append(chrom)


        # Process circular chromosomes
        for chromosome in circular_chromosomes:
            chrom = []
            gene = None
            chromosome_length = len(chromosome)

            # Start with the 'o' indicating a circular chromosome
            chrom.append('o')
            
            for i in range(chromosome_length):
                if i == 0:
                    gene = chromosome[i][0]
                else:
                    # Compare the current gene with the last gene to decide the next gene
                    if int(gene) == int(chromosome[i][0]):
                        gene = chromosome[i][1]
                    else:
                        gene = chromosome[i][0]

                # Ensure gene is numeric and apply integer conversion logic
                if isinstance(gene, (int, float)):
                    if gene % 1 == 0:
                        chrom.append(int(gene))
                    else:
                        chrom.append(-int(gene))
                else:
                    raise ValueError(f"Unexpected gene type: {type(gene)} in chromosome {chromosome}")

            genome.append(chrom)

        return genome
