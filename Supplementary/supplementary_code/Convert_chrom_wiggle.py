import os

def create_wiggle_file(chromosome_length, coordinates_of_interest, output_file_path):
    """
    Generates a Wiggle (WIG) file based on chromosome length and coordinates of interest.
    The file will have a fixedStep format with values set to 100 for specific positions of interest.

    Parameters:
    - chromosome_length (int): The total length of the chromosome.
    - coordinates_of_interest (list): List of integer positions where values should be set to 100.
    - output_file_path (str): The path where the Wiggle file will be created.

    Raises:
    - ValueError: If chromosome length is invalid or coordinates are out of bounds.
    """
    # Validate chromosome length
    if chromosome_length <= 0:
        raise ValueError("Chromosome length must be a positive integer.")
    
    # Initialize a list with default value 0 for all chromosome positions
    values = [0] * chromosome_length

    # Set the value to 100 for coordinates of interest, ensuring they are within bounds
    for coordinate in coordinates_of_interest:
        if 0 <= coordinate < chromosome_length:
            values[coordinate] = 100
        else:
            raise ValueError(f"Coordinate {coordinate} is out of bounds for chromosome length {chromosome_length}.")

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

    # Open the output file and write the Wiggle data
    with open(output_file_path, 'w') as output_file:
        # Write the fixedStep header
        output_file.write("fixedStep chrom=chromosome start=1 step=1\n")

        for value in values:
            output_file.write(f"{value}\n")

    print(f"Wiggle file '{output_file_path}' created successfully.")


def read_coordinates_from_file(file_path):
    """
    Reads a file containing chromosome positions of interest and returns them as a list of integers.

    Parameters:
    - file_path (str): Path to the file containing the coordinates.

    Returns:
    - list: A list of integer positions extracted from the file.

    Raises:
    - FileNotFoundError: If the file does not exist.
    - ValueError: If any position in the file is not a valid integer.
    """
    coordinates = []
    
    try:
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.strip().split('\t')
                if len(parts) >= 2:
                    try:
                        coordinate = int(parts[1])
                        coordinates.append(coordinate)
                    except ValueError:
                        raise ValueError(f"Invalid coordinate value in file: {parts[1]}")
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    
    return coordinates


if __name__ == "__main__":
    
    # Define the chromosome length (set to your chromosome's length)
    chromosome_length = 'actual chr length'

    coordinates_file_path = 'FILEPATH'  # Change to your file path

    output_file_path = '/FILEPATH'  # Change to your output file path

    # Read coordinates from the input file
    try:
        coordinates_of_interest = read_coordinates_from_file(coordinates_file_path)
    except (FileNotFoundError, ValueError) as e:
        print(f"Error reading coordinates: {e}")
    else:
        # Create the Wiggle file
        try:
            create_wiggle_file(chromosome_length, coordinates_of_interest, output_file_path)
        except (ValueError, IOError) as e:
            print(f"Error creating Wiggle file: {e}")
