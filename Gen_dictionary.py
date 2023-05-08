from networkx import DiGraph


class Net_work:

    def __init__(self):

        self.genome_dictionary = {}
        self.source_genome = []
        self.target_genome = []
        self.current_genome = []
        

            # Define an empty dictionary
        genome_dict = {}

        # Add the source genome and the target genome to the dictionary
        source_genome = (source_genome)
        target_genome = (target_genome)

        genome_dict[str(source_genome)] = {"parent": None, "child_operations": []}
        genome_dict[str(target_genome)] = {"parent": None, "child_operations": []}

        # Make the source genome the current genome
        current_genome = source_genome

    # Recursive function to perform legal operations
    def recursive_function(current_genome):
            # Find and create a list of all possible legal operations
            legal_operations = []
            for i in range(len(current_genome)):
                for j in range(i+1, len(current_genome)):
                    legal_operations.append((i, j))
                    legal_operations.append((j, i))
                    legal_operations.append((i, j, 1))
                    legal_operations.append((j, i, 1))

            # For each legal operation:
            for operation in legal_operations:
                # Execute the legal operation
                intermediary_genome = perform_legal_operation(current_genome, operation)
                # Add the legal operation to the current genome’s list of child operations
                child_operations = genome_dict[str(current_genome)]["child_operations"] + [operation]
                # Add the resulting intermediary genome to the current genome’s list of children
                genome_dict[str(current_genome)]["children"] = genome_dict[str(current_genome)].get("children", []) + [intermediary_genome]
                # Check if the resulting intermediary genome is already in the dictionary
                if str(intermediary_genome) in genome_dict:
                    # Move to and execute the next legal operation (jump to line 10)
                    continue
                else:
                    # Add it to the dictionary
                    genome_dict[str(intermediary_genome)] = {"parent": current_genome, "child_operations": child_operations}
                    # Make it the current genome (jump to line 7)
                    recursive_function(intermediary_genome)

    # Function to perform legal operation
    def perform_legal_operation(genome, operation):
            # Perform legal operation on the genome
            # Return the intermediary genome
            pass # You need to implement this function
            
            
            # Call the recursive function
        recursive_function(current_genome)
