class Wiggle:
	#comment code
	
	def __init__(self):
		self.header_lines = []
		self.chromosome_names = []
		self.data = []
		
	def IsFloat(self, test):
		true = True
		max = len(test)
		if max == 0:
			return False
		for char in range(0, max):
			if (test[char].isdigit()) or test[char] == '.':
				true = true and True
			else:
				return False
		return true

	def read_wiggle_file(self, path):
		data = []
		f = open(path,'r')
		for line in f:
			data.append(int(line.strip('\n')))
		return(data)

	
	
	def NormalizeWiggleFile(self, filename, conversion_factor):
		handle = open(filename,'r')
		factor = float(conversion_factor)
		wiggle_array = []
		total = 0
		number_of_values = 0
		for line in handle:
			line2 = line.rstrip('\n')
			if self.IsFloat(line2):
				number = float(line2)
				number = number*factor
				total += number
				number_of_values += 1
				wiggle_array.append(str(number)+'\n')
			else:
				wiggle_array.append(line)
		handle.close()
		return wiggle_array,total,number_of_values

	def CountsPerChromosome(self, filename):
		handle = open(filename, 'r')
		number_of_data_points_in_chromosome = []
		total_counts_in_chromosome = []
		chromosome_name = []
		first_chromosome = True
		total = 0
		number_of_values = 0
		for line in handle:
			line2 = line.rstrip('\n')
			if self.IsFloat(line2):
				number = float(line2)
				total += number
				number_of_values += 1
			else:
				temp_list = line2.split(' ')
				for item in temp_list:
					if('chrom=') in item:
						dot = item.find('=')
						name = item[dot+1:]
						if(first_chromosome):
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
		handle.close()
		return number_of_data_points_in_chromosome,total_counts_in_chromosome,chromosome_name