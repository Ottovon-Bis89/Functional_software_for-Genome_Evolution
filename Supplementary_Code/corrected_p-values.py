# Open the input file (hypergeometric outputfile)
with open('path/to/hypergeometric_output', 'r') as input_file:
    with open('Name_of_outputfile', 'w') as output_file:
        # Define the threshold for p-values
        threshold = 0.003 #(Bonferroni correction)


        header = input_file.readline()
        output_file.write(header)

        for line in input_file:
            columns = line.strip().split()

            # Check if the p-value in the last column is a positive number
            p_value = float(columns[-1])
            if p_value >= 0:
                if p_value <= threshold:
                    # If it is, write the entire row to the output file
                    output_file.write('\t'.join(columns) + '\n')


print("Filtered p-values written to 'outputfile_name'")
