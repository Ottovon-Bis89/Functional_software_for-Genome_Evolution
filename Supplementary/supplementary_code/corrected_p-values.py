# Open the input file with seven columns
with open('/home/22204911/Documents/chrom_mutations/hypergeometric_output14.txt', 'r') as input_file:
    # Open a new file for writing the filtered rows
    with open('corrected_p-value.txt2', 'w') as output_file:
        # Define the threshold for p-values
        threshold = 0.003


        # Read and write the header row
        header = input_file.readline()
        output_file.write(header)

        # Iterate through each line in the input file
        for line in input_file:
            # Split the line into columns
            columns = line.strip().split()

            # # Check if the p-value in the last column is less than the threshold
            # if float(columns[-1]) <= threshold:
            #     # If it is, write the entire row to the output file
            #     output_file.write('\t'.join(columns) + '\n')

            # Check if the p-value in the last column is a positive number

            p_value = float(columns[-1])
            if p_value >= 0:
                # Check if the p-value is less than the threshold
                if p_value <= threshold:
                    # If it is, write the entire row to the output file
                    output_file.write('\t'.join(columns) + '\n')


print("Filtered p-values written to 'corrected_p-values.txt2'")
