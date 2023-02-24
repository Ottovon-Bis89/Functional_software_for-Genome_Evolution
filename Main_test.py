import itertools
import Gen_xtremities
import Gen_Node #UNCOMMENT ME
#import Gen_Node_edited #COMMENT ME OUT
import random

def pretty_print(legal_opperations):
    for key, value in legal_opperations.items():
        print(f"{key}: {value}")
    print("\n")

# def sort_solution (sequence):
#     splices = []
#     for chromosome in sequence:
#         splices.append([index for (index, value) in enumerate(chromosome) if value.startswith('*')])

#     genome = []
#     for chromosome in sequence:
#         temp = [x for x in chromosome if '*' not in x]
#         genome.append(temp)

#     sorted_genome = []
#     for item in genome:
#         sort = sorted(item, key = lambda x : int(x.replace("_", "")))
#         sorted_genome.append(sort)

#     for index, value in enumerate(sorted_genome):
#         for region in splices[index]:
#             value.insert(region, sequence[index][region])

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

'''


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
#                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
# source_genome = [['*6', '1', '*7', '2', '*8', '3', '*7', '4', '*9', '1', '*7', '5'],['*6', '8', '*9', '7', '*10', '6', '*7', '5', '*5', '1', '*8', '4', '*9', '1', '*7', '3', '*8', '1', '*8', '2'], ['*8', '9', '*7', '11'], ['*7', '20', '*8', '19', '*9', '18', '*6', '17', '*8', '16', '*6', '32', '*9', '10', '*8', '31', '*9', '30', '*7', '29', '*8', '28', '*6', '27'], ['*8', '21', '*7', '22', '*7', '23', '*8', '24', '*7', '25', '*6', '26'], ['*8', '33'], ['*7', '34', '*9', '35', '*7', '36', '*8', '37']]
# target_genome = [['*5', '1', '*6', '2', '*7', '3', '*9', '4', '*8', '5', '*7', '6', '*6', '7', '*6', '8'],['*9', '9', '*8', '10', '*8', '11'], ['*8', '12', '*6', '13', '*7', '14', '*8', '15'],['*7', '16', '*6', '17', '*6', '18', '*8', '19', '*10', '20'], ['*9', '21', '*6', '22', '*7', '23', '*8', '24', '*8', '25', '*7', '26'], ['*8', '27', '*9', '28', '*9', '29', '*9', '30', '*8', '31', '*9', '32', '*8', '33'], ['*6', '34', '*6', '35', '*6', '36', '*7', '37', '*7', '38', '*6', '39', '*10', '40']]

source_genome = [['*6', '1', '*7', '2', '*8', '3', '*7', '4', '*9', '1', '*7', '5'],['*6', '8', '*9', '7', '*10', '6', '*7', '5', '*5', '1', '*8', '4', '*9', '1', '*7', '3', '*8', '1', '*8', '2']]
target_genome = [['*5', '1', '*6', '2', '*7', '3', '*9', '4', '*8', '5', '*7', '6', '*6', '7', '*6', '8'],['*9', '9', '*8', '10', '*8', '11']]


print("Target_genome:",target_genome)
print("\nSource_genome:",source_genome)
print()
print()
print()


list_of_legal_operations  = gen_n_obj.get_legal_operations(source_genome, target_genome)


print("Initializing ........")
print("\npredicting possible evolutionary events...")


print(f"Estimated total number of evolutionary events: {len(list_of_legal_operations)}\n")
print("Printing solution sets........\n")

print(list_of_legal_operations)



for item in list_of_legal_operations:
    for x in item:
        if (type(x) == dict):
            pretty_print(x)
        elif type(x) == list:
            for y in x:
                if (type(y) == dict):
                    pretty_print(y)
                else:
                    print(y)
        else:
            print(x)
 


# # List of mutations
# mutations = [list_of_legal_operations]

# # Generate all solution sets
# solutions = []
# for i in range(len(mutations)):
#     solution = random.sample(mutations, len(mutations))
#     solutions.append(solution)

# # Rearrange the mutations randomly in each solution set
# for i, solution in enumerate(solutions):
#     for j in range(len(solution)):
#         random.shuffle(solution)
#         solutions[i] = solution.copy()

# # Print each solution set
# for i, solution in enumerate(solutions):
#     print(f"Solution {i+1}:")
#     for j in range(0, len(solution), len(mutations)):
#         print(solution[j:j+len(mutations)])
#     print()


# solutions = []
# for i, item in enumerate(list_of_legal_operations):
#     solution = []
#     for x in item:
#         if type(x) == dict:
#             pretty_print(x)
#             solution.append(x)
#         elif type(x) == list:
#             for y in x:
#                 if type(y) == dict:
#                     pretty_print(y)
#                     solution.append(y)
#                 else:
#                     solution.append(y)
#         else:
#             solution.append(x)
#     random.shuffle(solution)
#     solutions.append(solution)

# for i, solution in enumerate(solutions):
#     print(f"Solution{i+1}: {solution}")


            
# all_fsrc = []
# all_solutions = []


# for i in range(len(list_of_legal_operations)):
   
#     try:
        
#         sub = list_of_legal_operations[i]
#         # print((sub[0]))
#         if type(sub[0]) is dict:
#             print(f"Solution: {(i)}")
#             print(sub[0]['Type'])
#         elif type(sub[0]) is list:
#             print(f"Solution: {(i)}")
#             print(sub[0])
#             single_solution = sub[0] 
#             print(single_solution)
#     except:
#         print("error")

# solution_counter = 1
# for sub in list_of_legal_operations:
#     try:
#         print(f"Solution: {solution_counter}")
#         print((sub[0]))
#     #     if type(sub[0]) is str:
#     #         print(sub[0])
#     #    elif type(sub[0]) is list:
#     #         print(sub[0])
#     #         print(sub[1])
#     #    sort_solution(sub[0]["Genome before mutation"])
#         sorted(sub[0]["Genome after mutation"])       
#         pretty_print(sub[0])

#         all_fsrc.append(sub[1])
#         all_solutions.append(sub[2])
#         for op in sub[0]:
#             print(op)
#         solution_counter +=1
#     except:
      
#         print("")
      

# # print(all_fsrc)
# print(all_solutions)
# #sys.exit(0)

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

