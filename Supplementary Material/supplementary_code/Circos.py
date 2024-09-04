import pandas as pd
from pycirclize import Circos
import matplotlib.pyplot as plt

def load_matrix(file_path):
    """
    Load the interaction matrix directly from a CSV or TSV file.
    """
    try:
        # Assuming the file is tab-delimited, but adjust delimiter as needed
        matrix_df = pd.read_csv(file_path, delimiter='\t', header=None)
        return matrix_df
    except Exception as e:
        print(f"Error loading matrix: {e}")
        return None

def create_circos_plot(matrix_df, row_names, col_names, output_file="circos_plot.png"):
    """
    Create a circos plot using the given matrix data and save it to a file.
    """
    # Initialize the Circos plot from the matrix data
    circos = Circos.initialize_from_matrix(
        matrix_df,
        space=3,  # Space between the segments
        r_lim=(93, 100),  # Radius limits for the plot
        cmap="tab10",  # Color map
        ticks_interval=500,  # Tick intervals for the circular plot
        label_kws=dict(r=94, size=12, color="white")  # Label customization
    )
    
    # Generate the plot
    fig = circos.plotfig()
    
    # Display and save the plot
    plt.show()
    fig.savefig(output_file)
    print(f"Circos plot saved to {output_file}")

def main():
    # Chromosome names (for yeast genome)
    row_names = [f"Chr{i}" for i in range(1, 17)]
    col_names = row_names
    
    # Path to the file with the interaction matrix
    matrix_file_path = 'path_to_matrix_file.txt'  # Replace with your file path
    
    # Load the interaction matrix from the file
    
    matrix_df = load_matrix(matrix_file_path)
    
    if matrix_df is None:
        print("Failed to load matrix data.")
        return
    
    # Create and save the circos plot
    create_circos_plot(matrix_df, row_names, col_names, output_file="circos_plot.png")


if __name__ == "__main__":
    main()
