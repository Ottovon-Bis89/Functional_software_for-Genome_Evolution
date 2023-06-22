import GenomeEvolver
from networkx import all_shortest_paths
from Class_wrDCJ_Node import Node
from Class_extremities_and_adjacencies import Extremities_and_adjacencies
import New_Network_wrDCJ
from Class_evolve import Evolve
import time
import sys
import random
stdoutOrigin = sys.stdout
sys.stdout = open("T3_same_as_solution_e2.txt","w")
randomized = 'Random weight ratios'
one_to_one = 'One to one weight ratios'
same_as_solution = 'Same as solution weight ratios'
#####################
number_of_simulations = 10000
number_of_sequence_blocks = 9
number_of_rearrangements = 8
type_of_weight_ratio = same_as_solution




results = []
t0 = time.time()

get_adjacencies = Extremities_and_adjacencies()

number_of_solutions_found = 0
get_adjacencies_and_genomes = Extremities_and_adjacencies()

for i in range(0, number_of_simulations):
    #print('SIMULATION NUMBER: ', i, '*****************************************************************')
   # print('num of sb, ', number_of_sequence_blocks)
    target_genome = GenomeEvolver.create_target_genome(number_of_sequence_blocks)
    evolving_genome = Evolve(target_genome)
    rearrangement_series = evolving_genome.evolve_with_random_rearrangements(number_of_rearrangements)
    reverse_the_series = GenomeEvolver.reverse_rearrangement_series(target_genome, rearrangement_series)
    source_genome = reverse_the_series[1]
    solution = reverse_the_series[2]
    target_adjacencies = get_adjacencies_and_genomes.adjacencies_ordered_and_sorted(target_genome)
    source_adjacencies = get_adjacencies_and_genomes.adjacencies_ordered_and_sorted(source_genome)

    solution_operations = [d for (c, d) in solution]
    sol_inv = sol_trp = sol_b_trl = sol_u_trl = sol_fis = sol_fus = 0
    for element in solution_operations:
        if element[0] == 'inv':
            sol_inv += 1
        elif element[0] == 'trp0':
            sol_trp += 1
        elif element[0] == 'b_trl':
            sol_b_trl += 1
        elif element[0] == 'u_trl':
            sol_u_trl += 1
        elif element[0] == 'fis':
            sol_fis += 1
        elif element[0] == 'fus':
            sol_fus += 1


    solution_ratios = [sol_inv, sol_trp, sol_b_trl, sol_u_trl, sol_fis, sol_fus]
    one_to_one_ratios = [1,1,1,1,1,1]
    random_ratios = []
    for i in range(6):
        random_ratios.append(random.randint(0,10))

    if type_of_weight_ratio == randomized:
        weight_ratios = random_ratios
    elif type_of_weight_ratio == one_to_one:
        weight_ratios =one_to_one_ratios
    elif type_of_weight_ratio == same_as_solution:
        weight_ratios = solution_ratios

    #weight_ratios = solution_ratios
    while hash(str(source_adjacencies)) == hash(str(target_adjacencies)):
        target_genome = GenomeEvolver.create_target_genome(number_of_sequence_blocks)
        evolving_genome = Evolve(target_genome)
        rearrangement_series = evolving_genome.evolve_with_random_rearrangements(number_of_rearrangements)
        reverse_the_series = GenomeEvolver.reverse_rearrangement_series(target_genome, rearrangement_series)
        source_genome = reverse_the_series[1]
        solution = reverse_the_series[2]
        target_adjacencies = get_adjacencies_and_genomes.adjacencies_ordered_and_sorted(target_genome)
        source_adjacencies = get_adjacencies_and_genomes.adjacencies_ordered_and_sorted(source_genome)


    #create start and target node for network
    source_node = Node(source_adjacencies)
    target_node = Node(target_adjacencies)

    #create dictionary of solutions
    dictionary_of_intermediates = {}
    source_key = hash(str(source_node.state))
    target_key = hash(str(target_node.state))

    dictionary_of_intermediates.update({source_key:source_node})
    dictionary_of_intermediates.update({target_key:target_node})
    # print('^^^^^^^^^^^^')
    # print('source: ', source_node)
    # print('target: ', target_node)
    # print('source key: ', source_key)
    # print('target_key: ', target_key)
    # print('dict:')
    # print(dictionary_of_intermediates)
    # print('^^^^^^^^^^^^^^^')

    #finding operation weights
    max_number = max(weight_ratios)
    weights = []
    for element in weight_ratios:
        if element == 0:
            weights.append(max_number ^ 2)
        else:
            weights.append(max_number / element)

    New_Network_wrDCJ.build_hash_table(source_node, dictionary_of_intermediates, target_adjacencies, weights)

    # print('*****************')
    # print(dictionary_of_intermediates)
    # print()

    network = New_Network_wrDCJ.build_network(dictionary_of_intermediates)


    shortest_paths = (list(all_shortest_paths(network, source_node, target_node, weight='weight')))

    number_of_shortest_paths = len(shortest_paths)

    rearrangement_scenarios_found = []

    j=1
    tot_inv=tot_trp1=tot_trp2=tot_b_trl=tot_u_trl=tot_fus=tot_fis=0

    for path in shortest_paths:
        path_state = []

        i=inv=trp1=trp2=b_trl=u_trl=fis=fus=0

        while i < len(path):
            current_intermediate = path[i]
            if i == 0:
                operation_type = 'none, this is the source genome'
                # operation_weight = 'N/A'
                operation = 'N/A'
            else:
                x = path[i - 1].children.index(current_intermediate)
                operation_type = path[i - 1].children_operations[x][1]
                if operation_type == 'b_trl':
                    b_trl += 1
                elif operation_type == 'u_trl':
                    u_trl += 1
                elif operation_type == 'inv':
                    inv += 1
                elif operation_type == 'trp1':
                    trp1 += 1
                elif operation_type == 'trp2':
                    trp2 += 1
                elif operation_type == 'fus':
                    fus += 1
                elif operation_type == 'fis':
                    fis += 1

                ###
                x = path[i - 1].children.index(current_intermediate)
                operation_type = path[i - 1].children_operations[x][1]
                operation = path[i - 1].children_operations[x][0]

                ###

            tot_b_trl += b_trl
            tot_u_trl += u_trl
            tot_inv += inv
            tot_trp1 += trp1
            tot_trp2 += trp2
            tot_fus += fus
            tot_fis += fis
            j += 1

            ###
            adjacencies = current_intermediate.state
            genome = get_adjacencies.adjacencies_to_genome(adjacencies)
            path_state.append((genome, (operation_type, operation)))
            ###

            i += 1

        rearrangement_scenarios_found.append((path_state))

    ave_b_trl = tot_b_trl / len(shortest_paths)
    ave_u_trl = tot_u_trl / len(shortest_paths)
    ave_inv = tot_inv / len(shortest_paths)
    ave_trp1 = tot_trp1 / len(shortest_paths)
    ave_trp2 = tot_trp2 / len(shortest_paths)
    ave_fus = tot_fus / len(shortest_paths)
    ave_fis = tot_fis / len(shortest_paths)

    ave_number_of_operations = 0
    paths_operations = []
   # print("*********", rearrangement_scenarios_found[0])
    for element in rearrangement_scenarios_found:
        path_operations = [y for (x, y) in element]
        paths_operations.append(path_operations)
        ave_num_of_ops_per_series=0
        for element in path_operations:
            if element[0] == 'trp1':
                pass
            elif element[0] == 'none, this is the source genome':
                pass
            else:
                ave_num_of_ops_per_series+=1
        ave_number_of_operations+=ave_num_of_ops_per_series
    ave_number_of_operations = ave_number_of_operations/len(rearrangement_scenarios_found)





    #number_of_operations = len(shortest_paths[0]) - 1
    results.append(
        [ave_number_of_operations, len(shortest_paths), ave_inv, ave_trp1, ave_trp2, ave_b_trl, ave_u_trl, ave_fus,
         ave_fis])

    network.clear()

    # paths_operations = []
    # for element in rearrangement_scenarios_found:
    #     path_operations = [y for (x, y) in element]
    #
    #     paths_operations.append(path_operations)


    # solution_operations = [d for (c, d) in solution]
    # sol_inv=sol_trp=sol_b_trl=sol_u_trl=sol_fis=sol_fus=0
    # for element in solution_operations:
    #     if element[0] == 'inv':
    #         sol_inv+=1
    #     elif element[0] == 'trp0':
    #         sol_trp+=1
    #     elif element[0] == 'b_trl':
    #         sol_b_trl+=1
    #     elif element[0] == 'u_trl':
    #         sol_u_trl+=1
    #     elif element[0] == 'fis':
    #         sol_fis+=1
    #     else:
    #         sol_fus+=1

    if solution_operations in paths_operations:
        number_of_solutions_found += 1


simulation_average = []
average_number_of_operations = 0
average_number_of_paths = 0
average_number_of_inv = 0
average_number_of_trp1 = 0
average_number_of_trp2 = 0
average_number_of_b_trl = 0
average_number_of_u_trl = 0
average_number_of_fus = 0
average_number_of_fis = 0
for element in results:
    average_number_of_operations += element[0]
    average_number_of_paths += element[1]
    average_number_of_inv += element[2]
    average_number_of_trp1 += element[3]
    average_number_of_trp2 += element[4]
    average_number_of_b_trl += element[5]
    average_number_of_u_trl += element[6]
    average_number_of_fus += element[7]
    average_number_of_fis += element[8]

average_number_of_operations = average_number_of_operations / number_of_simulations
average_number_of_paths = average_number_of_paths / number_of_simulations
average_number_of_inv = average_number_of_inv / number_of_simulations
average_number_of_trp1 = average_number_of_trp1 / number_of_simulations
average_number_of_trp2 = average_number_of_trp2 / number_of_simulations
average_number_of_b_trl = average_number_of_b_trl / number_of_simulations
average_number_of_u_trl = average_number_of_u_trl / number_of_simulations
average_number_of_fus = average_number_of_fus / number_of_simulations
average_number_of_fis = average_number_of_fis / number_of_simulations

ave_number_per_op = [average_number_of_inv, average_number_of_trp1, average_number_of_b_trl, average_number_of_u_trl, average_number_of_fis, average_number_of_fus, average_number_of_trp2]
num_per_op_ratios = []
tot_ave_op_num = 0
for element in ave_number_per_op:
    tot_ave_op_num+= element

for element in ave_number_per_op:
    ratio = element/tot_ave_op_num*average_number_of_operations
    num_per_op_ratios.append(ratio)



t1 = time.time()
print('##########################################################################################################')
print()
print('time: ', t1-t0)
print()
print('number of simulations: ', number_of_simulations)
print('number of sequence blocks: ', number_of_sequence_blocks)
print('number of rearrangements: ', number_of_rearrangements)
print('type of weighting ratio: ', type_of_weight_ratio)
print()
print('average number of solutions: ', average_number_of_paths)
print()
print('average solution length: ' ,average_number_of_operations)
print()
print('percentage time true solution was found: ',(number_of_solutions_found/number_of_simulations)*100)


print()
print('ratios as: inv:trp1:b_trl:u_trl:fis:fus:trp2')
print(num_per_op_ratios)


print('##########################################################################################################')

sys.stdout.close()
sys.stdout=stdoutOrigin
