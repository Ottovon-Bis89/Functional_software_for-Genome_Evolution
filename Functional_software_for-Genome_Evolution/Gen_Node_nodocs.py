from random import randint
from Data_generator import DataGenerator
import Intergenic_region_generator
import ForeignDNA
from LegalOperations import MutationOperations
import Helper_Methods as PF
from logger import log


class Node:
    def __init__(self):
        self.state = []

    def get_operations(self, source_genome, target_genome):
    

        list_of_operations = []
        switch = True
        foreign_Dna_counter = 0

        while switch:
            for i, element in enumerate(target_genome):
                if i < len(source_genome) and element == source_genome[i]:
                    pass
                else:
                    source_genome = source_genome[:]

            gen_obj = Intergenic_region_generator.IntergenicGenerator()
            legalOps = MutationOperations()
            data_generator = DataGenerator()
            source_genome = data_generator.check_genes(source_genome)
            target_genome = data_generator.check_genes(target_genome)
            source_genome = data_generator.generate_intergenic_regions(source_genome)
            target_genome = data_generator.generate_intergenic_regions(target_genome)

            count_applicable_region = 0
            for chromosome in source_genome:
                for i in range(len(chromosome)):
                    if (
                        isinstance(chromosome[i], str) and "*" in chromosome[i]
                    ) and len(chromosome[i]) > 1:
                        count_applicable_region += 1

            if count_applicable_region > 0:
                clean_chromosome = []
                clean_genome = []

                for chromosome in source_genome:
                    for i in range(len(chromosome)):
                        if isinstance(chromosome[i], str) and "*" not in chromosome[i]:
                            clean_chromosome.append(chromosome[i])
                        elif isinstance(chromosome[i], int):
                            clean_chromosome.append(chromosome[i])
                    clean_genome.append(clean_chromosome)
                    clean_chromosome = []

                insert_intergenic_region = gen_obj.inter_generator(clean_genome)
                source_genome = gen_obj.intergenic_regions(insert_intergenic_region)

                choose = randint(0, 5)
                if choose < 5:
                    mutations, required_mutation = legalOps.mutation_legal_operations(
                        source_genome, target_genome
                    )
                    if required_mutation:
                        source_genome, mutation_list = self.do_mutation(
                            source_genome, required_mutation
                        )
                        if mutation_list != []:
                            list_of_operations.append(mutation_list)
                        switch = True
                    else:
                        while (any(mutations)) and required_mutation:
                            final_mutations = []

                            for i in range(len(mutations)):
                                if i == 0:
                                    mutation_type = "ins"
                                elif i == 1:
                                    mutation_type = "del"
                                else:
                                    mutation_type = "dup"

                                mutation = mutations[i]

                                for chromosome_number in range(len(mutation)):
                                    if mutation[chromosome_number]:
                                        chromosome_index = chromosome_number
                                        chromosome = mutation[chromosome_number]

                                        for m in range(len(chromosome)):
                                            do_mutation = (
                                                mutation_type,
                                                chromosome_index,
                                                chromosome[m],
                                            )

                                            (
                                                source_genome,
                                                mutation_list,
                                            ) = self.do_mutation(
                                                source_genome, do_mutation
                                            )
                                            source_genome = source_genome[:]

                                            final_mutations.append(mutation_list)

                            list_of_operations.append(final_mutations)

                            clean_chromosome = []
                            clean_genome = []
                            for chromosome in source_genome:
                                for i in range(len(chromosome)):
                                    if (
                                        isinstance(chromosome[i], str)
                                        and "*" not in chromosome[i]
                                    ):
                                        clean_chromosome.append(chromosome[i])
                                    elif isinstance(chromosome[i], int):
                                        clean_chromosome.append(chromosome[i])
                                clean_genome.append(clean_chromosome)
                                clean_chromosome = []

                            gen_obj = Intergenic_region_generator.IntergenicGenerator()
                            insert_intergenic_region = gen_obj.inter_generator(
                                clean_genome
                            )
                            source_genome = gen_obj.intergenic_regions(
                                insert_intergenic_region
                            )

                            (
                                mutations,
                                required_mutation,
                            ) = legalOps.mutation_legal_operations(
                                source_genome, target_genome
                            )
                            if not required_mutation:
                                break
                            switch = False
                elif foreign_Dna_counter < 3 or foreign_Dna_counter != 0:
                    foreign_Dna_counter += 1

                    foreign_obj = ForeignDNA.Foreign_DNA()
                    foreign_dna = []
                    while foreign_dna == []:
                        foreign_dna = foreign_obj.foreign_dna_pool(
                            source_genome, target_genome
                        )

                    foreign_dna_len = len(foreign_dna) - 1

                    choice_foreign_dna = randint(0, foreign_dna_len)

                    chosen = foreign_dna[choice_foreign_dna]

                    source_genome, f_dna = foreign_obj.insert_foreign_dna(
                        source_genome, chosen
                    )
                    list_of_operations.append(f_dna)

                    mutations, required_mutation = legalOps.mutation_legal_operations(
                        source_genome, target_genome
                    )

                    if required_mutation:
                        source_genome, mutation_list = self.do_mutation(
                            source_genome, required_mutation
                        )

                        if mutation_list != []:
                            list_of_operations.append(mutation_list)
                        switch = True

                    else:
                        while any(mutations) and required_mutation:
                            final_mutations = []
                            for i in range(len(mutations)):
                                if i == 0:
                                    mutation_type = "ins"
                                elif i == 1:
                                    mutation_type = "del"
                                else:
                                    mutation_type = "dup"

                                mutation = mutations[i]

                                for chromosome_number in range(len(mutation)):
                                    if mutation[chromosome_number]:
                                        chromosome_index = chromosome_number
                                        chromosome = mutation[chromosome_number]

                                        for m in range(len(chromosome)):
                                            do_mutation = (
                                                mutation_type,
                                                chromosome_index,
                                                chromosome[m],
                                            )

                                            (
                                                source_genome,
                                                mutation_list,
                                            ) = self.do_mutation(
                                                source_genome, do_mutation
                                            )

                            clean_chromosome = []
                            clean_genome = []
                            for chromosome in source_genome:
                                for i in range(len(chromosome)):
                                    if (
                                        isinstance(chromosome[i], str)
                                        and "*" not in chromosome[i]
                                    ):
                                        clean_chromosome.append(chromosome[i])
                                    elif isinstance(chromosome[i], int):
                                        clean_chromosome.append(chromosome[i])

                                clean_genome.append(clean_chromosome)
                                clean_chromosome = []

                            gen_obj = Intergenic_region_generator.IntergenicGenerator()
                            insert_intergenic_region = gen_obj.inter_generator(
                                clean_genome
                            )
                            source_genome = gen_obj.intergenic_regions(
                                insert_intergenic_region
                            )

                            (
                                mutations,
                                required_mutation,
                            ) = legalOps.mutation_legal_operations(
                                source_genome, target_genome
                            )

                            if not required_mutation:
                                break
                        switch = False

        return list_of_operations

    def do_mutation(self, source_genome, required_mutation):

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

    def insertion(
        self, source_chromosome, position_applicable_region, gene, larger_length=False
    ):

        if larger_length:
            insertion_index = 0
            while (
                insertion_index < len(source_chromosome)
                and gene > source_chromosome[insertion_index]
            ):
                insertion_index += 1
            source_chromosome.insert(insertion_index, gene)
        else:
            source_chromosome[position_applicable_region] = gene

        return source_chromosome

    def deletion(self, source_chromosome, position_applicable_region):
        
        if (
            "_" not in source_chromosome[position_applicable_region]
            or "*" not in source_chromosome[position_applicable_region]
        ):
            del source_chromosome[position_applicable_region]
        return source_chromosome

    def duplication(self, source_chromosome, gene_to_duplicate, insertion_position):

        if (
            "_" not in source_chromosome[insertion_position]
            or "*" not in source_chromosome[insertion_position]
        ):
            source_chromosome.insert(insertion_position - 1, gene_to_duplicate)

        return source_chromosome
