
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.cm import ScalarMappable
from Intergenic_region_generator import Constraint

inter_weight = Constraint()
operation_weight, op_weight = inter_weight.intergenic_weight()





class Spatial3DWeight:
    def __init__(self, genome):
        self.genome = genome
        pass

    def generate_chromosome_genes(self, num_genes):
        return list(range(1, num_genes + 1))

    def calculate_average_angle(self, num_genes, Loop_size):
        return num_genes / Loop_size

    def calculate_num_loops(self, num_genes):
        num_loops = 0
        divisor = 1
        
        while divisor <= num_genes:
            num_loops += 1
            divisor *= 2
        return num_loops

    def calculate_weight(self, Loop_size):
        if Loop_size <= 4:
            operation_weight = 0.2 * operation_weight
            op_weight = 0.2 * op_weight
            
        else:
            operation_weight = 0.8 * operation_weight
            op_weight = 0.8 * op_weight
        return  operation_weight, op_weight

    def generate_data(self, num_genes):
        sizes = []
        average_angles = []
        Weights_3D = []

        for Loop_size in range(1, num_genes + 1):
            average_angle = self.calculate_average_angle(num_genes, Loop_size)
            weight = self.calculate_weight(Loop_size)
            sizes.append(Loop_size)
            average_angles.append(average_angle)
            Weights_3D.append(weight)

        return sizes, average_angles, Weights_3D
    

    def plot_data(self, sizes, average_angles, Weights_3D):
        cmap = plt.get_cmap('RdBu')
        sm = ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=min(Weights_3D), vmax=max(Weights_3D)))
        sm.set_array([])

        for i in range(len(sizes) - 1):
            plt.plot([sizes[i], sizes[i + 1]], [average_angles[i], average_angles[i + 1]], 
                     color=cmap(Weights_3D[i]), marker='o')

        plt.title('Relationship between Loop Size and Angle of the 3D spatial arrangement of chromosomes')
        plt.xlabel('Loop Size(bp)')
        plt.ylabel('Average Angle')
        plt.colorbar(sm, label='Weight')
        plt.grid(True)
        plt.show()

    def main(self):
        num_genes = max(len(chromosome) for chromosome in self.genome)
        sizes, average_angles, Weights_3D = self.generate_data(num_genes)
        self.plot_data(sizes, average_angles, Weights_3D)

if __name__ == "__main__":
    genome = [
        [1, 2, 3, 4],          # Chromosome 1
        [1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 14, 15, 16, 18, 20, 22],       # Chromosome 2
        [1, 2, 3, 4, 5, 6],    # Chromosome 3
    ]
    spatial_3d_weight = Spatial3DWeight(genome)
    spatial_3d_weight.main()
