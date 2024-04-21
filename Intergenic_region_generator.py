  
import random
from Rearrangement_extremities_and_adjacencies import Extremities_and_adjacencies
from new_Node import Node
# from Network_wrDCJ import Network
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import ScalarMappable

#net_work = Network()
node_instance = Node()


class Constraint:
    def __init__(self, node_instance):
        self.node_instance = node_instance
    

    def inter_generator(self):
        intergenic_regions = []
        for _ in range(0):
            random_bp = random.randint(1, 10)
            intergenic_regions.append('*' + str(random_bp))
            print(intergenic_regions)
        return intergenic_regions


    def operation_intergenic_regions(self, intergenic_regions):
        list_of_legal_operations = self.node_instance.get_legal_operations()
        operations_with_intergenic = []
        for operation in list_of_legal_operations:  
            if isinstance(operation, tuple):
                
                if len(operation) == 3 and isinstance(operation[0], tuple):
                    start_tuple, start, end = operation
                    start_tuple_with_intergenic = (start_tuple[0], random.choice(intergenic_regions), start_tuple[1])
                    operations_with_intergenic.append((start_tuple_with_intergenic, start, end))

                elif len(operation) == 3 and isinstance(operation[-1], tuple):
                    start, end, end_tuple = operation
                    end_tuple_with_intergenic = (end_tuple[0], random.choice(intergenic_regions), end_tuple[1])
                    operations_with_intergenic.append((start, end, end_tuple_with_intergenic))

                elif len(operation)==2 and isinstance(operation[0][1], tuple):
                    start, end =  operation
                    if isinstance(start, tuple):
                        new_start = start[0]
                        new_start_end = start[1]
                    
                    if isinstance(end, tuple):
                        new_end_start = end[0]
                        new_end = end[1]
                    operations_with_intergenic.append((((new_start[0],random.choice(intergenic_regions),new_start[1]),(new_start_end[0],random.choice(intergenic_regions),new_start_end[1])),((new_end_start[0],random.choice(intergenic_regions),new_end_start[1]),(new_end[0],random.choice(intergenic_regions),new_end[1]))))

            else:
                operations_with_intergenic.append(operation)
                # print(operations_with_intergenic)
        return operations_with_intergenic

    

    def intergenic_weight(self, net_work, operations_with_intergenic):
        
        operation_weight = net_work.operation_weight
        op_weight = net_work.op_weight
        
        for operation in operations_with_intergenic:
            if not isinstance(operation, tuple):
                continue
            bp = 0 
            
            if len(operation) == 3:
                for element in operation:
                    if isinstance(element, str) and '*' in element:
                        bp = int(element[1:])  
                        print("bp:", bp)  

            elif len(operation) == 2 and  (isinstance(operation[0], tuple) and isinstance(operation[1], tuple)):
                for outer_tuple in operation:
                    if isinstance(outer_tuple, tuple):
                        for element in outer_tuple:
                            if isinstance(element, str) and '*' in element:
                                bp = int(element.split('*')[1])  
                                print("bp:", bp) 

            if bp <= 4:
                operation_weight = 0.2 * operation_weight
                # print('op:', operation_weight)
                op_weight = 0.2 * op_weight
            else:
                operation_weight = 0.8 * operation_weight
                op_weight = 0.8 *  op_weight
                # print(op_weight)

        return operation_weight, op_weight






    

# # Example usage:
# genomeA = [[1,2,3,4,15],[-8,-7,6,-5,-14,-13,-12],[9,11],[-20,-19,-18,-17,-16,-32,10,-31,-30,-29,-28,-27,33],[21,22,23,24,25,26],[-33],[34,35,36,37,38,39,40]]
# genomeB = [[1,2,3,4,5,6,7,8],[9,10,11],[12,13,14,15],[16,17,18,19,20],[21,22,23,24,25,26],[27,28,29,30,31,32,33,33],[34,35,36,37,38,39,40]]

# adjacencies = Extremities_and_adjacencies()
# # adjacencies_list = adjacencies.ordered_and_sorted_adjacencies(genomeB)
# # adjacencies_genomeA = adjacencies.ordered_and_sorted_adjacencies(genomeA)
# adjacencies_genomeB = adjacencies.ordered_and_sorted_adjacencies(genomeB)
# #         #sprint(adjacencies_genomeB)
# target_node = Node(adjacencies_genomeB)
# list_of_legal_operations = target_node.get_legal_operations(adjacencies_genomeB)
# #genomeB = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]]
# # genomeB = [[6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]]

# # data_gen = DataGenerator()
# # genomeA = data_gen.check_genes(genomeA)
# # genomeB = data_gen.check_genes(genomeB)
# # print("checked : " + str(genomeA))
# intergenic_generator = IntergenicGenerator(genomeA, genomeB)

# intergenic_gen = IntergenicGenerator. inter_generator(genomeB)
# intergenic_gen = IntergenicGenerator.inter_generator(genomeA)
# adjacencies_with_intergenic = intergenic_gen.inter_generator(genomeB)
# intergenic_regions = intergenic_gen.inter_generator()
# adjacencies_intergenic = intergenic_gen.adjacencies_intergenic_regions(intergenic_regions)

# print(adjacencies_intergenic)