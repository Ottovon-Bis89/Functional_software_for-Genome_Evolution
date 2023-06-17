import GenomeEvolver
from networkx import all_shortest_paths
from Class_wrDCJ_Node import Node
from Class_extremities_and_adjacencies import Extremities_and_adjacencies
import New_Network_wrDCJ
from Class_evolve import Evolve
import time
import sys
import random
import pandas as pd
stdoutOrigin = sys.stdout
sys.stdout = open("run1.txt","w")
randomized = 'Random weight ratios'
one_to_one = 'One to one weight ratios'
same_as_solution = 'Same as solution weight ratios'
#####################
number_of_simulations = 10
number_of_sequence_blocks = 7
number_of_rearrangements = 6
type_of_weight_ratio = one_to_one
name_of_csv_file = 'run1.csv'



#create dataframe in which to store results
df = pd.DataFrame(columns=['Operation_sequences', 'Solution_sequence','True_solution_found','Genolve_time', 'Total_time'])




get_adjacencies = Extremities_and_adjacencies()

number_of_solutions_found = 0
get_adjacencies_and_genomes = Extremities_and_adjacencies()

for i in range(0, number_of_simulations):
    t0 = time.time()
    #EVOLVER: target genome is being evolved into the source genome
    target_genome = GenomeEvolver.create_target_genome(number_of_sequence_blocks)
    evolving_genome = Evolve(target_genome)
    rearrangement_series = evolving_genome.evolve_with_random_rearrangements(number_of_rearrangements)
    reverse_the_series = GenomeEvolver.reverse_rearrangement_series(target_genome, rearrangement_series)
    source_genome = reverse_the_series[1]
    solution = reverse_the_series[2]
    target_adjacencies = get_adjacencies_and_genomes.adjacencies_ordered_and_sorted(target_genome)
    source_adjacencies = get_adjacencies_and_genomes.adjacencies_ordered_and_sorted(source_genome)


    # if on the off chance the new source genome is exactly the same as the target genome, redo
    while hash(str(source_adjacencies)) == hash(str(target_adjacencies)):
        target_genome = GenomeEvolver.create_target_genome(number_of_sequence_blocks)
        evolving_genome = Evolve(target_genome)
        rearrangement_series = evolving_genome.evolve_with_random_rearrangements(number_of_rearrangements)
        reverse_the_series = GenomeEvolver.reverse_rearrangement_series(target_genome, rearrangement_series)
        source_genome = reverse_the_series[1]
        solution = reverse_the_series[2]
        target_adjacencies = get_adjacencies_and_genomes.adjacencies_ordered_and_sorted(target_genome)
        source_adjacencies = get_adjacencies_and_genomes.adjacencies_ordered_and_sorted(source_genome)

    #determing the operations used to evolve the target genome
    solution_operations = [d for (c, d) in solution]
    sol_inv = sol_trp = sol_b_trl = sol_u_trl = sol_fis = sol_fus = 0
    evolver_scenario_operation_sequence =[]
    for element in solution_operations:

        if element[0] == 'inv':
            sol_inv += 1
            evolver_scenario_operation_sequence.append(0)
        elif element[0] == 'trp0':
            sol_trp += 1
            evolver_scenario_operation_sequence.append(1)
        elif element[0] == 'b_trl':
            sol_b_trl += 1
            evolver_scenario_operation_sequence.append(2)
        elif element[0] == 'u_trl':
            sol_u_trl += 1
            evolver_scenario_operation_sequence.append(3)
        elif element[0] == 'fis':
            sol_fis += 1
            evolver_scenario_operation_sequence.append(4)
        elif element[0] == 'fus':
            sol_fus += 1
            evolver_scenario_operation_sequence.append(5)


    #getting the ratios of operations present in the 'true solution'
    solution_ratios = [sol_inv, sol_trp, sol_b_trl, sol_u_trl, sol_fis, sol_fus]
    one_to_one_ratios = [1,1,1,1,1,1]
    random_ratios = []
    #getting randomized ratios
    for i in range(6):
        random_ratios.append(random.randint(0,10))

    #seting the operation weighting to be used
    if type_of_weight_ratio == randomized:
        weight_ratios = random_ratios
    elif type_of_weight_ratio == one_to_one:
        weight_ratios =one_to_one_ratios
    elif type_of_weight_ratio == same_as_solution:
        weight_ratios = solution_ratios


    #GENOLVE: tool transforms the source genome back into the target genome
    genolve_ti = time.time()
    #create start and target node for network
    source_node = Node(source_adjacencies)
    target_node = Node(target_adjacencies)

    #create dictionary of solutions
    dictionary_of_intermediates = {}
    source_key = hash(str(source_node.state))
    target_key = hash(str(target_node.state))

    dictionary_of_intermediates.update({source_key:source_node})
    dictionary_of_intermediates.update({target_key:target_node})

    #finding operation weights
    max_number = max(weight_ratios)
    weights = []
    for element in weight_ratios:
        if element == 0:
            weights.append(max_number ^ 2)
        else:
            weights.append(max_number / element)

    New_Network_wrDCJ.build_hash_table(source_node, dictionary_of_intermediates, target_adjacencies, weights)

    network = New_Network_wrDCJ.build_network(dictionary_of_intermediates)

    shortest_paths = (list(all_shortest_paths(network, source_node, target_node, weight='weight')))

    rearrangement_scenarios_found = []

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

                ###
                x = path[i - 1].children.index(current_intermediate)
                operation_type = path[i - 1].children_operations[x][1]
                operation = path[i - 1].children_operations[x][0]

                ###

            ###
            adjacencies = current_intermediate.state
            genome = get_adjacencies.adjacencies_to_genome(adjacencies)
            path_state.append((genome, (operation_type, operation)))
            ###

            i += 1

        rearrangement_scenarios_found.append((path_state))

    #Get operations and locations for Genolve solutions set
    paths_operations = []
    for element in rearrangement_scenarios_found:
        path_operations = [y for (x, y) in element]
        paths_operations.append(path_operations)

    #check if true solution in solution set
    if solution_operations in paths_operations:
        number_of_solutions_found =1
    else:
        number_of_solutions_found = 0


    genolve_tf = time.time()

    #get list of operatations without locations
    #{0:'inv', 1:'trp1', 2:'b_trl', 3:'u_trl, 4:'fis', 5:'fus', 6:'trp2'}
    operation_sequences=[]
    for element in paths_operations:
        operation_sequence =[]
        for operation in element:
            if element.index(operation)==0:
                pass

            else:
                if operation[0] == 'inv':
                    operation_sequence.append(0)
                elif operation[0] =='trp0':
                    pass
                elif operation[0] == 'trp1':
                    operation_sequence.append(1)
                elif operation[0] == 'b_trl':
                    operation_sequence.append(2)
                elif operation[0] == 'u_trl':
                    operation_sequence.append(3)
                elif operation[0] == 'fis':
                    operation_sequence.append(4)
                elif operation[0] == 'fus':
                    operation_sequence.append(5)
                elif operation[0] == 'trp2':
                    operation_sequence.append(6)




        operation_sequences.append(operation_sequence)


    genolve_time = genolve_tf-genolve_ti
    t1 = time.time()
    total_time = t1-t0

    #add run results to dataframe
    df=df.append({'Operation_sequences':operation_sequences, 'Solution_sequence':evolver_scenario_operation_sequence, 'True_solution_found':number_of_solutions_found, 'Genolve_time':genolve_time, 'Total_time':total_time}, ignore_index=True)

    network.clear()


df.to_csv(name_of_csv_file)

#OUTPUT - run info
##############################
print("################################################################")
print()
print('Name of corresponding csv file: ', name_of_csv_file)
print('Number of simulations: ', number_of_simulations)
print('Number of sequence blocks: ', number_of_sequence_blocks)
print('Number of rearrangements: ', number_of_rearrangements)
print('Type of weighting system: ', type_of_weight_ratio)
print()
print("################################################################")

sys.stdout.close()
sys.stdout=stdoutOrigin


