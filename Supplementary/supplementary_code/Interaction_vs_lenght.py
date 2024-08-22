import matplotlib.pyplot as plt

chromosomes = ['Chr1', 'Chr2', 'Chr3', 'Chr4', 'Chr5', 'Chr6', 'Chr7', 'Chr8', 'Chr9', 'Chr10', 'Chr11', 'Chr12', 'Chr13', 'Chr14', 'Chr15', 'Chr16']  
chromosome_lengths = [230218, 813184, 316620, 1531933, 576874, 270161, 1090940, 562643, 439888, 745751, 666816, 1078177, 924431, 784333, 1091291, 948066]  
interaction_events = [0, 5, 0, 8, 4, 1, 7, 4, 2, 4, 5, 7, 7, 4, 6, 7]  # replace with your data

# Create a figure and a set of subplots
fig, ax = plt.subplots()

# Make a scatter plot
scatter = ax.scatter(chromosome_lengths, chromosomes, c=interaction_events)

# Set labels for x and y axis
ax.set_xlabel('Chromosome Length(bp)')
ax.set_ylabel('Chromosomes')


# Set a title for the plot
ax.set_title('A scatter plot of Chromosome Length against Number of interaction events')

# Create colorbar
cbar = plt.colorbar(scatter)
cbar.set_label('Interaction Events')

# Display the plot
plt.show()
