import os

def process_chromosome_HiC_data(input_file_path, output_dir):
    """
    Processes a file containing chromosome Hi-C data. 
    Each line is parsed, and Hi-C data are separated by chromosome, with each chromosome's data 
    written to a separate file.

    Parameters:
    - input_file_path (str): The path to the file containing chromosome hHi-C data.
    - output_dir (str): The directory where the output files will be stored.

    Raises:
    - FileNotFoundError: If the specified file does not exist.
    - Exception: For any other errors that occur during file processing.
    """
    tmp_chr = '1'  # Temporary variable to track the current chromosome
    file_name = f"chr_{tmp_chr}.txt"
    current_file_path = os.path.join(output_dir, file_name)

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    try:
        # Open the input file for reading
        with open(input_file_path, 'r') as file:
            # Open the first chromosome file for writing
            with open(current_file_path, 'w') as chr_file:
                for line in file:

                    if 'locus' in line:
                        continue

                    columns = line.split()

                    # Extract chromosome and locus information
                    chr = columns[0]
                    locus = columns[1]

                    # If the chromosome changes, close the old file and open a new one
                    if chr != tmp_chr:
                        tmp_chr = chr
                        file_name = f"chr_{tmp_chr}.txt"
                        current_file_path = os.path.join(output_dir, file_name)
                        
                        # Close the previous file and open a new one
                        chr_file.close()
                        chr_file = open(current_file_path, 'w')

                    # Write the chromosome and locus data to the file
                    chr_file.write(f"{chr}\t{locus}\n")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_file_path}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Define the path to the input file
    input_file_path = 'filepath'
    
    # Define the output directory for chromosome files
    output_dir = 'filepath'
    
    # Process the file
    process_chromosome_HiC_data(input_file_path, output_dir)
