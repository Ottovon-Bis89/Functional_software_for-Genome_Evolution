
# import new_version
# import gen_node_save
import random
# import New_gen_node
# import Gen_Node
import GEN_NODE


def pretty_print(list_of_legal_operations):
    for key, value in list_of_legal_operations.items():
        print(f"{key}: {value}")
    print("\n")
   




# def pretty_print(list_of_legal_operations):
#     for item in sorted(list_of_legal_operations):
#         for x in item:
#             if isinstance(x, dict):
#                 for key in sorted(x.keys()):
#                     value = x[key]
#                     print(f"  {key}:")
#                     pretty_print(value)
#             elif isinstance(x, list):
#                 sorted_list = sorted(x)
#                 for y in sorted_list:
#                     if isinstance(y, dict):
#                         for key in sorted(y.keys()):
#                             value = y[key]
#                             print(f"    {key}:")
#                             pretty_print(value)
#                     else:
#                         print(f"    {y}")
#             else:
#                 print(f"{x}")
#     print("\n")



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


# gen_n_obj = new_version.Node() #UNCOMMENT ME
# gen_n_obj  = New_gen_node.Node()
# gen_n_obj = Gen_Node_edited.Node() #COMMENT ME OUT
# gen_n_obj = Gen_Node.Node()

gen_n_obj = GEN_NODE.Node()



# data_source = [['*8', '1', '*6', '5','*6', '4', '*6','3', '*','9_' ], ['*8','10', '*10', '22', '*9', '37', '*9','33']]
# data_target = [['*8','1','*','4','*','5', '*','6'], ['*8','10','*9', '33','*', '33', '*', '40']]
#                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
# source_genome = [['*6', '1', '*7', '2', '*8', '3', '*7', '4', '*9', '1', '*7', '5'],['*6', '8', '*9', '7', '*10', '6', '*7', '5', '*5', '1', '*8', '4', '*9', '1', '*7', '3', '*8', '1', '*8', '2'], ['*8', '9', '*7', '11'], ['*7', '20', '*8', '19', '*9', '18', '*6', '17', '*8', '16', '*6', '32', '*9', '10', '*8', '31', '*9', '30', '*7', '29', '*8', '28', '*6', '27'], ['*8', '21', '*7', '22', '*7', '23', '*8', '24', '*7', '25', '*6', '26'], ['*8', '33'], ['*7', '34', '*9', '35', '*7', '36', '*8', '37']]
# target_genome = [['*5', '1', '*6', '2', '*7', '3', '*9', '4', '*8', '5', '*7', '6', '*6', '7', '*6', '8'],['*9', '9', '*8', '10', '*8', '11'], ['*8', '12', '*6', '13', '*7', '14', '*8', '15'],['*7', '16', '*6', '17', '*6', '18', '*8', '19', '*10', '20'], ['*9', '21', '*6', '22', '*7', '23', '*8', '24', '*8', '25', '*7', '26'], ['*8', '27', '*9', '28', '*9', '29', '*9', '30', '*8', '31', '*9', '32', '*8', '33'], ['*6', '34', '*6', '35', '*6', '36', '*7', '37', '*7', '38', '*6', '39', '*10', '40']]

source_genome = [['*6', '1', '*7', '2', '*8', '3', '*7', '4', '*9', '1', '*7', '5'],['*6', '8', '*9', '7', '*10', '6', '*7', '5', '*5', '1', '*8', '4', '*9', '1', '*7', '3', '*8', '1', '*8', '2']]
target_genome = [['*5', '1', '*6', '2', '*7', '3', '*9', '4', '*8', '5', '*7', '6', '*6', '7', '*6', '8'],['*9', '9', '*8', '10', '*8', '11']]

# target_genome = [[1,2,3],[ 4,5],[ 6,7,8,9],[ 10,11],[ 12,13,14,15,16,17],[ 18,19,20],[ 21,22,23,24,25],[ 26],[ 27,28,29,30,31],[ 32,33,34],[ 35],[ 36],[ 37]] 
# source_genome = [[1,3],[ 5],[8,6,4,7,9],[21,10,-30,11],[ 19,12,14,16,17],[ -15,18,20],[ 22,23,25],[ -24,26],[ 28,32,27,29,31],[ 33,-2,34],[ -13,35],[37],[ 36]] 


print("Target_genome:",target_genome)
print("\nSource_genome:",source_genome)
print()
print()

list_of_legal_operations  = gen_n_obj.get_legal_operations(source_genome, target_genome)
print()

if source_genome==target_genome:
    print("Source genome same as target genome")

else:
    print("Source genome is different from target genome, possibly due to evolution")
print()
print("Initializing genome transformation process........")
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


# # Define your list of legal operations
# legal_operations = [list_of_legal_operations]

# # Define the number of solutions you want to generate
# num_solutions = len(legal_operations)

# # Shuffle the list of legal operations
# random.shuffle(legal_operations)

# # Generate solutions by randomly dividing the shuffled list
# solutions = []
# for i in range(num_solutions):
#     start = i * (len(legal_operations) // num_solutions)
#     end = (i+1) * (len(legal_operations) // num_solutions)
#     solution = legal_operations[start:end]
#     random.shuffle(solution)
#     solutions.append(solution)

# # Print the solutions
# for i, solution in enumerate(solutions):
#     print(f"Solution {i+1}: {solution}")



#pretty_print(list_of_legal_operations)
 


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

