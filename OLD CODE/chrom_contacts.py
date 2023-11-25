def create_wiggle_file(chromosome_length, coordinates_of_interest, output_file_path):
    # Create a list to store the values for each coordinate
    values = [0] * chromosome_length

    # Set the value to 100 for coordinates of interest
    for coordinate in coordinates_of_interest:
        if 0 <= coordinate < chromosome_length:
            values[coordinate] = 100

    # Open the output file for writing
    with open(output_file_path, 'w') as output_file:
        # Write the fixedstep Wiggle file header
        output_file.write("fixedStep chrom=chromosome start=1 step=1\n")

        # Write the values to the file
        for value in values:
            output_file.write(str(value) + '\n')

# def read_coordinates_from_file(file_path):
#     coordinates = []
#     with open(file_path, 'r') as file:
#         for line in file:
#             coordinate = int(line.strip())
#             coordinates.append(coordinate)
#     return coordinates
def read_coordinates_from_file(file_path):
    coordinates = []
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line on tabs and take the second part as the position
            parts = line.strip().split('\t')
            if len(parts) >= 2:
                coordinate = int(parts[1])
                coordinates.append(coordinate)
    return coordinates

# Define the chromosome length (change this to your chromosome length)
chromosome_length = 948066

# Define the path to the file containing coordinates of interest
coordinates_file_path = '/home/22204911/Documents/chrom_interactions/chrom16_interac_points'  # provide file path

# Read coordinates from the file
coordinates_of_interest = read_coordinates_from_file(coordinates_file_path)

# Define the output file path
output_file_path = '/home/22204911/Documents/interaction.wig/chrom16_inter.wig'

# Create the Wiggle file
create_wiggle_file(chromosome_length, coordinates_of_interest, output_file_path)

print(f"Wiggle file '{output_file_path}' created successfully.")
