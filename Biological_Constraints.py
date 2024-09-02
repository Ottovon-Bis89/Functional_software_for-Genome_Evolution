import random
from Path_node import Node


class Constraints:
    def __init__(self, genomeB):
         self.genome = genomeB
       

    def longest_chromosome_genes(self):
        """
        Calculates the length of the longest chromosome in the genome.

        This method iterates through each chromosome in the genome and
        determines the length of the longest chromosome.

        @return: The length of the longest chromosome.
        @rtype: int
        """
        longest_chromosome_length = 0
        for chromosome in self.genome:
            chromosome_length = len(chromosome)
            if chromosome_length > longest_chromosome_length:
                longest_chromosome_length = chromosome_length
        return longest_chromosome_length
  
    def calculate_loop_size(self):
        """
    Calculates the loop sizes for the genes in the longest chromosome.
    
    @return List of loop sizes as a fraction of the total number of genes in the longest chromosome.
    """
        sizes = []
        num_genes = self.longest_chromosome_genes()
        if num_genes == 0:
            return sizes
        for gene_index in range(1, num_genes + 1):
            loop_size = gene_index / num_genes
            sizes.append(loop_size)
           
        return sizes

    def calculate_average_angle(self, sizes):
        """
        Calculates the average angle for each size provided.

        This method computes the average angle by dividing the number of genes
        in the longest chromosome by each size in the given list of sizes.

        Args:
            sizes (list): A list of sizes for which the average angles need to be calculated.

        Returns:
            list: A list of average angles corresponding to each size in the input list.
        """
        num_genes = self.longest_chromosome_genes()
        average_angles = []
        for size in sizes:
            average_angle = (num_genes / size)
            average_angles.append(average_angle)
        return average_angles
    
    def calculate_loop_weight(self, sizes):
        """
        Calculate loop weights based on the given sizes.

        This method calculates the loop weights for each size in the input list `sizes`.
        For each size, if the size is less than or equal to 0.4, the weight is set to 
        (W1 * 0.8, W2 * 0.8). Otherwise, the weight is set to (W1 * 0.2, W2 * 0.2).

        Args:
            sizes (list of float): A list of size values.

        Returns:
            list of tuple: A list of tuples containing the calculated weights.

        Example:
            sizes = [0.3, 0.5, 0.4]
            result = calculate_loop_weight(sizes)
            # result will be [(0.8, 0.8), (0.2, 0.2), (0.8, 0.8)]
        """
        W1, W2 = 1.0, 1.0
        # Multiply the weight by the probabilities of recombination at that loop depending on the loop size.
        self.loop_weights = [(W1 * 0.8, W2 * 0.8) if size <= 0.4 else (W1 * 0.2, W2 * 0.2) for size in sizes]
        return self.loop_weights


    def inter_generator(self, adjacencies_list):
        """
        Generates a list of intergenic regions with random base pairs.

        Args:
            adjacencies_list (list): A list of adjacency elements.

        Returns:
            list: A list of intergenic regions, each prefixed with an asterisk and containing a random number of base pairs.
        """
        intergenic_regions = []
        for i in adjacencies_list:
            random_bp = random.randint(1, 10)
            intergenic_regions.append('*' + str(random_bp))
        return intergenic_regions


    def operations_intergenic_regions(self, intergenic_regions, adjacencies_genomeA, adjacencies_genomeB):
        """
        Generates a list of operations involving intergenic regions based on the legal operations 
        between two genomes.

        Parameters:
        - intergenic_regions (list): A list of intergenic regions to be used in the operations.
        - adjacencies_genomeA (list): A list of adjacencies for genome A.
        - adjacencies_genomeB (list): A list of adjacencies for genome B.

        Returns:
        - list: A list of operations where each operation  includes intergenic regions.

        The method first retrieves all legal operations between the two genomes. For each legal operation, 
        it checks if the operation involves tuples of adjacencies and modifies these tuples to include 
        randomly chosen intergenic regions where appropriate. The updated operations are then returned 
        in a list.
        """
        Start_node = Node(adjacencies_genomeA)
        list_of_legal_operations = Start_node.get_legal_operations(adjacencies_genomeB)

        operations_with_intergenic = []

        for operation in list_of_legal_operations:
            if isinstance(operation, tuple):
                # If the operation is made up of 3 tuples of adjacencies.
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

                        # If the operation is made up of 2 tuples of adjacencies.
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
        """
        Calculate the weight for each operation involving intergenic regions based on 
        the loop weights and sizes.

        Parameters:
        - intergenic_regions (list): A list of intergenic regions.
        - operations_with_intergenic (list): A list of operations that include intergenic regions.

        Returns:
        - dict: A dictionary where the keys are operations and the values are dictionaries 
                containing weights ('W1' and 'W2') and intergenic regions ('IRs').

        This method calculates the weight for each operation by analyzing the intergenic regions 
        present in the operation. It uses predefined loop weights and sizes to determine the weight 
        values. The weights are based on the presence and values of intergenic regions in the operation.
        """
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
                                W1 = W2 = self.loop_weights[-1][0] * 0.2
                            elif len(IRs) == 1 and IRs[0] >= 5:
                                W1 = W2 = self.loop_weights[-1][0] * 0.2
                            else:
                                W1 = W2 = self.loop_weights[0][0] * 0.8
                        except ValueError:
                            print(f"Invalid integer value in string: {string_part}")
                elif isinstance(element, tuple):
                    for sub_element in element:
                        process_element(sub_element)

            for element in operation:
                process_element(element)

            operation_weights_dict[operation] = {"W1": W1, "W2": W2, "IRs": IRs}

        return operation_weights_dict





























