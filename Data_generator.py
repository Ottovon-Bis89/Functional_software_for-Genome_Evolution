import random

class Data_generator():
    def __init__(self):
        
     '''
    Function to generate intergenic regions.
    The function adds random numbers to the intergenic regions(space between genes)
    of genes which will used as identifiers or mutation points for the evolutionary events.
    These numbers represent the number of base pairs between(lenght of intergenic region) genes
    These numbers are preceded by an asterisk(*)  to differentiate them from the normal 
    genes(sequence blocks) since they both numbers.
    '''
    def intergenerator(self,numbered_genes_list):
        genes_with_intergenic_chrom = []
        genes_with_intergenic = []
        for i in range(len(numbered_genes_list)):
            chrom = numbered_genes_list[i]
            length = len(chrom)
          
            for j in range(len(chrom)):
                if j == 0 :
                    random_bp = random.randint(6,10)
                    region = '*' + str(random_bp)
                    genes_with_intergenic_chrom.append(region)
                random_bp = random.randint(6,10)
                start = chrom[j]
                region = '*' + str(random_bp)
                genes_with_intergenic_chrom.append(start)
                if j != length-1:
                    genes_with_intergenic_chrom.append(region)
            genes_with_intergenic.append(genes_with_intergenic_chrom)
            genes_with_intergenic_chrom = []
      
        return genes_with_intergenic


        #get length of gene for for loop
        # length = len(numbered_genes_list)
        # genes_with_intergenic = []
        # for i in range(length):
        #     random_bp = random.randint(0,10)
        #     start = numbered_genes_list[i]
        #     genes_with_intergenic.append(start)
        #     if i != length-1:
        #         genes_with_intergenic.append(region)
        # return genes_with_intergenic
        #

    '''
    Function to find applicable intergenic regions.
    The function removes numeric base pair values from
    intergenenic regions that are not viable mutation points.
    It then populates the intergenic regions with viable 
    intergenic regions which are needed for mutation to occur.
    '''
    def intergenic_regions(self,genes_with_intergenic_genome):
        
        for genes_with_intergenic in genes_with_intergenic_genome:
            for i in range(len(genes_with_intergenic)):
                if i % 2 == 0 or i == 0:
                    region = genes_with_intergenic[i]
                
                    if len(region) > 2:
                        value = region[2]+region[2]
                    else:
                        value = region[1]
                    if int(value) < 5:
                        genes_with_intergenic[i] = '*'
        return genes_with_intergenic_genome



# if __name__ == '__main__':
#     #  source_genome = []
#     # with open("genB0.txt") as csv:
#     #     line = [element.strip('\n').split(',') for element in csv]
#     #     for element in line:
#     #         element = list(map(int, element))
#     #         source_genome.append(element)
#     #print(genomeA)
#     data_gen_obj = Data_generator()
#     list_of_genome_with_intergenic = data_gen_obj.intergenerator(source_genome)
    #print(list_of_genome_with_intergenic)
    #list_of_genome_with_applicable_intergenic = data_gen_obj.intergenic_regions(list_of_genome_with_intergenic)
    #print(list_of_genome_with_applicable_intergenic)
    # for i in range(len(genomeA)):
    #     print(genomeA[i])
    #     data_with_intergenic = data_gen_obj.intergenerator(genomeA[i])
    #     list_of_genome_with_intergenic.append(data_with_intergenic)
    # for i in range(len(list_of_genome_with_intergenic)):
    #     data_with_applicable_intergenic = data_gen_obj.intergenic_regions(list_of_genome_with_intergenic[i])
    #     list_of_genome_with_applicable_intergenic.append(data_with_applicable_intergenic)


    #Write data to file
    # element = ''
    # with open('Generated_data_B.txt', 'w') as f:
    #     for i in range(len(list_of_genome_with_intergenic)):
    #         for j in range(len(list_of_genome_with_intergenic[i])):
    #             element = list_of_genome_with_intergenic[i]
    #             if j == len(list_of_genome_with_intergenic[i])-1:
    #                 element += str(element[j])
    #             else:
    #                 element += str(element[j]) + ','
    #         f.write(element+"\n")
    #         element = ''