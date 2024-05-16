
import os
import matplotlib.pyplot as plt
import roman
import re
from collections import defaultdict

def read_bed_file(filename, is_peak_data=False):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('#') or line.strip() == '' or line.startswith('chr'):
                continue  # Skip header lines or empty lines
            parts = re.split(r'\s+', line.strip())
            if len(parts) < 3:
                print(f"Ignoring line due to insufficient columns: {line.strip()}")
                continue  
            chromosome = parts[0]
            if not is_peak_data:
                try:
                    chromosome = int(chromosome)  
                except ValueError:
                    try:
                        chromosome = roman.fromRoman(chromosome) 
                    except roman.InvalidRomanNumeralError:
                        print(f"Ignoring line due to invalid Roman numeral: {chromosome}")
                        continue
            try:
                if is_peak_data:
                    start = int(parts[1])
                    end = int(parts[2])
                    peak_value = float(parts[3]) 
                    peak_data = (chromosome, start, end)
                    data.append(peak_data)
                else:
                    start = int(parts[1])
                    end = int(parts[2])
                    data.append((chromosome, start, end))
            except Exception as e:
                print(f"Ignoring line due to error: {line.strip()} - {e}")
    return data


# def map_recombination_to_peaks(peak_data, recombination_data):
#     mapped_data = {chromosome: 0 for chromosome in range(1, 17)}
#     for recombination_point in recombination_data:
#         recombination_chromosome, recombination_start, recombination_end = recombination_point
#         for peak in peak_data:
#             peak_chromosome, peak_start, peak_end = peak
#             if recombination_chromosome == peak_chromosome and peak_start >= recombination_start <= peak_end and peak_start >= recombination_end <= peak_end:
#                 mapped_data[recombination_chromosome] += 1
#                 break
#     return mapped_data

def map_recombination_to_peaks(peak_data, recombination_data):
    mapped_data = {chromosome: [] for chromosome in range(1, 17)}
    for recombination_point in recombination_data:
        recombination_chromosome, recombination_start, recombination_end = recombination_point
        for peak in peak_data:
            peak_chromosome, peak_start, peak_end = peak
            if recombination_chromosome == peak_chromosome and peak_start >= recombination_start <= peak_end and peak_start >= recombination_end <= peak_end:
                mapped_data[recombination_chromosome].append((recombination_start, recombination_end))
                break
        
    return mapped_data



# def visualize_mapping(mapped_data):
#     non_zero_mapped_data = {chromosome: counts for chromosome, counts in mapped_data.items() if any(counts.values())}
#     chromosomes = list(non_zero_mapped_data.keys())
#     counts = [sum(counts.values()) for counts in non_zero_mapped_data.values()]
    
#     chromosomes_labels = [chromosome.replace('_bed', '') for chromosome in chromosomes]
    
#     # Normalize counts for colormap intensity
#     norm = plt.Normalize(min(counts), max(counts))
    
#     # Generate a colormap with different shades of blue
#     colors = plt.cm.Blues(norm(counts))
    
#     fig, ax = plt.subplots(figsize=(10, 6))
#     bars = ax.bar(chromosomes, counts, color=colors)
#     ax.set_xlabel('Chromosome')
#     ax.set_ylabel('Number of Recombination coordinates Mapped to H3K9 acetylated  Regions')
#     ax.set_title('Mapping of Recombination Coordinates to H3K9ac Regions')
#     ax.set_xticks(chromosomes)
#     ax.set_xticklabels(chromosomes_labels, rotation=45)
#     plt.tight_layout()
    
#     # Create a ScalarMappable object
#     sm = plt.cm.ScalarMappable(cmap=plt.cm.Blues, norm=norm)
#     sm.set_array([])
    
#     # Create colorbar separately and add it to the plot
#     cbar = plt.colorbar(sm, ax=ax)
#     cbar.set_label('Number of recombination coordinates')

#     plt.show()


def visualize_mapping(mapped_data):
    # Initialize an empty list to store counts for each chromosome
    counts = []
    
    # Iterate over the mapped data
    for chromosome, coordinates in mapped_data.items():
        # Append the count of mapped coordinates for the current chromosome
        counts.append(len(coordinates))
    
    chromosomes = list(mapped_data.keys())
    chromosomes_labels = [chromosome.replace('_bed', '') for chromosome in chromosomes]
    
    # Normalize counts for colormap intensity
    norm = plt.Normalize(min(counts), max(counts))
    
    # Generate a colormap with different shades of blue
    colors = plt.cm.Blues(norm(counts))
    
    plt.figure(figsize=(10, 6))
    bars = plt.bar(chromosomes, counts, color=colors)
    plt.xlabel('Chromosome')
    plt.ylabel('Number of Recombination Points Mapped to Enriched Regions')
    plt.title('Mapping of Recombination Coordinates to H3K9ac Regions')
    plt.xticks(chromosomes, chromosomes_labels, rotation=45)
    plt.tight_layout()
    
    # Add color bar to show the intensity mapping
    sm = plt.cm.ScalarMappable(cmap=plt.cm.Blues, norm=norm)
    sm.set_array([])
    cbar = plt.colorbar(sm, ax=plt.gca())
    cbar.set_label('Number of recombination points')

    plt.show()



def write_mapped_coordinates(mapped_data):
    with open("mapped_coordinates_output.txt", "w") as output_file:
        for chromosome, coordinates in mapped_data.items():
            if isinstance(coordinates, int):
                output_file.write(f"No mapped coordinates for chromosome {chromosome}\n")
            else:
                for start_end, count in coordinates.items():
                    if isinstance(start_end, int):  # Check if start_end is an integer
                        output_file.write(f"{chromosome}\t{start_end}\t{coordinates[start_end]}\n")
                    else:
                        start, end = start_end
                        for _ in range(count):
                            output_file.write(f"{chromosome}\t{start}\t{end}\n")





# 
# def main():
#     peak_data = read_bed_file("/home/von/Documents/chip-seq/H3K9ac_rep1_peaks.bed")
#     mapped_data = defaultdict(lambda: defaultdict(list))

#     recombination_dir = "/home/von/Documents/chrom.BED"

#     for filename in os.listdir(recombination_dir):
#         if filename.endswith("_bed"):
#             recombination_data = read_bed_file(os.path.join(recombination_dir, filename))
#             mapped_data[filename.replace("_bed", "")] = map_recombination_to_peaks(peak_data, recombination_data)
#     # print(mapped_data)

#     visualize_mapping(mapped_data)
    

# if __name__ == "__main__":
#     main()

def main():
    peak_data = read_bed_file("/home/von/Documents/chip-seq/GSM4449447_13885_H3K9ac_rep1_peaks.bed")
    mapped_data = defaultdict(list)
    

    recombination_dir = "/home/von/Documents/chrom.BED"

    for filename in os.listdir(recombination_dir):
        if filename.endswith("_bed"):
            recombination_data = read_bed_file(os.path.join(recombination_dir, filename))
            mapped_data[filename.replace("_bed", "")] = map_recombination_to_peaks(peak_data, recombination_data)

    write_mapped_coordinates(mapped_data)
    visualize_mapping(mapped_data)

if __name__ == "__main__":
    main()

    

