import time
import argparse
import sys
from networkx import all_shortest_paths

from Rearrangements import Node_rearrangement
from Rearrangement_Extremities import Extremities
import Rearrangement_network

t0 = time.time()

def load_genome(file_path):
    with open(file_path) as f:
        lines = [line.strip().split(',') for line in f]
    genome = [[int(x) for x in line] for line in lines]

    return genome

def load_weight_ratios(file_path):
    with open(file_path) as f:
        lines = [line.strip().split(',') for line in f]
    weight_ratios = [[int(x) for x in line] for line in lines]

    return weight_ratios

def build_hash_table(start_node, target_node, adjacencies_genomeB, weights):
    hash_table = {}
    hash_key_start = hash(str(start_node.state))
    hash_key_target = hash(str(target_node.state))
    hash_table.update({hash_key_start: start_node})
    hash_table.update({hash_key_target: target_node})
    Rearrangement_network.build_hash_table(start_node, hash_table, adjacencies_genomeB, weights)

    return hash_table



def run(args):
    genomeA = load_genome(args.source_genome)
    genomeB = load_genome(args.target_genome)
    weight_ratios = load_weight_ratios(args.ratios)

    stdoutOrigin = sys.stdout 
    sys.stdout = open(args.output_file, 'w')

    get_adjacencies = Extremities()
    adjacencies_genomeA = get_adjacencies.adjacencies_ordered_and_sorted(genomeA)
    adjacencies_genomeB = get_adjacencies.adjacencies_ordered_and_sorted(genomeB)

    # Create start and target node
    start_node = Node_rearrangement(adjacencies_genomeA)
    target_node = Node_rearrangement(adjacencies_genomeB)

    # finding rearrangement weights
    max_number = max(weight_ratios[0])
    weights = []
    for element in weight_ratios[0]:
        if element == 0:
            weights.append(max_number ^ 2)
        else:
            weights.append(max_number / element)

        hash_table = build_hash_table(start_node, target_node, adjacencies_genomeB, weights)

        network = Rearrangement_network.build_network(hash_table)
        shortest_paths = (list(all_shortest_paths(network, start_node, target_node, weight='weight')))


# def print_output(shortest_paths):

    j = 1
    tot_b_trl = 0
    tot_u_trl = 0
    tot_inv = 0
    tot_trp1 = 0
    tot_trp2 = 0
    tot_fus = 0
    tot_fis = 0

    for path in shortest_paths:
        path_state = []
        path_state_weight = []
        Paths_state = []
        Paths_state_weight = []

        for i, current in enumerate(path):
            if i == 0:
                operation_type = 'Not applicable, this is the source genome'
                operation_weight = 'N/A'
                operation = 'N/A'
            else:
                x = path[i - 1].children.index(current)
                operation_type = path[i - 1].children_operations[x][1]
                operation_weight = path[i - 1].children_weights[x]
                operation = path[i - 1].children_operations[x][0]

            adjacencies = current.state
            genome = get_adjacencies.adjacencies_to_genome(adjacencies)
            path_state_weight.append((genome, ((operation_type, operation), operation_weight)))
            path_state.append((genome, (operation_type, operation)))

            i += 1
        Paths_state.append(path_state)
        Paths_state_weight.append(path_state_weight)


        # loop through shortest paths
    for path in shortest_paths:
        b_trl = u_trl = inv = trp1 = trp2 = fus = fis = 0  # initialize counters for this path
        for i in range(1, len(path)): # loop through nodes in path
            operation_type = path[i-1].children_operations[path[i-1].children.index(path[i])][1]

            # increment counters based on operation type
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
         # add path's counters to total counters
        tot_b_trl += b_trl
        tot_u_trl += u_trl
        tot_inv += inv
        tot_trp1 += trp1
        tot_trp2 += trp2
        tot_fus += fus
        tot_fis += fis
        j += 1

        
    print('############################################################################################################')

    # Print genomes
    print('Source Genome:', genomeA)
    print('Target Genome:', genomeB)

    # Print number of most parsimonious solutions
    print('Number of most parsimonious solutions:', len(shortest_paths))

    # Calculate and print average number of operations per solution
    averageg_operations = (tot_inv + tot_trp1 + 2 * tot_trp2 + tot_b_trl + tot_u_trl + tot_fis + tot_fus) / len(shortest_paths)
    print('Average number of operations per solution:', averageg_operations)

    # Calculate and print average number of each operation per solution
    avg_inv = tot_inv / len(shortest_paths)
    avg_trp1 = tot_trp1 / len(shortest_paths)
    avg_trp2 = tot_trp2 / len(shortest_paths)
    avg_b_trl = tot_b_trl / len(shortest_paths)
    avg_u_trl = tot_u_trl / len(shortest_paths)
    avg_fis = tot_fis / len(shortest_paths)
    avg_fus = tot_fus / len(shortest_paths)
    print('Average number of each operation per solution:')
    print('Inversions:', avg_inv, '  Transpositions type 1:', avg_trp1, '  Transpositions type 2:', avg_trp2, 
        '  Balanced translocations:', avg_b_trl, '  Unbalanced translocations:', avg_u_trl, '  Fusions:', avg_fus, 
        '  Fissions:', avg_fis)

    # Print solutions
    print('Solutions:')
    path_counter = 1
    for path in Paths_state:
        print('Solution number', path_counter)
        for genome in path:
            print(genome)
        path_counter += 1
        print()

    
    print('############################################################################################################')

    sys.stdout.close()
    sys.stdout = stdoutOrigin




def main():
    # Create an ArgumentParser object with a description of the program
    parser = argparse.ArgumentParser(
        description='A program that outputs all the optimal set of rearrangment operations that can describe the evolution of one genome into another')
    
    # Add arguments to the parser
    parser.add_argument("-t", help="the set of genes representing the target genome", dest='target_genome', required=True)
    parser.add_argument("-s", help="the set of genes representing the source genome", dest='source_genome', required=True)
    parser.add_argument("-r", help='the ratios of each rearrangement operation in the order inversions, transpositions, balanced translocations, unbalanced translocations, fissions, fusions', dest='ratios', required=True)
    parser.add_argument("-o", help="the name of the output file that will contain the set of rearrangements", dest='output_file', required=True)
    
    # Set the default function to run when the arguments are parsed
    parser.set_defaults(func=run)
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Call the function set as the default
    args.func(args)


    

if __name__ == "__main__":
    main()





    


