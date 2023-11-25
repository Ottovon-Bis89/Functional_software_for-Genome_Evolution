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
                new_chromosome = new_source_genome[j]
            # else:
            #     new_chromosome = []
            # target_chromosome = target_genome[j]

            for i in range(len(target_chromosome)):
                if ("*" not in str(target_chromosome[i])) and (
                    (target_chromosome[i]) not in new_chromosome
                ):
                    insertion_target.append((i, target_chromosome[i]))
                elif (
                    ((target_chromosome[i]) in new_chromosome)
                    and (new_chromosome.count(target_chromosome[i]) == 1)
                    and not (
                        (new_chromosome.index(target_chromosome[i]))
                        == math.floor(i / 2)
                    )
                ):
                    insertion_target.append((i, target_chromosome[i]))

            insertion_genome.append(insertion_target)

        if len(target_genome) > len(source_genome):
            for missing_chromosome in range(len(source_genome), len(target_genome)):
                new_chromosome = target_genome[missing_chromosome]
                new_source_genome.append(new_chromosome)

        return insertion_genome, new_source_genome


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
                    target_duplication.append(
                        [
                            i,
                            self.get_second_index(new_chromosome, new_chromosome[i]),
                            new_chromosome[i],
                            type,
                        ]
                    )

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


def do_mutation(self, source_genome, required_mutation):
        """
        Performs a specified mutation on the source genome with approved intergenic regions.
        The function interprets the required mutation and calls appropriate sub-functions
        (delete, duplicate, insert) to execute the mutation operation.
        The function follows these steps:
        1. Iterates over genes with approved intergenic regions in the source genome.
            - Identifies mutation points marked with '*' in the gene strings.
            - Stores genes and mutation points for each gene in their respective lists.
            - Appends the gene and mutation point lists to their respective genome lists.
        2. Extracts mutation type, chromosome index, and actual mutation details from the required mutation list.
        3. Performs the specified mutation operation:
            - For duplication, adjusts the position, checks for applicable regions, and updates the source genome.
            - For insertion, inserts genes at the specified position and updates the source genome.
            - For deletion, deletes genes at the specified position and updates the source genome.
        4. Records each mutation operation and appends it to the list of mutations.
        @param sourceGenome A list representing the source genome with approved intergenic regions.
        @param requiredMutation A list representing the required mutation with details such as type, chromosome index, and mutation data.
        @return A tuple containing the updated source genome and a list of mutation records.
        """

        log.debug("do mutation")

        
        list_of_mutations = []
        list_of_genes = []
        list_of_genes_genome = []
        list_of_mutation_points = []
        list_of_mutation_points_genome = []

        for genes_with_intergenic_approved in source_genome:
            for i in range(len(genes_with_intergenic_approved)):
                if (
                    isinstance(genes_with_intergenic_approved[i], str)
                    and len(genes_with_intergenic_approved[i]) > 1
                ) and "*" in genes_with_intergenic_approved[i]:
                    if i != len(genes_with_intergenic_approved) - 2:
                        list_of_mutation_points.append(i + 1)
                elif (not isinstance(genes_with_intergenic_approved[i], str)) or (
                    isinstance(genes_with_intergenic_approved[i], str)
                    and "*" not in genes_with_intergenic_approved[i]
                ):
                    list_of_genes.append(genes_with_intergenic_approved[i])
            list_of_genes_genome.append(list_of_genes)
            list_of_mutation_points_genome.append(list_of_mutation_points)

            list_of_genes = []
            list_of_mutation_points = []

        mutation_type = required_mutation[0]
        chromosome_index = required_mutation[1]
        actual_mutation = required_mutation[2]

        if mutation_type == "dup":
            position = actual_mutation[1]
            gene_to_duplicate = actual_mutation[2]
            type_of_duplication = actual_mutation[3]

            chromosome = source_genome[chromosome_index]
            if position > len(chromosome) - 1:
                position = len(chromosome) - 1

            if (
                isinstance(chromosome[position - 1], str)
                and "*" in chromosome[position - 1]
            ) and len(chromosome[position - 1]) > 1:
                mutated_chromosome = self.duplication(
                    chromosome, gene_to_duplicate, position
                )
                source_genome[chromosome_index] = mutated_chromosome

                operation = {
                    "Mut_Type": mutation_type,
                    "Chr": chromosome_index + 1,
                    "Gene": gene_to_duplicate,
                    "Pos": position,
                    "Type of dup": type_of_duplication,
                    "Genome after mutation": source_genome,
                }

                list_of_mutations.append(operation)

        elif mutation_type == "ins":
            position = actual_mutation[0]
            gene_to_insert = actual_mutation[1]

            while chromosome_index >= len(source_genome):
                source_genome.append([])
            chromosome = source_genome[chromosome_index]

            if (
                position > len(chromosome) - 1
                or "_" in str(chromosome[position])
                or len(chromosome) == 0
            ):
                mutated_chromosome = self.insertion(
                    chromosome, position, gene_to_insert, True
                )

                operation = {
                    "Mut_Type": mutation_type,
                    "Chr": chromosome_index + 1,
                    "Pos": len(chromosome) + 1,
                    "Gene": gene_to_insert,
                    "Genome after mutation": source_genome,
                }

                list_of_mutations.append(operation)

            elif (
                isinstance(chromosome[position - 1], str)
                and "*" in chromosome[position - 1]
            ) and len(chromosome[position - 1]) > 1:
                mutated_chromosome = self.insertion(
                    chromosome, position, gene_to_insert
                )

                operation = {
                    "Mut_Type": mutation_type,
                    "Chr": chromosome_index + 1,
                    "Pos": position,
                    "Gene": gene_to_insert,
                    "Genome after mutation": source_genome,
                }

                list_of_mutations.append(operation)

        elif mutation_type == "del":
            position = actual_mutation[0]

            gene_to_delete = actual_mutation[1]

            if chromosome_index < len(source_genome):
                chromosome = source_genome[chromosome_index]

            if position > len(chromosome) - 1:
                position = len(chromosome) - 1

            if (
                isinstance(chromosome[position - 1], str)
                and "*" in chromosome[position - 1]
            ) and len(chromosome[position - 1]) > 1:
                mutated_chromosome = self.deletion(chromosome, position)

                operation = {
                    "Mut_Type": mutation_type,
                    "Chr": chromosome_index + 1,
                    "Pos": position,
                    "Gene": gene_to_delete,
                    "Genome after mutation": source_genome,
                }

                list_of_mutations.append(operation)

        return source_genome, list_of_mutations