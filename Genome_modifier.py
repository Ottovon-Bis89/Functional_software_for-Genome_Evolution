from random import randint

class GenomeModifier:
    def __init__(self):
        pass

    def insert_foreign_dna(self, source_genome, fragment):
        """
        Inserts a fragment of foreign DNA into the source genome, with mutations in intergenic regions.
        
        This function adds a fragment of foreign DNA to the source genome. The foreign fragment can be identified 
        with an underscore(_) attached to an integer. The path of foreign DNA can be followed through the 
        evolutionary journey of the source genome into the target genome.
        
        :param source_genome: The source genome where the foreign DNA will be inserted.
        :param fragment: The fragment of foreign DNA to be inserted.
        :return: A tuple containing the modified source genome and information about the insertion.
        """
        # Step 1: Find applicable intergenic regions to associate with mutations
        list_of_mutation_points = []
        list_of_mutation_points_genome = []

        for genes_with_intergenic_approved in source_genome:
            mutation_points = [i + 1 for i, gene in enumerate(genes_with_intergenic_approved) if isinstance(gene, str) and len(gene) > 1 and '*' in gene]
            list_of_mutation_points_genome.append(mutation_points)

        # Step 2: Insert intergenic regions into the foreign DNA fragment
        fragment_with_intergenic_regions = []
        length = len(fragment)

        for j in range(len(fragment)):
            if j == 0:
                random_bp = randint(6, 10)
                region = '*' + str(random_bp)
                fragment_with_intergenic_regions.append(region)

            random_bp = randint(6, 10)
            start = fragment[j]
            region = '*' + str(random_bp)
            fragment_with_intergenic_regions.append(start)

            if j != length - 1:
                fragment_with_intergenic_regions.append(region)

        # Step 3: Identify applicable intergenic regions in the fragment
        for i in range(len(fragment_with_intergenic_regions)):
            if i % 2 == 0 or i == 0:
                region = fragment_with_intergenic_regions[i]

                if len(region) > 2:
                    value = region[1] + region[2]
                else:
                    value = region[1]
                if int(value) < 5:
                    fragment_with_intergenic_regions[i] = '*'

        # Step 4: Choose a chromosome with applicable intergenic regions
        position_applicable_region_chromosome = []
        source_chromosome = []
        rand_chromosome = []

        while len(position_applicable_region_chromosome) == 0:
            rand_chromosome = randint(0, len(list_of_mutation_points_genome) - 1)
            position_applicable_region_chromosome = list_of_mutation_points_genome[rand_chromosome]
            source_chromosome = source_genome[rand_chromosome]

        # Step 5: Randomly pick a position from applicable regions and insert the fragment
        rand_position = randint(0, len(position_applicable_region_chromosome) - 1)
        position = position_applicable_region_chromosome[rand_position]

        mutated = []
        if position == 0:  # Insert at the beginning
            mutated = fragment_with_intergenic_regions + source_chromosome
        else:  # Insert at the ending
            mutated = source_chromosome + fragment_with_intergenic_regions

        source_genome[rand_chromosome] = mutated

        return source_genome, ['F_DNA', rand_chromosome, position, fragment_with_intergenic_regions, mutated]
