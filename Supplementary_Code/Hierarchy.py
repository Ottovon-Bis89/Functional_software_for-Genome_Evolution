import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage


# Mapping of event codes to their classifications
# Assign each rearrangement to a number (0-10)
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
    'dup': 10
    
}

# Open the input file
input_file_path = "path_to_outputfile_from_Genolve+"  
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
output_file_path = "path_to_outfile"  
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

with open('path_to_outfile') as f:

    counter = 0
    for line in f:
        n = line.strip('').strip(',').split()
        if len(n) > 2:
            x.append(n[2])
           
            y_2 = []
            for j in n[2:]:
                y_2.append(j)
            y.append(y_2)

        counter += 1
        if counter == 100:
            break

data = list(zip(x, y))


# Perform hierarchical clustering
linkage_matrix = linkage(y, method = 'complete', metric = 'Euclidean')

# Plot the dendrogram
plt.figure(figsize=(5, 10))
dendrogram(linkage_matrix, labels=x)
plt.title("Hierarchical Clustering of the evolutionary paths of the yeast genome")
plt.xlabel("Paths (Solutions)")
plt.ylabel("Distance between Clusters (Dissimilarity)")
plt.show()

