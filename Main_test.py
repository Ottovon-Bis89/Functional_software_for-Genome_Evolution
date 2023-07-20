
import random
# import New_gen_node
# import Gen_Node
import GEN_NODE
import Gen_network
import sys


def pretty_print(list_of_operations):
    for key, value in list_of_operations.items():
        print(f"{key}: {value}")
    print("\n")
   




def pretty_print(list_of_legal_operations):
    for item in sorted(list_of_legal_operations):
        for x in item:
            if isinstance(x, dict):
                for key in sorted(x.keys()):
                    value = x[key]
                    print(f"  {key}:")
                    pretty_print(value)
            elif isinstance(x, list):
                sorted_list = sorted(x)
                for y in sorted_list:
                    if isinstance(y, dict):
                        for key in sorted(y.keys()):
                            value = y[key]
                            print(f"    {key}:")
                            pretty_print(value)
                    else:
                        print(f"    {y}")
            else:
                print(f"{x}")
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


# # gen_n_obj = new_version.Node() #UNCOMMENT ME
# # gen_n_obj  = New_gen_node.Node()
# # gen_n_obj = Gen_Node_edited.Node() #COMMENT ME OUT
# gen_i_obj = Intergenic_region_generator()

gen_n_obj = GEN_NODE.Node()
# gen_net = Gen_network()


 
# source_genome = [['*8', '1', '*6', '5','*6', '4', '*6','3', '*6','9' ], ['*8','10', '*10', '22', '*9', '37', '*9','33']]
# target_genome = [['*8','1','*8','4','*10','5', '*9','6'], ['*8','10','*9', '33','*7', '33', '*7', '40']]
# # #                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
source_genome = [['*6', '1', '*7', '2', '*8', '3', '*7', '4', '*9', '1', '*7', '5'],['*6', '8', '*9', '7', '*10', '6', '*7', '5', '*5', '1', '*8', '4', '*9', '1', '*7', '3', '*8', '1', '*8', '2'], ['*8', '9', '*7', '11'], ['*7', '20', '*8', '19', '*9', '18', '*6', '17', '*8', '16', '*6', '32', '*9', '10', '*8', '31', '*9', '30', '*7', '29', '*8', '28', '*6', '27'], ['*8', '21', '*7', '22', '*7', '23', '*8', '24', '*7', '25', '*6', '26'], ['*8', '33'], ['*7', '34', '*9', '35', '*7', '36', '*8', '37']]
target_genome = [['*5', '1', '*6', '2', '*7', '3', '*9', '4', '*8', '5', '*7', '6', '*6', '7', '*6', '8'],['*9', '9', '*8', '10', '*8', '11'], ['*8', '12', '*6', '13', '*7', '14', '*8', '15'],['*7', '16', '*6', '17', '*6', '18', '*8', '19', '*10', '20'], ['*9', '21', '*6', '22', '*7', '23', '*8', '24', '*8', '25', '*7', '26'], ['*8', '27', '*9', '28', '*9', '29', '*9', '30', '*8', '31', '*9', '32', '*8', '33'], ['*6', '34', '*6', '35', '*6', '36', '*7', '37', '*7', '38', '*6', '39', '*10', '40']]

# source_genome = [['*6', '1', '*7', '2', '*8', '3', '*7', '4', '*9', '1', '*7', '5'], ['*8', '4', '*9', '1', '*8', '1', '*8', '2', '*6', '8', '*9', '7', '*10', '6', '*7', '5', '*5', '1']]
# target_genome = [['*8', '1', '*6', '2', '*7', '3', '*9', '4','*8', '5', '*8' , '6', '*6', '7', '*6', '8'],['*9', '9','*8', '10', '*8', '11', "*9"]]

# source_genome = [['*6', 1, '*7', 2, '*8', 3, *7, 4, '*9', 1, '*7', 5], ['*8', 4, '*9', 1, '*8', 1, '*8', 2, '*6', 8, '*9', 7, '*10', 6, '*7', 5, '*5', 1]]
# target_genome = [['*8', 1, '*6', 2, '*7', 3, '*9', 4,'*8', 5, '*8' , 6, '*6', 7, '*6', 8],['*9', 9,'*8', 10, '*8', 11, '*9']]

# source_genome = [['*8', '1', '*9', '2', '*7', '3', '*6' , '4', '*10', '15'], ['*7', '-8', '*9', '-7','*6' ,'6', '*9', '-5', '*8', '-14', '*9', '-13', '*8' ,'-12'], ['*8', '9', '*7', '11'], ['*8','-20','*7', '-19', '*9','-18', '*7','-17','*8', '-16','*10', '-32','*9', '10','*8', '-31','*7', '-30', '*6','-29','*7', '-28','*8', '-27'], ['*8','21','*8', '22', '*8','23','*8' ,'24','*8' ,'25','*8' ,'26'], ['*8','-33'], ['*8','34','*8', '35', '*8','36', '*8','37','*8','38','*8', '39','*8', '40']]
# target_genome = [['*8','1', '*8','2', '*8','3', '*8','4','*8', '5', '*8','5' ,'*8','6', '*8','7','*8', '8'], ['*8','9', '*8','10','*8', '11'], ['*8','12','*8', '13','*8', '14','*8', '15', '*9', '13'], ['*8','16','*8', '17','*8', '18','*8', '19','*8', '20'], ['*8','21', '*8','22', '*8','23','*8', '24','*8','25','*8', '26'], ['*8','27','*8', '28', '*8','29', '*8','30','*8', '31','*8', '32','*8', '33'], ['*8','34', '*8','35','*8', '36','*8','37', '*8','38', '*8','39','*8','40']]

# # print(len(target_genome))
# for i, element in enumerate(target_genome):
#     print(i, element)


# target_genome = [['*7','1','*7', '2','*7', '3','*7', '4', '*7','5','*7', '6','*7', '7', '*7','8','*7', '9','*7', '10', '*7','11','*7', '12','*7', '13','*7', '14','*7', '15','*7', '16','*7', '17'], ['*7','18','*7', '19','*7', '20','*7', '21','*7', '22','*7', '23','*7', '24','*7', '25','*7', '26','*7', '27', '*7','28','*7', '29', '*7','30', '*7','31','*7', '32','*7', '33', '*7','34', '*7','35', '*7','36','*7', '37','*7', '38','*7', '39'], ['*7','40', '*7','41','*7', '42','*7', '43', '*7','44', '*7','45'], ['*7','46','*7', '47'],['*7','48'], ['*7','49','*7', '50']]
# source_genome =[['*9','1','*9', '2', '*9','3','*9', '4','*9', '5','*9', '6','*9', '7','*9', '8','*9', '9', '*9','10','*9', '-16','*9', '-15', '*9','-14', '*9','-13','*9', '-12', '*9','-11','*9', '42', '*9','43','*9', '44', '*9','-34','*9', '-33', '*9','-32', '*9','-31', '*9','-30','*9', '-29', '*9','-28','*9', '-27','*9', '-26', '*9','-25','*9', '-24','*9', '-40'], ['*9','-17', '*9','35','*9', '36', '*9','37', '*9','38', '*9','39'], ['*9','18','*9', '19','*9', '20', '*9','21','*9', '22', '*9','23', '*9','-50'], ['*9','-45'], ['*9','46'], ['*9','-47'], ['*9','48'], ['*9','49'], ['*9','41']]

# target_genome = [['*9','1','*9','2','*9','3'],['*9', '4','*9','5','*9','5'],['*9', '6','*9','7','*9','8','*9','9','*9','7'],['*9','10','*9','11'],['*9','12','*9','13','*9','14','*9','15','*9','16','*9','17'],['*9','18','*9','19','*9','20'],['*9','21','*9','22','*9','23','*9','24','*9','25'],['*9','26'],['*9', '27','*9','28','*9','29','*9','30','*9','31'],['*9','32','*9','33','*9','34'],['*9','35'],['*9','36'],['*9','37']] 
# source_genome = [['*9','1','*9','3'],[ '*9','5'],['*9','8','*9','6','*9','4','*9','7','*9','9'],['*9','21','*9','10','*9','-30','*9','11'],['*9', '19','*9','12','*9','14','*9','16','*9','17'],['*9','-15','*9','18','*9','20'],['*9', '22','*9','23','*9','25'],['*9','-24','*9','26'],['*9','28','*9','32','*9','27','*9','29','*9','31'],['*9','33','*9','-2','*9','34'],['*9','-13','*9','35'],['*9','37'],['*9','36']] 

# target_genome = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33], [34, 35, 36, 37, 38, 39, 40, 41, 42], [43], [44], [45, 46], [47], [48], [49, 50]]
# source_genome = [[1, 5], [6, 7, 8, 9, 10, 11, 12, 13, 29, 30, 2, 3, 31, 32, 33], [-18, -17, -16, -15, -14, -28, -27, -26, -25, -24, -23, -22, -21, -20, -19, -43], [34, 35, 36, 4, -50, -49], [-42, -41, -40, -39, -38, -37], [44], [45], [-46], [47], [48]]

# target_genome = [['*9', '1','*9', '2','*9', '3','*9', '4','*8', '5','*9', '6','*9', '7','*9', '8','*9', '9','*9' ,'10','*9', '11','*9', '12','*6', '13'], ['*9','14','*6', '15','*8', '16','*9','17','*6', '18','*9', '19','*9', '20','*10', '21','*10', '22','*7', '23','*9', '24','*9', '25','*6', '26','*9', '27','*9', '28','*8', '29','*9', '30','*6', '31'], ['*9','32','*7', '33','*9', '34'], ['*10','35','*9', '36','*6', '37','*9', '38'], ['*8','39','*9', '40']]
# source_genome = [['*9', '-13', '*9', '-12', '*9', '-11', '*9', '-10', '*9',  '-9','*9', '-8', '*9', '-7', '*9', '-6', '*9', '-5', '*9', '-4', '*9', '-3', '*9',  '-2', '*9',  '-1','*9',  '-29', '*9', '-28', '*9', '-27','*9', '-26','*9', '-25','*9', '-24', '*9', '-23','*9', '-22','*9', '-21','*9', '-20','*9' ,'-19','*9' ,'-18','*9', '*9', '-17','*9', '-16','*9', '-15','*9', '-14','*9', '-32'], ['*9','-38','*9', '37','*9', '-36','*9', '-35','*9','-40','*9', '-39'], ['*9','33','*9', '34','*9', '-31','*9', '-30']]

print("Target_genome:",target_genome)
print("\nSource_genome:",source_genome)
# print(len(target_genome))
# print(len(source_genome))

list_of_operations  = gen_n_obj.get_operations(source_genome, target_genome)
# network = gen_net.build_hash_table(source_genome, target_genome)

# print(network)

if source_genome==target_genome:
    print("Source genome same as target genome")

else:
    print("Source genome is different from target genome, possibly due to evolution")
print()
print("Initializing genome transformation process........")
print("\npredicting possible evolutionary events...")


print(f"Estimated total number of mutations: {len(list_of_operations)}\n")
# print("Printing solution sets........\n")

# for item in non_empty_legal_sub:
for item in list_of_operations:
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
#             solution.append(x)
#     random.shuffle(solution)
#     solutions.append(solution)

# for i, solution in enumerate(solutions):
#     print(f"Solution{i+1}: {solution}")


            
# all_fsrc = []
# all_solutions = []


# for i in range(len(list_of_operations)):
   
#     try:
        
#         sub = list_of_operations[i]
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
# for sub in list_of_operations:
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
      

# print(all_fsrc)
# print(all_solutions)
# sys.exit(0)

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


# all_fsrc = []
# all_solutions = []
# for sub in list_of_operations:
#     print("solution")
#     print(len(sub))
#     print(sub[0])
#     print()
#     all_fsrc.append(sub[1])
#     all_solutions.append(sub[2])
#     for op in sub[0]:
#         print(op)
#         print()
#     print('\n')

# print(all_fsrc)
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