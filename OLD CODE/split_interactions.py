import Helper_Methods

# Open a file in read mode ('r')
file_path = '/home/22204911/Documents/working_scripts/chrom_interaction_data'  # Replace with the path to your file
tmp = '1'
file_name = "chr_" + str(tmp)
Helper_Methods.create_new_file(file_name)
try:
    with open(file_path, 'r') as file:
        # Iterate through each line in the file
        for line in file:
            if 'locus' not in line:
                line = line.split()
                chr = line[0]
                locus = line[1]
                if chr != tmp:
                    tmp = chr
                    file_name = "chr_"+str(tmp)
                tmpStr = str(chr)+'\t'+str(locus)+'\n'
                Helper_Methods.append_to_file(file_name, tmpStr)
except FileNotFoundError:
    print(f"The file '{file_path}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")