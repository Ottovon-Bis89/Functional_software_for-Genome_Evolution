# Function to count unique numbers in a text file
def count_unique_numbers_in_file(file_path):
    unique_numbers = set()  # Use a set to store unique numbers

    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Split the line into words and convert them to integers
                numbers = [int(word) for word in line.split() if word.isdigit()]

                # Add the unique numbers to the set
                unique_numbers.update(numbers)

    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

    return len(unique_numbers)

# Example usage
file_path = "/home/22204911/Documents/chrom_interactions/chr16_hi_c.txt"  # Replace with your file path
unique_count = count_unique_numbers_in_file(file_path)

if unique_count is not None:
    print(f"Number of unique numbers in {file_path}: {unique_count}")
