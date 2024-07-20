from Rearrangement_extremities_and_adjacencies import Extremities_and_adjacencies
from new_Node import Node
from Biological_Constraints import Constraints
import New_Network_wrDCJ
from ForeignDNA import Foreign_DNA
import sys

genomeA = []
genomeB = []
with open("/home/22204911/Documents/New_Test/T3_A.txt") as f:
    line = [element.strip('\n').split(',') for element in f]
    for element in line:
        element = list(map(int, element))
        genomeA.append(element)
    print("genomeA:" ,genomeA)

with open("/home/22204911/Documents/New_Test/T3_B.txt") as f:
    line = [element.strip('\n').split(',') for element in f]
    for element in line:
        element = list(map(int, element))
        genomeB.append(element)
    print("genomeB:"  ,genomeB)

with open("/home/22204911/Documents/New_Test/Weight_ratios.txt") as f:
    line = [element.strip('\n').split(',') for element in f]
    weights = []
    for element in line:
        element = list(map(int, element))
        weights.append(element)
    #print("weights:" ,weights)

      
    #current_node = Node
    
    intergen = Constraints(genomeB)
    get_adjacencies = Extremities_and_adjacencies()
    #foreign_dna = Foreign_DNA(get_adjacencies)
    # fragments = foreign_dna.foreign_dna_pool(genomeA, genomeB)
    #genomeA = foreign_dna.insert_fragments_into_genome(genomeA, fragments)
    #print("Source_genomeA:", genomeA)
    #net_work = Network()
    adjacencies_genomeA = get_adjacencies.ordered_and_sorted_adjacencies(genomeA)
    adjacencies_genomeB = get_adjacencies.ordered_and_sorted_adjacencies(genomeB)

    start_node = Node(adjacencies_genomeA)
    target_node = Node(adjacencies_genomeB)
    list_of_legal_operations = start_node.get_legal_operations(adjacencies_genomeB)
    print("LOP:", list_of_legal_operations)

    # adjacsA = get_adjacencies.create_adjacency_list(genomeA)
    # adjacsB = get_adjacencies.create_adjacency_list(genomeB)
    intergic_regions = intergen.inter_generator(adjacencies_genomeB)

    legal_ops = start_node.get_legal_operations(adjacencies_genomeB)
    # operations_with_intergenic = intergen.operations_intergenic_regions(intergic_regions, list_of_legal_operations)
    operations_with_intergenic = intergen.operations_intergenic_regions(intergic_regions, adjacencies_genomeA, adjacencies_genomeB)

    print('legal:', legal_ops)
    # legal_ops = list_of_legal_operations
    #operations = intergen.operations_intergenic_regions(intergic_regions, legal_ops)

    # print("intergenic regions : " + str(intergic_regions))
    print("operations" + str(operations_with_intergenic))
    
    
    operation_weights_dict = intergen.intergenic_weight(intergic_regions, operations_with_intergenic)
    print(operation_weights_dict)
    for i, (operation, weights) in enumerate(operation_weights_dict.items()):
        W1 = weights['W1']
        W2 = weights['W2']
        irs = weights['IRs']

        print(f"Operation {i + 1}: {operation}")
        print(f"  W1: {W1}")
        print(f"  W2: {W2}")
        print(f"  IRs: {irs}")

# for operation, weights in operation_weights_dict.items():
#     operation_weight = weights['operation_weight']
#     op_weight = weights['op_weight']
#     irs = weights['IRs']

#     print(f"Operation: {operation (i + 1)}, Operation Weight: {operation_weight}, Op Weight: {op_weight}, IRs: {irs}")

    # operation_weights_dict = intergen.intergenic_weight(net_work, intergic_regions, operations_with_intergenic)

    # for i, (operation_weight, op_weight, irs) in enumerate(operation_weights_dict):
    #     print(f"Operation {i + 1}: Operation Weight = {operation_weight}, Op Weight = {op_weight}, IRs = {irs}")

   
    


   