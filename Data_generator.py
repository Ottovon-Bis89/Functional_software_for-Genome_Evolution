import random
import sys
from logger import log


class DataGenerator:
    def __init__(self):
        """
        Constructor for the DataGenerator class.
        This class is used to generate intergenic regions and manipulate genomes.
        """
        pass  # No additional comments for the constructor

    def generate_intergenic_regions(self, source_genome):
        log.debug("generate_intergenic_regions")
        """
        Function to generate intergenic regions in the source genome.
        
        The function adds random numbers to the intergenic regions (non-coding regions between genes)
        of genes which will be used as identifiers or mutation points for evolutionary events.
        These numbers represent the number of base pairs between (length of intergenic region) genes.
        These numbers are preceded by an asterisk (*) to differentiate them from the normal
        genes (sequence blocks) since they are all numbers.

        :param source_genome: The source genome to generate intergenic regions for.
        :return: A new genome with intergenic regions added.
        """
        new_source_genome = [[] * 1 for i in range(len(source_genome))]

        j = 0
        for index in source_genome:
            value = 0
            while value < len(index):
                random_bp = random.randint(6, 10)

                if "*" not in source_genome[j][value]:
                    new_source_genome[j].append("*" + str(random_bp))
                    new_source_genome[j].append(source_genome[j][value])
                    value += 1
                else:
                    for _ in range(2):
                        try:
                            new_source_genome[j].append(source_genome[j][value])
                            value += 1
                        except:
                            break
            j += 1
        return new_source_genome

    def check_genes(self, source_genome):
        log.debug("check genes")
        """
        Function to check that the input (source genome) is the correct type.

        If the input is of type String then convert to Integer and return the source genome
        input, else if the input is of type String then return the source genome as is.
        :param source_genome: The source genome to insert foreign DNA fragments into.
        :return: The source genome of type String.
        """
        flattened_src = [gene for chromosome in source_genome for gene in chromosome]
        if all(isinstance(x, int) for x in flattened_src):
            for i in source_genome:
                for x in range(len(i)):
                    i[x] = str(i[x])
            return source_genome
        elif all(isinstance(x, str) for x in flattened_src):
            return source_genome
        else:
            sys.exit(
                "Inconsistent types for source genome, check that your input is of a consistent type (such as Integer or String)"
            )

    def get_foreign_DNA(self, source_genome):
        log.debug("get_foreign_DNA")
        """
        Function to insert foreign DNA fragments into the source genome.
        
        This function adds a fragment of foreign DNA to the source genome. The foreign fragment
        can be identified with an underscore (_) attached to an integer. The path of foreign DNA
        fragment can be followed through the evolutionary journey of the source genome into the
        target genome.

        :param source_genome: The source genome to insert foreign DNA fragments into.
        :return: A modified genome with foreign DNA fragments added.
        """
        largest_gene = 0
        smallest_gene = 10000
        count_genes = 0
        f_DNA_pool = []

        for chromosome in source_genome:
            temp = [x for x in chromosome if "*" not in x]
            count_genes += len(temp)
            for c in temp:
                largest_gene = max(int(largest_gene), int(c))
                smallest_gene = min(int(smallest_gene), int(c))

        for i in range(int(count_genes / 2)):
            random_bp = random.randint(int(smallest_gene), int(largest_gene))
            chromosome_to_insert = random.randint(0, int(len(source_genome) - 1))

            pool = []
            pool.append(random_bp)
            pool.append(chromosome_to_insert)
            f_DNA_pool.append(pool)

        new_source_genome = [[0] * 1 for i in range(len(source_genome))]

        j = 0
        for index in source_genome:
            count = 0
            for i in range(len(index) - 1):
                count += 1
                new_source_genome[j].append("0")
            j += 1

        for i in f_DNA_pool:
            chromosome = i[1]
            f_dna = i[0]

            chosen_chromosome = source_genome[chromosome]
            gene = random.randint(0, int(len(chosen_chromosome) - 1))

            while "*" not in chosen_chromosome[gene]:
                gene = random.randint(0, int(len(chosen_chromosome) - 1))

            new_source_genome[chromosome][gene] = str(f_dna) + "_"

        j = 0
        for index in new_source_genome:
            for value in range(len(index)):
                if (
                    new_source_genome[j][value] == 0
                    or new_source_genome[j][value] == "0"
                ):
                    new_source_genome[j][value] = str(source_genome[j][value])
            j += 1

        return self.generate_intergenic_regions(new_source_genome)


# # # Example usage:
# source_genome = [[1, 5], [6, 7, 8, 9, 10, 11, 12, 13, 29, 30, 2, 3, 31, 32, 33]]
# source_genome = [['*8', '1', '*6', '5','*6', '4', '*6','3', '*6','9' ], ['10', '22', '37', '33']]

# # target_genome = [['*5', '1', '*6', '2', '*7', '3', '*9', '4',  '5', '*7', '6', '*6', '7', '*6', '8'],['*9', '9', '*8', '10', '*8', '11']]
# data_generator = DataGenerator()
# source_genome = data_generator.check_genes(source_genome)
# new_source_genome = data_generator.generate_intergenic_regions(source_genome)
# print(source_genome)
# print(new_source_genome)


# if __name__ == '__main__':
#     Data_generator().get_foreign_DNA(source_genome)
# Data_generator().generate_integenic_regions(source_genome)
