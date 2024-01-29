from Rearrangement_Extremities import Gene_extremities
from Rearrangement_node import Node
import Rearrangement_network
import Intergenic_region_generator
from Data_generator import DataGenerator
import sys

node =Node()
source_genomeA = []
target_genomeB = []
with open("/home/22204911/Documents/Test_run/GenoA.txt") as f:
    line = [element.strip('\n').split(',') for element in f]
    for element in line:
        element = list(map(int, element))
        source_genomeA.append(element)
    # print("source_genomeA:" ,source_genomeA)

with open("/home/22204911/Documents/Test_run/GenoB.txt") as f:
    line = [element.strip('\n').split(',') for element in f]
    for element in line:
        element = list(map(int, element))
        target_genomeB.append(element)
    # print("target_genomeB:"  ,target_genomeB)

    gen_obj = Intergenic_region_generator.IntergenicGenerator()
    data_generator = DataGenerator()
    # source_genome = data_generator.check_genes(source_genomeA)
    # target_genome = data_generator.check_genes(target_genomeB)
    # source_genome = data_generator.generate_intergenic_regions(source_genomeA)
    # target_genome = data_generator.generate_intergenic_regions(target_genomeB)
    source_genomeA = gen_obj.inter_generator(source_genomeA)
    target_genomeB = gen_obj.inter_generator(target_genomeB)
      
    print("target_genomeB:"  ,target_genomeB)
    print("source_genomeA:" ,source_genomeA)
      

   
    get_adjacencies = Gene_extremities()
    adjacencies_genomeA = get_adjacencies.ordered_and_sorted_adjacencies(source_genomeA)
    adjacencies_genomeB = get_adjacencies.ordered_and_sorted_adjacencies(target_genomeB)
    adjacsA = get_adjacencies.create_adjacency_list(source_genomeA)
    adjacsB = get_adjacencies.create_adjacency_list(target_genomeB)
    # print("adjacsA:", adjacsA)
    # print("AdjacsB:", adjacsB)
    # print('adjA:' , adjacencies_genomeA)
    # print('adjB:' , adjacencies_genomeB)

    start_node = Node(adjacencies_genomeA)
    target_node = Node(adjacencies_genomeB)

    get_genome = Gene_extremities()
    get_legal = Node()
    # get_legal_ops = get_legal.get_legal_operations(adjacencies_genomeA)
    # action = get_legal.take_action(get_legal_ops)
    # print(adjacencies_genomeA)
    linear_chromA = node.find_chromosomes(adjacencies_genomeA)
    linear_chromB = node.find_chromosomes(adjacencies_genomeB)
    circular_chromA = node.find_chromosomes(adjacencies_genomeA)
    circular_chromB = node.find_chromosomes(adjacencies_genomeB)
    get_genomeA = get_genome.find_genome(adjacencies_genomeA)
    get_genomeB = get_genome.find_genome(adjacencies_genomeB)

    # gen_X = Extremities()
    # genomeA_x = gen_X.gene_extremities(genomeA)
    # genomeB_x = gen_X.gene_extremities(genomeB)
    # adja_A = next_obj.find_next_adjacency(genomeA)


    # adjacencies_genomeA = get_extremities.create_adjacencyList(genomeA)
    # adjacencies_sorted_genomeA = get_extremities.adjacencies_ordered_and_sorted(genomeA)                   
    # next_extremity_genomeA = get_extremities.find_next_extremity(gene_extremities_genomeA, genomeA)
    # next_adjacency_genomeA = get_extremities.find_next_adjacency(next_extremity_genomeA, genomeA,
    #                                                              adjacencies_sorted_genomeA)
    # Linear_chromosomes_genomeA = get_extremities.find_chromosome(adjacencies_genomeA)
    chromosome_genomeA = node.find_chromosomes(adjacencies_genomeA)
    chromosome_genomeB = node.find_chromosomes(adjacencies_genomeB)
    print("linear_chromA: ", linear_chromA)
    # print("linear_chromB: ", linear_chromB)
    # print("circular_chromA:" , circular_chromA)
    # print("circular_chromB:" , circular_chromB)
    # print("get_genomeA:" , get_genomeA)
    # print("get_genomeB:" , get_genomeB)
    # # print("genomeA_x:", genomeA_x)
    # # print("genomeB_x:", genomeB_x)
    print("adjacenciesA:", adjacencies_genomeA)
    print("adjacenciesB:", adjacencies_genomeB)
    print("adjacsA: ", adjacsA)
    print("adjacsB: ", adjacsB)
    print("Linear_chromosomes_genomeA: ", linear_chromA)
    print("chromosome_genomeA: ", chromosome_genomeA)
    # print("chromosome_genomeB: ", chromosome_genomeB)
    # print("get_legal_ops:" , get_legal_ops)
    # print("take action:", action)
