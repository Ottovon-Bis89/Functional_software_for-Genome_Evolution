
import random

class IntergenicGenerator:
    def __init__(self):
        '''
        Constructor for the IntergenicGenerator class.
        This class is used to generate intergenic regions and manipulate genomic data.
        '''
        pass  # No additional comments for the constructor

    def inter_generator(self, numbered_genes_list):
        '''
        Function to generate intergenic regions in a list of numbered genes.

        The function adds random numbers to the intergenic regions (non-coding regions between genes)
        of genes which will be used as identifiers or mutation points for evolutionary events.
        These numbers represent the number of base pairs between (length of intergenic region) genes.
        These numbers are preceded by an asterisk (*) to differentiate them from the normal
        genes (sequence blocks) since they are all numbers.

        :param numbered_genes_list: A list of numbered genes to generate intergenic regions for.
        :return: A list of genes with intergenic regions added.
        '''
        genes_with_intergenic_chromosome = []
        genes_with_intergenic_region = []

        for i in range(len(numbered_genes_list)):
            chromosome = numbered_genes_list[i]
            length = len(chromosome)

            for j in range(len(chromosome)):
                if j == 0:
                    random_bp = random.randint(6, 10)
                    region = '*' + str(random_bp)
                    genes_with_intergenic_chromosome.append(region)

                random_bp = random.randint(6, 10)
                start = chromosome[j]
                region = '*' + str(random_bp)
                genes_with_intergenic_chromosome.append(start)
                genes_with_intergenic_chromosome.append(region)

            genes_with_intergenic_region.append(genes_with_intergenic_chromosome)
            genes_with_intergenic_chromosome = []

        return genes_with_intergenic_region

    def intergenic_regions(self, genes_with_intergenic_genome):
        '''
        Function to find applicable intergenic regions and remove non-mutable regions.

        This function removes numeric base pair values from intergenic regions that cannot mutate
        and checks for viable intergenic regions.

        :param genes_with_intergenic_genome: A list of genes with intergenic regions.
        :return: A modified list with applicable intergenic regions.
        '''
        for genes_with_intergenic_region in genes_with_intergenic_genome:
            for i in range(len(genes_with_intergenic_region)):
                if i % 2 == 0 or i == 0:
                    region = genes_with_intergenic_region[i]
                    if len(region) > 2:
                        value = region[1] + region[2]
                    else:
                        value = region[1]
                    if int(value) < 5:
                        genes_with_intergenic_region[i] = '*'
        return genes_with_intergenic_genome

# # Example usage:
# genomeA = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33], [34, 35, 36, 37, 38, 39, 40, 41, 42], [43], [44], [45, 46], [47], [48], [49, 50]] # Provide your genomic data here
# intergenic_gen = IntergenicGenerator()
# list_of_genome_with_intergenic = intergenic_gen.inter_generator(genomeA)
# list_of_genome_with_applicable_intergenic = intergenic_gen.intergenic_regions(list_of_genome_with_intergenic)
# # Write data to a file, if needed.
