import itertools
import Gen_xtremities
import Gen_Node #UNCOMMENT ME
#import Gen_Node_edited #COMMENT ME OUT
import random

def pretty_print(legal_opperations):
    for key, value in legal_opperations.items():
        print(f"{key}: {value}")
    print("\n")

# def shuffle_solution (legal_opperations):
#     print(f"Total number of possible solutions: {len(legal_opperations)}")

#     for L in range(len(legal_opperations) + 1):
#         for subset in itertools.combinations(legal_opperations, L):
#             print(subset)

def sort_solution (sequence):
    splices = []
    for chromosome in sequence:
        splices.append([index for (index, value) in enumerate(chromosome) if value.startswith('*')])

    genome = []
    for chromosome in sequence:
        temp = [x for x in chromosome if '*' not in x]
        genome.append(temp)

    sorted_genome = []
    for item in genome:
        sort = sorted(item, key = lambda x : int(x.replace("_", "")))
        sorted_genome.append(sort)

    for index, value in enumerate(sorted_genome):
        for region in splices[index]:
            value.insert(region, sequence[index][region])

# data_target = []
# data_source = []
# with open("Generated_data.txt") as f:
#      lines = f.readlines()
#      for l in lines:
#          k = l.strip('\n').split(',')
#          data_source.append(k)

# with open("Generated_data_B.txt") as f:
#      lines = f.readlines()
#      for l in lines:
#          k = l.strip('\n').split(',')
#          data_target.append(k)

# print(data_source)
# print(data_target)
'''
gen_obj = Gen_Node.Node()
for_dna = gen_obj.foreign_dna_pool(data_source, data_target)
print(for_dna)
# print(len(for_dna))



#create the object
gen_x_obj = Gen_xtremities.Xtremities()
genome_gene_extremity = gen_x_obj.gene_extremity(data_source)
# print(genome_gene_extremity)
adjacencies_one = gen_x_obj.create_adjacencyList(data_source) #chromosome
# print()
# print((adjacencies_one))
# for i in adjacencies:
#     print(i)

adjacencies_sorted, adjacencies, telomers = gen_x_obj.adjacencies_ordered_and_sorted(data_source)
# print(adjacencies_sorted)
# print()
# print(adjacencies)
# print()
# print(telomers)
next_ext = gen_x_obj.find_next_extremity(adjacencies)
print(next_ext)
print()

next_extrem = gen_x_obj.find_next_adjacency(next_ext, adjacencies_one, telomers)
# print(telomers)
# print()
# print(next_ext)
# print()
# print(next_extrem)
linear_chromosomes, circular_chromosomes, genome = gen_x_obj.find_chromosome_type(adjacencies_one)
print(linear_chromosomes)
'''
#test mutations
#chrom = [1, '*', 2, '*8', 5, '*7', 6, '*6', 7, '*9', 8, '*', 9, '*',10]
# print(chrom)

gen_n_obj = Gen_Node.Node() #UNCOMMENT ME
#gen_n_obj = Gen_Node_edited.Node() #COMMENT ME OUT

# insert_mutation = gen_n_obj.insertion(chrom, 4)
# print(insert_mutation)

# del_mutation = gen_n_obj.deletion(chrom, 4)
# print(del_mutation)
# print(chrom)
# dup_mutation = gen_n_obj.duplication(chrom, 4, 8)
# print(dup_mutation)

# print(data_source)

# for_chrom = gen_n_obj.add_for_dna(data_source, [1,1,1,3])
# print(for_chrom)
# print(data_source)
# print()
# #test do mutation
# mutated_genome, list_of_mutations = gen_n_obj.do_mutation(data_source)
# print(list_of_mutations), [10,11,'*9', 33]
# print(mutated_genome) , [10, '*10', 22, '*9', 33]
# data_source = [['*8', '1', '*6', '5','*6', '4', '*6','3', '*','9_' ], ['*8','10', '*10', '22', '*9', '37', '*9','33']]
# data_target = [['*8','1','*','4','*','5', '*','6'], ['*8','10','*9', '33','*', '33', '*', '40']]
#                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      6                        
# source_genome = [['*6', '1', '*7', '2', '*8', '3', '*7', '4', '*9', '1', '*7', '5'],['*6', '8', '*9', '7', '*10', '6', '*7', '5', '*5', '1', '*8', '4', '*9', '1', '*7', '3', '*8', '1', '*8', '2'], ['*8', '9', '*7', '11'], ['*7', '20', '*8', '19', '*9', '18', '*6', '17', '*8', '16', '*6', '32', '*9', '10', '*8', '31', '*9', '30', '*7', '29', '*8', '28', '*6', '27'], ['*8', '21', '*7', '22', '*7', '23', '*8', '24', '*7', '25', '*6', '26'], ['*8', '33'], ['*7', '34', '*9', '35', '*7', '36', '*8', '37']]
# target_genome = [['*5', '1', '*6', '2', '*7', '3', '*9', '4', '*8', '5', '*7', '6', '*6', '7', '*6', '8'],['*9', '9', '*8', '10', '*8', '11'], ['*8', '12', '*6', '13', '*7', '14', '*8', '15'],['*7', '16', '*6', '17', '*6', '18', '*8', '19', '*10', '20'], ['*9', '21', '*6', '22', '*7', '23', '*8', '24', '*8', '25', '*7', '26'], ['*8', '27', '*9', '28', '*9', '29', '*9', '30', '*8', '31', '*9', '32', '*8', '33'], ['*6', '34', '*6', '35', '*6', '36', '*7', '37', '*7', '38', '*6', '39', '*10', '40']]

source_genome = [['*6', '1', '*7', '2', '*8', '3', '*7', '4', '*9', '1', '*7', '5'],['*6', '8', '*9', '7', '*10', '6', '*7', '5', '*5', '1', '*8', '4', '*9', '1', '*7', '3', '*8', '1', '*8', '2']]
target_genome = [['*5', '1', '*6', '2', '*7', '3', '*9', '4', '*8', '5', '*7', '6', '*6', '7', '*6', '8'],['*9', '9', '*8', '10', '*8', '11']]


list_of_legal_operations  = gen_n_obj.get_legal_operations(source_genome, target_genome)

print("\nList_of_legal_operations...")
# for item in list_of_legal_operations:
#     for x in item:
#         if (type(x) == dict):
#             pretty_print(x)
#         elif type(x) == list:
#             for y in x:
#                 if (type(y) == dict):
#                     pretty_print(y)
#                 else:
#                     print(y)
#         else:
#             print(x)
print(f"Total number of legal operations: {len(list_of_legal_operations)}\n")

# shuffle the list of list_legal_operations to get different sets of solutions
# create a master list to hold  the solutions
# master_list = []
# shuffle_solution(list_of_legal_operations)


# solution1  = random.sample(list_of_legal_operations, len(list_of_legal_operations))
# print(f"solution 1: {solution1}")

# shuffle list of legal operations and loop through the list to create new solutions
# for i in range(len(list_of_legal_operations)):
#     solution = random.sample(list_of_legal_operations, len(list_of_legal_operations))
#     master_list.append(solution)
#     print(f"solution {i}: {solution}")

#     #print(master_list)
#     print()
#     print()
#     print("list of solutions:" +str(master_list))
            
all_fsrc = []
all_solutions = []

for sub in list_of_legal_operations:
    try:
        print(f"Solution: {len(sub)}")
        sort_solution(sub[0]["Genome before mutation"])
        sort_solution(sub[0]["Genome after mutation"])
        pretty_print(sub[0])

        all_fsrc.append(sub[1])
        all_solutions.append(sub[2])
        for op in sub[0]:
            print(op)
    except:
        print("")
    

# print(all_fsrc)
# print(all_solutions)
#sys.exit(0)

# f = open("collection_final_source.txt", "w")
# for item in all_fsrc:
#     f.write(str(item))
#     f.write('\n')
# f.close()

# f1 = open("collection_final_solutions.txt", "w")
# for item in all_solutions:
#     f1.write(str(item))
#     f1.write('\n')
# f1.close()

