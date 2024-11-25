import math
import class_wiggle

class hypergeometric:
	"""
    A class to perform hypergeometric probability calculations and related binning operations.
    """

	def __init__(self, stepsize=1):
		"""
        Initializes the hypergeometric class with a step size for binning operations.
        :param stepsize: Step size for binning, default is 1.
        """
		self.stepsize = stepsize
		self.number_of_entries_in_file_1 = 0


	def nCr(self,n,r):
		"""
        Calculates the number of combinations (n choose r).
        :param n: Total number of recombination points found within defined bin width..
        :param r: Number of overlaps with regions of spatial proximity at a time
        :return: The number of combinations, or -1 if an error occurs.
        """
		try:
			factorial_n = math.factorial(n)
			factorial_r = math.factorial(r)
			if (n-r == 0):
				factorial_nminusr = 1
			else:
				factorial_nminusr = math.factorial(n-r)
			nCr = factorial_n/(factorial_r*factorial_nminusr)
		except OverflowError:
			print('Factorial too big')
			nCr = -1
		except ValueError:
			print('Negative values not defined for factorial()')
			nCr = -1
		return nCr

	def calculate_hypergeometric(self,N,n,K,k):
		"""
        Calculates the hypergeometric probability.
        :param N: Total population size.
        :param n: Sample size.
        :param K: Total number of successes in the population.
        :param k: Number of successes in the sample.
        :return: Hypergeometric probability or -1 if an error occurs.
        """
		NCn = self.nCr(N,n)
		N_KCn_k = self.nCr(N-K, n-k)
		KCk = self.nCr(K,k)
		if NCn == -1 or N_KCn_k == -1 or KCk == -1:
			return -1
		else:
			p = KCk*N_KCn_k/NCn
		return p
	

	def number_of_bins(self,bin_width, list_of_values):
		"""
        Calculates the number of bins required for binning the values.
        :param bin_width: Width of each bin.
        :param list_of_values: List of values to be binned.
        :return: Number of bins.
        """
		number_of_values = len(list_of_values)
		number_of_bins = number_of_values // bin_width
		if number_of_values % bin_width != 0:
			number_of_bins += 1
		return number_of_bins

	def bin_values(self,bin_width, list_of_values):
		"""
        Bins the values into bins of specified width.
        :param bin_width: Width of each bin.
        :param list_of_values: List of values to be binned.
        :return: List of bins with presence/absence of non-zero values.
        """
		number_of_values = len(list_of_values)
		number_of_bins = self.number_of_bins(bin_width, list_of_values)
		bins = [0]*number_of_bins
		for bin_number in range(number_of_bins):
			for current_position in range(bin_number*bin_width,(bin_number+1)*bin_width):
				if current_position < number_of_values:
					if list_of_values[current_position] != 0:
						if bins[bin_number] != 0:
							print("More than 1 entry in bin", bin_number)
						else:
							bins[bin_number] = 1

		return bins

	def does_list_contain_non_zero_value(self, short_list):
		"""
        Checks if a list contains any non-zero values.
        :param short_list: List to check.
        :return: True if non-zero values are present, False otherwise.
        """
		length_of_list = len(short_list)
		number_of_zeros = short_list.count(0)
		if number_of_zeros < length_of_list:
			return True
		else:
			return False
		

	def find_overlap_with_bins(self, bin_width,  bins_of_sequence_1, sequence_2_values):
		"""
        Finds bins in sequence 1 that overlap with non-zero values in sequence 2.
        :param bin_width: Width of each bin.
        :param bins_of_sequence_1: Bins of sequence 1 (recombination points).
        :param sequence_2_values: Values of sequence 2 (regions of spatial proximity or H3K9 acetylated regions)
        :return: List of overlapping bins.
        """
		k_bin_list = []
		number_of_bins = len(bins_of_sequence_1)
		for bin_number in range(number_of_bins):
			start_position = bin_number*bin_width
			end_position = (bin_number+1)*bin_width
			if end_position > len(sequence_2_values):
				end_position = len(sequence_2_values)
			contains_non_zero_value = self.does_list_contain_non_zero_value(sequence_2_values[start_position:end_position])
			if bins_of_sequence_1[bin_number] != 0 and contains_non_zero_value:
				k_bin_list.append(bin_number)
		return k_bin_list
	

	def number_of_bin_overlaps(self, bin_width,  bins1, sequence_2_values):
		"""
        Calculates the number of overlapping bins.
        :param bin_width: Width of each bin.
        :param bins1: Bins of sequence 1.
        :param sequence_2_values: Values of sequence 2.
        :return: Number of overlapping bins.
        """
		k_bin_list = self.find_overlap_with_bins(bin_width, bins1, sequence_2_values)
		return len(k_bin_list)
	

	def number_of_non_zero_bins(self, bins):
		"""
        Counts the number of non-zero bins.
        :param bins: List of bins.
        :return: Number of non-zero bins.
        """
		number_of_entries = len(bins)
		number_of_zero_entries = bins.count(0)
		number_of_non_zeros = number_of_entries-number_of_zero_entries
		return number_of_non_zeros


	def get_hypergeometric_probability(self, bin_width,  sequence_1_values, sequence_2_values):
		"""
        Computes the hypergeometric probability for two sequences.
        :param bin_width: Width of each bin.
        :param sequence_1_values: Values of sequence 1.
        :param sequence_2_values: Values of sequence 2.
        :return: Tuple containing probability, N, n, K, k.
        """
		bins1 = self.bin_values(bin_width, sequence_1_values)
		K = self.number_of_non_zero_bins(bins1)
		N = self.number_of_bins(bin_width, sequence_1_values)
		bins2 = self.bin_values(bin_width, sequence_2_values)
		n = self.number_of_non_zero_bins(bins2)
		k = self.number_of_bin_overlaps(bin_width,  bins1, sequence_2_values)
		probability = self.calculate_hypergeometric(N, n, K, k)
		return (probability, N, n, K, k)


def main():
	hg = hypergeometric()
	"""
    Main function to compute hypergeometric probabilities for multiple pairs of files (input files).
    """
	# Full path to the text format file of "events".  The file should contain an entry for each nucleotide
 	# with a 0 if there is no "event" at the nucleotide, and 1 if there is an "event".  The file is in
 	# text format with no wiggle style headers or entries.  See ""
 	# filename1 = 'chrom_recomb.txt' 
 	# filename2 = 'chrom_hi_c.txt'
 	# wigglefile = class_wiggle.Wiggle()
	# sequence_1_values = wigglefile.read_wiggle_file(filename1)
 	# sequence_2_values = wigglefile.read_wiggle_file(filename2)
 	# probability, N, n, K, k = hg.get_hypergeometric_probability(bin_width,  sequence_1_values, sequence_2_values)
 	# print(probability, "N =",N, "n =",n, "K =", K, "k =",k)
	f = open("output_filename", "a")
    
    # Write a header for the table
	f.write("Chr_recomb\tRecomb\tN\tn\tK\tk\tProbability\n")


	def run_with_bin_width(bin_width):
		"""
        Executes the hypergeometric calculation for all chromosome pairs with the given bin width.
        :param bin_width: Width of each bin.
        """
		for i in range(1, 17):
			for j in range(1, 17):
				print('Chrom_proxi: ' + str(i))
				print('Recomb: ' + str(j))
				filename1 = '/path_to_recombination_fil' + str(j) + '_recomb.txt'
				filename2 = '/path_to_regions_spatial_proximity' + str(i) + '_proximity.txt'
				wigglefile = class_wiggle.Wiggle()
				sequence_1_values = wigglefile.read_wiggle_file(filename1)
				sequence_2_values = wigglefile.read_wiggle_file(filename2)
				probability, N, n, K, k = hg.get_hypergeometric_probability(bin_width, sequence_1_values, sequence_2_values)
				print(probability, "N =", N, "n =", n, "K =", K, "k =", k)
				out = f"{i}\t{j}\t{N}\t{n}\t{K}\t{k}\t{probability}\n"
				f.write(out)
			
		
	for i in range(0,1): # adjust number of iterations as desired
		run_with_bin_width(1) # adjust bin width as needed
	

	f.close()


if __name__ == "__main__":

	main()
	
