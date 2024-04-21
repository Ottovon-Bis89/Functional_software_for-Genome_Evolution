import random
from Network_wrDCJ import Network
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.cm import ScalarMappable
from Intergenic_region_generator import Constraint


net_work = Network()
# operation_weight, op_weight = net_work.build_hash_table()

class Constraints:
    def __init__(self):
        self.genome = genome
        pass

    def inter_generator(self, adjacencies_list):
        intergenic_regions = []
        for i in adjacencies_list:
            random_bp = random.randint(1, 10)
            intergenic_regions.append('*' + str(random_bp))
        return intergenic_regions

    def operation_intergenic_regions(self, intergenic_regions, list_of_legal_operations):
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

    def intergenic_weight(self, net_work, intergenic_regions, list_of_legal_operations):
        # operation_weight = net_work.operation_weight
        # op_weight = net_work.op_weight
        
        for operation in list_of_legal_operations:
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

            if bp >= 5:
                operation_weight = 0.8 * operation_weight
                print('op:', operation_weight)
                op_weight = 0.8 * op_weight
            else:
                operation_weight = 0.2 * operation_weight
                op_weight = 0.2 * op_weight
                print(op_weight)

        return operation_weight, op_weight

    def longest_chromosome_genes(self):
        longest_chromosome_length = 0
        for chromosome in self.genome:
            chromosome_length = len(chromosome)
            if chromosome_length > longest_chromosome_length:
                longest_chromosome_length = chromosome_length
        return longest_chromosome_length
    


    def calculate_loop_size(self):
        sizes = []
        num_genes = self.longest_chromosome_genes()
        if num_genes == 0:
            return sizes
        
        for gene_index in range(1, num_genes + 1):
            loop_size = gene_index / num_genes
            sizes.append(loop_size)
            
        return sizes
    
    def calculate_average_angle(self, sizes):
        num_genes = self.longest_chromosome_genes()
        average_angles = []
        for size in sizes:
            average_angle = (num_genes / size )
            average_angles.append(average_angle)
        return average_angles




    # def calculate_weight(self, Loop_size):

    #     if Loop_size <= 0.4:
    #         operation_weight = 0.2 * operation_weight
    #         op_weight = 0.2 * op_weight
            
    #     else:
    #         operation_weight = 0.8 * operation_weight
    #         op_weight = 0.8 * op_weight

    #     return  operation_weight, op_weight
    
    
    # def calculate_weight(self, Loop_size):
    #     if Loop_size <= 0.4:
    #         return 0.2
    #     else:
    #         return 0.8


    # def calculate_loop_weight(self, sizes, operation_weight, op_weight):
    #     loop_weight = []
    #     for size in sizes:
    #         if size < 4:
    #             loop_weight.append(operation_weight * 0.2)
    #             loop_weight.append(op_weight * 0.2)
    #         else:
    #             loop_weight.append(operation_weight * 0.4)
    #             loop_weight.append(op_weight * 0.4)
    #     return loop_weight

    

    def calculate_loop_weight(self, sizes):
        loop_weight = []
        for size in sizes:
            if size <= 0.4:
                loop_weight.append(0.2)
            else:
                loop_weight.append(0.8)
        return loop_weight


    def generate_data(self):
        sizes = self.calculate_loop_size()
        average_angles = self.calculate_average_angle(sizes)
        weights_3D = self.calculate_loop_weight(sizes)
        return sizes, average_angles, weights_3D

    def plot_data(self, sizes, average_angles, weights_3D):
        cmap = plt.get_cmap('RdBu')
        sm = ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=min(weights_3D), vmax=max(weights_3D)))
        sm.set_array([])

        for i in range(len(sizes) - 1):
            plt.plot([sizes[i], sizes[i + 1]], [average_angles[i], average_angles[i + 1]], 
                    color=cmap(weights_3D[i]), marker='o')

        plt.title('Relationship between Loop Size and Angle of the 3D spatial arrangement of chromosomes')
        plt.xlabel('Loop Size(bp)')
        plt.ylabel('Angle')
        plt.colorbar(sm, label='Weight')
        plt.grid(False)
        plt.show()

    def main(self):
        sizes, average_angles, weights_3D = self.generate_data()
        self.plot_data(sizes, average_angles, weights_3D)

if __name__ == "__main__":
    genome = [
        [1, 2, 3, 4],          # Chromosome 1
        [1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 14, 15, 16, 18, 20, 22],       # Chromosome 2
        [1, 2, 3, 4, 5, 6, 14, 15, 78, 23, 25, 28, 32, 36, 19, 28, 42, 48, 50]  # Chromosome 3
    ]
    spatial_3d_weight = Constraints()
    spatial_3d_weight.main()

