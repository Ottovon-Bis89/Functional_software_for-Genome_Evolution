
# Mapping of event codes to their classifications
event_classification = {
    'trp0': 0,
    'trp1': 1,
    'trp2': 2,
    'inv': 3,
    'ins': 4,
    'fus': 5,
    'fis': 6,
    'b_trl': 7,
    'u_trl': 8,
    'del': 9,
    'dup': 10,
    'fdna': 11
}

# Open the input file
input_file_path = "/home/22204911/Documents/Test_run/output21.txt"  # Replace with your input file path
with open(input_file_path, 'r') as input_file:
    lines = input_file.readlines()

# Find the first and last occurrence of '#' symbol
# first_hash_index = None
# last_hash_index = None
# for i, line in enumerate(lines):
#     if '#' in line:
#         if first_hash_index is None:
#             first_hash_index = i
#         last_hash_index = i
first_hash_index = None
for i, line in enumerate(lines):
    if '#' in line:
        first_hash_index = i
        break

# Extract the relevant lines between the first and last hash
lines = lines[first_hash_index:]

solutions = []
current_solution = None
solution_count = 0

# Parse the text file
for line in lines:
    line = line.strip()
    if line.startswith('*') or not line:
        continue
    if line.startswith('#'):
        solution_count += 1
        if current_solution is not None:
            solutions.append(current_solution)
        current_solution = {'solution': f'solution {solution_count}', 'events': []}
    else:
        events = line.split("'")
        current_solution['events'].extend(events)

# Append the last solution
if current_solution is not None:
    solutions.append(current_solution)

# Write the data to an output file
output_file_path = "/home/22204911/Documents/Test_run/extract5.txt"  # Replace with your output file path
with open(output_file_path, 'w') as output_file:
    for solution in solutions:
        output_file.write(f'# {solution["solution"]}' + '  ')
        for event in solution['events']:
            event_code = event_classification.get(event, -1)
            if event_code != -1:
                output_file.write(str(event_code) + ' ')
        output_file.write('\n')
