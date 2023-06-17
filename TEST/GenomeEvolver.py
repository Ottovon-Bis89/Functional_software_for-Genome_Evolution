from Class_extremities_and_adjacencies import Extremities_and_adjacencies
from Class_evolve import Evolve
import random
def create_target_genome(number_of_seq_blocks):
    #print('number of sb',number_of_seq_blocks)
    #get number of chromosomes
    if number_of_seq_blocks < 4:
        number_of_chromosomes = 1
    else:
        number_of_chromosomes = random.randint(1, int((number_of_seq_blocks/4+1)))


    #create target genome
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
    #print('target genome: ', target_genome)
    return target_genome

    #execute rearrangements

def reverse_rearrangement_series(target_genome, rearrangement_series):
    get_adjacencies = Extremities_and_adjacencies()

    #Get reversed scenario:

    true_scenario = []

    for element in rearrangement_series[::-1]:
        if element[0][1] == 'inv':
            operation_type = 'inv'
            intermediate = get_adjacencies.adjacencies_to_genome(element[1])
            operation = (element[0][0][1], element[0][0][0])
            true_scenario.append((intermediate, (operation_type, operation)))

        elif element[0][1] == 'trp1':
            operation_type = 'trp0'
            intermediate = get_adjacencies.adjacencies_to_genome(element[1])
            operation = (element[0][0][1], element[0][0][0])
            true_scenario.append((intermediate, (operation_type, operation)))

        elif element[0][1] == 'trp0':
            operation_type = 'trp1'
            intermediate = get_adjacencies.adjacencies_to_genome(element[1])
            operation = (element[0][0][1], element[0][0][0])
            true_scenario.append((intermediate, (operation_type, operation)))

        elif element[0][1] == 'b_trl':
            operation_type = 'b_trl'
            intermediate = get_adjacencies.adjacencies_to_genome(element[1])
            operation = (element[0][0][1], element[0][0][0])
            true_scenario.append((intermediate, (operation_type, operation)))

        elif element[0][1] == 'u_trl':
            operation_type = 'u_trl'
            intermediate = get_adjacencies.adjacencies_to_genome(element[1])
            operation = (element[0][0][1], element[0][0][0])
            true_scenario.append((intermediate, (operation_type, operation)))

        elif element[0][1] == 'fis':
            operation_type = 'fus'
            intermediate = get_adjacencies.adjacencies_to_genome(element[1])
            if element[0][0][2] < element[0][0][1]:
                operation = (element[0][0][2], element[0][0][1], element[0][0][0])
            else:
                operation = (element[0][0][1], element[0][0][2], element[0][0][0])
            true_scenario.append((intermediate, (operation_type, operation)))

        elif element[0][1] == 'fus':
            operation_type = 'fis'
            intermediate = get_adjacencies.adjacencies_to_genome(element[1])
            if element[0][0][1] < element[0][0][0]:
                operation = (element[0][0][2], element[0][0][1], element[0][0][0])
            else:
                operation = (element[0][0][2], element[0][0][0], element[0][0][1])
            true_scenario.append((intermediate, (operation_type, operation)))


    true_scenario.append((target_genome, ('none, this is the source genome', 'N/A'))) #The source genome is not the product of some rearrangement

    reverse_scenario = []
    for i in range(0, len(true_scenario)):
        if i == 0:
            reverse_scenario.append((true_scenario[i][0], ('none, this is the source genome', 'N/A')))
            evolved_genome = true_scenario[i][0]
        else:
            reverse_scenario.append((true_scenario[i][0], true_scenario[i - 1][1]))



    return (target_genome, evolved_genome, reverse_scenario)

target_genome = create_target_genome(40)
start_genome = Evolve(target_genome)
rearrangement_series = start_genome.evolve_with_random_rearrangements(8)
reverse_the_series = reverse_rearrangement_series(target_genome, rearrangement_series)
source_genome = reverse_the_series[1]
solution = reverse_the_series[2]


print("target genome:", target_genome)
print("source genome:" , source_genome)
# print("solution:" , solution)
# print("rearrangement series:" , rearrangement_series)