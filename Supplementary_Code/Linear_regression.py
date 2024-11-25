import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from scipy.stats import spearmanr

# Specify the paths where your files are located
folder_A = '/path_to_regions_of_spatial_proximity (Hi-C contact points)'
folder_B = '/path_to_recombination_files'

# Initialize empty lists to store correlation coefficients
correlation_coefficients = []

# Loop over the file pairs
for i in range(1, 17):
    # Construct the file names
    file_A_name = os.path.join(folder_A, f'chr{i}_Hi_C.txt')
    file_B_name = os.path.join(folder_B, f'chr{i}_recomb.txt')

    # Read the data from the files
    file_A = pd.read_csv(file_A_name, header=None, nrows=50)
    file_B = pd.read_csv(file_B_name, header=None, nrows=50)


# Loop over the file pairs
# for i in range(1, 17):
#     # Construct the file names
#     file_A_name = os.path.join(folder_A, f'chr{i}_Hi_C.txt')
#     file_B_name = os.path.join(folder_B, f'chr{i}_recomb.txt')

#     # Read the data from the files
#     if i in [1, 3, 6, 9]: # you can specify which chromosomes you want to plot
#         nrows = 50 # specify number of rows in data you want to plot
#     else:
#         nrows = 150

#     file_A = pd.read_csv(file_A_name, header=None, nrows=nrows)
#     file_B = pd.read_csv(file_B_name, header=None, nrows=nrows)


    # Reshape the data for sklearn
    X = file_A.values.reshape(-1, 1)
    y = file_B.values.reshape(-1, 1)

    # Perform linear regression
    model = LinearRegression()
    model.fit(X, y)

    print(f"For chr{i}:")
    print(f"Linear Regression Coefficient: {model.coef_}")
    print(f"Linear Regression Intercept: {model.intercept_}")

    # Calculate the Spearman rank-order correlation coefficient
    corr, p_value = spearmanr(X, y)
    correlation_coefficients.append(corr)
    print(f"Spearman Correlation Coefficient: {corr}")
    print(f"P-value: {p_value}")

    # Generate a scatter plot of the data
    plt.scatter(X, y, color='blue')

    # Generate a line plot of the regression
    x_line = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
    y_line = model.predict(x_line)
    plt.plot(x_line, y_line, color='red')

    plt.xlabel('Hi-C coordinates (bp)')
    plt.ylabel('Recombination coordinates (bp)')

    plt.title(f"Linear Regression between Hi-C and Recombination data for chr{i}")
    plt.show()

# Print the correlation coefficients for all pairs
print("Spearman correlation coefficients for all pairs:")
for i, corr in enumerate(correlation_coefficients, 1):
    print(f"chr{i}: {corr}")

