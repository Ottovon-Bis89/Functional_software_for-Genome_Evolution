import matplotlib.pyplot as plt
import numpy as np

# Sample data for the 16 chromosomes in each data set
# Replace these with your actual data
recombination_points = [92, 284, 154, 621, 263, 125, 482, 192, 212, 294, 272, 304, 389, 282, 411, 305]
H3K9ac_points = [67, 269, 40, 505, 226, 0, 482, 189, 169, 294, 238, 304, 168, 224, 324, 289]

chromosomes = [f'chr{i+1}' for i in range(16)]

# Bar width
bar_width = 0.35

# Positions of the bars on the x-axis
r1 = np.arange(len(recombination_points))
r2 = [x + bar_width for x in r1]

# Create the plot
plt.figure(figsize=(12, 8))

# Create bars for data set 1
plt.bar(r1, recombination_points, color='blue', width=bar_width, edgecolor='grey', label='Recombination points')

# Create bars for data set 2
plt.bar(r2, H3K9ac_points, color='orange', width=bar_width, edgecolor='grey', label='H3K9 acetylated regions')

# Add labels
plt.xlabel('Chromosomes', fontweight='bold')
plt.ylabel('Number of Recombination points in H3K9ac enriched regions', fontweight='bold')
plt.title('Recombinations in H3K9 acetylated regions')

# Add xticks on the middle of the group bars
plt.xticks([r + bar_width/2 for r in range(len(recombination_points))], chromosomes)

# Add a legend
plt.legend()

# Show the plot
plt.show()
