def filter_p_values(input_filepath, output_filepath, threshold=0.003):
    """
    Filters rows from the input file based on a p-value threshold and writes them to the output file.
    
    Parameters:
    - input_filepath (str): Path to the input file containing p-values.
    - output_filepath (str): Path to the output file where filtered rows will be written.
    - threshold (float): P-value threshold for filtering rows. Defaults to 0.003.
    """

    try:
        # Open the input and output files
        with open(input_filepath, 'r') as input_file, open(output_filepath, 'w') as output_file:
            # Write the header to the output file
            header = input_file.readline()
            output_file.write(header)

            for line in input_file:
                columns = line.strip().split()

                # Attempt to parse the p-value from the last column
                try:
                    p_value = float(columns[-1])

                    if 0 <= p_value <= threshold:
                        # Write the row to the output file if it meets the threshold condition
                        output_file.write('\t'.join(columns) + '\n')
                        
                except ValueError:
                    # Handle any lines where the last column is not a valid float
                    print(f"Warning: Unable to parse p-value in line: {line.strip()}")
                    
        print(f"Filtered p-values written to '{output_filepath}'")

    except FileNotFoundError:
        print(f"Error: Input file '{input_filepath}' not found.")
    except IOError as e:
        print(f"IO Error: {e}")


# Example usage
input_filepath = 'path_to_input_file.txt'  # Replace with actual path
output_filepath = 'corrected_p-values.txt'  # Replace with actual path
filter_p_values(input_filepath, output_filepath)
