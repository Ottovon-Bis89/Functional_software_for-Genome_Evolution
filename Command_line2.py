import GEN_NODE
import Helper_Methods as HM
from tqdm import tqdm
import hashlib
from logger import log
from Cost_function import Cost
from collections import defaultdict
import argparse
import time
import sys

t0 = time.time()

itterations =1

def run(args):
    genomeA_file = args.source_genome
    genomeB_file = args.target_genome
    weight_ratios_file = args.ratios
    stdoutOrigin = sys.stdout
    sys.stdout = open(args.output_file, 'w')
    # outfile = open(args.output_file, 'w')
    with open(genomeA_file) as csv:
        line = [element.strip('\n').split(',') for element in csv]
    genomeA = []

    for element in line:
        element = list(map(int, element))
        genomeA.append(element)

    with open(genomeB_file) as csv:
        line = [element.strip('\n').split(',') for element in csv]
    genomeB = []

    for element in line:
        element = list(map(int, element))
        genomeB.append(element)

    with open(weight_ratios_file) as csv:
        line = [element.strip('\n').split(',') for element in csv]
    weight_ratios = []

    for element in line:
        element = list(map(int, element))
        weight_ratios.append(element)



gen_n_obj = GEN_NODE.Node()

genomeB = [[1, 2],[3, 4, 5],[6, 7],[8, 9, 10],[11],[12, 13, 14],[15, 16, 17, 18],[19, 20],[21, 22, 23]]
genomeA = [[1, 4, 2],[3, 5],[6],[8],[9, -13, 11],[12, 14],[15, 17, 22, 18],[19, 16, 20],[21, 7, 10, 23]]



solution = {}
solution_num = 1
solution_cost = {}
total_mutations = 0
mutation_counts = defaultdict(int)  # Initialize counts for each mutation type

#HM.create_new_file('solution_set.txt')

for _ in tqdm(range(itterations), total=itterations):
    for _ in range(itterations):
        list_of_operations = gen_n_obj.get_operations(genomeA, genomeB)
        mutation_solution = ""
        for item in list_of_operations:
            operations = item[0]
            mutation_solution += str(operations['Mut'])
            mutation_solution += str(operations['Chr'])
            mutation_solution += str(operations['Pos'])
            mutation_solution += str(operations['Gene'])
            total_mutations += 1
            # Increment counts for each mutation type in the solution
            for mutation_type in ['ins', 'del', 'dup', 'F_DNA']:
                mutation_counts[mutation_type] += 1 if operations['Mut'] == mutation_type else 0
        
        sha256_hash = hashlib.sha256(mutation_solution.encode()).hexdigest()

        if sha256_hash not in solution:
            solution[sha256_hash] = list_of_operations
            solution_cost[sha256_hash] = Cost().calc_cumulative_ratio(list_of_operations)

# Sort solution sets based on the accumulated cost
sorted_solution = sorted(solution.items(), key=lambda x: solution_cost[x[0]])
print()
print('************************************************************************************Genome Evolution Results*********************************************************')

# Write sorted solution sets to file
with open('solution_set.txt', 'a') as file:
    num_solutions = len(sorted_solution)
    avg_mutations_per_solution = total_mutations / num_solutions
    avg_mut_counts = {key: value / num_solutions for key, value in mutation_counts.items()}
    
    file.write(f"Estimated number of solutions: {num_solutions}\n")
    file.write(f"Average number of mutations per solution: {avg_mutations_per_solution}\n")
    file.write("Average number of each mutation per solution:\n")
    file.write(" ".join([f"{mutation_type}: {avg_count}" for mutation_type, avg_count in avg_mut_counts.items()]) + "\n")
    
    for i, (sha256_hash, list_of_operations) in enumerate(sorted_solution, 1):
        file.write(f"\nSolution {i}, Total Cost: {solution_cost[sha256_hash]}\n")
        
        for item in list_of_operations:
            operations = item[0]
            Mut = f"Mut: {operations['Mut']}, "
            Chr = f"Chr: {operations['Chr']}, "
            Pos = f"Pos: {operations['Pos']}, "
            Gene = f"Gene: {operations['Gene']}"
            Genome_after_mutation = f"Genome after mutation: {operations['Genome after mutation']}\n"

            file.write(Mut)
            file.write(Chr)
            file.write(Pos)
            file.write(Gene)
            file.write("\n")
            file.write(Genome_after_mutation)
            file.write("\n")


    print('***********************************************************************************Evolution Completed Successfully**************************************************')
    print()

    sys.stdout.close()
    stdoutOrigin = sys.stdout

def main():
    parser = argparse.ArgumentParser(
        description='A program that outputs all the possible set of evolutionary events that can describe the evolution of one genome into another')
    parser.add_argument("-t", help="this is the set of genes representing the target genome", dest='target_genome',
                        required=True)
    parser.add_argument("-s", help="this is the set of genes representing the source genome",
                        dest='source_genome', required=True, )
    parser.add_argument("-r",
                        help='the ratios in which each event is expected to occur in the order insertions, deletions, duplications, foreign DNA',
                        dest='ratios', required=True)
    parser.add_argument("-o", help="the name of the output file that will contain the set of events",
                        dest='output_file', required=True)
    parser.set_defaults(func=run)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()




