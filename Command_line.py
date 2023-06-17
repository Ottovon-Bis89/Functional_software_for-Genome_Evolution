import time
import argparse
import sys
from networkx import all_shortest_paths

from Rearrangement_node import Node
from Rearrangement_Extremities import Gene_extremities
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


def run(args):
    genomeA = load_genome("genA0.txt")
    genomeB = load_genome("genB0.txt")
    weight_ratios = load_weight_ratios("weight_ratios.txt")

    stdoutOrigin = sys.stdout 
    sys.stdout = open(args.output_file, 'w')

    get_adjacencies = Gene_extremities()
    adjacencies_genomeA = get_adjacencies.ordered_and_sorted_adjacencies(genomeA)
    adjacencies_genomeB = get_adjacencies.ordered_and_sorted_adjacencies(genomeB)

    # Create start and target node
    start_node = Node(adjacencies_genomeA)
    target_node = Node(adjacencies_genomeB)

    hash_table = {}
    hash_key_start = hash(str(start_node.state))
    hash_key_target = hash(str(target_node.state))
    hash_table.update({hash_key_start: start_node})
    hash_table.update({hash_key_target: target_node})

    # finding rearrangement weights
    max_number = max(weight_ratios[0])
    weights = []
    for element in weight_ratios[0]:
        if element == 0:
            weights.append(max_number ^ 2)
        else:
            weights.append(max_number / element)

    Rearrangement_network.build_hash_table(start_node, hash_table, adjacencies_genomeB, weights)

    network = Rearrangement_network.build_network(hash_table)

    shortest_paths = (list(all_shortest_paths(network, start_node, target_node, weight='weight')))    


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

        i = 0
        while i < len(path):
            current = path[i]
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
            genome = get_adjacencies.find_genome(adjacencies)
            path_state_weight.append((genome, ((operation_type, operation), operation_weight)))
            path_state.append((genome, (operation_type, operation)))

            i += 1
        Paths_state.append(path_state)
        Paths_state_weight.append(path_state_weight)


        # loop through shortest paths
    for path in shortest_paths:
        b_trl = u_trl = inv = trp1 = trp2 = fus = fis = 0  # initialize counters for this path
        while i < len(path):

            current = path[i]
            if i == 0:
                pass
            else:
                x = path[i - 1].children.index(current)
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
            i += 1

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
    print('Estimated number of rearrangement events:', len(shortest_paths))
    print()
    print('Average number of events per solution: ',
          float(tot_inv / len(shortest_paths)) + float(tot_trp1 / len(shortest_paths)) + float(
              2 * (tot_trp2 / len(shortest_paths))) + float(tot_b_trl / len(shortest_paths)) + float(
              tot_u_trl / len(shortest_paths)) + float(tot_fis / len(shortest_paths)) + float(
              tot_fus / len(shortest_paths)))
    print()
    print('Average number of each event per solution:')
    print('Inversions: ', float(tot_inv / len(shortest_paths)), '  Transpositions type 1: ',
          float(tot_trp1 / len(shortest_paths)), '  Transpositions type 2: ', float(tot_trp2 / len(shortest_paths)),
          '  Balanced translocations: ', float(tot_b_trl / len(shortest_paths)), '  Unbalanced translocations: ',
          float(tot_u_trl / len(shortest_paths)),
          '  Fusions: ', float(tot_fus / len(shortest_paths)),
          '  Fissions: ', float(tot_fis / len(shortest_paths)))
    print()
    print()
    print('Solutions: ')
    print()
    path_counter = 1
    for path in Paths_state:
        print('Solution number ', path_counter)
        for genome in path:
            print(genome)
        path_counter += 1

    
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





    


