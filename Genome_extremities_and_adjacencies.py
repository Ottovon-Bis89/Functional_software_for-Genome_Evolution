class Extremities_and_adjacencies:

    def __init__(self):

        pass

    def gene_extremities(self, genome):
        '''
        Generates a list of gene extremities for each chromosome in the given genome.

        Parameters:
        - genome (list): A list of chromosomes, where each chromosome is represented as a list of markers.

        Returns:
        list: A list of gene extremities for each chromosome in the genome. Each chromosome's gene extremities
              are represented as a list of numeric values.

        Algorithm:
        1. Initialize an empty list `genome_gene_extremities` to store gene extremities for each chromosome.
        2. Iterate through each chromosome in the genome.
            a. Initialize an empty list `chromosome_gene_extremities` to store gene extremities for the current chromosome.
            b. Iterate through each marker in the chromosome.
                i. If the marker is an integer and greater than or equal to 0, add (marker_int + 0.5) to the gene extremities.
                ii. If the marker  does not meet the first condtion, add (abs(marker_int) + 0.5) to the gene extremities.
            c. Add the gene extremities for the current chromosome to `genome_gene_extremities`.
        3. Return the final list of gene extremities for each chromosome in the genome.

        '''
        genome_gene_extremities = []
        for chromosome in genome:
            chromosome_gene_extremities = []
            for marker in chromosome:
                if isinstance(marker, str) and '_' in marker:
                    continue
                try:
                    marker_int = int(marker)
                    if int(marker) >= 0:
                        chromosome_gene_extremities.append(marker_int)
                        chromosome_gene_extremities.append(marker + 0.5)
                    else:
                        chromosome_gene_extremities.append(abs(marker_int) + 0.5)
                        chromosome_gene_extremities.append(abs(marker_int))
                except ValueError:
                    print("marker cannot be converted to int:", marker_int)
                    continue
            genome_gene_extremities.append(chromosome_gene_extremities)
               
            
        return genome_gene_extremities
    


    def create_adjacency_list(self, genome):

        '''
        Creates an adjacency list based on the given genome.

        Parameters:
        - genome (list): A list representing the genome.

        Returns:
        list: An adjacency list representing the relationships between elements in the genome.

        Algorithm:
        1. Obtain gene extremities using Gene_extremities.gene_extremities method.
        2. Iterate over each chromosome in gene_extremities.
        3. For each chromosome, iterate over its elements.
        4. If the element is the first or last in the chromosome, add it to adjacencies.
        5. If the element is not the first or last, add a tuple of the current element and the next element to adjacencies.
        6. Return the final adjacency list.

        '''
        adjacencies = []
        gene_extremities = Extremities_and_adjacencies.gene_extremities(self, genome)
        for chromosome in gene_extremities:
            i = 0
            while i < len(chromosome):
                if chromosome[i] == chromosome[0] or chromosome[i] == chromosome[-1]:
                    adjacencies.append((chromosome[i]))
                    i += 1
                else:
                    adjacencies.append((chromosome[i], chromosome[i + 1]))
                    i += 2
       
        return adjacencies

    def ordered_and_sorted_adjacencies(self, genome):
        """
        Retrieves the ordered and sorted list of adjacencies from the given genome.

        This method takes a genome as input, creates an adjacency list using the 
        Gene_extremities.create_adjacency_list method, and then orders and sorts 
        the adjacencies. The resulting list includes telomeres and sorted adjacencies.

        Parameters:
        - genome (type): The genome for which adjacencies are to be retrieved.

        Returns:
        - list: A sorted list of adjacencies, including telomeres.

        Note:
        - The input genome should be a valid sequence for accurate results.
        """
        adjacencies = Extremities_and_adjacencies.create_adjacency_list(self, genome)
        adjacys = []
        telomeres = []
        for element in adjacencies:
            if isinstance(element, tuple):
                if int(element[0]) < int(element[1]):
                    adjacys.append(element)
                else:
                    adjacys.append((element[1], element[0]))
            else:
                telomeres.append(element)

       
        adjacys.sort()
       
        telomeres.sort()
        sorted_adjacencies = telomeres+adjacys


        return sorted_adjacencies


    def find_next_extremity(self, current, next_extremity):
        """
        Finds the next extremity based on the current extremity and a specified next extremity.

        This method determines the next extremity by checking the equality of the first element of the current extremity
        with the specified next extremity. If they are equal, it further checks the decimal part of the second element
        of the current extremity to determine the next extremity.

        Parameters:
        - current (tuple): The current extremity represented as a tuple (x, y).
        - next_extremity: The specified next extremity.

        Returns:
        - next_extremity: The next extremity calculated based on the input parameters.
        """
        if current[0] == next_extremity:
            if current[1] % 1 == 0:
                next = current[1] + 0.5
            else:
                next = current[1] - 0.5
        else:
            if current[0] % 1 == 0:
                next = current[0] + 0.5
            else:
                next = current[0] - 0.5
        return next

    def find_next_adjacency(self, next_extremity, chromosome, not_telomeres):
        '''
        This method processes elements in the 'not_telomeres' list, selecting elements whose first or second element
        matches the 'next_extremity'. The selected element is then appended to the 'chromosome' list, and removed from
        the 'not_telomeres' list. The 'Gene_extremities.find_next_extremity' method is called to find the next extremity
        based on the current element and the current 'next_extremity'. The updated 'next_extremity', 'chromosome', and
        'not_telomeres' lists are returned.
        
        @param not_telomeres The list of elements to be processed.
        @param next_extremity The current extremity to be matched against the elements in 'not_telomeres'.
        @param chromosome The list to which the selected elements are appended.
        @return An array containing the updated 'next_extremity', 'chromosome', and 'not_telomeres' lists.
        
        '''
        for element in not_telomeres:
            if element[0] == next_extremity or element[1] == next_extremity:
                current = element
                chromosome.append(current)
                not_telomeres.remove(current)
                next_extremity = Extremities_and_adjacencies.find_next_extremity(self, current, next_extremity)
                return next_extremity, chromosome, not_telomeres
        return [next_extremity]

    def find_adjacency_cycle(self, next_extremity, chromosome, not_telomeres):
        """
        Finds an adjacency cycle starting from the given 'next_extremity' in the specified 'chromosome'.
        
        Parameters:
        - next_extremity (int): The starting extremity to search for the adjacency cycle.
        - chromosome (list): The list representing the chromosome.
        - not_telomeres (list): List of extremities that should not be considered as telomeres.

        Returns:
        Tuple[int, list, list]: A tuple containing the following:
            - int: The next extremity in the adjacency cycle.
            - list: The chromosome.
            - list: The list of extremities excluding telomeres.
        """

        next_adjacency = Extremities_and_adjacencies.find_next_adjacency(self, next_extremity, chromosome, not_telomeres)

        while len(next_adjacency) != 1:

            next_extremity = next_adjacency[0]
            next_adjacency = Extremities_and_adjacencies.find_next_adjacency(self, next_extremity, chromosome, not_telomeres)


        else:
            next_extremity = next_adjacency[0]

            return next_extremity, chromosome, not_telomeres

    def find_chromosomes(self, adjacencies):
        """
        Finds linear and circular chromosomes from a list of gene adjacencies.

        Parameters:
        - adjacencies (list): A list containing gene adjacencies, where each element is either an integer (telomere) or a tuple (gene adjacency).

        Returns:
        tuple: A tuple containing two lists - linear_chromosomes and circular_chromosomes.
            linear_chromosomes (list): List of linear chromosomes, each represented as a list of gene adjacencies.
            circular_chromosomes (list): List of circular chromosomes, each represented as a list of gene adjacencies.

        Algorithm:
        - Separate telomeres and gene adjacencies into two lists: telomeres and not_telomeres.
        - Initialize empty lists for linear_chromosomes and circular_chromosomes.
        - Iterate through telomeres:
            - Start a new chromosome with the first telomere.
            - Extend the chromosome until the next telomere is found.
            - Add the completed chromosome to linear_chromosomes.
        - Iterate through not_telomeres:
            - Start a new chromosome with the first gene adjacency.
            - Extend the chromosome until a circular chromosome is found or the adjacency cycle is completed.
            - Add the completed chromosome to either linear_chromosomes or circular_chromosomes based on the result.
        """

        telomeres = [element for element in adjacencies if type(element) is not tuple]
        not_telomeres = [element for element in adjacencies if type(element) is tuple]

        linear_chromosomes = []
        circular_chromosomes = []
        chromosome = []
        i = 0

        while len(telomeres) > 0: # linear chr

            i += 1
            current = telomeres[0]

            telomeres.remove(current)
            chromosome.append(current)

            if current % 1 == 0:
                next_extremity = current + 0.5
            else:
                next_extremity = current - 0.5

            if next_extremity in telomeres:
                current = next_extremity

                telomeres.remove(current)
                chromosome.append(current)
                linear_chromosomes.append(chromosome)
                chromosome = []
            else:
                adjacency_cycle = Extremities_and_adjacencies.find_adjacency_cycle(self, next_extremity, chromosome, not_telomeres)
                next_extremity = adjacency_cycle[0]

                if next_extremity in telomeres:
                    current = next_extremity
                    telomeres.remove(current)
                    chromosome.append(current)
                    linear_chromosomes.append(chromosome)
                    chromosome = []

        while len(not_telomeres) > 0: # circular chr
            current = not_telomeres[0]
            not_telomeres.remove(current)
            chromosome.append(current)

            if current[0] % 1 == 0:
                next_extremity = current[0] + 0.5
            else:
                next_extremity = current[0] - 0.5

            if next_extremity == current[1]:
               

                circular_chromosomes.append(chromosome)
                chromosome = []

            else:
                adjacency_cycle = Extremities_and_adjacencies.find_adjacency_cycle(self, next_extremity, chromosome, not_telomeres)
                next_extremity = adjacency_cycle[0]

                if next_extremity == chromosome[0][1]:
                    

                    circular_chromosomes.append(chromosome)
                    chromosome = []

        return linear_chromosomes, circular_chromosomes

    def find_genome(self, adjacencies):
        """
        Finds the genome from the given list of adjacencies.

        Parameters:
        - adjacencies (list): A list of adjacencies representing chromosomes.

        Returns:
        - genome (list): A list containing the discovered genome.

        The function processes linear and circular chromosomes from the given adjacencies
        and constructs a genome based on the adjacency information.

        Linear chromosomes are processed by extracting genes from adjacent pairs. Each gene is
        represented as an integer, and its sign indicates the direction in the chromosome.

        Circular chromosomes are processed similarly, with the addition of marking them as circular ('o')
        in the genome list.
        """

        genome = []
        chromosomes = Extremities_and_adjacencies.find_chromosomes(self, adjacencies)
        linear_chromosomes = chromosomes[0]
        circular_chromosomes = chromosomes[1]

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


                else:

                    if int(gene) == int(chromosome[i][0]):

                        gene=chromosome[i][1]
                    else:
                        gene = chromosome[i][0]

                    if gene%1 == 0:
                        chrom.append(int(gene))
                    else:
                        chrom.append(-int(gene))


            genome.append(chrom)


        for chromosome in circular_chromosomes:
            chrom =[]
            gene = []
            chromosome_length = len(chromosome)

            chrom.append('o')
            for i in range(0, chromosome_length):

                if i==0:
                    gene = chromosome[i][0]
                    if gene%1 == 0:
                        chrom.append(int(gene))
                    else:
                        chrom.append(-int(gene))

                else:
                    if int(gene) == int(chromosome[i][0]):

                        gene=chromosome[i][1]
                    else:
                        gene = chromosome[i][0]

                    if gene%1 == 0:
                        chrom.append(int(gene))
                    else:
                        chrom.append(-int(gene))

            genome.append(chrom)

        return genome


