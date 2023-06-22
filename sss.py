from Rearrangement_Extremities import Gene_extremities
from Rearrangement_node import Rearrangement_node
import Rearrangement_network


genomeA = []
genomeB = []
with open("/home/22204911/Documents/Test_run/genA0.txt") as f:
    line = [element.strip('\n').split(',') for element in f]
    for element in line:
        element = list(map(int, element))
        genomeA.append(element)
    print("genomeA:" ,genomeA)

with open("/home/22204911/Documents/Test_run/genB0.txt") as f:
    line = [element.strip('\n').split(',') for element in f]
    for element in line:
        element = list(map(int, element))
        genomeB.append(element)
    print("genomeB:"  ,genomeB)


    # get_adjacencies = Extremities()
      
      

   
    get_adjacencies = Gene_extremities()
    adjacencies_genomeA = get_adjacencies.ordered_and_sorted_adjacencies(genomeA)
    adjacencies_genomeB = get_adjacencies.ordered_and_sorted_adjacencies(genomeB)
    adjacsA = get_adjacencies.create_adjacency_list(genomeA)
    adjacsB = get_adjacencies.create_adjacency_list(genomeB)

    # start_node = Node_rearrangement(adjacencies_genomeA)
    # target_node = Node_rearrangement(adjacencies_genomeB)
    get_chromosomes = Gene_extremities()
    get_genome = Gene_extremities()
    get_legal = Rearrangement_node()
    # get_legal_ops = get_legal.get_legal_operations(adjacencies_genomeA)
    # action = get_legal.take_action(get_legal_ops)

    linear_chromA = get_chromosomes.find_chromosomes(adjacencies_genomeA)
    linear_chromB = get_chromosomes.find_chromosomes(adjacencies_genomeB)
    circular_chromA = get_chromosomes.find_chromosomes(adjacencies_genomeA)
    circular_chromB = get_chromosomes.find_chromosomes(adjacencies_genomeB)
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
    chromosome_genomeA = get_chromosomes.find_chromosomes(adjacencies_genomeA)
    chromosome_genomeB = get_chromosomes.find_chromosomes(adjacencies_genomeB)
    print("linear_chromA: ", linear_chromA)
    # print("linear_chromB: ", linear_chromB)
    # print("circular_chromA:" , circular_chromA)
    # print("circular_chromB:" , circular_chromB)
    # print("get_genomeA:" , get_genomeA)
    # print("get_genomeB:" , get_genomeB)
    # # print("genomeA_x:", genomeA_x)
    # # print("genomeB_x:", genomeB_x)
    # print("adjacenciesA:", adjacencies_genomeA)
    # print("adjacenciesB:", adjacencies_genomeB)
    # print("adjacsA: ", adjacsA)
    # print("adjacsB: ", adjacsB)
    # # print("Linear_chromosomes_genomeA: ", Linear_chromosomes_genomeA)
    # print("chromosome_genomeA: ", chromosome_genomeA)
    # print("chromosome_genomeB: ", chromosome_genomeB)
    # print("get_legal_ops:" , get_legal_ops)
    # print("take action:", action)
