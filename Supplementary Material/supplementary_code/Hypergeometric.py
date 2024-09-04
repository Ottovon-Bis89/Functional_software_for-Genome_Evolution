import math
import class_wiggle

class Hypergeometric:
    """
    Class for calculating hypergeometric probabilities and performing binning operations.
    """

    def __init__(self, stepsize=1000):
        """
        Initialize the Hypergeometric class with the step size.

        Args:
            stepsize (int): The step size for calculations. Default is 1000.
        """
        self.stepsize = stepsize
        self.number_of_entries_in_file_1 = 0

    def nCr(self, n, r):
        """
        Calculate the binomial coefficient (n choose r).

        Args:
            n (int): Total number of items.
            r (int): Number of selected items.

        Returns:
            int: The binomial coefficient or -1 if an error occurs.
        """
        try:
            factorial_n = math.factorial(n)
            factorial_r = math.factorial(r)
            factorial_nminusr = math.factorial(n - r) if n - r > 0 else 1
            return factorial_n // (factorial_r * factorial_nminusr)
        except (OverflowError, ValueError) as e:
            print(f"Error in calculating nCr: {e}")
            return -1

    def calculate_hypergeometric(self, N, n, K, k):
        """
        Calculate the hypergeometric probability.

        Args:
            N (int): Total population size.
            n (int): Number of draws.
            K (int): Number of successes in population.
            k (int): Number of successes in draws.

        Returns:
            float: Hypergeometric probability.
        """
        NCn = self.nCr(N, n)
        N_KCn_k = self.nCr(N - K, n - k)
        KCk = self.nCr(K, k)
        if NCn == -1 or N_KCn_k == -1 or KCk == -1:
            return -1
        return KCk * N_KCn_k / NCn

    def number_of_bins(self, bin_width, list_of_values):
        """
        Calculate the number of bins based on bin width and list length.

        Args:
            bin_width (int): Width of each bin.
            list_of_values (list): List of values to be binned.

        Returns:
            int: Number of bins.
        """
        number_of_values = len(list_of_values)
        return (number_of_values + bin_width - 1) // bin_width

    def bin_values(self, bin_width, list_of_values):
        """
        Bin values based on the bin width.

        Args:
            bin_width (int): Width of each bin.
            list_of_values (list): List of values to be binned.

        Returns:
            list: List of bin counts (1 if a non-zero value exists in the bin, otherwise 0).
        """
        number_of_values = len(list_of_values)
        number_of_bins = self.number_of_bins(bin_width, list_of_values)
        bins = [0] * number_of_bins

        for i in range(number_of_values):
            bin_index = i // bin_width
            if list_of_values[i] != 0:
                if bins[bin_index] != 0:
                    print(f"Warning: More than 1 entry in bin {bin_index}")
                bins[bin_index] = 1

        return bins

    def does_list_contain_non_zero_value(self, sublist):
        """
        Check if a sublist contains any non-zero values.

        Args:
            sublist (list): The sublist to check.

        Returns:
            bool: True if the sublist contains a non-zero value, False otherwise.
        """
        return any(value != 0 for value in sublist)

    def find_overlap_with_bins(self, bin_width, bins_of_sequence_1, sequence_2_values):
        """
        Find overlapping bins between two sequences.

        Args:
            bin_width (int): Width of each bin.
            bins_of_sequence_1 (list): Binned values of the first sequence.
            sequence_2_values (list): Values of the second sequence.

        Returns:
            list: List of bins where overlap occurs.
        """
        k_bin_list = []
        number_of_bins = len(bins_of_sequence_1)

        for bin_number in range(number_of_bins):
            start_pos = bin_number * bin_width
            end_pos = min((bin_number + 1) * bin_width, len(sequence_2_values))

            if bins_of_sequence_1[bin_number] != 0 and self.does_list_contain_non_zero_value(sequence_2_values[start_pos:end_pos]):
                k_bin_list.append(bin_number)

        return k_bin_list

    def number_of_bin_overlaps(self, bin_width, bins1, sequence_2_values):
        """
        Count the number of overlapping bins between two sequences.

        Args:
            bin_width (int): Width of each bin.
            bins1 (list): Binned values of the first sequence.
            sequence_2_values (list): Values of the second sequence.

        Returns:
            int: Number of overlapping bins.
        """
        return len(self.find_overlap_with_bins(bin_width, bins1, sequence_2_values))

    def number_of_non_zero_bins(self, bins):
        """
        Count the number of non-zero bins.

        Args:
            bins (list): List of bins.

        Returns:
            int: Number of non-zero bins.
        """
        return sum(1 for bin_value in bins if bin_value != 0)

    def get_hypergeometric_probability(self, bin_width, sequence_1_values, sequence_2_values):
        """
        Calculate the hypergeometric probability for two sequences.

        Args:
            bin_width (int): Width of each bin.
            sequence_1_values (list): Values of the first sequence.
            sequence_2_values (list): Values of the second sequence.

        Returns:
            tuple: Probability and parameters (N, n, K, k).
        """
        bins1 = self.bin_values(bin_width, sequence_1_values)
        K = self.number_of_non_zero_bins(bins1)
        N = self.number_of_bins(bin_width, sequence_1_values)
        bins2 = self.bin_values(bin_width, sequence_2_values)
        n = self.number_of_non_zero_bins(bins2)
        k = self.number_of_bin_overlaps(bin_width, bins1, sequence_2_values)
        probability = self.calculate_hypergeometric(N, n, K, k)
        return probability, N, n, K, k


def run_with_bin_width(hg, bin_width, f):
    """
    Run the hypergeometric probability calculation for specified bin width and save the results to a file.

    Args:
        hg (Hypergeometric): Instance of the Hypergeometric class.
        bin_width (int): Bin width for the calculation.
        f (file object): File to write the results.
    """
    for i in range(1, 17):
        for j in range(1, 17):
            print(f"Hi-C: {i}, Recomb: {j}")
            filename1 = f'filepath{j}_recomb.txt' # change filename to suit you
            filename2 = f'filepath{i}_hi_c.txt'

            wigglefile = class_wiggle.Wiggle()
            sequence_1_values = wigglefile.read_wiggle_file(filename1)
            sequence_2_values = wigglefile.read_wiggle_file(filename2)

            probability, N, n, K, k = hg.get_hypergeometric_probability(bin_width, sequence_1_values, sequence_2_values)
            print(f"Probability: {probability}, N: {N}, n: {n}, K: {K}, k: {k}")

            f.write(f"{i}\t{j}\t{N}\t{n}\t{K}\t{k}\t{probability}\n")


def main():
    """
    Main function to run the hypergeometric probability calculation for different bin widths and save results.
    """
    hg = Hypergeometric()

    with open("filename", "a") as f:
        f.write("Hi-C\tRecomb\tN\tn\tK\tk\tProbability\n")
        
        # Run for bin widths from 500 to 5000 with a step of 10
        for bin_width in range(500, 5001, 10):
            run_with_bin_width(hg, bin_width, f)


if __name__ == "__main__":
    main()
