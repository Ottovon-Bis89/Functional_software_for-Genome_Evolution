import os
import re

# Function to read data from a single file
def read_data_file(file_path):
    data_coordinates = {}
    with open(file_path, 'r') as file:
        next(file)  # Skip the header line
        for line in file:
            parts = re.split(r'\s+', line.strip())  # Split by whitespace characters
            chromosome, start, stop = parts[:3]
            try:
                chromosome = int(chromosome.replace('chr', ''))  # Remove 'chr' prefix and convert to int
                start, stop = map(int, (start, stop))
                if chromosome not in data_coordinates:
                    data_coordinates[chromosome] = []
                data_coordinates[chromosome].append((start, stop))
            except ValueError:
                print(f"Invalid data in file '{file_path}': {line.strip()}")

    return data_coordinates

# Function to write output to a file per chromosome
def write_output(output_file, output_data):
    with open(output_file, 'w') as file:
        for line in output_data:
            file.write(line + '\n')

# Read data1 file
data1_file_path = "/home/von/Documents/chip-seq/H3K9ac_rep1_peaks.bed" # Path to data1 file
data1_coordinates = read_data_file(data1_file_path)

# Process data2 files and write output to one file per chromosome
data2_directory = "/home/von/Documents/chrom.BED"   # Directory containing data2 files
for filename in os.listdir(data2_directory):
    if filename.endswith('_bed'):
        chromosome = filename.split('_')[0].replace('chr', '')
        if chromosome.isdigit():
            chromosome = int(chromosome)
            data2_file_path = os.path.join(data2_directory, filename)
            output_data = []

            with open(data2_file_path, 'r') as file:
                next(file)  # Skip the header line
                for line in file:
                    parts = re.split(r'\s+', line.strip())  # Split by whitespace characters
                    if len(parts) >= 3:  # Ensure there are at least 3 parts
                        start, stop = map(int, parts[:2])
                        if chromosome in data1_coordinates:
                            for data1_start, data1_stop in data1_coordinates[chromosome]:
                                if data1_start >= start and data1_stop <= stop:
                                    output_data.append(f"Chromosome {chromosome}, Data1 Start {data1_start}, Data1 Stop {data1_stop}, Data2 Start {start}, Data2 Stop {stop} in {filename} falls within data1.txt")
                                    break  # No need to continue checking data1 coordinates for this data2 range
                    else:
                        print(f"Invalid data in file '{data2_file_path}': {line.strip()}")

            # Write output to a file per chromosome
            output_file_path = f'output_chr{chromosome}.txt'
            write_output(output_file_path, output_data)
        else:
            print(f"Invalid chromosome value '{chromosome}' in file '{filename}'")
