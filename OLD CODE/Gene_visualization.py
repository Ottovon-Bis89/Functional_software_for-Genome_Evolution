import matplotlib.pyplot as plt
import random


# Read chromosome lengths from a text file
chromosome_lengths = {}
with open("/home/22204911/Documents/chromosome_length.txt", "r") as f:
    for line in f:
        chromosome, length = line.strip().split()
        chromosome_lengths[chromosome] = int(length)
        

# Read gene data from a text file
gene_data = []
with open("/home/22204911/Downloads/ncbi_dataset.zip_yeast/ncbi_dataset/data/GCF_000146045.2/output_file1.txt", "r") as f:
    for line in f:
        # print(line)
        if line.startswith("Chromosome"):
            continue
        chromosome, gene_start, gene_end, gene_name = line.strip().split(', ')
            
        gene_data.append((chromosome, int(gene_start), int(gene_end), gene_name))
       
        # print("Values:", chromosome, gene_start, gene_end, gene_name)
        # try:
        #     gene_data.append((chromosome, int(gene_start), int(gene_end), gene_name))
        # except ValueError as e:
        #     print("Error:", e)
        #     print("Line with issue:", line)
            

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Generate random colors for each gene
gene_colors = {}
for gene in gene_data:
    gene_colors[gene[3]] = "#" + "%06x" % random.randint(0, 0xFFFFFF)

# Plot genes on chromosomes
for gene in gene_data:
    chromosome = gene[0]
    start = gene[1]
    end = gene[2]
    color = gene_colors[gene[3]]
    
    ax.fill_betweenx([chromosome_lengths[chromosome]], start, end, color=color)

# Customize the plot
ax.set_xlim(0, max(chromosome_lengths.values()))
ax.set_ylim(0, len(chromosome_lengths))
ax.set_yticks(range(1, len(chromosome_lengths) + 1))
ax.set_yticklabels(chromosome_lengths.keys())
ax.set_xlabel("Genomic Position")
ax.set_title("Yeast Genome Gene Visualization")

# Create a legend for gene colors
legend_patches = [plt.Line2D([0], [0], color=color, label=gene) for gene, color in gene_colors.items()]
ax.legend(handles=legend_patches, loc="upper right")

# Show the plot
plt.tight_layout()
plt.show()
