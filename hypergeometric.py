import math
import class_wiggle

class hypergeometric:

	def __init__(self, stepsize=1000):
		self.stepsize = stepsize
		self.number_of_entries_in_file_1 = 0

	def calculate_probability(self, list1, list2):
		pass

	def nCr(self,n,r):
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
		NCn = self.nCr(N,n)
		N_KCn_k = self.nCr(N-K, n-k)
		KCk = self.nCr(K,k)
		if NCn == -1 or N_KCn_k == -1 or KCk == -1:
			return -1
		else:
			p = KCk*N_KCn_k/NCn
		return p

	def number_of_bins(self,bin_width, list_of_values):
		number_of_values = len(list_of_values)
		number_of_bins = number_of_values // bin_width
		if number_of_values % bin_width != 0:
			number_of_bins += 1
		return number_of_bins

	def bin_values(self,bin_width, list_of_values):
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
		length_of_list = len(short_list)
		number_of_zeros = short_list.count(0)
		if number_of_zeros < length_of_list:
			return True
		else:
			return False
		
		
	# def does_list_contain_non_zero_value(self, short_list):
	# 	return any(value != 0 for value in short_list)


	def find_overlap_with_bins(self, bin_width,  bins_of_sequence_1, sequence_2_values):
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
		k_bin_list = self.find_overlap_with_bins(bin_width, bins1, sequence_2_values)
		return len(k_bin_list)
	

	def number_of_non_zero_bins(self, bins):
		number_of_entries = len(bins)
		number_of_zero_entries = bins.count(0)
		number_of_non_zeros = number_of_entries-number_of_zero_entries
		return number_of_non_zeros


	def get_hypergeometric_probability(self, bin_width,  sequence_1_values, sequence_2_values):
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
	# Full path to the text format file of "events".  The file should contain an entry for each nucleotide
# 	# with a 0 if there is no "event" at the nucleotide, and 1 if there is an "event".  The file is in
# 	# text format with no wiggle style headers or entries.  See ""
# 	# filename1 = 'chrom_recomb.txt' 
# 	# filename2 = 'chrom_hi_c.txt'
# 	# wigglefile = class_wiggle.Wiggle()
# 	# sequence_1_values = wigglefile.read_wiggle_file(filename1)
# 	# sequence_2_values = wigglefile.read_wiggle_file(filename2)
# 	# probability, N, n, K, k = hg.get_hypergeometric_probability(bin_width,  sequence_1_values, sequence_2_values)
# 	# print(probability, "N =",N, "n =",n, "K =", K, "k =",k)
	f = open("hypergeometric_output17.txt", "a")
    
    # Write a header for the table
	f.write("Chp_sq\tRecomb\tN\tn\tK\tk\tProbability\n")


    # Repeat run function with specified bin widths
	def run_with_bin_width(bin_width):
		for i in range(1, 17):
			for j in range(1, 17):
				print('ChiP_sep: ' + str(i))
				print('Recomb: ' + str(j))
				filename1 = '/home/von/Documents/Recomb.wiggle/chrom' + str(j) + '_recomb.txt'
				filename2 = '/home/von/Documents/ch_seq.wiggle/chrom' + str(i) + '_seq.txt'
				wigglefile = class_wiggle.Wiggle()
				sequence_1_values = wigglefile.read_wiggle_file(filename1)
				sequence_2_values = wigglefile.read_wiggle_file(filename2)
				probability, N, n, K, k = hg.get_hypergeometric_probability(bin_width, sequence_1_values, sequence_2_values)
				print(probability, "N =", N, "n =", n, "K =", K, "k =", k)
				out = f"{i}\t{j}\t{N}\t{n}\t{K}\t{k}\t{probability}\n"
				f.write(out)
			# Write the data in a tab-separated format
			# out = f"{i}\t{j}\t{N}\t{n}\t{K}\t{k}\t{probability}\n"
			# f.write(out)
		
		# Start the recursion with bin_width = 100
	for i in range(0,1):
		run_with_bin_width(1000)
	

	f.close()


if __name__ == "__main__":

	main()
	

