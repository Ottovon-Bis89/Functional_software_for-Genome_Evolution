import random


class Intergenic_generator():
    def __init__(self):
        pass
       

    def inter_generator(self, numbered_genes_list):
        """
        Function to generate intergenic regions.
        The function adds random numbers to the intergenic regions(non-coding regions between genes)
        of genes which will used be as identifiers or mutation points for the evolutionary events.
        These numbers represent the number of base pairs between(lenght of intergenic region) genes
        These numbers are preceded by an asterisk(*)  to differentiate them from the normal
        genes(sequence blocks) since they are all numbers.
        """
         # Initialize empty lists to store the results
        genes_with_intergenic_chromosome = []
        genes_with_intergenic_region = []

         # Iterate over each chromosome in the numbered_genes_list
        for i in range(len(numbered_genes_list)):
            chromosome = numbered_genes_list[i]
            length = len(chromosome)

             # Iterate over each gene within the chromosome
            for j in range(len(chromosome)):
                if j == 0:
                    # If it's the first gene, generate a random intergenic region
                    random_bp = random.randint(6, 10)
                    region = '*' + str(random_bp)
                    genes_with_intergenic_chromosome.append(region)
                    # print(genes_with_intergenic_chromosome)

                # Generate a random intergenic region for each gene
                random_bp = random.randint(6, 10)
                start = chromosome[j]
                region = '*' + str(random_bp)
                genes_with_intergenic_chromosome.append(start)
                # if j != length-1:

                  # for every gene, append an intergenic region
                genes_with_intergenic_chromosome.append(region)
                
                # Append the genes with intergenic regions to the final result list
            genes_with_intergenic_region.append(genes_with_intergenic_chromosome)
            # print(genes_with_intergenic_region)
            genes_with_intergenic_chromosome = []  # Reset genes with intergenic chromosome list for next iteration

        # Return the modified list containing genes with intergenic regions
        return genes_with_intergenic_region


    

    def intergenic_regions(self, genes_with_intergenic_genome):

        '''
        Function to find applicable intergenic regions, it removes numeric base pair values from
        intergenenic regions that cannot mutate,  and then checks for viable intergenic region
        '''

        for genes_with_intergenic_region in genes_with_intergenic_genome:
            # Iterate over each genes_with_intergenic_region in genes_with_intergenic_genome list
            for i in range(len(genes_with_intergenic_region)):

                # For each index i in genes_with_intergenic_region

                # Check if i is divisible by 2 or if i is equal to 0
                if i % 2 == 0 or i == 0:

                    # Select every other element starting from the first element

                    # Get the current element at index i
                    region = genes_with_intergenic_region[i]
                    # print(region)

                    # Check the length of region
                    if len(region) > 2:
                        # If length is greater than 2, assign concatenated value of third character with itself
                        value = region[1]+region[2]
                        # print("val1: ", value)
                    else:
                        # If length is less than or equal to 2, assign the second character
                        value = region[1]
                        # print("val2: ", value)
                    # Check if the parsed integer value is less than 5 
                    if int(value) < 5:
                    # If value is less than 5, replace the element at index i with '*'
                        genes_with_intergenic_region[i] = '*'

        # Return the modified genes_with_intergenic_genome list
        return genes_with_intergenic_genome


# if __name__ == '__main__':
#     genomeA = []
#     with open("genB0.txt") as csv:
#         line = [element.strip('\n').split(',') for element in csv]
#         for element in line:
#             element = list(map(int, element))
#             genomeA.append(element)
#     #print(genomeA)
#     data_gen_obj = Data_generator()
#     list_of_genome_with_intergenic = data_gen_obj.intergenerator(genomeA)
#     #print(list_of_genome_with_intergenic)
#     #list_of_genome_with_applicable_intergenic = data_gen_obj.intergenic_regions(list_of_genome_with_intergenic)
#     #print(list_of_genome_with_applicable_intergenic)
#     # for i in range(len(genomeA)):
#     #     print(genomeA[i])
#     #     data_with_intergenic = data_gen_obj.intergenerator(genomeA[i])
#     #     list_of_genome_with_intergenic.append(data_with_intergenic)
#     # for i in range(len(list_of_genome_with_intergenic)):
#     #     data_with_applicable_intergenic = data_gen_obj.intergenic_regions(list_of_genome_with_intergenic[i])
#     #     list_of_genome_with_applicable_intergenic.append(data_with_applicable_intergenic)


#     #Write data to file
#     element = ''
#     with open('Generated_data_B.txt', 'w') as f:
#         for i in range(len(list_of_genome_with_intergenic)):
#             for j in range(len(list_of_genome_with_intergenic[i])):
#                 element = list_of_genome_with_intergenic[i]
#                 if j == len(list_of_genome_with_intergenic[i])-1:
#                     element += str(element[j])
#                 else:
#                     element += str(element[j]) + ','
#             f.write(element+"\n")
#             element = ''
