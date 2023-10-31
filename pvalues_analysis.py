
import pandas as pd
import matplotlib.pyplot as plt

# Read the data from your file into a DataFrame
file_path = '/home/22204911/Documents/chrom_mutations/hypergeometric_output11.txt'  # file path
df = pd.read_csv(file_path, sep='\t')  #

# Define the list of bin widths with a step 
bin_widths = list(range(500, 5000, 10))
average_p_values = []
current_bin_p_values = []

# Iterate through the rows
for index, row in df.iterrows():
    if index % 257 == 0:
        # Calculate the average p-value for the previous bin width
        if current_bin_p_values:
            # Filter out negative values from the current bin's p-values
            non_negative_p_values = [p for p in current_bin_p_values if p >= 0]
            if non_negative_p_values:
                average_p_value = sum(non_negative_p_values) / len(non_negative_p_values)
                average_p_values.append(average_p_value)
                # print(len(average_p_values))
            else:
                average_p_values.append(0)  # If all values were negative, set the average to 0
        current_bin_p_values = []
    else:
        # Convert the 'Probability' column to numeric, handling missing values
        probability = pd.to_numeric(row['Probability'], errors='coerce')
        if not pd.isna(probability):
            current_bin_p_values.append(probability)

#iterate through the rows
# for index, row in df.iterrows():
#     if index % 257 == 0:
#         # Calculate the average p-value for the previous bin width
#         if current_bin_p_values:
#             average_p_value = sum(current_bin_p_values) / len(current_bin_p_values)
#             average_p_values.append(average_p_value)
#         current_bin_p_values = []
#     else:
#         # Convert the 'Probability' column to numeric, handling missing values
#         probability = pd.to_numeric(row['Probability'], errors='coerce')
#         if not pd.isna(probability):
#             current_bin_p_values.append(probability)

            # print(len(current_bin_p_values))

# Check if there are any empty bins and remove them
bin_widths, average_p_values = zip(*[(bw, avg) for bw, avg in zip(bin_widths, average_p_values) if avg])

# Create a plot
plt.figure(figsize=(10, 6))
plt.plot(bin_widths, average_p_values, marker='.', linestyle='-')
plt.title('A graph of Average P-Values vs. Bin Widths of Hi-C contact points interactions with Recombination points in the Saccharromyces cerevisiae genome')
plt.xlabel('Bin Width(nt)')
plt.ylabel('Average P-Value')
plt.grid(False)

# Show the plot or save it to a file
plt.show()
