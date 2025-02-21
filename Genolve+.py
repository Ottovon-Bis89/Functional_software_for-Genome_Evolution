from networkx import all_shortest_paths
from Path_node import Node
from Genome_extremities_and_adjacencies import Extremities_and_adjacencies
import Path_network
import random
import time
import argparse
import sys
from tqdm import tqdm

t0 = time.time()
bar_format = '{l_bar}{bar}| {n_fmt}/{total_fmt}'


def read_csv(file_path):
    """
    Reads a CSV file and returns a list of lists, where each inner list represents a row.
    Assumes the file is comma-separated.
    """
    with open(file_path, 'r') as file:
        return [list(map(int, line.strip().split(','))) for line in file]

def flatten_csv(file_path):
    """
    Reads a CSV file and flattens all rows into a single list of strings.
    """
    with open(file_path, 'r') as file:
        return [item for line in file for item in line.strip().split(',')]

def run(args):
    """
    Main function to process genomes, weight ratios, and fragments.
    Redirects output to the specified file.
    """
    stdoutOrigin = sys.stdout
    sys.stdout = open(args.output_file, 'w')

    # change filepath to your working directory
    genomeA = read_csv("/home/22204911/Documents/Run_1/FJSA.txt")
    genomeB = read_csv("/home/22204911/Documents/Run_1/MTZ.txt")
    weight_ratios = read_csv("/home/22204911/Documents/Run_1/Weight_ratios.txt")
    fragments = flatten_csv("/home/22204911/Documents/Run_1/frag.txt")


    
    get_adjacencies = Extremities_and_adjacencies()
    
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

    max_number = max(weight_ratios[0])
    weights = []
    for element in weight_ratios[0]:
        if element == 0:
            weights.append(max_number ^ 2)
        else:
            weights.append(max_number / element)

    Path_network.build_hash_table(start_node, hash_table, adjacencies_genomeB, weights, genomeB, genomeA)

    network = Path_network.build_network(hash_table)


    shortest_paths = (list(all_shortest_paths(network, start_node, target_node, weight='weight')))

    j = 1
    tot_b_trl = tot_u_trl = tot_inv = tot_trp0 = tot_trp1 = tot_trp2 = tot_fus = tot_fis = tot_ins = tot_dele = tot_dup  = 0  

    Paths_state = []
    Paths_state_weight = []
   
    for path in tqdm(shortest_paths, desc="Printing Shortest Paths", bar_format=bar_format, ascii='-*'):
        path_state = []
        path_state_weight = []

        i = 0
        while i < len(path):
            current = path[i]
            if i == 0:
                operation_type = 'none, this is the source genome'
                operation_weight = 'N/A'
                operation = 'None'
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
        Paths_state.append((path_state))
        Paths_state_weight.append(path_state_weight)
        #time.sleep(0.00001)

    for path in tqdm(shortest_paths, desc="Calculating Paths Metrics", bar_format=bar_format, ascii='-*'):

        operation_counters = {
            'b_trl': 0,
            'u_trl': 0,
            'inv': 0,
            'trp0': 0,
            'trp1': 0,
            'trp2': 0,
            'fus': 0,
            'fis': 0,
            'ins': 0,
            'dele': 0,
            'dup': 0
        }

        for i in range(len(path)):
            current = path[i]
            if i > 0:
                x = path[i - 1].children.index(current)
                operation_type = path[i - 1].children_operations[x][1]

                if operation_type in operation_counters:
                    operation_counters[operation_type] += 1

        tot_b_trl += operation_counters['b_trl']
        tot_u_trl += operation_counters['u_trl']
        tot_inv += operation_counters['inv']
        tot_trp0 += operation_counters['trp0']
        tot_trp1 += operation_counters['trp1']
        tot_trp2 += operation_counters['trp2']
        tot_fus += operation_counters['fus']
        tot_fis += operation_counters['fis']
        tot_ins += operation_counters['ins']
        tot_dele += operation_counters['dele']
        tot_dup += operation_counters['dup']

        j += 1
        # time.sleep(0.00001)

    print('*****************************************************************************************Genome Evolution Analysis*******************************************************************************')
    print('\n')
    print('Source Genome: ', genomeA)
    print('Target Genome: ', genomeB)
    print('\n')
    print('Number of most likely biological paths (solutions): ', len(shortest_paths))
    print('\n')
    print('Average number of evolutionary events per solution (Edit Distance): ',
          float(tot_inv / len(shortest_paths)) + float(tot_trp1 / len(shortest_paths)) + float(
              2 * (tot_trp1 / len(shortest_paths))) + float(tot_b_trl / len(shortest_paths)) + float(
              tot_u_trl / len(shortest_paths)) + float(tot_fis / len(shortest_paths)) + float(
              tot_fus / len(shortest_paths)) + float(tot_ins/len(shortest_paths)) + float(tot_dele/len(shortest_paths)) + float(tot_dup/len(shortest_paths)))
    print('\n')
    print('Average number of each event per solution:')
    print('Inversions: ', float(tot_inv / len(shortest_paths)),  'Transpositions_type 1: ',
          float(tot_trp1 / len(shortest_paths)), '  Transpositions_type 2: ', float(tot_trp2 / len(shortest_paths)),
          '  Balanced translocations: ', float(tot_b_trl / len(shortest_paths)), '  Unbalanced translocations: ',
          float(tot_u_trl / len(shortest_paths)), '  Fusions: ', float(tot_fus / len(shortest_paths)), '  Fissions: ', float(tot_fis / len(shortest_paths)), 
          'Insertions: ', float(tot_ins/len(shortest_paths)), 'Deletions: ', float(tot_dele/len(shortest_paths)), 'Duplications: ', float(tot_dup/len(shortest_paths)))
    
    print('\n\n')
    print('Solutions: ')
    path_counter = 1
    for path in Paths_state:
        print('\n')
        print('#Solution number ', path_counter)
        
        inserted_fragment = None  
        chosen_chromosome_index = None  

        for genome in path:
            new_genome = genome[0]  
            operation = genome[1]
            
            valid_chromosomes = [chrom for chrom in new_genome if isinstance(chrom, list)]
            
            if valid_chromosomes:
                
                if inserted_fragment is None:
                    num_fragments_to_insert = random.randint(1, 3) #change number of FDNA fragments here
                    num_fragments_to_insert = min(num_fragments_to_insert, len(valid_chromosomes))

                    inserted_fragments = []
                    chosen_chromosome_indices = random.sample(range(len(valid_chromosomes)), num_fragments_to_insert)

                    for i in range(num_fragments_to_insert):
                        chosen_chromosome_index = chosen_chromosome_indices[i]
                        chosen_chromosome = valid_chromosomes[chosen_chromosome_index]
                        fragment = random.choice(fragments)
                        
                        while fragment in inserted_fragments:
                            fragment = random.choice(fragments)
                        
                        inserted_fragments.append(fragment)
                        position = random.randint(0, len(chosen_chromosome) - 1)
                        chosen_chromosome.insert(position, fragment)
                        new_genome[chosen_chromosome_index] = chosen_chromosome

                    inserted_fragment = inserted_fragments

                for i, chosen_chromosome_index in enumerate(chosen_chromosome_indices):
                    if 0 <= chosen_chromosome_index < len(valid_chromosomes) and 0 <= chosen_chromosome_index < len(new_genome):
                        chosen_chromosome = valid_chromosomes[chosen_chromosome_index]
                        fragment = inserted_fragments[i]
                        if fragment not in chosen_chromosome:
                            position = random.randint(0, len(chosen_chromosome))
                            chosen_chromosome.insert(position, fragment)
                        new_genome[chosen_chromosome_index] = chosen_chromosome
            else:
                print("No valid chromosomes available.")

            new_genome = tuple(new_genome) if isinstance(new_genome, tuple) else new_genome

            print(f"({new_genome}, {operation})")
        path_counter += 1


    print('\n\n')
    print('****************************************************************************************End of Analysis****************************************************************************************')
    print('*** ins = insertion, dele = deletion, dup = duplication, inv = inversion, fis = fission, fus = fusion, u_trl = unbalance translocation, b_trl = balance translocation, trp = transposition ***')

    sys.stdout.close()
    sys.stdout = stdoutOrigin



def main():
    parser = argparse.ArgumentParser(
        description='A program that outputs all the likely biological pathways that describes the evolution of one genome into another')
    parser.add_argument("-t", help="this is the set of genes(sequence blocks) representing the target genome", dest='target_genome',
                        required=True)
    parser.add_argument("-s", help="this is the set of genes(sequence blocks) representing the source genome",
                        dest='source_genome', required=True, )
    parser.add_argument("-r",
                        help='the ratios in which each evolutionary events is expected to occur in the order inversions, transpositions, balanced translocations, unbalanced translocations, fissions, fusions, insertions, deletions,duplications',
                        dest='ratios', required=True)
    parser.add_argument("-f", help="this is the set of foreign DNA fragments that are to be inserted into the genome", dest= "fDNA", required=True)
    parser.add_argument("-o", help="the name of the output file that will contain the set of evolutionary events that transformed the source genome into the target genome (solutions)",
                        dest='output_file', required=True)
    parser.set_defaults(func=run)
    args = parser.parse_args()
    args.func(args)



if __name__ == "__main__":
    main()
