from Genome_extremities_and_adjacencies import Extremities_and_adjacencies
import Evolve

import random

def create_target_genome(number_of_seq_blocks):
    if number_of_seq_blocks < 4:
        number_of_chromosomes = 1
    else:
        number_of_chromosomes = random.randint(1, int((number_of_seq_blocks/4+1)))

    target_genome = []
    counter = 1
    while number_of_chromosomes > 1:
        first_SB = counter
        last_SB = random.randint(counter, number_of_seq_blocks - number_of_chromosomes)

        chromosome = []
        for i in range(first_SB, last_SB + 1):
            chromosome.append(i)
        counter = last_SB + 1
        target_genome.append(chromosome)
        number_of_chromosomes -= 1
    chromosome = []
    for i in range(counter, number_of_seq_blocks + 1):
        chromosome.append(i)
    target_genome.append(chromosome)
    return target_genome

def apply_insertion(genome, element, position):
    """Insert an element at a specific position in the genome."""
    # Find the target chromosome and position
    total_length = 0
    for chrom_idx, chromosome in enumerate(genome):
        if total_length + len(chromosome) > position:
            pos_in_chrom = position - total_length
            chromosome.insert(pos_in_chrom, element)
            break
        total_length += len(chromosome)
    return genome

def apply_deletion(genome, position):
    """Delete an element at a specific position in the genome."""
    # Find the target chromosome and position
    total_length = 0
    for chrom_idx, chromosome in enumerate(genome):
        if total_length + len(chromosome) > position:
            pos_in_chrom = position - total_length
            if len(chromosome) > 1:  # Ensure we don't create empty chromosomes
                del chromosome[pos_in_chrom]
            break
        total_length += len(chromosome)
    return genome

def apply_duplication(genome, position):
    """Duplicate an element at a specific position in the genome."""
    # Find the target chromosome and position
    total_length = 0
    for chrom_idx, chromosome in enumerate(genome):
        if total_length + len(chromosome) > position:
            pos_in_chrom = position - total_length
            element = chromosome[pos_in_chrom]
            chromosome.insert(pos_in_chrom + 1, element)
            break
        total_length += len(chromosome)
    return genome

def reverse_rearrangement_series(target_genome, rearrangement_series):
    get_adjacencies = Extremities_and_adjacencies()
    true_scenario = []

    for element in rearrangement_series[::-1]:
        operation_type = element[0][1]
        intermediate = get_adjacencies.adjacencies_to_genome(element[1])
        
        if operation_type == 'inv':
            operation = (element[0][0][1], element[0][0][0])
            true_scenario.append((intermediate, (operation_type, operation)))
        
        elif operation_type == 'trp1':
            operation = (element[0][0][1], element[0][0][0])
            true_scenario.append((intermediate, ('trp0', operation)))
        
        elif operation_type == 'trp0':
            operation = (element[0][0][1], element[0][0][0])
            true_scenario.append((intermediate, ('trp1', operation)))
        
        elif operation_type in ['b_trl', 'u_trl']:
            operation = (element[0][0][1], element[0][0][0])
            true_scenario.append((intermediate, (operation_type, operation)))
        
        elif operation_type == 'fis':
            if element[0][0][2] < element[0][0][1]:
                operation = (element[0][0][2], element[0][0][1], element[0][0][0])
            else:
                operation = (element[0][0][1], element[0][0][2], element[0][0][0])
            true_scenario.append((intermediate, ('fus', operation)))
        
        elif operation_type == 'fus':
            if element[0][0][1] < element[0][0][0]:
                operation = (element[0][0][2], element[0][0][1], element[0][0][0])
            else:
                operation = (element[0][0][2], element[0][0][0], element[0][0][1])
            true_scenario.append((intermediate, ('fis', operation)))
        
        elif operation_type == 'ins':
            # Reverse of insertion is deletion
            operation = element[0][0][1]  # Position to delete from
            true_scenario.append((intermediate, ('dele', operation)))
        
        elif operation_type == 'dele':
            # Reverse of deletion is insertion
            operation = (element[0][0][0], element[0][0][1])  # (element, position)
            true_scenario.append((intermediate, ('ins', operation)))
        
        elif operation_type == 'dup':
            # Reverse of duplication is deletion of the duplicated element
            operation = element[0][0][1] + 1  # Position to delete from (after duplication)
            true_scenario.append((intermediate, ('dele', operation)))

    true_scenario.append((target_genome, ('none, this is the source genome', 'N/A')))

    reverse_scenario = []
    for i in range(len(true_scenario)):
        if i == 0:
            reverse_scenario.append((true_scenario[i][0], ('none, this is the source genome', 'N/A')))
            evolved_genome = true_scenario[i][0]
        else:
            reverse_scenario.append((true_scenario[i][0], true_scenario[i - 1][1]))

    return (target_genome, evolved_genome, reverse_scenario)


if __name__ == "__main__":
    target_genome = create_target_genome(20)
    start_genome = Evolve(target_genome)
    rearrangement_series = start_genome.evolve_with_random_rearrangements(5)
    reverse_the_series = reverse_rearrangement_series(target_genome, rearrangement_series)
    source_genome = reverse_the_series[1]
    solution = reverse_the_series[2]

