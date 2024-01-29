import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import cdist

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
input_file_path = "/home/22204911/Documents/New_Test/test_oout8"  # Replace with your input file path
with open(input_file_path, 'r') as input_file:
    lines = input_file.readlines()

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
output_file_path = "/home/22204911/Documents/New_Test/output.herachy"  # Replace with your output file path
with open(output_file_path, 'w') as output_file:
    for solution in solutions:
        output_file.write(f'# {solution["solution"]}' + '  ')
        for event in solution['events']:
            event_code = event_classification.get(event, -1)
            if event_code != -1:
                output_file.write(str(event_code) + ' ')
        output_file.write('\n')

# Read from the output file
i = 1
x = []
y = []

with open('/home/22204911/Documents/New_Test/output.herachy') as f:

    counter = 0
    for line in f:
        n = line.strip('').strip(',').split()
        if len(n) > 2:
            x.append(n[2])
            # print(x)
            y_2 = []
            for j in n[2:]:
                y_2.append(j)
            y.append(y_2)
            # print(y)

        counter += 1
        if counter == 100:
            break

data = list(zip(x, y))


# Perform hierarchical clustering
linkage_matrix = linkage(y, method = 'complete', metric = 'Euclidean')

# Plot the dendrogram
plt.figure(figsize=(5, 10))
dendrogram(linkage_matrix, labels=x)
plt.title("Hierarchical Clustering of Evolution Events")
plt.xlabel("Solutions")
plt.ylabel("Distance between Clusters")
plt.show()
