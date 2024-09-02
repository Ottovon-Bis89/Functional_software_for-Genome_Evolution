import pandas as pd
import matplotlib.pyplot as plt


def load_and_preprocess_data(file_path):
    """Loads the data and preprocesses the Probability column."""
    # Read the data from the file
    df = pd.read_csv(file_path, sep='\t')
    
    # Convert 'Probability' column to numeric and filter out NaN and negative values
    df['Probability'] = pd.to_numeric(df['Probability'], errors='coerce')
    df = df[df['Probability'] >= 0].reset_index(drop=True)
    
    return df


def calculate_average_p_values(df, bin_size):
    """Groups the data into bins of size `bin_size` and calculates average p-values."""
    # Add bin column based on the index and bin size
    df['bin'] = df.index // bin_size
    
    # Group by bin and calculate the average Probability per bin
    average_p_values = df.groupby('bin')['Probability'].mean().tolist()
    
    return average_p_values


def generate_bin_widths(start, stop, step, num_bins):
    """Generates a list of bin widths, ensuring it matches the number of bins."""
    return list(range(start, stop, step))[:num_bins]


def plot_average_p_values(bin_widths, average_p_values):
    """Generates and displays a plot of bin widths against average p-values."""
    plt.figure(figsize=(10, 6))
    plt.plot(bin_widths, average_p_values, marker='.', linestyle='-')
    plt.title('title of graph')
    plt.xlabel('X-axis label ')
    plt.ylabel('Y-axis label')
    plt.grid(False)
    plt.show()


def main(file_path, bin_size=257, start=500, stop=5000, step=10):
    """Main function to execute the workflow."""
    # Load and preprocess the data
    df = load_and_preprocess_data(file_path)
    
    # Calculate average p-values for each bin
    average_p_values = calculate_average_p_values(df, bin_size)
    
    # Generate bin widths matching the number of bins
    bin_widths = generate_bin_widths(start, stop, step, len(average_p_values))
    
    # Plot the average p-values against bin widths
    plot_average_p_values(bin_widths, average_p_values)


# File path (you can change this as needed)
file_path = '/home/22204911/Documents/chrom_mutations/hypergeometric_output11.txt'

# Run the main function with the file path
main(file_path)
