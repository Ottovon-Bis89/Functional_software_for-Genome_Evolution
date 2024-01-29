from random import randint
import math
from logger import log
import sys

class MutationOperations:
   
    def __init__(self):
        self.state = []

    def mutation_legal_operations(self, source_genome, target_genome):
        '''
         Performs acceptable mutation operations on a source genome to transform it to targeted genome.

        This method applies various mutation checks and operations on the source_genome
        with respect to the target_genome.

        Args:
            source_genome (list): The original genetic data to be mutated.
            target_genome (list): The target genetic data for mutation.

        Returns:
            list or tuple: Depending on the mutation operations, returns a list of mutated genomes
            and a boolean flag indicating whether any mutation should be performed.
        '''

        log.debug("mutation_legal_operations")
        new_source_genome, new_source_genome_with_positions = self.modify_source_genome(source_genome)

        insertion_genome, new_source_genome_with_positions = self.check_insertion(
            new_source_genome, target_genome, new_source_genome_with_positions
        )
        deletion_genome = self.check_deletion(target_genome, new_source_genome_with_positions)
        duplication_genome = self.check_duplication(new_source_genome, target_genome)

        do_mutation = self.choose_mutation(insertion_genome, deletion_genome, duplication_genome)

        if all(len(new_source_genome) > 0 for new_source_genome in [insertion_genome, deletion_genome, duplication_genome]):
            return [insertion_genome, deletion_genome, duplication_genome], do_mutation
        else:
            # If any of the mutation lists is empty, only perform the mutation
            return do_mutation


    def modify_source_genome(self, source_genome):
        """
        Modifies the provided source genome by filtering out genes containing underscores or asterisks.
        This method creates two lists: one with the modified source genome and another with positions of valid genes.

        :param source_genome: The original source genome to be modified.
        :type source_genome: list[list[object]]

        :return: A tuple containing two lists - the modified source genome and positions of valid genes.
        :rtype: tuple[list[list[object]], list[list[tuple[int, object]]]
        """
        log.debug("modify_source_genome")
        new_source_genome = []
        new_source_genome_with_positions = []

        for chromosome in source_genome:
            new_chromosome_positions_with_genes = []
            new_chromosome = []

            for i in range(len(chromosome)):
                gene = chromosome[i]
                if isinstance(gene, str) and "_" not in gene and "*" not in gene:
                    new_chromosome_positions_with_genes.append((i, gene))

            for gene in chromosome:
                if isinstance(gene, str) and "_" not in gene and "*" not in gene:
                    new_chromosome.append(gene)
                else:
                    new_chromosome.append(gene)

            new_source_genome.append(new_chromosome)
            new_source_genome_with_positions.append(new_chromosome_positions_with_genes)

        return new_source_genome, new_source_genome_with_positions


    
    def check_insertion(self, source_genome, target_genome, new_source_genome):

        """
        Checks and identifies insertion mutations required to transform a source genome into a target genome
        with respect to a new source genome.
        The function performs the following steps:
        1. Initializes an empty list to store the insertion mutations required.
        2. Iterates over the chromosomes in the target genome.
        3. Checks if the target and source genomes have the same number of chromosomes.
        4. If the length of the target genome is less than or equal to the length of the new source genome,
        it compares chromosomes at the same positions for differences.
        5. Iterates over the genes in target chromosomes and checks if target genes are in the isolated source chromosome.
        Adds the required insertion mutation to the list of insertion mutations.
        6. If the length of the target genome is greater than the source genome, copies over the extra chromosome
        from the target genome to the source genome.

        @param sourceGenome The original source genome.
        @param targetGenome The target genome to be transformed into.
        @param newSourceGenome The new source genome for comparison.
        """
        log.debug("check_insertion")
        insertion_genome = []

       
        for j in range(len(target_genome)):
            insertion_target = []

            
            if j < len(new_source_genome):
                target_chromosome = target_genome[j]
                new_chromosome = source_genome[j]
            else:
                new_chromosome = []
            target_chromosome = target_genome[j]

           
            for i in range(len(target_chromosome)):
                if ('*' not in str(target_chromosome[i])) and ((target_chromosome[i]) not in new_chromosome):
                    insertion_target.append((i, target_chromosome[i]))
                # elif ((target_chromosome[i]) in new_chromosome) and not ((new_chromosome.index(target_chromosome[i])) == math.floor(i/2)):
                #     insertion_target.append((i, target_chromosome[i]))


            insertion_genome.append(insertion_target)

    
        if len(target_genome) > len(source_genome):
            for missing_chromosome in range(len(source_genome), len(target_genome)):
                new_chromosome = target_genome[missing_chromosome]
                source_genome.append(new_chromosome)
        

        return insertion_genome, new_source_genome





    def check_deletion(self, target_genome, new_source_genome_with_positions):
        
        """
        Checks and identifies deletion mutations required to transform a target genome into a new source genome
        with respect to gene positions in the new source genome.

        The function performs the following steps:
        1. Logs a debug message indicating the start of the deletion check.
        2. Initializes empty lists to store deletion information for the entire genome and individual chromosomes.
        3. If the target genome has more chromosomes than the new source genome with positions,
           pads the new source genome with empty lists to match the chromosome count.
        4. Iterates over each chromosome in the target genome and compares it with the corresponding chromosome
           in the new source genome using gene positions.
        5. Identifies genes in the new source genome that are not present in the target chromosome
           and records their positions and values as deletion mutations.
        6. Appends the deletion information for each chromosome to the deletion genome list.
        7. If the target genome has more chromosomes than the new source genome with positions,
           identifies and records the entire target chromosome as a deletion mutation.

        @param targetGenome The target genome to be transformed.
        @param newSourceGenomeWithPositions The new source genome with gene positions for comparison.
        @return A list containing deletion information for each chromosome in the genome.
        """

        log.debug("check_deletion")
        
        deletion_genome = []
        deletion_target = []

        if len(target_genome) > len(new_source_genome_with_positions):
            difference = len(target_genome) - len(new_source_genome_with_positions)
            new_source_genome_with_positions.extend([[]] * difference)

        for j in range(len(target_genome)):
            deletion_target = []
            new_chromosome_with_positions_source = new_source_genome_with_positions[j]
            if j < len(new_source_genome_with_positions):
                target_chromosome = target_genome[j]
            else:
                target_chromosome = []

            for i in range(len(new_chromosome_with_positions_source)):
                gene_with_position = new_chromosome_with_positions_source[i]
                position = gene_with_position[0]
                gene = gene_with_position[1]

                if gene not in target_chromosome:
                    deletion_target.append((position, gene))

            deletion_genome.append(deletion_target)
            deletion_target = []

        if len(target_genome) > len(new_source_genome_with_positions):
            for gene_target in range(
                len(new_source_genome_with_positions), len(target_genome)
            ):
                target_chromosome = target_genome[gene_target]
                deletion_target = [
                    (position, gene) for position, gene in enumerate(target_chromosome)
                ]
                deletion_genome.append(deletion_target)

        return deletion_genome




    def check_duplication(self, source_genome, target_genome):

        """
        Identifies duplications in the target genome and determines if duplication mutations are required
        for transforming the source genome into the target genome.
    
        The function performs the following steps:
        1. Iterates over each chromosome in the target genome.
        2. Identifies duplications present in the target genome.
        3. Checks if a duplication is present in the target genome and if it is present in the source genome.
           If not present in the source genome, a duplication mutation is required.
        4. Iterates over each chromosome in the new source genome.
        5. Iterates over each duplicated gene in the sub-list of the duplication genome.
        6. Checks if the duplicated gene exists in the new chromosome.
        7. Checks if the duplicated gene occurs exactly twice.
        8. Removes the current duplicated gene from the sub-list.
        9. If there is only one duplicated gene, replaces the sub-list with an empty list.
    
        @param sourceGenome The original source genome.
        @param targetGenome The target genome with potential duplications.
        """

        log.debug("check_duplication")
        
        new_source_genome, new_source_genome_with_positions = self.modify_source_genome(
            source_genome
        )
        duplication_genome = []
        duplicated_genes = []

        for new_chromosome in target_genome:
            target_duplication = []

            for i in range(len(new_chromosome)):
                if (
                    isinstance(new_chromosome[i], str)
                    and new_chromosome.count(new_chromosome[i]) > 1
                ) and (
                    "*" not in new_chromosome[i]
                    and new_chromosome[i] not in duplicated_genes
                ):
                    if (
                        new_chromosome[i] == new_chromosome[i + 2]
                        or new_chromosome[i] == new_chromosome[i - 2]
                    ):
                        type = "tandem"
                    else:
                        type = "transpositional"

                    duplicated_genes.append(new_chromosome[i])
                    target_duplication.append([i,self.get_second_index(new_chromosome, new_chromosome[i]),new_chromosome[i],type,])

            duplication_genome.append(target_duplication)
            target_duplication = []
            duplicated_genes = []

        if any(duplication_genome):
            for j in range(len(new_source_genome)):
                new_chromosome = new_source_genome[j]
                sub = duplication_genome[j]

                for i in range(len(sub)):
                    duplicate = sub[i]
                    duplicated = duplicate[2]

                    if duplicated in new_chromosome:
                        occurances = new_chromosome.count(duplicated)

                        if occurances == 2:
                            if len(sub) > 1:
                                n_sub = [item for item in sub if item != duplicate]
                                duplication_genome[j] = n_sub
                            else:
                                n_sub = []
                                duplication_genome[j] = n_sub

        return duplication_genome

   

    def choose_mutation(self, insertion_genome, deletion_genome, duplication_genome):

        '''
        Chooses a mutation type based on the provided genomes.
        This method evaluates the given insertion, deletion, and duplication genomes
        to determine which mutation type to perform. It randomly selects a mutation type
        if there are multiple options available.

        Parameters:
        - insertion_genome (iterable):  insertion mutation that needs to be done on the source genome.
        - deletion_genome (iterable): deletion mutation operations that needs to be done the source genome.
        - duplication_genome (iterable): duplication mutation operations that needs to be done on the source genome.

        Returns:
        tuple: The result of the chosen mutation operation.

        Example:
        ```
        mutation_result = instance.choose_mutation(insertion_genome, deletion_genome, duplication_genome)
        ```

        '''
        log.debug("choose_mutation")
        do_mutation = ()
        deletion = False
        insertion = False
        duplication = False

        if any(duplication_genome):
            duplication = True
        if any(deletion_genome):
            deletion = True
        if any(insertion_genome):
            insertion = True

        if insertion and deletion and duplication:
            pick = randint(0, 2)
            if pick == 0:
                do_mutation = self.choose_insertion_mutation(insertion_genome)
            elif pick == 1:
                do_mutation = self.choose_deletion_mutation(deletion_genome)
            elif pick == 2:
                do_mutation = self.choose_duplication_mutation(duplication_genome)
        elif insertion and deletion:
            pick = randint(0, 1)
            if pick == 0:
                do_mutation = self.choose_insertion_mutation(insertion_genome)
            elif pick == 1:
                do_mutation = self.choose_deletion_mutation(deletion_genome)
        elif deletion and duplication:
            pick = randint(0, 1)
            if pick == 0:
                do_mutation = self.choose_deletion_mutation(deletion_genome)
            elif pick == 1:
                do_mutation = self.choose_duplication_mutation(duplication_genome)
        elif insertion and duplication:
            pick = randint(0, 1)
            if pick == 0:
                do_mutation = self.choose_insertion_mutation(insertion_genome)
            elif pick == 1:
                do_mutation = self.choose_duplication_mutation(duplication_genome)
        elif insertion:
            do_mutation = self.choose_insertion_mutation(insertion_genome)
        elif deletion:
            do_mutation = self.choose_deletion_mutation(deletion_genome)
        elif duplication:
            do_mutation = self.choose_duplication_mutation(duplication_genome)

        return do_mutation

    def choose_insertion_mutation(self, insertion_genome):

        '''
        Chooses a mutation operation for the given insertion genome.
        This method selects a random gene from each chromosome in the insertion genome
        and returns a tuple indicating the mutation operation ("ins"), the index of the
        selected chromosome, and the selected gene.

        Args:
            insertion_genome (list): The insertion genome containing chromosomes nad genes.

        Returns:
            tuple: A tuple containing the mutation operation, chromosome index, and selected gene.

        Example:
            If the insertion genome is [[1, 2, 3], [4, 5, 6], [], [7, 8]], the method
            may return ('ins', 1, 5), indicating an insertion mutation on the second
            chromosome with the gene 5.
            where each chromosome is represented as a list of genes.

        '''
        log.debug("choose_insertion_mutation")
        for i in range(len(insertion_genome)):
            new_chromosome = insertion_genome[i]
            if new_chromosome != []:
                picker = randint(0, len(new_chromosome) - 1)
                return ("ins", i, new_chromosome[picker])


    def choose_deletion_mutation(self, deletion_genome):

        '''
        Method to choose a deletion mutation in a genome evolution

        This method selects a random chromosome from the given deletion genome and returns a tuple representing the deletion mutation.
        The tuple contains the mutation type, index of the selected chromosome, and the value to be deleted from that chromosome.

        @param deletion_genome: A list of chromosomes representing the deletion genome.
        @return: A tuple containing the deletion mutation information in the form (mutation_type, chromosome_index, value_to_delete).
        '''
        log.debug("choose_deletion_mutation")
        for i in range(len(deletion_genome)):
            new_chromosome = deletion_genome[i]
            if new_chromosome != []:
                picker = randint(0, len(new_chromosome) - 1)
                return ("del", i, new_chromosome[picker])
            


    def choose_duplication_mutation(self, duplication_genome):

        '''
        Chooses a duplication mutation from the given duplication genome.

        This method iterates through the provided duplication genome and selects a random
        duplication mutation to be applied.

        Parameters:
            duplication_genome (list): The duplication genome to choose a mutation from.

        Returns:
            tuple: A tuple representing the chosen duplication mutation. The tuple has three
            elements: the type of mutation ('dup'), the index of the chromosome in the
            duplication genome, and the selected element from the chromosome.

        Example:
            Suppose duplication_genome = [[1, 2, 3], [], [4, 5]]. The method might return
            ('dup', 2, 5), indicating that a duplication mutation was chosen from the third
            chromosome, and the element 5 was selected.
        '''
        log.debug("choose_duplication_mutation")
        for i in range(len(duplication_genome)):
            new_chromosome = duplication_genome[i]
            if new_chromosome != []:
                picker = randint(0, len(new_chromosome) - 1)
                return ("dup", i, new_chromosome[picker])

    def get_second_index(self, int_list, num):
        '''
        Finds the index of the second occurrence of a specified number in a given list.
        
        This method iterates through the elements of the list and counts occurrences
        of the specified number. It returns the index of the second occurrence of the
        specified number, or -1 if the number does not appear twice in the list.
        
        @param intList The list of integers to search for the second occurrence of the number.
        @param num The target number whose second occurrence index needs to be found.
        @return The index of the second occurrence of the specified number, or -1 if not found.
        '''
        log.debug("get_second_index")
        
        count = 0
        for i, n in enumerate(int_list):
            if n == num:
                count += 1
            if count == 2:
           
                return i
        else:
            return -1
