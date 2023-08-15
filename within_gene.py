

def is_mutation_within_gene_range(gene_start, gene_end, mutation_border):
    upstream_range = 1000
    downstream_range = 1000
    

    gene_start_upstream = gene_start - upstream_range
    gene_end_downstream = gene_end + downstream_range

    return gene_start_upstream <= mutation_border <= gene_end_downstream

def find_mutations_within_gene_ranges(genes, mutation_borders_A, mutation_borders_B):
    mutations_within_ranges = []

    for gene in genes:
        Chromosome, gene_start, gene_end, gene_name = gene

        borders_for_chromosome_A = []
        borders_for_chromosome_B = []
    
        # Separate mutation borders for Genome A and Genome B
        for mutation_border in mutation_borders_A:
            if mutation_border[0] == Chromosome:
                borders_for_chromosome_A.append(mutation_border[1])
            
        for mutation_border in mutation_borders_B:
            if mutation_border[0] == Chromosome:
                borders_for_chromosome_B.append(mutation_border[1])
        
        for border in borders_for_chromosome_A:
            if is_mutation_within_gene_range(gene_start, gene_end, border):
                mutations_within_ranges.append((Chromosome, gene_start, gene_end, gene_name, border, "Genome A"))

        for border in borders_for_chromosome_B:
            if is_mutation_within_gene_range(gene_start, gene_end, border):
                mutations_within_ranges.append((Chromosome, gene_start, gene_end, gene_name, border, "Genome B"))

    return mutations_within_ranges





def read_genes_from_file(file_path):
    genes = []
    with open(file_path, 'r') as file:
        for line in file:
            if any(i.isdigit() for i in line) and line.strip() and ':' not in line:
                Chromosome, gene_start, gene_end, gene_name = line.strip().split(',')
                genes.append((Chromosome, int(gene_start), int(gene_end), gene_name))
               
    return genes


def read_mutation_borders_from_file(file_path):
    mutation_borders_A = []
    mutation_borders_B = []
    with open(file_path, 'r') as file:
        genome = None  # variable to track the current genome (A or B)
        for line in file:
            line = line.strip()
            if line == "Genome A:":
                genome = 'A'
            elif line == "Genome B:":
                genome = 'B'
            else:
                data = line.replace('[', '').replace(']', '').replace("'", '').split(', ')
                if len(data) >= 2:
                    chromosome, border, *_ = data
                    border = int(border)
                    if genome == 'A':
                        mutation_borders_A.append([chromosome, border])
                        
                    elif genome == 'B':
                        mutation_borders_B.append([chromosome, border])


    return mutation_borders_A, mutation_borders_B

genes_file = "/home/22204911/Downloads/ncbi_dataset.zip_yeast/ncbi_dataset/data/GCF_000146045.2/output_file.txt"
mutation_borders_file = '/home/22204911/Documents/working_scripts/output1.txt'
output_file_path = '/home/22204911/Documents/working_scripts/output3.txt'


genes = read_genes_from_file(genes_file)
mutation_borders_A, mutation_borders_B = read_mutation_borders_from_file(mutation_borders_file)

# Obtain the list of mutations within gene ranges for Genome A and Genome B
mutations_within_ranges_A = find_mutations_within_gene_ranges(genes, mutation_borders_A, [])
mutations_within_ranges_B = find_mutations_within_gene_ranges(genes, [], mutation_borders_B)

upstream_count_A = 0
downstream_count_A = 0
between_count_A = 0
upstream_count_B =0
downstream_count_B = 0
between_count_B = 0


# Write the output to the file for Genome A
with open(output_file_path + 'output3.txt_GenomeA.txt', 'w') as output_file_A:

    for chromosome, gene_start, gene_end, gene_name, mutation_border, genome in mutations_within_ranges_A:
        distance_from_gene_start =  gene_start - 1000
        
        distance_from_gene_end = gene_end + 1000
    
        if mutation_border <= distance_from_gene_start:
            position = "Upstream"
            upstream_count_A +=1

        elif mutation_border >= distance_from_gene_end:
            position = "Downstream"
            downstream_count_A +=1

        else:
            position = "Between"
            between_count_A +=1

    
        output_file_A.write(f"Mutation at {mutation_border} falls within the range of {gene_name} on chromosome {chromosome} ({gene_start}-{gene_end}) in Genome A. Position: {position}\n")
    output_file_A.write(f"Number of Upstream Mutations in Genome A: {upstream_count_A}\n")
    output_file_A.write(f"Number of Downstream Mutations in Genome A: {downstream_count_A}\n")
    output_file_A.write(f"Number of Between Mutations in Genome A: {between_count_A}\n\n")
# Write the output to the file for Genome B
with open(output_file_path + 'output3.txt_GenomeB.txt', 'w') as output_file_B:
    
    for chromosome, gene_start, gene_end, gene_name, mutation_border, genome in mutations_within_ranges_B:
        distance_from_gene_start = gene_start - 1000
        distance_from_gene_end = gene_end + 1000
        if mutation_border <= distance_from_gene_start:
            position = "Upstream"
            upstream_count_B +=1

        elif mutation_border >= distance_from_gene_end:
            position = "Downstream"
            downstream_count_B +=1

        else:
            position = "Between"
            between_count_B +=1

        output_file_B.write(f"Mutation at {mutation_border} falls within the range of {gene_name} on chromosome {chromosome} ({gene_start}-{gene_end}) in Genome B. Position: {position}\n")
    output_file_B.write(f"Number of Upstream Mutations in Genome B: {upstream_count_B}\n")
    output_file_B.write(f"Number of Downstream Mutations in Genome B: {downstream_count_B}\n")
    output_file_B.write(f"Number of Between Mutations in Genome B: {between_count_B}\n\n")
