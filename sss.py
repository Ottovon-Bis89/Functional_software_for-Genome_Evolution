from Rearrangement_extremities_and_adjacencies import Extremities_and_adjacencies
#from Class_extremities_and_adjacencies import Extremities_and_adjacencies
# from Rearrangement_node import Node
from new_Node import Node
#from Class_wrDCJ_Node import Node
from Network_wrDCJ import Network
#import Rearrangement_network
#from New_weight import Constraints
#from Data_generator import DataGenerator
import sys

genomeA = []
genomeB = []
with open("/home/22204911/Documents/New_Test/MTZ.txt") as f:
    line = [element.strip('\n').split(',') for element in f]
    for element in line:
        element = list(map(int, element))
        genomeA.append(element)
    print("source_genomeA:" ,genomeA)

with open("/home/22204911/Documents/New_Test/FJSA.txt") as f:
    line = [element.strip('\n').split(',') for element in f]
    for element in line:
        element = list(map(int, element))
        genomeB.append(element)
    print("target_genomeB:"  ,genomeB)

with open("/home/22204911/Documents/New_Test/Weight_ratios.txt") as f:
    line = [element.strip('\n').split(',') for element in f]
    weights = []
    for element in line:
        element = list(map(int, element))
        weights.append(element)

    # gen_obj = Intergenic_region_generator.IntergenicGenerator()
    # data_generator = DataGenerator()
    # # source_genome = data_generator.check_genes(source_genomeA)
    # # target_genome = data_generator.check_genes(target_genomeB)
    # # source_genome = data_generator.generate_intergenic_regions(source_genomeA)
    # # target_genome = data_generator.generate_intergenic_regions(target_genomeB)
    # source_genomeA = gen_obj.inter_generator(source_genomeA)
    # target_genomeB = gen_obj.inter_generator(target_genomeB)
      
    # print("target_genomeB:"  ,target_genomeB)
    # print("source_genomeA:" ,source_genomeA)
      
    # current_node = Node
    # intergen = Constraints()
    get_adjacencies = Extremities_and_adjacencies()
    net_work = Network()
    adjacencies_genomeA = get_adjacencies.ordered_and_sorted_adjacencies(genomeA)
    adjacencies_genomeB = get_adjacencies.ordered_and_sorted_adjacencies(genomeB)

    start_node = Node(adjacencies_genomeA)
    target_node = Node(adjacencies_genomeB)
    list_of_legal_operations = start_node.get_legal_operations(adjacencies_genomeB)
    print(list_of_legal_operations)
    #ope_weight, ope_weight= net_work.build_hash_table(current_node,  adjacencies_genomeB,  weights)
   

    adjacsA = get_adjacencies.create_adjacency_list(genomeA)
    adjacsB = get_adjacencies.create_adjacency_list(genomeB)
    # intergic_regions = intergen.inter_generator(adjacencies_genomeB)
    # legal_ops = start_node.get_legal_operations(adjacencies_genomeB)
    # print('legal:', legal_ops)
    # operations = intergen.operation_intergenic_regions(intergic_regions, legal_ops)
    # print("intergenic regions : " + str(intergic_regions))
    # print("operations" + str(operations))
    # for op in operations:
    #     ope_weight = intergen.intergenic_weight(net_work, intergic_regions, op)
    #     print(net_work.operation_weight)
    #     print('opp:', net_work.op_weight)
    # # chrom_A = get_adjacencies.find_chromosomes(adjacsA)
    # chrom_B = get_adjacencies.find_chromosomes(adjacsB)
    # print("chromA: ", chrom_A)
    # print("chromB: ", chrom_B)
    # print("adjacsA:", adjacsA)
    # print("AdjacsB:", adjacsB)
    # print('adjA:' , adjacencies_genomeA)
    # print('adjB:' , adjacencies_genomeB)

    

    
   
    #print("legal: ", legal_ops)
    # take = start_node.take_action(legal_ops)
    # print(take)
    
   
    


   