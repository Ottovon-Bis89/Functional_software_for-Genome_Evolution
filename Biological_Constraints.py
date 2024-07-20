import random
from Rearrangement_extremities_and_adjacencies import Extremities_and_adjacencies
from new_Node import Node


class Constraints:
    def __init__(self, genomeB):
         self.genome = genomeB
       

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
            average_angle = (num_genes / size)
            average_angles.append(average_angle)
        return average_angles
    
    def calculate_loop_weight(self, sizes):
        W1, W2 = 1.0, 1.0
        self.loop_weights = [(W1 * 0.2, W2 * 0.2) if size < 0.4 else (W1 * 0.8, W2 * 0.8) for size in sizes]
        return self.loop_weights


    def inter_generator(self, adjacencies_list):
        intergenic_regions = []
        for i in adjacencies_list:
            random_bp = random.randint(1, 10)
            intergenic_regions.append('*' + str(random_bp))
        return intergenic_regions

    # change param list_of_legal_operations to adjacenciesA/B in order to create Node object and generate list of legal ops within the function
    def operations_intergenic_regions(self, intergenic_regions, adjacencies_genomeA, adjacencies_genomeB):
        Start_node = Node(adjacencies_genomeA)
        list_of_legal_operations = Start_node.get_legal_operations(adjacencies_genomeB)

        operations_with_intergenic = []

        for operation in list_of_legal_operations:
            if isinstance(operation, tuple):
                if len(operation) == 3:
                    if isinstance(operation[0], tuple):
                        start_tuple, start, end = operation
                        start_tuple_with_intergenic = (
                            start_tuple[0],
                            random.choice(intergenic_regions),
                            start_tuple[1]
                        )
                        operations_with_intergenic.append((start_tuple_with_intergenic, start, end))
                    elif isinstance(operation[2], tuple):
                        start, end, end_tuple = operation
                        end_tuple_with_intergenic = (
                            end_tuple[0],
                            random.choice(intergenic_regions),
                            end_tuple[1]
                        )
                        operations_with_intergenic.append((start, end, end_tuple_with_intergenic))
                elif len(operation) == 2 and isinstance(operation[0][1], tuple):
                    start, end = operation
                    new_start = (
                        (start[0][0], random.choice(intergenic_regions), start[0][1]),
                        (start[1][0], random.choice(intergenic_regions), start[1][1])
                    )
                    new_end = (
                        (end[0][0], random.choice(intergenic_regions), end[0][1]),
                        (end[1][0], random.choice(intergenic_regions), end[1][1])
                    )
                    operations_with_intergenic.append((new_start, new_end))
            else:
                operations_with_intergenic.append(operation)

        return operations_with_intergenic


    def intergenic_weight(self, intergenic_regions, operations_with_intergenic):
        """Calculate intergenic weight based on intergenic regions and operations."""
        sizes = self.calculate_loop_size()
        self.loop_weights = self.calculate_loop_weight(sizes)

        if not hasattr(self, 'loop_weights'):
            raise AttributeError("loop_weights has not been calculated yet.")
        
        operation_weights_dict = {}

        for operation in operations_with_intergenic:
            if not isinstance(operation, tuple):
                continue

            IRs = []
            W1, W2 = 0, 0

            def process_element(element):
                nonlocal W1, W2  
                if isinstance(element, tuple) and len(element) == 3:
                    parts = list(element)
                    string_part = None
                    for part in parts:
                        if isinstance(part, str) and part.startswith('*'):
                            string_part = part
                            parts.remove(part)
                            break

                    if string_part is not None:
                        integer_part, float_part = parts
                        try:
                            IR = int(string_part[1:])
                            IRs.append(IR)
                            
                            if len(IRs) == 4 and IRs[0] >= 5 and IRs[1] >= 5:
                                W1 = W2 = self.loop_weights[-1][0] * 0.8
                            elif len(IRs) == 1 and IRs[0] >= 5:
                                W1 = W2 = self.loop_weights[-1][0] * 0.8
                            else:
                                W1 = W2 = self.loop_weights[0][0] * 0.2
                        except ValueError:
                            print(f"Invalid integer value in string: {string_part}")
                elif isinstance(element, tuple):
                    for sub_element in element:
                        process_element(sub_element)

            for element in operation:
                process_element(element)

            operation_weights_dict[operation] = {"W1": W1, "W2": W2, "IRs": IRs}

        return operation_weights_dict





























