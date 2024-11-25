class Wiggle:
    """
    A class for processing and analyzing Wiggle format files containing genomic data.

    Attributes:
        header_lines (list): Stores header lines from a Wiggle file.
        chromosome_names (list): Stores names of chromosomes.
        data (list): Stores numeric data from the Wiggle file.
    """
    
    def __init__(self):
        """
        Initializes an empty Wiggle object with default attributes.
        """
        self.header_lines = []
        self.chromosome_names = []
        self.data = []
    
    def IsFloat(self, test):
        """
        Checks if a given string can be converted to a float.

        Args:
            test (str): The string to check.

        Returns:
            bool: True if the string is a valid float, False otherwise.
        """
        true = True
        max_len = len(test)  
        if max_len == 0:  
            return False
        for char in range(0, max_len): 
            if test[char].isdigit() or test[char] == '.': 
                true = true and True  
            else:
                return False 
        return true
    

    def read_wiggle_file(self, path):
        """
        Reads a Wiggle file and extracts numerical data.

        Args:
            path (str): The file path of the Wiggle file.

        Returns:
            list: A list of integers extracted from the file.
        """
        data = []
        with open(path, 'r') as f: 
            for line in f:
                data.append(int(line.strip('\n'))) 
        return data

    def NormalizeWiggleFile(self, filename, conversion_factor):
        """
        Normalizes the numeric data in a Wiggle file by a given factor.

        Args:
            filename (str): Path to the Wiggle file.
            conversion_factor (float): Factor by which to normalize values.

        Returns:
            tuple: A list of normalized data, total of all normalized values, 
                   and the count of numerical values processed.
        """
        factor = float(conversion_factor) 
        wiggle_array = []
        total = 0
        number_of_values = 0

        with open(filename, 'r') as handle:  
            for line in handle:
                line2 = line.rstrip('\n')  
                if self.IsFloat(line2):  
                    number = float(line2) * factor 
                    total += number 
                    number_of_values += 1  
                    wiggle_array.append(str(number) + '\n')  
                else:
                    wiggle_array.append(line)  
        
        return wiggle_array, total, number_of_values
    

    def CountsPerChromosome(self, filename):
        """
        Counts data points and their total value per chromosome in a Wiggle file.

        Args:
            filename (str): Path to the Wiggle file.

        Returns:
            tuple: Three lists containing:
                - Number of data points per chromosome.
                - Total counts per chromosome.
                - Names of chromosomes.
        """
        number_of_data_points_in_chromosome = []  
        total_counts_in_chromosome = []  
        chromosome_name = []  

        total = 0  
        number_of_values = 0  
        first_chromosome = True  

        with open(filename, 'r') as handle: 
            for line in handle:
                line2 = line.rstrip('\n')  
                
                if self.IsFloat(line2):  
                    number = float(line2)
                    total += number
                    number_of_values += 1
                else:
                    # Extract chromosome name from the line
                    temp_list = line2.split(' ')
                    for item in temp_list:
                        if 'chrom=' in item:  # Look for the 'chrom=' pattern
                            dot = item.find('=')
                            name = item[dot+1:]  
                            
                            if first_chromosome:
                                new_name = name
                                old_name = new_name
                                first_chromosome = False  
                            else:
                                old_name = new_name
                                new_name = name

                                chromosome_name.append(old_name)
                                number_of_data_points_in_chromosome.append(number_of_values)
                                total_counts_in_chromosome.append(int(total))
                                
                               
                                total = 0
                                number_of_values = 0

        chromosome_name.append(new_name)
        number_of_data_points_in_chromosome.append(number_of_values)
        total_counts_in_chromosome.append(int(total))

        return number_of_data_points_in_chromosome, total_counts_in_chromosome, chromosome_name
