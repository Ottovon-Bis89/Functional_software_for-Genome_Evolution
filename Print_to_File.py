
'''
Helper Functions for printing
'''
def list_to_string(my_list):
    list_string = '\n'.join([','.join(sublist) for sublist in my_list])
    return list_string

'''
Main file Printing
'''
def list_to_string(my_list):
    list_string = '\n'.join([','.join(sublist) for sublist in my_list])
    return list_string

file_path = 'solution_set.txt'

def create_new_file():
    with open(file_path, 'w+') as file:
        file.write("***************************************************************************Genome Evolution Results*********************************************************")
        file.write("\n\n")

def append_to_file(my_string):
    with open(file_path, 'a') as file:
        file.write(my_string)

def append_new_line():
    with open(file_path, 'a') as file:
        file.write("\n")

def append_new_solution_heading(solution_num):
    with open(file_path, 'a') as file:
        file.write("Solution number: ")
        file.write(str(solution_num))
        file.write(" -----> \n\n")

def End_of_file():
    with open(file_path, 'a') as file:
        file.write("\n\n")
        file.write("********************************************************************************End of Analysis************************************************************")


