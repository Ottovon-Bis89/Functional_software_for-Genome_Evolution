import GEN_NODE
import Helper_Methods as HM
from tqdm import tqdm
import hashlib
from logger import log

itterations = 1

gen_n_obj = GEN_NODE.Node()

# source_genome = [['*6', '1', '*7', '2', '*8', '3', '*7', '4', '*9', '1', '*7', '5','*9'], ['*8', '4', '*9', '1', '*8', '1', '*8', '2', '*6', '8', '*9', '7', '*10', '6', '*7', '5', '*5', '1','*9']]
# target_genome = [['*8', '1', '*6', '2', '*7', '3', '*9', '4','*8', '5', '*8' , '6', '*6', '7', '*6', '5','*7','8','*9'],['*9', '9','*8', '10', '*8', '11', '*9']]

target_genome = [[1, 2],[3, 4, 5],[6, 7],[8, 9, 10],[11],[12, 13, 14],[15, 16, 17, 18],[19, 20],[21, 22, 23]]
source_genome = [[1, 4, 2],[3, 5],[6],[8],[9, -13, 11],[12, 14],[15, 17, 22, 18],[19, 16, 20],[21, 7, 10, 23]]

log.debug("HELLO")

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

 
# source_genome = [['*8', '1', '*6', '5','*6', '4', '*6','3', '*6','9' ], ['*8','10', '*10', '22', '*9', '37', '*9','33']]
# target_genome = [['*8','1','*8','4','*10','5', '*9','6'], ['*8','10','*9', '33','*7', '33', '*7', '40']]

# source_genome = [['*8', '1', '*6', '5','*6', '4', '*6','3', '*6','9' ], ['*8','10', '*10', '22', '*9', '37', '*9','33']]
# target_genome = [['*8','1', '*8', '3','*8','4','*10','5', '*9','6'], ['*8','10','*9', '33','*7', '34', '*7', '33', '*8', '40']]


# target_genome = [['*6', '1', '*9', '2', '*7', '3'],['*8', '4', '*6', '5'],['*6', '6', '*10', '7', '*10', '8', '*9', '9'],['*9', '10', '*10', '11', '*10', '12'],['*9', '13', '*9', '14'],['*7', '15', '*10', '16'],['*6', '17'],['*6', '18'],['*6', '19', '*10', '20', '*6', '21'],['*6', '22']] 
# source_genome = [['*6', '1', '*6', '3'],['*6', '5','*9', '8' ],['*7', '6', '*9', '4', '*9', '7', '*9', '9'],['*8', '13', '*10', '10', '*9', '12'],['*9', '14'],['*9', '16'],['*6', '-15','*9', '17'],['*9','19', '*8', '18'],['*9', '20', '*7', '-2', '*9', '21'],['*9', '-11', '*8', '22']] 
# # # # # # #                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
# source_genome = [['*6', '1', '*7', '2', '*8', '3', '*7', '4', '*9', '1', '*7', '5'],['*6', '8', '*9', '7', '*10', '6', '*7', '5', '*5', '1', '*8', '4', '*9', '1', '*7', '3', '*8', '1', '*8', '2'], ['*8', '9', '*7', '11'], ['*7', '20', '*8', '19', '*9', '18', '*6', '17', '*8', '16', '*6', '32', '*9', '10', '*8', '31', '*9', '30', '*7', '29', '*8', '28', '*6', '27'], ['*8', '21', '*7', '22', '*7', '23', '*8', '24', '*7', '25', '*6', '26'], ['*8', '33'], ['*7', '34', '*9', '35', '*7', '36', '*8', '37']]
# target_genome = [['*5', '1', '*6', '2', '*7', '3', '*9', '4', '*8', '5', '*7', '6', '*6', '7', '*6', '8'],['*9', '9', '*8', '10', '*8', '11'], ['*8', '12', '*6', '13', '*7', '14', '*8', '15'],['*7', '16', '*6', '17', '*6', '18', '*8', '19', '*10', '20'], ['*9', '21', '*6', '22', '*7', '23', '*8', '24', '*8', '25', '*7', '26'], ['*8', '27', '*9', '28', '*9', '29', '*9', '30', '*8', '31', '*9', '32', '*8', '33'], ['*6', '34', '*6', '35', '*6', '36', '*7', '37', '*7', '38', '*6', '39', '*10', '40']]


'''
Printing file containing the solution set
'''
# HM.create_new_file()
# HM.append_to_file("Target_genome:")
# HM.append_to_file(HM.list_to_string(target_genome))
# HM.append_to_file("\nSource_genome:")
# HM.append_to_file(HM.list_to_string(source_genome))
# HM.append_new_line()
# HM.append_new_line()

# solution_sets = {}
# solution_num = 1

# for _ in tqdm(range(itterations), total=itterations):
    
#     list_of_operations  = gen_n_obj.get_operations(source_genome, target_genome)
#     mutation_solution = ""
    
#     for item in list_of_operations:
#         operations = item[0]
#         mutation_solution += str(operations['Mut_Type'])
#         mutation_solution += str(operations['Chr'])
#         mutation_solution += str(operations['Pos'])
#         mutation_solution += str(operations['Gene'])

#     hashvalue = hash(mutation_solution)
#     if solution_sets.get(hashvalue) is None:
#         HM.append_new_solution_heading(solution_num)
#         solution_num += 1
#         solution_sets[hashvalue] = mutation_solution

#         HM.append_to_file("\nEstimated total number of mutations:")
#         HM.append_to_file(str(len(list_of_operations)))
#         HM.append_to_file("\nPrinting solution sets........\n\n")

#         for item in list_of_operations:
#             operations = item[0]
#             Mut_Type = f"Mut_Type: {operations['Mut_Type']}, "
#             Chr = f"Chr: {operations['Chr']}, "
#             Pos = f"Pos: {operations['Pos']}, "
#             Gene = f"Gene: {operations['Gene']}"
#             Genome_after_mutation = f"Genome after mutation: {operations['Genome after mutation']}\n"

solution_sets = {}
solution_num = 1

HM.create_new_file('solution_set.txt')


for _ in tqdm(range(itterations), total=itterations):
    for _ in range(itterations):

        list_of_operations = gen_n_obj.get_operations(source_genome, target_genome)
    mutation_solution = ""
    # print(list_of_operations)
    for item in list_of_operations:
        # print(item)
        operations = item[0]
        mutation_solution += str(operations['Mut_Type'])
        mutation_solution += str(operations['Chr'])
        mutation_solution += str(operations['Pos'])
        mutation_solution += str(operations['Gene'])

    # Use SHA-256 to calculate the hash value
    sha256_hash = hashlib.sha256(mutation_solution.encode()).hexdigest()

    if sha256_hash not in solution_sets:
        HM.append_new_solution_heading(solution_num)
        solution_num += 1
        solution_sets[sha256_hash] = mutation_solution

        HM.append_to_file("solution_set.txt","\nEstimated total number of mutations:")
        HM.append_to_file("solution_set.txt",str(len(list_of_operations)))
        HM.append_to_file("solution_set.txt","\nPrinting solution sets........\n\n")

        for item in list_of_operations:
            operations = item[0]
            Mut_Type = f"Mut_Type: {operations['Mut_Type']}, "
            Chr = f"Chr: {operations['Chr']}, "
            Pos = f"Pos: {operations['Pos']}, "
            Gene = f"Gene: {operations['Gene']}"
            Genome_after_mutation = f"Genome after mutation: {operations['Genome after mutation']}\n"

            HM.append_to_file("solution_set.txt",Mut_Type)
            HM.append_to_file("solution_set.txt",Chr)
            HM.append_to_file("solution_set.txt",Pos)
            HM.append_to_file("solution_set.txt",Gene)
            HM.append_new_line()
            HM.append_to_file("solution_set.txt",Genome_after_mutation)
            HM.append_new_line()

HM.End_of_file()

# # import hashlib

# def append_to_solution_file(file_path, data):
#     with open(file_path, 'a') as solution_file:
#         solution_file.write(data + '\n')

# def format_mutation_data(mutation):
#     operations = mutation[0]
#     mutation_info = f"Mut_Type: {operations['Mut_Type']}, Chr: {operations['Chr']}, Pos: {operations['Pos']}, Gene: {operations['Gene']}"
#     genome_after_mutation = f"Genome after mutation: {operations['Genome after mutation']}"
#     return f"{mutation_info}\n{genome_after_mutation}"

# def main():
#     solution_sets = {}
#     solution_num = 1
#     list_of_operations = gen_n_obj.get_operations(source_genome, target_genome)

#     for mutation_solution in list_of_operations:
#         sha256_hash = hashlib.sha256(mutation_solution.encode()).hexdigest()

#         if sha256_hash not in solution_sets:
#             solution_sets[sha256_hash] = mutation_solution

#             append_to_solution_file("solution_set.txt", "Estimated total number of mutations:")
#             append_to_solution_file("solution_set.txt", str(len(list_of_operations)))
#             append_to_solution_file("solution_set.txt", "Printing solution sets........\n")

#             mutation_data = format_mutation_data(mutation_solution)
#             append_to_solution_file("solution_set.txt", mutation_data)

#     # Close the file or perform any other cleanup operations here

# if __name__ == "__main__":
#     main()



