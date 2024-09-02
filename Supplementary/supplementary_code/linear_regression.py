import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from scipy.stats import spearmanr

def read_data(file_path_A, file_path_B, nrows):
    """
    Reads the Hi-C and recombination data for each chromosome.
    
    Args:
        file_path_A (str): Path to the Hi-C data file.
        file_path_B (str): Path to the recombination data file.
        nrows (int): Number of rows to read from the files.
    
    Returns:
        tuple: A tuple containing the Hi-C data (X) and recombination data (y) as numpy arrays.
    """
    file_A = pd.read_csv(file_path_A, header=None, nrows=nrows)
    file_B = pd.read_csv(file_path_B, header=None, nrows=nrows)
    return file_A.values, file_B.values

def perform_linear_regression(X, y):
    """
    Performs linear regression on the given data.
    
    Args:
        X (numpy.ndarray): The input feature data (Hi-C coordinates).
        y (numpy.ndarray): The target data (recombination coordinates).
    
    Returns:
        LinearRegression: The trained linear regression model.
    """
    model = LinearRegression()
    model.fit(X, y)
    return model

def calculate_spearman_correlation(X, y):
    """
    Calculates the Spearman rank-order correlation coefficient between two sets of data.
    
    Args:
        X (numpy.ndarray): The first set of data (Hi-C coordinates).
        y (numpy.ndarray): The second set of data (recombination coordinates).
    
    Returns:
        tuple: A tuple containing the Spearman correlation coefficient and the p-value.
    """
    corr, p_value = spearmanr(X, y)
    return corr, p_value

def plot_regression(X, y, model, i):
    """
    Generates a scatter plot of the data and overlays the linear regression line.
    
    Args:
        X (numpy.ndarray): The input feature data (Hi-C coordinates).
        y (numpy.ndarray): The target data (recombination coordinates).
        model (LinearRegression): The trained linear regression model.
        i (int): The chromosome number for labeling the plot.
    
    Returns:
        None
    """
    plt.scatter(X, y, color='blue', label='Data points')

    # Generate a line plot of the regression
    x_line = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
    y_line = model.predict(x_line)
    plt.plot(x_line, y_line, color='red', label='Regression line')

    # Label the axes and add a title
    plt.xlabel('X-axis label')
    plt.ylabel('Y-axis label')
    plt.title(f"title of graph")
    plt.legend()
    plt.show()

def process_chromosomes(folder_A, folder_B):
    """
    Processes Hi-C and recombination data for multiple chromosomes, performing linear regression
    and calculating Spearman correlation coefficients.
    
    Args:
        folder_A (str): Path to the folder containing Hi-C data files.
        folder_B (str): Path to the folder containing recombination data files.
    
    Returns:
        list: A list of Spearman correlation coefficients for each chromosome.
    """
    correlation_coefficients = []

    for i in range(1, 17):
        # Construct the file names
        file_A_name = os.path.join(folder_A, f'chr{i}_Hi_C.txt')
        file_B_name = os.path.join(folder_B, f'chr{i}_recomb.txt')

        # Adjust number of rows to read based on chromosome number
        nrows = 50 if i in [1, 3, 6, 9] else 150

        # Read the data
        X, y = read_data(file_A_name, file_B_name, nrows)
        X = X.reshape(-1, 1)  # Reshape for sklearn compatibility
        y = y.reshape(-1, 1)

        # Perform linear regression
        model = perform_linear_regression(X, y)
        print(f"For chr{i}:")
        print(f"Linear Regression Coefficient: {model.coef_[0][0]}")
        print(f"Linear Regression Intercept: {model.intercept_[0]}")

        # Calculate and store the Spearman rank-order correlation coefficient
        corr, p_value = calculate_spearman_correlation(X, y)
        correlation_coefficients.append(corr)
        print(f"Spearman Correlation Coefficient: {corr}")
        print(f"P-value: {p_value}")

        # Plot the regression and scatter plot
        plot_regression(X, y, model, i)

    return correlation_coefficients

def print_correlation_coefficients(correlation_coefficients):
    """
    Prints the Spearman correlation coefficients for each chromosome.
    
    Args:
        correlation_coefficients (list): List of Spearman correlation coefficients.
    
    Returns:
        None
    """
    print("Spearman correlation coefficients for all pairs:")
    for i, corr in enumerate(correlation_coefficients, 1):
        print(f"chr{i}: {corr}")

if __name__ == "__main__":
    """
    Main script execution. Processes the chromosome data from specified folders, 
    calculates linear regression and correlation, and prints the results.
    """
    folder_A = '/home/22204911/Documents/Chrom_Hi-C_unique.txt'
    folder_B = '/home/22204911/Documents/chrom_Recomb'

    # Process all chromosomes and get the correlation coefficients
    correlation_coefficients = process_chromosomes(folder_A, folder_B)

    # Print the correlation coefficients
    print_correlation_coefficients(correlation_coefficients)
