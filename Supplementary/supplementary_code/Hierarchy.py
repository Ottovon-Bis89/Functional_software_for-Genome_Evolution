import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

# Global mapping of event codes to their classifications
event_classification = {
    'trp0': 0, 'trp1': 1, 'trp2': 2, 'inv': 3, 'ins': 4,
    'fus': 5, 'fis': 6, 'b_trl': 7, 'u_trl': 8, 'del': 9, 'dup': 10
}

def read_input_file(file_path):
    """
    Reads the input file and returns the lines starting from the first occurrence of '#'.
    
    Parameters:
    - file_path (str): The path to the input file.
    
    Returns:
    - list: A list of lines starting from the first hash symbol ('#').
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Find the first line containing '#'
    first_hash_index = next(i for i, line in enumerate(lines) if '#' in line)
    return lines[first_hash_index:]

def parse_solutions(lines):
    """
    Parses the lines to extract solutions and their associated events.
    
    Parameters:
    - lines (list): A list of lines from the input file starting from the first hash.
    
    Returns:
    - list: A list of solutions, each with its solution number and associated events.
    """
    solutions = []
    current_solution = None
    solution_count = 0

    for line in lines:
        line = line.strip()
        if line.startswith('*') or not line:
            continue
        if line.startswith('#'):
            solution_count += 1
            if current_solution is not None:
                solutions.append(current_solution)
            current_solution = {'solution': f'solution {solution_count}', 'events': []}
        else:
            events = line.split("'")
            current_solution['events'].extend(events)

    if current_solution is not None:
        solutions.append(current_solution)

    return solutions

def classify_events_and_write_output(solutions, output_file_path):
    """
    Classifies the events for each solution and writes the classified data to an output file.
    
    Parameters:
    - solutions (list): A list of solutions with their events.
    - output_file_path (str): The path to the output file.
    """
    with open(output_file_path, 'w') as output_file:
        for solution in solutions:
            output_file.write(f'# {solution["solution"]}  ')
            for event in solution['events']:
                event_code = event_classification.get(event, -1)
                if event_code != -1:
                    output_file.write(f'{event_code} ')
            output_file.write('\n')

def read_classified_data(file_path, limit=100):
    """
    Reads classified event data from a file and returns the solutions and their corresponding event codes.
    
    Parameters:
    - file_path (str): The path to the file containing classified event data.
    - limit (int): The maximum number of solutions to read (default is 100).
    
    Returns:
    - tuple: A tuple containing two lists:
        - x (list): A list of solution labels.
        - y (list): A list of event classifications for each solution.
    """
    x = []
    y = []

    with open(file_path, 'r') as file:
        counter = 0
        for line in file:
            n = line.strip().split()
            if len(n) > 2:
                x.append(n[2])
                y_2 = [j for j in n[2:]]
                y.append(y_2)

            counter += 1
            if counter == limit:
                break

    return x, y

def perform_hierarchical_clustering(y, method='complete', metric='euclidean'):
    """
    Performs hierarchical clustering on the event data and returns the linkage matrix.
    
    Parameters:
    - y (list): A list of event classifications for each solution.
    - method (str): The linkage method to use (default is 'complete').
    - metric (str): The distance metric to use (default is 'euclidean').
    
    Returns:
    - ndarray: The linkage matrix produced by the hierarchical clustering.
    """
    return linkage(y, method=method, metric=metric)

def plot_dendrogram(linkage_matrix, labels, title="title of graph", xlabel="x-axis label", ylabel="Y-axis label"):
    """
    Plots a dendrogram based on the provided linkage matrix.
    
    Parameters:
    - linkage_matrix (ndarray): The linkage matrix produced by hierarchical clustering.
    - labels (list): A list of labels for the solutions.
    - title (str): The title of the plot.
    - xlabel (str): The label for the x-axis.
    - ylabel (str): The label for the y-axis.
    """
    plt.figure(figsize=(5, 10))
    dendrogram(linkage_matrix, labels=labels)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def main(input_file_path, output_file_path):
    """
    Main function to orchestrate the reading, processing, and clustering of evolutionary path data.
    
    Parameters:
    - input_file_path (str): The path to the input file.
    - output_file_path (str): The path to the output file for storing classified events.
    """
    # Step 1: Read and parse the input file
    lines = read_input_file(input_file_path)
    solutions = parse_solutions(lines)

    # Step 2: Classify events and write output
    classify_events_and_write_output(solutions, output_file_path)

    # Step 3: Read classified data for clustering
    x, y = read_classified_data(output_file_path)

    # Step 4: Perform hierarchical clustering
    linkage_matrix = perform_hierarchical_clustering(y)

    # Step 5: Plot the dendrogram
    plot_dendrogram(linkage_matrix, x)

# Entry point for script execution
if __name__ == "__main__":
    input_file_path = "filepath"
    output_file_path = "filepath"
    main(input_file_path, output_file_path)
