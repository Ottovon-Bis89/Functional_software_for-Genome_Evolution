import os
import matplotlib.pyplot as plt
import roman
import re
from collections import defaultdict


def read_bed_file(filename, is_peak_data=False):
    """
    Reads a BED file and processes its contents into a list of tuples.

    Parameters:
    - filename (str): The path to the BED file.
    - is_peak_data (bool): If True, expects peak data format with an additional column for peak values.

    Returns:
    - data (list of tuples): Parsed BED file data. Each tuple contains:
        - For non-peak data: (chromosome, start, end)
        - For peak data: (chromosome, start, end, peak_value)
    """
    data = [] 

    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('#') or line.strip() == '':
                continue
            
            parts = re.split(r'\s+', line.strip())
            
            if len(parts) < 3:
                print(f"Ignoring line due to insufficient columns: {line.strip()}")
                continue
            
            chromosome = parts[0] 
            
            if not is_peak_data:
                # Try converting the chromosome identifier to an integer or Roman numeral
                try:
                    chromosome = int(chromosome) 
                except ValueError:
                    try:
                        chromosome = roman.fromRoman(chromosome) 
                    except roman.InvalidRomanNumeralError:
                        print(f"Ignoring line due to invalid Roman numeral: {chromosome}")
                        continue
            try:
                start = int(parts[1])
                end = int(parts[2])
                
                if is_peak_data:
                    peak_value = float(parts[3])
                    peak_data = (chromosome, start, end, peak_value)
                    data.append(peak_data)
                else:
                    data.append((chromosome, start, end))
            except Exception as e:
                print(f"Ignoring line due to error: {line.strip()} - {e}")

    return data


def map_recombination_to_H3k9ac(peak_data, recombination_data):
    """
    Maps recombination points to H3K9 acetylated regions on chromosomes.

    This function takes recombination data and H3K9 acetylation data and determines 
    how many recombination points fall within the H3K9 acetylated regions on 
    each chromosome. It returns a dictionary where the keys are 
    chromosome numbers (1-16) and the values are the counts of 
    recombination points mapped to H3K9 acetylated regions.

    Parameters:
    - H3K9 acetylated data: list of tuples
        Each tuple represents a region in the format 
        (chromosome, start_position, end_position).
    - recombination_data: list of tuples
        Each tuple represents a recombination point in the format 
        (chromosome, start_position, end_position).

    Returns:
    - mapped_data: dict
        A dictionary where keys are chromosome numbers (1-16) and values 
        are counts of recombination points that fall within the acetylated regions.
    """
    mapped_data = {chromosome: 0 for chromosome in range(1, 17)}

    
    for recombination_point in recombination_data:
        recombination_chromosome, recombination_start, recombination_end = recombination_point

        # Iterate through the peak data to check for overlaps.
        # acetylated region = peak
        for peak in peak_data:
            peak_chromosome, peak_start, peak_end = peak

            # Check if the recombination point falls entirely within an acetylated region on the same chromosome.
            if (recombination_chromosome == peak_chromosome and 
                peak_start >= recombination_start <= peak_end and 
                peak_start >= recombination_end <= peak_end):

                mapped_data[recombination_chromosome] += 1
                break
    return mapped_data


def visualize_mapping(mapped_data):
    """
    Visualize mapped genomic data by generating a bar plot with a colormap.

    Parameters:
    mapped_data (dict): A dictionary where keys are chromosome names (strings) and 
                        values are dictionaries containing counts (int) of mapped data.

    Returns:
    None: Displays a bar plot of the mapped data with a colormap.
    """
    non_zero_mapped_data = {chromosome: counts for chromosome, counts in mapped_data.items() if any(counts.values())}
    chromosomes = list(non_zero_mapped_data.keys())
    counts = [sum(counts.values()) for counts in non_zero_mapped_data.values()]
    
    chromosomes_labels = [chromosome.replace('_bed', '') for chromosome in chromosomes]
    
    norm = plt.Normalize(min(counts), max(counts))
    colors = plt.cm.Blues(norm(counts))
    

    plt.figure(figsize=(10, 6))
    bars = plt.bar(chromosomes, counts, color=colors)
    plt.xlabel('Chromosome')
    plt.ylabel('Number of Recombination Points Mapped to Enriched Regions') # adjust titles as needed
    plt.title('Mapping of Recombination Coordinates to H3K9ac Regions')
    plt.xticks(chromosomes, chromosomes_labels, rotation=45)
    plt.tight_layout()
    
    # Add color bar to show the intensity mapping
    sm = plt.cm.ScalarMappable(cmap=plt.cm.Blues, norm=norm)
    sm.set_array([])
    cbar = plt.colorbar(sm)
    cbar.set_label('Number of recombination points')

    plt.show()


def main():
    peak_data = read_bed_file("/path_to_H3k9ac_files")
    mapped_data = defaultdict(lambda: defaultdict(list))

    recombination_dir = "/path_to_recombination_BEDfiles"

    for filename in os.listdir(recombination_dir):
        if filename.endswith("_bed"):
            recombination_data = read_bed_file(os.path.join(recombination_dir, filename))
            mapped_data[filename.replace("_bed", "")] = map_recombination_to_H3k9ac(peak_data, recombination_data)

    visualize_mapping(mapped_data)

if __name__ == "__main__":
    main()
    


