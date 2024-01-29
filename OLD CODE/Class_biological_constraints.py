import random

class Biological_constraints:
    def __init__(self):
        pass

    # def intergenic_region(self, filename, intergenic_length=5):
    #     genic_record = SeqIO.parse(open(filename), "genome").next()
    #     intergenic_region = []

    #     # Find gene features over entire genome

    #     for feature in genic_record.features:
    #         if feature.type == "*":
    #             gen_start = feature.location._start.position
    #             gen_end = feature.location._end.position
    #             if intergenic_length >= 5:
    #                 intergenic_region.append(gene)

    #             else:
    #                 intergenic_region.remove(gene)

    #     return intergenic_region

    '''
    Function to generate intergenic regions
    '''
    def intergenerator(numbered_genes_list):
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
    def intergenic_regions(genes_with_intergenic):
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



    def proximity_of_DNA_segments(self):
        pass