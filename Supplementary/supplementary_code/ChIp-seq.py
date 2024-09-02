import os
import matplotlib.pyplot as plt
import roman
import re
from collections import defaultdict

def read_bed_file(filename, is_peak_data=False):
    """
    Reads a BED file and extracts H3K9 acetylation data.
    
    Args:
        filename (str): Path to the BED file.
        is_peak_data (bool): Flag indicating whether the file contains peak data.
        
    Returns:
        list: List of tuples representing the chromosome, start, and end positions of the peaks or recombination data.
    """
    data = []
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('#') or line.strip() == '':
                continue  # Skip header lines or empty lines
            parts = re.split(r'\s+', line.strip())
            if len(parts) < 3:
                print(f"Ignoring line due to insufficient columns: {line.strip()}")
                continue  
            chromosome = parts[0]
            if not is_peak_data:
                try:
                    chromosome = int(chromosome)  # Convert chromosome to integer if possible
                except ValueError:
                    try:
                        chromosome = roman.fromRoman(chromosome)  # Convert Roman numerals to integer
                    except roman.InvalidRomanNumeralError:
                        print(f"Ignoring line due to invalid Roman numeral: {chromosome}")
                        continue
            try:
                start = int(parts[1])
                end = int(parts[2])
                if is_peak_data:
                    peak_value = float(parts[3])  # Peak data has an additional column for the peak value
                    data.append((chromosome, start, end, peak_value))
                else:
                    data.append((chromosome, start, end))
            except ValueError as e:
                print(f"Ignoring line due to error: {line.strip()} - {e}")
    return data

def map_recombination_to_peaks(peak_data, recombination_data):
    """
    Maps recombination points to enriched regions (H3K9 acetylated regions) on the same chromosome.

    Args:
        H3K9ac (peak_data) (list): List of tuples containing chromosome, start, and end positions of peaks.
        recombination_data (list): List of tuples containing chromosome, start, and end positions of recombination points.
    
    Returns:
        dict: A dictionary mapping chromosomes to the count of recombination points overlapping with peaks (H3K9 acetylated regions).
    """
    mapped_data = defaultdict(int)
    
    for recombination_chromosome, recombination_start, recombination_end in recombination_data:
        for peak_chromosome, peak_start, peak_end, _ in peak_data:
            if (recombination_chromosome == peak_chromosome and
                recombination_start >= peak_start and recombination_end <= peak_end):
                mapped_data[recombination_chromosome] += 1
                break  
    return mapped_data

def visualize_mapping(mapped_data):
    """
    Visualizes the mapping of recombination points to enriched regions (H3K9ac regions) using a bar chart.

    Args:
        mapped_data (dict): Dictionary mapping chromosomes to the number of recombination points mapped to enriched regions.
    """
    chromosomes = list(mapped_data.keys())
    counts = [mapped_data[chrom] for chrom in chromosomes]

    # Normalize counts for color intensity
    norm = plt.Normalize(min(counts), max(counts))
    
    # Generate color map with shades of blue
    colors = plt.cm.Blues(norm(counts))
    
    plt.figure(figsize=(10, 6))
    plt.bar(chromosomes, counts, color=colors)
    plt.xlabel('Chromosome') # change to suit you
    plt.ylabel('Number of Recombination Points Mapped to enriched regions') # change to suit you
    plt.title('Mapping of Recombination Points to H3K9ac regions') # change to suit you
    plt.xticks(chromosomes, rotation=45)
    plt.tight_layout()
    
    # Add color bar to indicate the mapping intensity
    sm = plt.cm.ScalarMappable(cmap=plt.cm.Blues, norm=norm)
    sm.set_array([])
    cbar = plt.colorbar(sm)
    cbar.set_label('Number of Recombination Points')
    
    plt.show()

def main():
    """
    Main function to process H3K9 acetylated regions and recombination data, and visualize the mapping.
    """
    peak_data = read_bed_file("filepath to H3K9ac data", is_peak_data=True)
    mapped_data = defaultdict(int)

    recombination_dir = "filepath_to_BED_files_of_recombination datac"

    for filename in os.listdir(recombination_dir):
        if filename.endswith("_bed"):
            recombination_data = read_bed_file(os.path.join(recombination_dir, filename))
            chromosome_name = filename.replace("_bed", "")
            chromosome_number = roman.fromRoman(chromosome_name) if chromosome_name.isalpha() else int(chromosome_name)
            recombination_mapping = map_recombination_to_peaks(peak_data, recombination_data)
            for chrom, count in recombination_mapping.items():
                mapped_data[chrom] += count

    visualize_mapping(mapped_data)

if __name__ == "__main__":
    main()
