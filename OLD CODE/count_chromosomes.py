
def count_chromosomes(filename):
    genome_A_counts = {}
    genome_B_counts = {}
    current_genome = None
    
    with open(filename, 'r') as file:
        for line in file:
            data = line.strip().split(',')
            
            if data[0] == "Genome A:":
                current_genome = "Genome A"
            elif data[0] == "Genome B:":
                current_genome = "Genome B"
            else:
                chromosome = data[0]
                
                if current_genome == "Genome A":
                    if chromosome in genome_A_counts:
                        genome_A_counts[chromosome] += 1
                    else:
                        genome_A_counts[chromosome] = 1
                elif current_genome == "Genome B":
                    if chromosome in genome_B_counts:
                        genome_B_counts[chromosome] += 1
                    else:
                        genome_B_counts[chromosome] = 1
    
    return genome_A_counts, genome_B_counts

if __name__ == "__main__":
    genome_file ='/home/22204911/Documents/working_scripts/output1.txt'  # Replace with your actual file name
    genome_A_counts, genome_B_counts = count_chromosomes(genome_file)
    
    print("Genome A chromosome counts:")
    for chromosome, count in genome_A_counts.items():
        print(f"Chromosome {chromosome}: {count} occurrences")
    
    print("\nGenome B chromosome counts:")
    for chromosome, count in genome_B_counts.items():
        print(f"Chromosome {chromosome}: {count} occurrences")


