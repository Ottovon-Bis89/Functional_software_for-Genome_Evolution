def filter_genomic_data(input_file, output_file):
    headers = {'Chromosome', 'Start', 'End', 'D', 'Name'}

    with open(input_file, 'r') as file:
        lines = file.readlines()

    filtered_lines = [line for line in lines if any(header in line for header in headers)]

    with open(output_file, 'w') as file:
        file.writelines(filtered_lines)

# Usage example:
input_file = "/home/22204911/Downloads/ncbi_dataset.zip_yeast/ncbi_dataset/data/GCF_000146045.2/output.csv_genes"
output_file = "/home/22204911/Downloads/ncbi_dataset.zip_yeast/ncbi_dataset/data/GCF_000146045.2/output.txt"
filter_genomic_data(input_file, output_file)
