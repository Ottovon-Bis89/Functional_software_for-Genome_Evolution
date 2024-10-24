
import os

# Directory containing the files
directory = "/home/22204911/Documents/chrom_Recomb"

# Loop over the files in the directory
for filename in os.listdir(directory):
    # Check if the filename starts with 'chr' and ends with '_recomb.txt'
    if filename.startswith('chr') and filename.endswith('_recomb.txt'):
        # Get the chromosome number from the file name
        chromosome_number = filename.split('_')[0][3:]

        # Open the file
        with open(os.path.join(directory, filename), "r") as in_f:
            # Open the output file for this chromosome
            with open(f"chr{chromosome_number}_output.bed", "w") as out_f:
                # Write the column headers to the BED file
                out_f.write("chr\tstart\tstop\n")

                # Loop over the lines in the file
                for line in in_f:
                    # Get the start position from the line
                    start = int(line.strip())

                    # Calculate the stop position
                    stop = start + 1

                    # Write the data point to the BED file
                    out_f.write(f"{chromosome_number}\t{start}\t{stop}\n")

