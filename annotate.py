# import matplotlib.pyplot as plt

# # Read coordinates from the first file
# with open("/home/22204911/Documents/chrom_interactions/chr1_hi_c.txt", "r") as file1:
#    coordinates1 = [int(line.strip().split("\t")[1]) for line in file1]

# # Read coordinates from the second file
# with open("/home/22204911/Documents/chrom_mutations/chr1_recombinations.txt", "r") as file2:
#     coordinates2 = [int(line.strip().split("\t")[1]) for line in file2]

# # Define the width of the bars
# bar_width = 0.4

# # Create a figure and axis
# fig, ax = plt.subplots()

# # Plot bars for the first set of coordinates
# ax.bar(coordinates1, [1] * len(coordinates1), width=bar_width, color='blue', label='Chromosome 1')

# # Plot bars for the second set of coordinates
# ax.bar(coordinates2, [1] * len(coordinates2), width=bar_width, color='red', label='Chromosome 2')

# # Find the positions where the bars fully align and mark with an 'x'
# for coordinate in coordinates1:
#     if coordinate in coordinates2:
#         ax.annotate('x', (coordinate, 1), color='black', ha='center', va='center')

# # Set axis labels and legend
# ax.set_xlabel('Coordinates')
# ax.set_ylabel('Chromosome')
# plt.legend()

# # Show the plot
# plt.show()


import matplotlib.pyplot as plt
# Function to skip header lines in a file
def skip_headers(file):
    for line in file:
        if not line.startswith("ChromosomeID"):
            return line

# Read the lengths of the chromosomes from the first file
with open("/home/22204911/Documents/chrom_interactions/chr1_hi_c.txt", "r") as file1:
    chromosome1_data = [line.strip().split("\t") for line in file1]
    chromosome1_ids, chromosome1_lengths = zip(*[(int(data[0]), int(data[1])) for data in chromosome1_data])

# Read the lengths of the chromosomes from the second file
with open("/home/22204911/Documents/chrom_mutations/chr1_recombinations.txt", "r") as file2:
    chromosome2_data = [line.strip().split("\t") for line in file2]
    chromosome2_ids, chromosome2_lengths = zip(*[(int(data[0]), int(data[1])) for data in chromosome2_data])

# Define the width of the bars
bar_width = 0.4

# Create a figure and axis
fig, ax = plt.subplots()

# Plot bars for the first chromosome
ax.bar(chromosome1_ids, chromosome1_lengths, width=bar_width, color='blue', label='Chromosome 1')

# Plot bars for the second chromosome on top of the first
ax.bar(chromosome2_ids, chromosome2_lengths, width=bar_width, color='red', label='Chromosome 2', alpha=0.5)

# Set axis labels and legend
ax.set_xlabel('Chromosome')
ax.set_ylabel('Length')
plt.legend()

# Show the plot
plt.show()
