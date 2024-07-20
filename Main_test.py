# import GEN_NODE
# import Helper_Methods as HM
# from tqdm import tqdm
# import hashlib
# from logger import log
# from Cost_function import Cost
# from collections import defaultdict
# import networkx as nx
from ForeignDNA import Foreign_DNA

# itterations =2

# gen_n_obj = GEN_NODE.Node()

# # source_genome = [['*6', '1', '*7', '2', '*8', '3', '*7', '4', '*9', '1', '*7', '5','*9'], ['*8', '4', '*9', '1', '*8', '1', '*8', '2', '*6', '8', '*9', '7', '*10', '6', '*7', '5', '*5', '1','*9']]
# # target_genome = [['*8', '1', '*6', '2', '*7', '3', '*9', '4','*8', '5', '*8' , '6', '*6', '7', '*6', '5','*7','8','*9'],['*9', '9','*8', '10', '*8', '11', '*9']]

# target_genome = [[1, 2],[3, 4, 5],[6, 7],[8, 9, 10],[11],[12, 13, 14],[15, 16, 17, 18],[19, 20],[21, 22, 23]]
# source_genome = [[1, 4, 2],[3, 5],[6],[8],[9, -13, 11],[12, 14],[15, 17, 22, 18],[19, 16, 20],[21, 7, 10, 23]]

# log.debug("HELLO")

# source_genome = [['*8','1','*9','2','*7','3','*6','4','*10','15'], ['*7','-8','*9','-7','*6','6','*9','-5','*8','-14','*9','-13','*8','-12'], ['*8','9','*7','11'], ['*8','-20','*7','-19','*9','-18','*7','-17','*8','-16','*10','-32','*9','10','*8','-31','*7','-30','*6','-29','*7','-28','*8','-27'], ['*8','21','*8','22','*8','23','*8','24','*8','25','*8','26'], ['*8','-33'], ['*8','34','*8', '35','*8','36','*8','37','*8','38','*8','39','*8','40']]
# target_genome = [['*8','1', '*8','2', '*8','3', '*8','4','*8', '5', '*8' ,'6', '*8','7','*8', '8'], ['*8','9', '*8','10','*8', '11'], ['*8','12','*8', '13','*8', '14','*8', '15', '*9'], ['*8','16','*8', '17','*8', '18','*8', '19','*8', '20'], ['*8','21', '*8','22', '*8','23','*8', '24','*8','25','*8', '26'], ['*8','27','*8', '28', '*8','29', '*8','30','*8', '31','*8', '32','*8', '33'], ['*8','34', '*8','35','*8', '36','*8','37', '*8','38', '*8','39','*8','40']]

# target_genome = [['*7','1','*7', '2','*7', '3','*7', '4', '*7','5','*7', '6','*7', '7', '*7','8','*7', '9','*7', '10', '*7','11','*7', '12','*7', '13','*7', '14','*7', '15','*7', '16','*7', '17'], ['*7','18','*7', '19','*7', '20','*7', '21','*7', '22','*7', '23','*7', '24','*7', '25','*7', '26','*7', '27', '*7','28','*7', '29', '*7','30', '*7','31','*7', '32','*7', '33', '*7','34', '*7','35', '*7','36','*7', '37','*7', '38','*7', '39'], ['*7','40', '*7','41','*7', '42','*7', '43', '*7','44', '*7','45'], ['*7','46','*7', '47'],['*7','48'], ['*7','49','*7', '50']]
# source_genome =[['*9','1','*9', '2', '*9','3','*9', '4','*9', '5','*9', '6','*9', '7','*9', '8','*9', '9', '*9','10','*9', '-16','*9', '-15', '*9','-14', '*9','-13','*9', '-12', '*9','-11','*9', '42', '*9','43','*9', '44', '*9','-34','*9', '-33', '*9','-32', '*9','-31', '*9','-30','*9', '-29', '*9','-28','*9', '-27','*9', '-26', '*9','-25','*9', '-24','*9', '-40'], ['*9','-17', '*9','35','*9', '36', '*9','37', '*9','38', '*9','39'], ['*9','18','*9', '19','*9', '20', '*9','21','*9', '22', '*9','23', '*9','-50'], ['*9','-45'], ['*9','46'], ['*9','-47'], ['*9','48'], ['*9','49'], ['*9','41']]


# target_genome = [['*9','1','*9','2','*9','3'],['*9', '4','*9','5','*9'],['*9', '6','*9','7','*9','8','*9','9','*9'],['*9','10','*9','11'],['*9','12','*9','13','*9','14','*9','15','*9','16','*9','17'],['*9','18','*9','19','*9','20'],['*9','21','*9','22','*9','23','*9','24','*9','25'],['*9','26'],['*9', '27','*9','28','*9','29','*9','30','*9','31'],['*9','32','*9','33','*9','34'],['*9','35'],['*9','36'],['*9','37']] 
# source_genome = [['*9','1','*9','3'],[ '*9','5'],['*9','6','*9','4','*9','7','*9','9'],['*9','21','*9','10','*9','-30','*9','11'],['*9', '19','*9','12','*9','14','*9','16','*9','17'],['*9','-15','*9','18','*9','20'],['*9', '22','*9','23','*9','25'],['*9','-24','*9','26'],['*9','27','*9','32','*9','28','*9','29','*9','31'],['*9','33','*9','-2','*9','34'],['*9','-13','*9','35'],['*9','37'],['*9','36']] 

# target_genome = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33], [34, 35, 36, 37, 38, 39, 40, 41, 42], [43], [44], [45, 46], [47], [48], [49, 50]]
# source_genome = [[1, 5], [6, 7, 8, 9, 10, 11, 12, 13, 29, 30, 2, 3, 31, 32, 33], [-18, -17, -16, -15, -14, -28, -27, -26, -25, -24, -23, -22, -21, -20, -19, -43], [34, 35, 36, 4, -50, -49], [-42, -41, -40, -39, -38, -37], [44], [45], [-46], [47], [48]]

# target_genome = [['*9', '1','*9', '2','*9', '3','*9', '4','*8', '5','*9', '6','*9', '7','*9', '8','*9', '9','*9' ,'10','*9', '11','*9', '12','*6', '13'], ['*9','14','*6', '15','*8', '16','*9','17','*6', '18','*9', '19','*9', '20','*10', '21','*10', '22','*7', '23','*9', '24','*9', '25','*6', '26','*9', '27','*9', '28','*8', '29','*9', '30','*6', '31'], ['*9','32','*7', '33','*9', '34'], ['*10','35','*9', '36','*6', '37','*9', '38'], ['*8','39','*9', '40']]
# source_genome = [['*9', '-13', '*9', '-12', '*9', '-11', '*9', '-10', '*9',  '-9','*9', '-8', '*9', '-7', '*9', '-6', '*9', '-5', '*9', '-4', '*9', '-3', '*9',  '-2', '*9',  '-1','*9',  '-29', '*9', '-28', '*9', '-27','*9', '-26','*9', '-25','*9', '-24', '*9', '-23','*9', '-22','*9', '-21','*9', '-20','*9' ,'-19','*9' ,'-18','*9', '*9', '-17','*9', '-16','*9', '-15','*9', '-14','*9', '-32'], ['*9','-38','*9', '37','*9', '-36','*9', '-35','*9','-40','*9', '-39'], ['*9','33','*9', '34','*9', '-31','*9', '-30']]

 
# source_genome = [['*8', '1','*6', '4', '*6','3', '*6','9' ], ['*8','10', '*10', '22', '*9', '37', '*9','33']]
# target_genome = [['*8','1','*8','4','*10','5', '*9','6'], ['*8','10','*9', '33','*7', '33', '*7', '40']]

# source_genome = [['*8', '1','*6', '5','*6', '4', '*6','3' ], ['*8','10', '*10', '22', '*9', '37', '*9','33']]
# target_genome = [['*8','1', '*9','2','*8', '3','*8','4','*10','5', '*9','6'], ['*8','10','*9', '33','*7', '34', '*7', '33', '*8', '40']]


# target_genome = [['*6', '1', '*9', '2', '*7', '3'],['*8', '4', '*6', '5'],['*6', '6', '*10', '7', '*10', '8', '*9', '9'],['*9', '10', '*10', '11', '*10', '12'],['*9', '13', '*9', '14'],['*7', '15', '*10', '16'],['*6', '17'],['*6', '18'],['*6', '19', '*10', '20', '*6', '21'],['*6', '22']] 
# source_genome = [['*6', '1', '*6', '3'],['*6', '5','*9', '8' ],['*7', '6', '*9', '4', '*9', '7', '*9', '9'],['*8', '13', '*10', '10', '*9', '12'],['*9', '14'],['*9', '16'],['*6', '-15','*9', '17'],['*9','19', '*8', '18'],['*9', '20', '*7', '-2', '*9', '21'],['*9', '-11', '*8', '22']] 
# # # # #                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
# source_genome = [['*6', '1', '*7', '2', '*8', '3', '*7', '4', '*9', '1', '*7', '5'],['*6', '8', '*9', '7', '*10', '6', '*7', '5', '*5', '1', '*8', '4', '*9', '1', '*7', '3', '*8', '1', '*8', '2'], ['*8', '9', '*7', '11'], ['*7', '20', '*8', '19', '*9', '18', '*6', '17', '*8', '16', '*6', '32', '*9', '10', '*8', '31', '*9', '30', '*7', '29', '*8', '28', '*6', '27'], ['*8', '21', '*7', '22', '*7', '23', '*8', '24', '*7', '25', '*6', '26'], ['*8', '33'], ['*7', '34', '*9', '35', '*7', '36', '*8', '37']]
# target_genome = [['*5', '1', '*6', '2', '*7', '3', '*9', '4', '*8', '5', '*7', '6', '*6', '7', '*6', '8'],['*9', '9', '*8', '10', '*8', '11'], ['*8', '12', '*6', '13', '*7', '14', '*8', '15'],['*7', '16', '*6', '17', '*6', '18', '*8', '19', '*10', '20'], ['*9', '21', '*6', '22', '*7', '23', '*8', '24', '*8', '25', '*7', '26'], ['*8', '27', '*9', '28', '*9', '29', '*9', '30', '*8', '31', '*9', '32', '*8', '33'], ['*6', '34', '*6', '35', '*6', '36', '*7', '37', '*7', '38', '*6', '39', '*10', '40']]

# target_genome=[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17],[18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39]]
# source_genome=[[1,2,3,4,5,6,7,8,9,10,-16,-15,-14,-13,-12,-11,42,43,44,-34,-33,-32,-31,-30,-29,-28,-27,-26,-25,-24,-40],[-17,35,36,37,38,39]]

# source_genome=[[1,2,3,4,15],[-8,-7,6,-5,-14,-13,-12],[9,11],[-20,-19,-18,-17,-16,-32,10,-31,-30,-29,-28,-27],[21,22,23,24,25,26],[-33],[34,35,36,37,38,39,40]]
# target_genome=[[1,2,3,4,5,6,7,8],[9,10,11],[12,13,14,15],[16,17,18,19,20],[21,22,23,24,25,26],[27,28,29,30,31,32,33],[34,35,36,37,38,39,40]]


# solution_sets = {}
# solution_num = 1

# HM.create_new_file('solution_set.txt')


# for _ in tqdm(range(itterations), total=itterations):
#     for _ in range(itterations):

#         list_of_operations = gen_n_obj.get_operations(source_genome, target_genome)
#     mutation_solution = ""
#     for item in list_of_operations:

#         operations = item[0]
#         mutation_solution += str(operations['Mut'])
#         mutation_solution += str(operations['Chr'])
#         mutation_solution += str(operations['Pos'])
#         mutation_solution += str(operations['Gene'])
#     print(len(list_of_operations))
#     W = Cost()
#     print(W.calc_cumulative_ratio(list_of_operations))
#     # Use SHA-256 to calculate the hash value
#     sha256_hash = hashlib.sha256(mutation_solution.encode()).hexdigest()

#     if sha256_hash not in solution_sets:
#         HM.append_new_solution_heading(solution_num)
#         solution_num += 1
#         solution_sets[sha256_hash] = mutation_solution

#         HM.append_to_file("solution_set.txt","\nEstimated total number of mutations:")
#         HM.append_to_file("solution_set.txt",str(len(list_of_operations)))
#         HM.append_to_file("solution_set.txt","\nPrinting solution sets........\n\n")

#         for item in list_of_operations:
#             operations = item[0]
#             Mut = f"Mut: {operations['Mut']}, "
#             Chr = f"Chr: {operations['Chr']}, "
#             Pos = f"Pos: {operations['Pos']}, "
#             Gene = f"Gene: {operations['Gene']}"
#             Genome_after_mutation = f"Genome after mutation: {operations['Genome after mutation']}\n"

#             HM.append_to_file("solution_set.txt",Mut)
#             HM.append_to_file("solution_set.txt",Chr)
#             HM.append_to_file("solution_set.txt",Pos)
#             HM.append_to_file("solution_set.txt",Gene)
#             HM.append_new_line()
#             HM.append_to_file("solution_set.txt",Genome_after_mutation)
#             HM.append_new_line()

# HM.End_of_file()






# solutions = {}
# solution_num = 1
# solution_cost = {}  # Dictionary to store the total cost for each solution set

# HM.create_new_file('solutions.txt')

# for _ in tqdm(range(itterations), total=itterations):
#     for _ in range(itterations):
#         list_of_operations = gen_n_obj.get_operations(source_genome, target_genome)
#         mutation_solution = ""
#         for item in list_of_operations:
#             operations = item[0]
#             mutation_solution += str(operations['Mut'])
#             mutation_solution += str(operations['Chr'])
#             mutation_solution += str(operations['Pos'])
#             mutation_solution += str(operations['Gene'])
        
#         sha256_hash = hashlib.sha256(mutation_solution.encode()).hexdigest()

#         if sha256_hash not in solutions:
#             solutions[sha256_hash] = list_of_operations
#             solution_cost[sha256_hash] = Cost().calc_cumulative_ratio(list_of_operations)

# # Sort solution sets based on the accumulated cost
# sorted_solutions = sorted(solutions.items(), key=lambda x: solution_cost[x[0]])

# # Write sorted solution sets to file
# with open('solutions.txt', 'a') as file:
#     for i, (sha256_hash, list_of_operations) in enumerate(sorted_solutions, 1):
#         file.write(f"Solution {i}, Total Cost: {solution_cost[sha256_hash]}\n")
#         file.write(f"\nEstimated total number of mutations: {len(list_of_operations)}\n")
#         for item in list_of_operations:
#             operations = item[0]
#             Mut = f"Mut: {operations['Mut']}, "
#             Chr = f"Chr: {operations['Chr']}, "
#             Pos = f"Pos: {operations['Pos']}, "
#             Gene = f"Gene: {operations['Gene']}"
#             Genome_after_mutation = f"Genome after mutation: {operations['Genome after mutation']}\n"

#             file.write(Mut)
#             file.write(Chr)
#             file.write(Pos)
#             file.write(Gene)
#             file.write("\n")
#             file.write(Genome_after_mutation)
#             file.write("\n")



# solution_sets = {}
# solution_num = 1
# solution_costs = {}
# total_mutations = 0
# mutation_counts = {'Mut': 0}

# HM.create_new_file('solution_set.txt')

# for _ in tqdm(range(itterations), total=itterations):
#     for _ in range(itterations):
#         list_of_operations = gen_n_obj.get_operations(source_genome, target_genome)
#         mutation_solution = ""
#         for item in list_of_operations:
#             operations = item[0]
#             mutation_solution += str(operations['Mut'])
#             mutation_solution += str(operations['Chr'])
#             mutation_solution += str(operations['Pos'])
#             mutation_solution += str(operations['Gene'])
#             total_mutations += 1
#             mutation_counts['Mut'] += mutation_solution.count('Mut')
        
#         sha256_hash = hashlib.sha256(mutation_solution.encode()).hexdigest()

#         if sha256_hash not in solution_sets:
#             solution_sets[sha256_hash] = list_of_operations
#             solution_costs[sha256_hash] = Cost().calc_cumulative_ratio(list_of_operations)

# # Sort solution sets based on the accumulated cost
# sorted_solution_sets = sorted(solution_sets.items(), key=lambda x: solution_costs[x[0]])

# # Write sorted solution sets to file
# with open('solution_set.txt', 'a') as file:
#     num_solutions = len(sorted_solution_sets)
#     avg_mutations_per_solution = total_mutations / num_solutions
#     avg_mut_counts = {key: value / num_solutions for key, value in mutation_counts.items()}
    
#     file.write(f"Estimated number of solutions: {num_solutions}\n")
#     file.write(f"Average number of mutations per solution: {avg_mutations_per_solution}\n")
#     file.write("Average number of each mutation per solution:\n")
#     for key, value in avg_mut_counts.items():
#         file.write(f"{key}: {value}\n")
    
#     for i, (sha256_hash, list_of_operations) in enumerate(sorted_solution_sets, 1):
#         file.write(f"\nSolution Set {i}, Total Cost: {solution_costs[sha256_hash]}\n")
#         file.write(f"Estimated total number of mutations: {len(list_of_operations)}\n")
#         file.write("Printing solution sets........\n\n")
#         for item in list_of_operations:
#             operations = item[0]
#             Mut = f"Mut: {operations['Mut']}, "
#             Chr = f"Chr: {operations['Chr']}, "
#             Pos = f"Pos: {operations['Pos']}, "
#             Gene = f"Gene: {operations['Gene']}"
#             Genome_after_mutation = f"Genome after mutation: {operations['Genome after mutation']}\n"

#             file.write(Mut)
#             file.write(Chr)
#             file.write(Pos)
#             file.write(Gene)
#             file.write("\n")
#             file.write(Genome_after_mutation)
#             file.write("\n")




# solution = {}
# solution_num = 1
# solution_cost = {}
# total_mutations = 0
# mutation_counts = {'Mut': 0}

# HM.create_new_file('solution_set.txt')

# for _ in tqdm(range(itterations), total=itterations):
#     for _ in range(itterations):
#         list_of_operations = gen_n_obj.get_operations(source_genome, target_genome)
#         mutation_solution = ""
#         for item in list_of_operations:
#             operations = item[0]
#             mutation_solution += str(operations['Mut'])
#             mutation_solution += str(operations['Chr'])
#             mutation_solution += str(operations['Pos'])
#             mutation_solution += str(operations['Gene'])
#             total_mutations += 1
#             mutation_counts['Mut'] += 1
        
#         sha256_hash = hashlib.sha256(mutation_solution.encode()).hexdigest()

#         if sha256_hash not in solution:
#             solution[sha256_hash] = list_of_operations
#             solution_cost[sha256_hash] = Cost().calc_cumulative_ratio(list_of_operations)

# # Sort solution sets based on the accumulated cost
# sorted_solution_set = sorted(solution.items(), key=lambda x: solution_cost[x[0]])

# # Write sorted solution set to file
# with open('solution_set.txt', 'a') as file:
#     num_solutions = len(sorted_solution_set)
#     avg_mutations_per_solution = total_mutations / num_solutions
#     avg_mut_counts = {key: value / num_solutions for key, value in mutation_counts.items()}
    
#     file.write(f"Estimated number of solutions: {num_solutions}\n")
#     file.write(f"Average number of mutations per solution: {avg_mutations_per_solution}\n")
#     file.write("Average number of each mutation per solution:\n")
#     for key, value in avg_mut_counts.items():
#         file.write(f"{key}: {value}\n")
    
#     for i, (sha256_hash, list_of_operations) in enumerate(sorted_solution_set, 1):
#         file.write(f"\nSolution {i}, Total Cost: {solution_cost[sha256_hash]}\n")
#         for item in list_of_operations:
#             operations = item[0]
#             Mut = f"Mut: {operations['Mut']}, "
#             Chr = f"Chr: {operations['Chr']}, "
#             Pos = f"Pos: {operations['Pos']}, "
#             Gene = f"Gene: {operations['Gene']}"
#             Genome_after_mutation = f"Genome after mutation: {operations['Genome after mutation']}\n"

#             file.write(Mut)
#             file.write(Chr)
#             file.write(Pos)
#             file.write(Gene)
#             file.write("\n")
#             file.write(Genome_after_mutation)
#             file.write("\n")



# solution = {}
# solution_num = 1
# solution_cost = {}
# total_mutations = 0
# mutation_counts = defaultdict(int)  # Initialize counts for each mutation type

# HM.create_new_file('solution_set.txt')

# for _ in tqdm(range(itterations), total=itterations):
#     for _ in range(itterations):
#         list_of_operations = gen_n_obj.get_operations(source_genome, target_genome)
#         mutation_solution = ""
#         for item in list_of_operations:
            
#             operation = item[0]
#             mutation_solution += str(operation['Mut'])
#             mutation_solution += str(operation['Chr'])
#             mutation_solution += str(operation['Pos'])
#             mutation_solution += str(operation['Gene'])
#             total_mutations += 1
#             # Increment counts for each mutation type in the solution
#             for mutation_type in ['ins', 'del', 'dup', 'F_DNA']:
#                 mutation_counts[mutation_type] += 1 if operation['Mut'] == mutation_type else 0
        
#         sha256_hash = hashlib.sha256(mutation_solution.encode()).hexdigest()

#         if sha256_hash not in solution:
#             solution[sha256_hash] = list_of_operations
#             solution_cost[sha256_hash] = Cost().calc_cumulative_ratio(list_of_operations)

# # Sort solution sets based on the accumulated cost
# sorted_solution = sorted(solution.items(), key=lambda x: solution_cost[x[0]])

# # Write sorted solution sets to file
# with open('solution_set.txt', 'a') as file:
#     num_solutions = len(sorted_solution)
#     avg_mutations_per_solution = total_mutations / num_solutions
#     avg_mut_counts = {key: value / num_solutions for key, value in mutation_counts.items()}
    
#     file.write(f"Estimated number of solutions: {num_solutions}\n")
#     file.write(f"Average number of mutations per solution: {avg_mutations_per_solution}\n")
#     file.write("Average number of each mutation per solution:\n")
#     file.write(" ".join([f"{mutation_type}: {avg_count}" for mutation_type, avg_count in avg_mut_counts.items()]) + "\n")
    
#     for i, (sha256_hash, list_of_operations) in enumerate(sorted_solution, 1):
#         file.write(f"\nSolution {i}, Total Cost: {solution_cost[sha256_hash]}\n")
        
#         for item in list_of_operations:
#             operations = item[0]
#             Mut = f"Mut: {operations['Mut']}, "
#             Chr = f"Chr: {operations['Chr']}, "
#             Pos = f"Pos: {operations['Pos']}, "
#             Gene = f"Gene: {operations['Gene']}"
#             Genome_after_mutation = f"Genome after mutation: {operations['Genome after mutation']}\n"

#             file.write(Mut)
#             file.write(Chr)
#             file.write(Pos)
#             file.write(Gene)
#             file.write("\n")
#             file.write(Genome_after_mutation)
#             file.write("\n")

# HM.End_of_file()

# import networkx as nx
# from collections import defaultdict
# from tqdm import tqdm

# def solution_hash_to_list_of_operations(solution_hash):
#     """
#     Given a solution hash, retrieve the list of operations associated with it.
#     """
#     # # Reverse the process of hashing by decoding the solution hash
#     # decoded_hash = bytes.fromhex(solution_hash).decode()
#     # Split the decoded hash into individual operations
#     operations = [solution_hash[i:i+4] for i in range(0, len(solution_hash), 4)]
#     # Convert each operation back to dictionary format
#     list_of_operations = [{'Mut': op[:1], 'Chr': op[1:2], 'Pos': op[2:3], 'Gene': op[3:]} for op in operations]
#     return list_of_operations

# solution_cost = {}
# mutation_counts = defaultdict(int)  # Initialize counts for each mutation type

# HM.create_new_file('solution_set.txt')

# # Create a graph to store solutions and their costs
# solution_graph = nx.DiGraph()

# for _ in tqdm(range(itterations), total=itterations):
#     for _ in range(itterations):
#         list_of_operations = gen_n_obj.get_operations(source_genome, target_genome)
#         mutation_solution = ""
#         for item in list_of_operations:
#             operation = item[0]
#             mutation_solution += str(operation['Mut'])
#             mutation_solution += str(operation['Chr'])
#             mutation_solution += str(operation['Pos'])
#             mutation_solution += str(operation['Gene'])
#             # Increment counts for each mutation type in the solution
#             mutation_counts[operation['Mut']] += 1
        
#         sha256_hash = hashlib.sha256(mutation_solution.encode()).hexdigest()

#         if sha256_hash not in solution_cost:
#             solution_cost[sha256_hash] = Cost().calc_cumulative_ratio(list_of_operations)
#             solution_graph.add_node(sha256_hash, cost=solution_cost[sha256_hash])
        
#         for i in range(len(list_of_operations) - 1):
#             from_node = hashlib.sha256("".join(map(str, list_of_operations[:i + 1])).encode()).hexdigest()
#             to_node = hashlib.sha256("".join(map(str, list_of_operations[:i + 2])).encode()).hexdigest()
#             solution_graph.add_edge(from_node, to_node)

# # Find the shortest path in the graph
# shortest_path = nx.shortest_path(solution_graph, weight='cost')

# # Write sorted solution sets to file based on the shortest path
# with open('solution_set.txt', 'a') as file:
#     num_solutions = len(shortest_path)
#     avg_mutations_per_solution = sum(mutation_counts.values()) / num_solutions
#     avg_mut_counts = {key: value / num_solutions for key, value in mutation_counts.items()}
    
#     file.write(f"Estimated number of solutions: {num_solutions}\n")
#     file.write(f"Average number of mutations per solution: {avg_mutations_per_solution}\n")
#     file.write("Average number of each mutation per solution:\n")
#     file.write(" ".join([f"{mutation_type}: {avg_count}" for mutation_type, avg_count in avg_mut_counts.items()]) + "\n")
    
#     for i, solution_hash in enumerate(shortest_path, 1):
#         if solution_hash in solution_cost:
#             file.write(f"\nSolution {i}, Total Cost: {solution_cost[solution_hash]}\n")
        
#             # Retrieve the list_of_operations associated with the solution_hash using the function
#             list_of_operations = solution_hash_to_list_of_operations(solution_hash)
            
#             for item in list_of_operations:
#                 operation = item[0]
#                 Mut = f"Mut: {operation['Mut']}, "
#                 Chr = f"Chr: {operation['Chr']}, "
#                 Pos = f"Pos: {operation['Pos']}, "
#                 Gene = f"Gene: {operation['Gene']}\n"

#                 file.write(Mut)
#                 file.write(Chr)
#                 file.write(Pos)
#                 file.write(Gene)

# HM.End_of_file()







# def main():
#     parser = argparse.ArgumentParser(
#         description='A program that outputs all the possible set of evolutionary events that can describe the evolution of one genome into another')
#     parser.add_argument("-t", help="this is the set of genes representing the target genome", dest='target_genome',
#                         required=True)
#     parser.add_argument("-s", help="this is the set of genes representing the source genome",
#                         dest='source_genome', required=True, )
#     parser.add_argument("-r",
#                         help='the ratios in which each rearrangement is expected to occur in the order inversions, transpositions, balanced translocations, unbalanced translocations, fissions, fusions',
#                         dest='ratios', required=True)
#     parser.add_argument("-o", help="the name of the output file that will contain the set of rearrangements",
#                         dest='output_file', required=True)
#     parser.set_defaults(func=run)
#     args = parser.parse_args()
#     args.func(args)


# if __name__ == "__main__":
#     main()




# Original tuples
# tuple1 = (14.5, 21)
# tuple2 = (15, 20.5)

# # Function to create a rearranged tuple with elements in increasing order
# def create_ordered_tuple(a, b, c):
#     if a < b:
#         return (a, '*new', b)
#     else:
#         return (b, '*new', a)

# # Rearranging tuples
# rearranged_tuple1 = create_ordered_tuple(tuple1[1], tuple2[1], '*new')  # (21, '*new', 20.5)
# rearranged_tuple2 = create_ordered_tuple(tuple1[0], tuple2[0], '*new')  # (14.5, '*new', 15)

# print(rearranged_tuple1)
# print(rearranged_tuple2)

# Original tuples in operation
# operation = [((14.5, 21), (15, 20.5))]

# # Assuming state_copy contains the original tuples
# state_copy = list(operation[0])

# # Initialize operation_type
# operation_type = None

# # Check if the elements in operation are tuples
# if isinstance(operation[0][0], tuple) and isinstance(operation[0][1], tuple):
#     # Print original tuples (for debugging)
#     # print('opp1: ', operation[0][0], operation[0][1])
    
#     # Deletion operation: Remove the original tuples from state_copy
#     state_copy.remove(operation[0][0])
#     state_copy.remove(operation[0][1])
    
#     # Set the operation type to 'del' for deletion
#     operation_type = 'del'
#     print("Operation type (deletion):", operation_type)
    
#     # Insertion operation: Create new tuples and add to state_copy
#     state_copy.append(operation[0][0][0], operation[0][1][0])  # (14.5, 15)
#     state_copy.append(operation[0][1][1], operation[0][0][1])  # (20.5, 21)
#     # state_copy.append(new_tuple1)
#     # state_copy.append(new_tuple2)
    
#     # Set the operation type to 'ins' for insertion
#     operation_type = 'ins'

# # Print the updated state_copy
# print(state_copy)
# print("Operation type (insertion):", operation_type)




#single DNA fragment insertion code

            # if valid_chromosomes:
            #     if inserted_fragment is None:
            #         chosen_chromosome_index = random.randint(0, len(valid_chromosomes) - 1) 
            #         chosen_chromosome = valid_chromosomes[chosen_chromosome_index]
            #         fragment = random.choice(fragments)
            #         position = random.randint(0, len(chosen_chromosome) - 1)
            #         chosen_chromosome.insert(position, fragment)
            #         inserted_fragment = fragment
                
            #     if 0 <= chosen_chromosome_index < len(valid_chromosomes) and 0 <= chosen_chromosome_index < len(new_genome):
            #         chosen_chromosome = valid_chromosomes[chosen_chromosome_index]
            #         if inserted_fragment not in chosen_chromosome:
            #             position = random.randint(0, len(chosen_chromosome))
            #             chosen_chromosome.insert(position, inserted_fragment)
            #         new_genome[chosen_chromosome_index] = chosen_chromosome
            # else:
            #     print("No valid chromosomes available.")
                
            
            # new_genome = tuple(new_genome) if isinstance(genome, tuple) else new_genome
            
            # print(f"[{new_genome}], {operation}")

dna = Foreign_DNA()
dna.run("/home/22204911/Documents/Test_test/T4_A.txt", "/home/22204911/Documents/Test_test/T4_B.txt", "/home/22204911/Documents/Test_test/fragg.txt")
