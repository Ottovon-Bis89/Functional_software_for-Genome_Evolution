class Wiggle:
    """
    A class to handle reading, normalizing, and counting data from wiggle files.
    
    Attributes:
    ----------
    header_lines : list
        Stores header lines from the wiggle file.
    chromosome_names : list
        Stores the names of chromosomes found in the wiggle file.
    data : list
        Stores the numeric data found in the wiggle file.

    Methods:
    -------
    IsFloat(test):
        Checks if a given string can be converted to a float.
        
    read_wiggle_file(path):
        Reads wiggle data from a file and returns it as a list of integers.
        
    NormalizeWiggleFile(filename, conversion_factor):
        Normalizes the numeric data in the wiggle file by a given factor.
        
    CountsPerChromosome(filename):
        Computes the number of data points and total counts per chromosome from a wiggle file.
    """

    def __init__(self):
        """Initializes the Wiggle class with empty attributes for headers, chromosomes, and data."""
        self.header_lines = []
        self.chromosome_names = []
        self.data = []

    def IsFloat(self, test):
        """
        function to heck if a given string represents a float number.

        Parameters:
        ----------
        test : str
            The string to be tested.
        
        Returns:
        -------
        bool
            True if the string is a float, False otherwise.
        """
        if not test:  # Empty string check
            return False

        try:
            float(test)
            return True
        except ValueError:
            return False

    def read_wiggle_file(self, path):
        """
        Reads a wiggle file containing integer data.

        Parameters:
        ----------
        path : str
            The path to the wiggle file.
        
        Returns:
        -------
        list
            A list of integers representing the data in the wiggle file.
        """
        data = []
        try:
            with open(path, 'r') as f:
                for line in f:
                    data.append(int(line.strip()))
        except FileNotFoundError:
            print(f"Error: The file '{path}' does not exist.")
        except ValueError:
            print(f"Error: Invalid data found in the file '{path}'. Expected integers.")
        return data

    def NormalizeWiggleFile(self, filename, conversion_factor):
        """
        Normalizes the numeric data in the wiggle file by multiplying it by a conversion factor.

        Parameters:
        ----------
        filename : str
            The path to the wiggle file.
        conversion_factor : float
            The factor by which to normalize the data.
        
        Returns:
        -------
        tuple
            A tuple containing:
            - A list of normalized data (as strings with newlines).
            - The total sum of the normalized data.
            - The count of numeric values in the file.
        """
        wiggle_array = []
        total = 0
        number_of_values = 0

        try:
            with open(filename, 'r') as handle:
                factor = float(conversion_factor)

                for line in handle:
                    line2 = line.rstrip('\n')

                    if self.IsFloat(line2):
                        number = float(line2) * factor
                        total += number
                        number_of_values += 1
                        wiggle_array.append(f"{number}\n")
                    else:
                        wiggle_array.append(line)
        except FileNotFoundError:
            print(f"Error: The file '{filename}' does not exist.")
        except ValueError as e:
            print(f"Error: {e}. Ensure the conversion factor and wiggle data are valid.")
        
        return wiggle_array, total, number_of_values

    def CountsPerChromosome(self, filename):
        """
        Computes the number of data points and total counts per chromosome.

        Parameters:
        ----------
        filename : str
            The path to the wiggle file.
        
        Returns:
        -------
        tuple
            A tuple containing:
            - A list of data point counts per chromosome.
            - A list of total counts per chromosome.
            - A list of chromosome names.
        """
        number_of_data_points_in_chromosome = []
        total_counts_in_chromosome = []
        chromosome_name = []
        
        total = 0
        number_of_values = 0
        first_chromosome = True

        try:
            with open(filename, 'r') as handle:
                old_name = new_name = None

                for line in handle:
                    line2 = line.rstrip('\n')

                    if self.IsFloat(line2):
                        number = float(line2)
                        total += number
                        number_of_values += 1
                    else:
                        # Extract chromosome name from line
                        temp_list = line2.split(' ')
                        for item in temp_list:
                            if 'chrom=' in item:
                                name = item.split('=')[1]

                                # On chromosome change, store previous data and reset counters
                                if first_chromosome:
                                    new_name = name
                                    old_name = new_name
                                    first_chromosome = False
                                elif new_name != name:
                                    chromosome_name.append(old_name)
                                    number_of_data_points_in_chromosome.append(number_of_values)
                                    total_counts_in_chromosome.append(int(total))

                                    # Reset for the new chromosome
                                    old_name = new_name
                                    new_name = name
                                    total = 0
                                    number_of_values = 0

                # Append data for the last chromosome
                chromosome_name.append(new_name)
                number_of_data_points_in_chromosome.append(number_of_values)
                total_counts_in_chromosome.append(int(total))

        except FileNotFoundError:
            print(f"Error: The file '{filename}' does not exist.")
        
        return number_of_data_points_in_chromosome, total_counts_in_chromosome, chromosome_name
