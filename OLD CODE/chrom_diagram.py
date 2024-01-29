import matplotlib.pyplot as plt
import mplcursors


def read_mutation_borders_from_file(file_path):
    # find mutation borders of genome A and genome B
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

        #Sort mutation borders for each genome in ascending order by both chromosome and border
        mutation_borders_A = sorted(mutation_borders_A, key=lambda x: (x[0], x[1]))
        mutation_borders_B = sorted(mutation_borders_B, key=lambda x: (x[0], x[1]))
        
    return mutation_borders_A, mutation_borders_B


def read_chromosome_lengths(file_path):
    chromosome_lengths = {}
    with open(file_path, 'r') as file:
        for line in file:
            chromosome, length = line.strip().split()
            chromosome_lengths[chromosome] = int(length)
            # print(chromosome_lengths)
    return chromosome_lengths

def generate_chromosome_diagrams(data, chromosome_lengths):
    for genome, borders in data.items():
        # plt.figure()
        plt.figure(figsize=(12, 8))
        plt.title(f"Rearrangement borders in - Genome {genome}")
        plt.xlabel("Chromosome length(bp)")
        plt.ylabel("Chromosomes")
        
        chromosomes = {}
        for chromosome, border in borders:
            chromosomes.setdefault(chromosome, []).append(border)
        
        for chromosome, borders in chromosomes.items():
            # chromosome_length = chromosome_lengths.get(chromosome, 1)
            plt.scatter(borders, [chromosome] * len(borders), color='blue', marker='o', facecolor='yellow')
            
        # # Annotate mutation borders with their values when hovering
        # cursor = mplcursors.cursor(hover=True)  # Enable hovering
        # @cursor.connect("add")
        # def on_add(sel):
        #     x, y = sel.target
        #     sel.annotation.set_text(f"Border: {int(x)}")
            # sel.annotation.set_position((0, 10))  # Offset the annotation a bit
            
        plt.yticks(list(chromosomes.keys()))
        plt.show()



if __name__ == "__main__":
    input_file = '/home/22204911/Documents/working_scripts/output1.txt'  # Update with your mutation_borders file's name
    chromosome_lengths_file = '/home/22204911/Documents/working_scripts/chrom_length.txt'  # Update with chromosome lengths file
    mutation_borders_A, mutation_borders_B = read_mutation_borders_from_file(input_file)
    chromosome_lengths = read_chromosome_lengths(chromosome_lengths_file)
    
    data = {
        "A": mutation_borders_A,
        "B": mutation_borders_B
    }
    
    generate_chromosome_diagrams(data, chromosome_lengths)




