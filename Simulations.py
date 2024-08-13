
from networkx import all_shortest_paths
from Path_node import Node
from Genome_extremities_and_adjacencies import Extremities_and_adjacencies
import Path_network
import random
import time
import argparse
import sys
import tracemalloc


def run_simulation(source_genome, target_genome, weight_ratios, fragments, output_file):
    t0 = time.time()
    tracemalloc.start()

    stdoutOrigin = sys.stdout
    sys.stdout = open(output_file, 'w')

    get_adjacencies = Extremities_and_adjacencies()

    adjacencies_genomeA = get_adjacencies.ordered_and_sorted_adjacencies(source_genome)
    adjacencies_genomeB = get_adjacencies.ordered_and_sorted_adjacencies(target_genome)

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

    Path_network.build_hash_table(start_node, hash_table, adjacencies_genomeB, weights, target_genome, source_genome)
    network = Path_network.build_network(hash_table)

    shortest_paths = list(all_shortest_paths(network, start_node, target_node, weight='weight'))

    tot_b_trl = tot_u_trl = tot_inv = tot_trp1 = tot_trp2 = tot_fus = tot_fis = tot_ins = tot_dele = tot_dup = 0

    Paths_state = []
    Paths_state_weight = []

    for path in shortest_paths:
        path_state = []
        path_state_weight = []

        i = 0
        while i < len(path):
            current = path[i]
            if i == 0:
                operation_type = 'none, this is the source genome'
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
        Paths_state.append((path_state))
        Paths_state_weight.append(path_state_weight)

    for path in shortest_paths:
        i = 0
        b_trl = u_trl = inv = trp1 = trp2 = fus = fis = ins = dele = dup = 0
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
                elif operation_type == 'ins':
                    ins += 1
                elif operation_type == 'dele':
                    dele += 1
                elif operation_type == 'dup':
                    dup += 1
            i += 1

        tot_b_trl += b_trl
        tot_u_trl += u_trl
        tot_inv += inv
        tot_trp1 += trp1
        tot_trp2 += trp2
        tot_fus += fus
        tot_fis += fis
        tot_ins += ins
        tot_dele += dele
        tot_dup += dup

    t1 = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    num_paths = len(shortest_paths)
    avg_edit_distance = float(tot_inv / num_paths) + float(tot_trp1 / num_paths) + float(2 * (tot_trp2 / num_paths)) + float(tot_b_trl / num_paths) + float(tot_u_trl / num_paths) + float(tot_fis / num_paths) + float(tot_fus / num_paths) + float(tot_ins / num_paths) + float(tot_dele / num_paths) + float(tot_dup / num_paths)

    print(f"Number of most likely biological paths (solutions): {num_paths}")
    print(f"Average number of evolutionary events per solution (Edit Distance): {avg_edit_distance}")
    print(f"Average number of each operation per solution:")
    print(f"Inversions: {float(tot_inv / num_paths)}  Transpositions type 1: {float(tot_trp1 / num_paths)}  Transpositions type 2: {float(tot_trp2 / num_paths)}  Balanced translocations: {float(tot_b_trl / num_paths)}  Unbalanced translocations: {float(tot_u_trl / num_paths)}  Fusions: {float(tot_fus / num_paths)}  Fissions: {float(tot_fis / num_paths)}  Insertions: {float(tot_ins / num_paths)}  Deletions: {float(tot_dele / num_paths)}  Duplications: {float(tot_dup / num_paths)}")
    print(f"Average time per simulation: {t1 - t0} seconds")
    print(f"Average memory used: {current / 10**6} MB, Peak memory: {peak / 10**6} MB")

    sys.stdout.close()
    sys.stdout = stdoutOrigin

    return num_paths, avg_edit_distance, t1 - t0, current / 10**6, peak / 10**6


def main():
    parser = argparse.ArgumentParser(description='A program that outputs all the optimal set of rearrangement operations that can describe the evolution of one genome into another')
    parser.add_argument("-r", help='the ratios in which each rearrangement is expected to occur in the order inversions, transpositions, balanced translocations, unbalanced translocations, fissions, fusions, insertions, deletions, duplications', dest='ratios', required=True)
    parser.add_argument("-f", help="this is the set of foreign DNA fragments that are to be inserted into the genome", dest="fDNA", required=True)
    args = parser.parse_args()

    with open(args.ratios) as f:
        weight_ratios = [list(map(int, line.strip().split(','))) for line in f]
    with open(args.fDNA) as f:
        fragments = [line.strip() for line in f]

    num_simulations = 10000
    num_pairs = 15

    for pair_index in range(1, num_pairs + 1):
        source_file = f"T{pair_index}_A.txt"
        target_file = f"T{pair_index}_B.txt"
        output_file = f"T{pair_index}_results.txt"

        with open(source_file) as f:
            source_genome = [list(map(int, line.strip().split(','))) for line in f]
        with open(target_file) as f:
            target_genome = [list(map(int, line.strip().split(','))) for line in f]

        total_paths = 0
        total_edit_distance = 0
        total_time = 0
        total_memory = 0
        total_peak_memory = 0

        for _ in range(num_simulations):
            num_paths, avg_edit_distance, exec_time, memory_used, peak_memory = run_simulation(source_genome, target_genome, weight_ratios, fragments, output_file)
            total_paths += num_paths
            total_edit_distance += avg_edit_distance
            total_time += exec_time
            total_memory += memory_used
            total_peak_memory += peak_memory

        with open(output_file, 'w') as out_file:
            out_file.write(f"Average number of most likely biological paths: {total_paths / num_simulations}\n")
            out_file.write(f"Average number of evolutionary events per solution: {total_edit_distance / num_simulations}\n")
            out_file.write(f"Average time per simulation: {total_time / num_simulations} seconds\n")
            out_file.write(f"Average memory used per simulation: {total_memory / num_simulations} MB\n")
            out_file.write(f"Average peak memory used per simulation: {total_peak_memory / num_simulations} MB\n")


if __name__ == "__main__":
    main()
