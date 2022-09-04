import random

class Data_generator():
    def __init__(self) -> None:
        
     '''
    Function to generate intergenic regions
    '''
    def intergenerator(self,numbered_genes_list):
        #get length of gene for for loop
        length = len(numbered_genes_list)
        genes_with_intergenic = []
        for i in range(length):
            random_bp = random.randint(0,10)
            start = numbered_genes_list[i]
            region = '*' + str(random_bp)
            genes_with_intergenic.append(start)
            if i != length-1:
                genes_with_intergenic.append(region)
        return genes_with_intergenic

    '''
    Function to find applicable intergenic regions
    '''
    def intergenic_regions(self,genes_with_intergenic):
        #function removes numeric base pair values from
        #intergenenic regions that cannot mutate
        #check for viable intergenic region
        for i in range(len(genes_with_intergenic)):
            if i % 2 != 0:
                region = genes_with_intergenic[i]
                if len(region) > 2:
                    value = region[1]+region[2]
                else:
                    value = region[1]
                if int(value) <= 5:
                    genes_with_intergenic[i] = '*'
        return genes_with_intergenic

if __name__ == '__main__':
    genomeA = []
    with open("genA0.txt") as csv:
        line = [element.strip('\n').split(',') for element in csv]
        for element in line:
            element = list(map(int, element))
            genomeA.append(element)
        
    data_gen_obj = Data_generator()
    list_of_genome_with_intergenic = []
    list_of_genome_with_applicable_intergenic = []
    for i in range(len(genomeA)):
        print(genomeA[i])
        data_with_intergenic = data_gen_obj.intergenerator(genomeA[i])
        list_of_genome_with_intergenic.append(data_with_intergenic)
    for i in range(len(list_of_genome_with_intergenic)):
        data_with_applicable_intergenic = data_gen_obj.intergenic_regions(list_of_genome_with_intergenic[i])
        list_of_genome_with_applicable_intergenic.append(data_with_applicable_intergenic)


    #Write data to file
    ele = ''
    with open('Generated_data.txt', 'w') as f:
        for i in range(len(list_of_genome_with_intergenic)):
            for j in range(len(list_of_genome_with_intergenic[i])):
                element = list_of_genome_with_intergenic[i]
                if j == len(list_of_genome_with_applicable_intergenic[i])-1:
                    ele += str(element[j])
                else:
                    ele += str(element[j]) + ','
            f.write(ele+"\n")
            ele = ''