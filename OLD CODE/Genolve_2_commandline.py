from networkx import all_shortest_paths
from Gen_Node import Node

from Gen_xtremities import Xtremities
import Gen_network

import time
import argparse
import sys

t0 = time.time()


def run(args):
    genomeA_file = args.source_genome
    genomeB_file = args.target_genome
    weight_ratios_file = args.ratios
    stdoutOrigin = sys.stdout
    sys.stdout = open(args.output_file, 'w')
    # outfile = open(args.output_file, 'w')
    with open("D:/Bioinformatics/python_work/genA0.txt") as csv:
        line = [element.strip('\n').split(',') for element in csv]
    genomeA_file = []

    for element in line:
        element = list(map(int, element))
        genomeA_file.append(element)

    with open("D:/Bioinformatics/python_work/genB0.txt") as csv:
        line = [element.strip('\n').split(',') for element in csv]
    genomeB_file = []

    for element in line:
        element = list(map(int, element))
        genomeB_file.append(element)

    with open("D:/Bioinformatics/python_work/new_weight_ratios.txt") as csv:
        line = [element.strip('\n').split(',') for element in csv]
    weight_ratios_file = []

    for element in line:
        element = list(map(int, element))
        weight_ratios_file.append(element)

    get_extremities = Xtremities()
    adjacencies_genomeA = get_extremities.adjacencies_ordered_and_sorted(genomeA_file)

    adjacencies_genomeB = get_extremities.adjacencies_ordered_and_sorted(genomeB_file)

    # Create start and target node
    start_node = Node(adjacencies_genomeA)
    target_node = Node(adjacencies_genomeB)

    hash_table = {}
    hash_key_start = hash(str(start_node.state))
    hash_key_target = hash(str(target_node.state))
    hash_table.update({hash_key_start: start_node})
    hash_table.update({hash_key_target: target_node})

    # finding evolutionary events weights
    max_number = max(weight_ratios_file[0])
    weights = []
    for element in weight_ratios_file[0]:
        if element == 0:
            weights.append(max_number ^ 2)
        else:
            weights.append(max_number / element)

    Gen_network.build_hash_table(start_node, hash_table, adjacencies_genomeB, weights)

    network = Gen_network.build_network(hash_table)

    shortest_paths = (list(all_shortest_paths(network, start_node, target_node, weight='weight')))

    j = 1
    tot_ins = 0
    tot_del_ = 0
    tot_dup = 0
    tot_fDNA = 0

    Paths_state = []
    Paths_state_weight = []
    # print(shortest_paths[0][4].children_weights[2])
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
            genome = get_extremities.adjacencies_to_genome(adjacencies)
            path_state_weight.append((genome, ((operation_type, operation), operation_weight)))

            path_state.append((genome, (operation_type, operation)))

            i += 1
        Paths_state.append(path_state)
        Paths_state_weight.append(path_state_weight)

    for path in shortest_paths:

        i = 0
        ins = 0
        del_ = 0
        dup = 0
        fDNA = 0

        while i < len(path):

            current = path[i]
            if i == 0:
                pass
            else:
                x = path[i - 1].children.index(current)
                operation_type = path[i - 1].children_operations[x][1]
                if operation_type == 'ins':
                    ins += 1
                elif operation_type == 'del_':
                    del_ += 1
                elif operation_type == 'dup':
                    dup += 1
                elif operation_type == 'fDNA':
                    fDNA += 1
            i += 1

        tot_ins += ins
        tot_del_ += del_
        tot_dup += dup
        tot_fDNA += fDNA

        j += 1

    print(
        '############################################################################################################')
    print()
    print('Source Genome: ', genomeA_file)
    print('Target Genome: ', genomeB_file)
    print()
    print('Number of most parsimonious solutions: ', len(shortest_paths))
    print()
    print('Average number of operations per solution: ',
          float(tot_ins / len(shortest_paths)) + float(tot_del_ / len(shortest_paths)) + float(
              2 * (tot_dup / len(shortest_paths))) + float(tot_fDNA / len(shortest_paths)))
    print()
    print('Average number of each operation per solution:')
    print('Insertions: ', float(tot_ins / len(shortest_paths)), '  Deletions: ',
          float(tot_del_ / len(shortest_paths)), '  Duplications: ', float(tot_dup / len(shortest_paths)),
          '  Fragments_of_foreign_DNA: ', float(tot_fDNA / len(shortest_paths)))

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
        print()
    print()
    print(
        '############################################################################################################')

    sys.stdout.close()
    sys.stdout = stdoutOrigin


def main():
    parser = argparse.ArgumentParser(
        description='A program that outputs the optimal sequence and number of structural evolutionary events that '
                    'can cause the evolution of one genome into another')
    parser.add_argument("-t", help="this is the set of genes representing the target genome",
                        dest='target_genome',
                        required=True)
    parser.add_argument("-s", help="this is the set of genes representing the source genome",
                        dest='source_genome', required=True, )
    parser.add_argument("-r", help="the ratios in which each evolutionary event is expected to occur in the order "
                                   'insertions, duplication, deletion, fragment of foreign DNA',
                        dest='ratios', required=True)
    parser.add_argument("-o", help="the name of the output file that will contain the set of evolutionary events",
                        dest='output_file', required=True)
    parser.set_defaults(func=run)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
