  
import random
from Rearrangement_extremities_and_adjacencies import Extremities_and_adjacencies
from new_Node import Node
# from Network_wrDCJ import Network
#import numpy as np
#import matplotlib.pyplot as plt
#from matplotlib.cm import ScalarMappable

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
                print(operations_with_intergenic)
        return operations_with_intergenic


    def calculate_loop_weight(self, sizes, W1: float = 1.0, W2: float = 1.0):
        loop_weights = [(W1 * 0.2, W2 * 0.2) if size < 0.4 else (W1 * 0.8, W2 * 0.8) for size in sizes]
        return loop_weights


    def calculate_loop_weight(self, sizes, W1: float = 1.0, W2: float = 1.0):
        print('op:',W1)
        print('op1:' ,W2)
        loop_weights = []
        for size in sizes:
            if size < 0.4:
                loop_weights.append((W2 * 0.2, W2 * 0.2))
            else:
                loop_weights.append((W1 * 0.8, W2 * 0.8))
            # print('lw1:' ,loop_weights)
            
        return loop_weights


    def operations_intergenic_regions(self, intergenic_regions):
        list_of_legal_operations = self.node.get_legal_operations()
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
                elif len(operation) == 2 and isinstance(operation[0][1], tuple):
                    start, end = operation
                    if isinstance(start, tuple):
                        new_start = start[0]
                        new_start_end = start[1]
                    if isinstance(end, tuple):
                        new_end_start = end[0]
                        new_end = end[1] 
                    operations_with_intergenic.append((((new_start[0], random.choice(intergenic_regions), new_start[1]), (new_start_end[0], random.choice(intergenic_regions), new_start_end[1])), ((new_end_start[0], random.choice(intergenic_regions), new_end_start[1]), (new_end[0], random.choice(intergenic_regions), new_end[1]))))
                
            else:
                operations_with_intergenic.append(operation)
            
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
                print(op_weight)

        return operation_weight, op_weight






    

# Example usage:
genomeA = [[1,2,3,4,15],[-8,-7,6,-5,-14,-13,-12],[9,11],[-20,-19,-18,-17,-16,-32,10,-31,-30,-29,-28,-27,33],[21,22,23,24,25,26],[-33],[34,35,36,37,38,39,40]]
genomeB = [[1,2,3,4,5,6,7,8],[9,10,11],[12,13,14,15],[16,17,18,19,20],[21,22,23,24,25,26],[27,28,29,30,31,32,33,33],[34,35,36,37,38,39,40]]

adjacencies = Extremities_and_adjacencies()
# adjacencies_list = adjacencies.ordered_and_sorted_adjacencies(genomeB)
# adjacencies_genomeA = adjacencies.ordered_and_sorted_adjacencies(genomeA)
adjacencies_genomeB = adjacencies.ordered_and_sorted_adjacencies(genomeB)
print(adjacencies_genomeB)
target_node = Node(adjacencies_genomeB)
list_of_legal_operations = target_node.get_legal_operations(adjacencies_genomeB)
#genomeB = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]]
# genomeB = [[6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]]

# data_gen = DataGenerator()
# genomeA = data_gen.check_genes(genomeA)
# genomeB = data_gen.check_genes(genomeB)
# print("checked : " + str(genomeA))
# intergenic_generator = IntergenicGenerator(genomeA, genomeB)

# intergenic_gen = IntergenicGenerator. inter_generator(genomeB)
# intergenic_gen = IntergenicGenerator.inter_generator(genomeA)
# adjacencies_with_intergenic = intergenic_gen.inter_generator(genomeB)
# intergenic_regions = intergenic_gen.inter_generator()
# adjacencies_intergenic = intergenic_gen.adjacencies_intergenic_regions(intergenic_regions)

# print(adjacencies_intergenic)




#old code for reference
#class Constraints:
#     def __init__(self, genome=None):
#         self.genome = genome
        

#     def inter_generator(self, adjacencies_list):
#         intergenic_regions = []
#         for i in adjacencies_list:
#             random_bp = random.randint(1, 10)
#             intergenic_regions.append('*' + str(random_bp))
#         return intergenic_regions

#     def operation_intergenic_regions(self, intergenic_regions, list_of_legal_operations):
#         operations_with_intergenic = []
#         for operation in list_of_legal_operations:
#             if isinstance(operation, tuple):
#                 if len(operation) == 3 and isinstance(operation[0], tuple):
#                     start_tuple, start, end = operation
#                     start_tuple_with_intergenic = (start_tuple[0], random.choice(intergenic_regions), start_tuple[1])
#                     operations_with_intergenic.append((start_tuple_with_intergenic, start, end))
#                 elif len(operation) == 3 and isinstance(operation[-1], tuple):
#                     start, end, end_tuple = operation
#                     end_tuple_with_intergenic = (end_tuple[0], random.choice(intergenic_regions), end_tuple[1])
#                     operations_with_intergenic.append((start, end, end_tuple_with_intergenic))
#                 elif len(operation) == 2 and isinstance(operation[0][1], tuple):
#                     start, end = operation
#                     if isinstance(start, tuple):
#                         new_start = start[0]
#                         new_start_end = start[1]
#                     if isinstance(end, tuple):
#                         new_end_start = end[0]
#                         new_end = end[1] 
#                     operations_with_intergenic.append((((new_start[0], random.choice(intergenic_regions), new_start[1]), (new_start_end[0], random.choice(intergenic_regions), new_start_end[1])), ((new_end_start[0], random.choice(intergenic_regions), new_end_start[1]), (new_end[0], random.choice(intergenic_regions), new_end[1]))))
                   
#             else:
#                 operations_with_intergenic.append(operation)
#         print("OWR:" , operations_with_intergenic)
#         return operations_with_intergenic
    

#     def intergenic_weight(self, net_work, intergenic_regions, list_of_legal_operations):
#         individual_weights_and_irs = []

#         for operation in list_of_legal_operations:
#             if not isinstance(operation, tuple):
#                 continue

#             operation_weight = net_work.operation_weight
#             op_weight = net_work.op_weight

#             IRs = [] 
#             def process_element(element):
#                 nonlocal operation_weight, op_weight
#                 if isinstance(element, tuple) and len(element) == 3:
#                     integer_part, string_part, float_part = element
#                     if isinstance(string_part, str) and string_part.startswith('*'):
#                         try:
#                             IR = int(string_part[1:])  
#                             IRs.append(IR)
#                             print("IR:", IR)
#                             if IR > 5:
#                                 operation_weight *= 0.8
#                                 op_weight *= 0.8
#                             else:
#                                 operation_weight *= 0.2
#                                 op_weight *= 0.2
#                         except ValueError:
#                             print(f"Invalid integer value in string: {string_part}")
#                 elif isinstance(element, tuple):
#                     for sub_element in element:
#                         process_element(sub_element)

#             for element in operation:
#                 process_element(element)

#             individual_weights_and_irs.append((operation_weight, op_weight, IRs))
#             #print('Operation Weight:', operation_weight, 'Op Weight:', op_weight, 'IRs:', IRs)
        
#         return individual_weights_and_irs
    



#     def longest_chromosome_genes(self):
#         longest_chromosome_length = 0
#         for chromosome in self.genome:
#             chromosome_length = len(chromosome)
#             if chromosome_length > longest_chromosome_length:
#                 longest_chromosome_length = chromosome_length
#         return longest_chromosome_length
    


#     def calculate_loop_size(self):
#         sizes = []
#         num_genes = self.longest_chromosome_genes()
#         if num_genes == 0:
#             return sizes
        
#         for gene_index in range(1, num_genes + 1):
#             loop_size = gene_index / num_genes
#             sizes.append(loop_size)
            
#         return sizes
    
#     def calculate_average_angle(self, sizes):
#         num_genes = self.longest_chromosome_genes()
#         average_angles = []
#         for size in sizes:
#             average_angle = (num_genes / size )
#             average_angles.append(average_angle)
#         return average_angles





#     def calculate_loop_weight(self, sizes, operation_weight, op_weight):
#         loop_weight = []
#         for size in sizes:
#             if size < 4:
#                 loop_weight.append(operation_weight * 0.2)
#                 loop_weight.append(op_weight * 0.2)
#             else:
#                 loop_weight.append(operation_weight * 0.4)
#                 loop_weight.append(op_weight * 0.4)
#         return loop_weight

    

    # def calculate_loop_weight(self, sizes):
    #     loop_weight = []
    #     for size in sizes:
    #         if size <= 0.4:
    #             loop_weight.append(0.2)
    #         else:
    #             loop_weight.append(0.8)
    #     print("lw: ", loop_weight)
    #     return loop_weight


#     def generate_data(self):
#         sizes = self.calculate_loop_size()
#         average_angles = self.calculate_average_angle(sizes)
#         weights_3D = self.calculate_loop_weight(sizes)
#         return sizes, average_angles, weights_3D

#     def plot_data(self, sizes, average_angles, weights_3D):
#         cmap = plt.get_cmap('RdBu')
#         sm = ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=min(weights_3D), vmax=max(weights_3D)))
#         sm.set_array([])

#         for i in range(len(sizes) - 1):
#             plt.plot([sizes[i], sizes[i + 1]], [average_angles[i], average_angles[i + 1]], 
#                     color=cmap(weights_3D[i]), marker='o')

#         plt.title('Relationship between Loop Size and Angle of the 3D spatial arrangement of chromosomes')
#         plt.xlabel('Loop Size(bp)')
#         plt.ylabel('Angle')
#         plt.colorbar(sm, label='Weight')
#         plt.grid(False)
#         plt.show()

#     def main(self):
#         sizes, average_angles, weights_3D = self.generate_data()
#         self.plot_data(sizes, average_angles, weights_3D)

# if __name__ == "__main__":
#     genome = [
#         [1, 2, 3, 4],          # Chromosome 1
#         [1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 14, 15, 16, 18, 20, 22],       # Chromosome 2
#         [1, 2, 3, 4, 5, 6, 14, 15, 78, 23, 25, 28, 32, 36, 19, 28, 42, 48, 50]  # Chromosome 3
#     ]
#     spatial_3d_weight = Constraints()
#     spatial_3d_weight.main()





# ForeignDNA original code

#from random import randint

#class Foreign_DNA:

    # def __init__(self):
    #     self.state = []


    
    # def foreign_dna_pool(self, source_genome, target_genome):
        
    #     """
    #     Finds the difference in genes between the source and target genomes. Creates a pool of random integers and
    #     generates foreign DNA fragments from the pool. Fragments are tagged with an underscore(_) for identification
    #     in the source genome and to be ignored by the delete function during the transformation process.
        
    #     :param source: The source genome.
    #     :param target: The target genome.
    #     :return: A list of foreign DNA fragments.
    #     """
       
    #     source_genome = []
    #     target_genome = []


    #     for chromosome in source_genome:
    #         for i in range(len(chromosome)):
    #             if isinstance(chromosome[i],int):
    #                 source_genome.append(int(chromosome[i]))
    #             elif isinstance(chromosome[i],str) and "_" in chromosome[i]:
    #                 if len(chromosome[i])==2:
    #                     gene = chromosome[i]
    #                     source_genome.append(int(gene[:1]))
    #                 elif len(chromosome[i])==3:
    #                     gene = chromosome[i]
    #                     source_genome.append(int(gene[:2]))
        
    #     for chromosome in target_genome:
    #         for i in range(len(chromosome)):
    #             if isinstance(chromosome[i],int):
    #                 target_genome.append(int(chromosome[i]))

       
    #     difference = list(set(target_genome) - set(source_genome))

    #     if len(difference) > 0:
    #         # define the ratio (1/2)
    #         number_of_random_ints = (len(difference) * 2) - (len(difference)) 
            
    #         foreign_dna = []
    #         count = 0
    #         while count < (number_of_random_ints):
    #             gene = randint(1, 10)
    #             if len(foreign_dna) >= 1:
    #                 if gene not in foreign_dna:
    #                     foreign_dna.append(gene)
    #                     count += 1
    #             else:
    #                 foreign_dna.append(gene)

           
    #         foreign_dna = difference + foreign_dna
    #         foreign_dna = list(set(foreign_dna))
    #         if len(foreign_dna) < ((len(difference)) * 2):  
    #             count = len(foreign_dna)
    #             while (len(foreign_dna) < ((len(difference)) * 2)):
    #                 gene = randint(1, 10)
    #                 if gene not in foreign_dna:
    #                     foreign_dna.append(gene)
    #                     count += 1
            
    #         number_of_fragments = randint(1,10)
    #         len_fragments = 1
            
           
    #         list_of_fragments = []
    #         fragment = []
    #         for j in range(number_of_fragments):
    #             for i in range(len_fragments):
    #                 choice = randint(0,len(foreign_dna)-1)
    #                 fragment.append(foreign_dna[choice])
               
    #             if j > 0 and fragment not in list_of_fragments:
    #                 list_of_fragments.append(fragment)
    #             else:
    #                 j -= 1
    #             fragment = []

    #         check = True
    #         for fragmt in list_of_fragments:
    #             if difference in fragmt:
    #                 check = False
    #         if check == True:
    #             final_fragment = difference[:]
           
    #             while len(final_fragment) <= len(difference)+1:
    #                 selected_gene =  foreign_dna[randint(0, len(foreign_dna)-1)]
    #                 if selected_gene not in final_fragment:
    #                     final_fragment.append(selected_gene)
    #             list_of_fragments.append(final_fragment)

    #         for i in list_of_fragments:
    #             fragment = i
    #             for j in range(len(fragment)):
    #                 fragment[j] = str(fragment[j])+"_"
    #         return list_of_fragments

    #     else:
           
    #         number_of_random_ints = randint(1,10)

            
    #         foreign_dna = []
    #         count = 0
    #         while count < (number_of_random_ints):
    #             gene = randint(1, 10)
    #             if len(foreign_dna) >= 1:
    #                 if gene not in foreign_dna:
    #                     foreign_dna.append(gene)
    #                     count += 1
    #             else:
    #                 foreign_dna.append(gene)
            
    #         number_of_fragments = randint(1,10)
    #         len_fragments = 1
    #         list_of_fragments = []
    #         fragment = []
    #         for j in range(number_of_fragments):
    #             for i in range(len_fragments):
    #                 choice = randint(0,len(foreign_dna)-1)
    #                 fragment.append(foreign_dna[choice])
                
    #             if j > 0 and fragment not in list_of_fragments:
    #                 list_of_fragments.append(fragment)
                   
    #             else:
    #                 j -= 1
    #             fragment = []

    #         for i in list_of_fragments:
    #             fragment = i
    #             for j in range(len(fragment)):
    #                 fragment[j] = str(fragment[j])+"_"

    #         return list_of_fragments
    

     # def insert_foreign_dna(self, source_genome, fragment):
    #     """
    #     Adds/inserts a fragment of foreign DNA to the source genome. The foreign fragment is identified with an
    #     underscore(_) attached to an integer. The path of foreign DNA fragments can be traced through the evolutionary
    #     journey of the source genome into the target genome.
        
    #     :param source_genome: The source genome.
    #     :param fragment: The foreign DNA fragment to insert.
    #     :return: The updated source genome and information about the insertion.
    #     """
    #     list_of_mutation_points = []
    #     list_of_mutation_points_genome = []

    #     for genes_with_intergenic_approved in source_genome:
    #         for i in range(len(genes_with_intergenic_approved)):
    #             if (isinstance(genes_with_intergenic_approved[i], str) and len(genes_with_intergenic_approved[i]) > 1) and '*' in genes_with_intergenic_approved[i]:
    #                 list_of_mutation_points.append(i+1)

    #         list_of_mutation_points_genome.append(list_of_mutation_points)
    #         list_of_mutation_points = []
        
    #     fragment_with_intergenic_regions = []
    #     length = len(fragment)
    #     for j in range(len(fragment)):
    #         if j == 0 :
    #             random_bp = randint(6,10)
    #             region = '*' + str(random_bp)
    #             fragment_with_intergenic_regions.append(region)
    #         random_bp = randint(6,10)
    #         start = fragment[j]
    #         region = '*' + str(random_bp)
    #         fragment_with_intergenic_regions.append(start)
    #         if j != length-1:
    #             fragment_with_intergenic_regions.append(region)

        
    #     for i in range(len(fragment_with_intergenic_regions)):
    #         if i % 2 == 0 or i == 0:
    #             region = fragment_with_intergenic_regions[i]
               
    #             if len(region) > 2:
    #                 value = region[1]+region[2]
    #             else:
    #                 value = region[1]
    #             if int(value) < 5:
    #                 fragment_with_intergenic_regions[i] = '*'


    #     position_applicable_region_chromosome = []
    #     source_chromosome = []
    #     rand_chromosome = []

    #     while len(position_applicable_region_chromosome) == 0 :
    #         rand_chromosome = randint(0,len(list_of_mutation_points_genome)-1)
    #         position_applicable_region_chromosome = list_of_mutation_points_genome[rand_chromosome]
    #         source_chromosome = source_genome[rand_chromosome]
        

    #     rand_position = randint(0, len(position_applicable_region_chromosome)-1)
    #     position = position_applicable_region_chromosome[rand_position]

    #     mutated = []
    #     if position == 0: 
    #         mutated = fragment_with_intergenic_regions + source_chromosome
    #     else:  
    #         mutated = source_chromosome + fragment_with_intergenic_regions

    #     source_genome[rand_chromosome] = mutated
        
    #     operation = {
    #                 "Mut": 'F_DNA',
    #                 "Chr": rand_chromosome,
    #                 "Gene": fragment_with_intergenic_regions,
    #                 "Pos": position,
    #                 #"Mutated Chromosome": fragment_with_intergenic_regions,
    #                 "Genome after mutation": source_genome,
    #             }
    #     return source_genome,  [operation]







    # target_genome = [[1, 2],[3, 4, 5],[6, 7],[8, 9, 10],[11],[12, 13, 14],[15, 16, 17, 18],[19, 20],[21, 22, 23]]
    # source_genome = [[1, 4, 2],[3, 5],[6],[8],[9, -13, 11],[12, 14],[15, 17, 22, 18],[19, 16, 20],[21, 7, 10, 23]]
