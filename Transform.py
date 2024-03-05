import networkx as nx
class Genome:
    def __init__(self, genes):
        self.genes = genes
        self.intergenic_regions = [0] + [sum(len(x) for x in zip(self.genes[i-1:i+1])) for i in range(1, len(self.genes))] + [0]
        self.adjacencies = []
    def __str__(self):
        return ' '.join(str(gene) for gene in self.genes)

def calculate_transformations(genome1, genome2):
    # Calculate the DCJ distance between the two genomes
    dcj_distance = calculate_dcj_distance(genome1, genome2)

    # Calculate the number of genes in each genome
    genome1_genes = len(genome1.genes)
    genome2_genes = len(genome2.genes)

    # Calculate the number of genes in the larger genome
    larger_genome_genes = max(genome1_genes, genome2_genes)

    # Calculate the number of genes in the smaller genome
    smaller_genome_genes = min(genome1_genes, genome2_genes)

    # Initialize the list of operations
    operations = []

    # Calculate the number of rearrangements
    rearrangements = 0

    # Calculate the number of insertions and deletions
    insertions_deletions = abs(genome1_genes - genome2_genes)

    # Calculate the number of duplications
    duplications = 0

    # Calculate the rearrangements
    while dcj_distance > 0:
        # Find the adjacency with the minimum weight
        min_weight = float('inf')
        min_weight_adjacency = None
        for adjacency in genome1.adjacencies:
            weight = adjacency.weight
            if weight < min_weight:
                min_weight = weight
                min_weight_adjacency = adjacency

        # Find the adjacency in genome2 that corresponds to the minimum weight adjacency in genome1
        genome2_adjacency = None
        for adjacency in genome2.adjacencies:
            if (adjacency.gene1 == min_weight_adjacency.gene2 and adjacency.gene2 == min_weight_adjacency.gene1) or \
               (adjacency.gene1 == min_weight_adjacency.gene1 and adjacency.gene2 == min_weight_adjacency.gene2):
                genome2_adjacency = adjacency
                break

        # If the adjacencies are not adjacent in genome2, perform a reversal
        if genome2_adjacency is not None and genome2_adjacency.gene2 != genome2_adjacency.next.gene1:
            operations.append({'type': 'reversal', 'genes': genome2_adjacency.genes})
            genome2_adjacency.next.prev = genome2_adjacency.prev
            genome2_adjacency.prev.next = genome2_adjacency.next
            genome2_adjacency.prev = genome2_adjacency.next = None
            genome2_adjacency.gene1 = None
            genome2_adjacency.gene2 = None
            rearrangements += 1
            dcj_distance -= 1

        # Otherwise, perform a fission
        else:
            operations.append({'type': 'fission', 'genes': [min_weight_adjacency.gene1]})
            new_gene = Adjacency(min_weight_adjacency.gene2, None, min_weight_adjacency.next)
            min_weight_adjacency.next.prev = min_weight_adjacency.prev
            min_weight_adjacency.prev.next = new_gene
            min_weight_adjacency.next = new_gene
            min_weight_adjacency.prev = new_gene
            min_weight_adjacency.gene1 = None
            min_weight_adjacency.gene2 = None
            dcj_distance -= 1

    # Calculate the insertions and deletions
    while insertions_deletions > 0:
        # If genome1 is larger, perform a deletion in genome1
        if genome1_genes > genome2_genes:
            gene = genome1.genes.pop(0)
            position = genome1.intergenic_regions[0]
            operations.append({'type': 'deletion', 'position': position, 'gene': gene})
            genome1_genes -= 1
            genome1.intergenic_regions[0] += len(str(gene))
            insertions_deletions -= 1

        # Otherwise, perform an insertion in genome2
        else:
            gene = genome2.genes.pop()
            position = genome2.intergenic_regions[-2]
            genome2.intergenic_regions[-2] += len(str(gene)) + 1
            genome2.genes.insert(genome2.genes.index(genome2.genes[-2]) + 1, gene)
            operations.append({'type': 'insertion', 'position': position, 'gene': gene})
            genome2_genes += 1
            insertions_deletions -= 1

    # Calculate the duplications
    while duplications < larger_genome_genes - smaller_genome_genes:
        # Find the gene with the minimum multiplicity
        min_multiplicity = float('inf')
        min_multiplicity_gene = None
        for gene in genome1.genes:
            multiplicity = genome1.genes.count(gene)
            if multiplicity < min_multiplicity:
                min_multiplicity = multiplicity
                min_multiplicity_gene = gene

        # Duplicate the gene
        position = genome1.intergenic_regions[genome1.genes.index(min_multiplicity_gene)]
        genome1.genes.insert(genome1.genes.index(min_multiplicity_gene) + 1, min_multiplicity_gene)
        genome1.intergenic_regions.insert(genome1.genes.index(min_multiplicity_gene) + 1, 0)
        for i in range(genome1.genes.index(min_multiplicity_gene) + 1, len(genome1.genes)):
            genome1.intergenic_regions[i] += len(str(min_multiplicity_gene))
        operations.append({'type': 'duplication', 'position': position, 'gene': min_multiplicity_gene})
        genome1_genes += 1
        duplications += 1

    # Create the directed acyclic graph
    dag = DirectedAcyclicGraph()
    for i, operation in enumerate(operations):
        if operation['type'] == 'reversal':
            for gene in operation['genes']:
                dag.add_node(f'R{i}:{gene}')
            dag.add_edge(f'R{i}:{operation["genes"][0]}', f'R{i}:{operation["genes"][-1]}')
        elif operation['type'] == 'fission':
            for gene in operation['genes']:
                dag.add_node(f'F{i}:{gene}')
            dag.add_edge(f'F{i}:{operation["genes"][0]}', f'F{i}:{operation["genes"][0]}')
        elif operation['type'] == 'insertion':
            dag.add_node(f'I{i}:{operation["gene"]}')
            dag.add_edge(f'I{i}:{operation["gene"]}', f'I{i}:{operation["gene"]}')
        elif operation['type'] == 'deletion':
            dag.add_node(f'D{i}:{operation["gene"]}')
            dag.add_edge(f'D{i}:{operation["gene"]}', f'D{i}:{operation["gene"]}')

    return operations, dag

def calculate_dcj_distance(genome1, genome2):
    # Calculate the adjacencies in genome1
    genome1_adjacencies = []
    gene = genome1.genes[0]
    prev = None
    for next in genome1.genes[1:]:
        genome1_adjacencies.append(Adjacency(gene, prev))
        prev = gene
        gene = next
    genome1_adjacencies.append(Adjacency(gene, prev))

    # Calculate the adjacencies in genome2
    genome2_adjacencies = []
    gene = genome2.genes[0]
    prev = None
    for next in genome2.genes[1:]:
        genome2_adjacencies.append(Adjacency(gene, prev))
        prev = gene
        gene = next
    genome2_adjacencies.append(Adjacency(gene, prev))

    # Calculate the weight of each adjacency in genome1
    for adjacency in genome1_adjacencies:
        adjacency.weight = 0
        for genome2_adjacency in genome2_adjacencies:
            if (adjacency.gene1 == genome2_adjacency.gene1 and adjacency.gene2 == genome2_adjacency.gene2) or \
               (adjacency.gene1 == genome2_adjacency.gene2 and adjacency.gene2 == genome2_adjacency.gene1):
                adjacency.weight = 1

    # Calculate the number of telomeres in genome1
    telomeres = 0
    for adjacency in genome1_adjacencies:
        if adjacency.weight == 0:
            telomeres += 1

    return len(genome1_adjacencies) - telomeres

class Adjacency:
    def __init__(self, gene1, gene2=None, next=None, prev=None):
        self.gene1 = gene1
        self.gene2 = gene2
        self.next = next
        self.prev = prev
        self.weight = 0

class DirectedAcyclicGraph:
    def __init__(self):
        self.nodes = set()
        self.edges = set()

    def add_node(self, node):
        self.nodes.add(node)

    def add_edge(self, node1, node2):
        self.edges.add((node1, node2))

    def draw(self, filename):
        # Create the graph
        graph = nx.Digraph()

        # Add the nodes
        for node in self.nodes:
            graph.node(node)

        # Add the edges
        for edge in self.edges:
            graph.edge(*edge)

        # Save the graph to a file
        graph.save(filename)

# Test the implementation
genome1 = Genome([1, 1, 2, 3, 3, 3])
genome2 = Genome([1, 2, 2, 3, 3])
operations, dag = calculate_transformations(genome1, genome2)
dag.draw('transformations.dot')




def get_legal_operations(self, adjacencies_genomeB):

    """
    This method takes a list of adjacencies for genome B and returns a list of legal operations
    to transform the adjacencies of genome A into genome B.

    Parameters:
    - adjacencies_genomeB (list): The list of adjacencies for genome B.

    Returns:
    - list_of_legal_operations (list): A list of legal operations to transform genome A to genome B.
    """
    list_of_legal_operations = [] 
    adjacencies_genomeA = self.state  
    adjacencies_genomeB = adjacencies_genomeB 

    for element in adjacencies_genomeB:

        if element in adjacencies_genomeA:
            pass  

        else:

            adjacencies_genomeA_copy = adjacencies_genomeA[:]

            if type(element) is tuple:
                p, q = element[0], element[1] 
                u, v = 0, 0  

                for marker in adjacencies_genomeA_copy:
                    if type(marker) is tuple:
                        if marker[0] == p or marker[1] == p:
                            u = marker  

                        if marker[0] == q or marker[1] == q:
                            v = marker  

                if u == 0:
                    u = p

                if v == 0:
                    v = q

                if u != v:   

                    adjacencies_genomeA_copy.append((p, q))

                    adjacencies_genomeA_copy.remove(u)
                    
                    adjacencies_genomeA_copy.remove(v)

                     
                    if type(u) is tuple:
                       
                        if u[0] == p:
                            u_not_p = u[1]
                        else:
                            u_not_p = u[0]

                     
                        if type(v) is tuple:

                         
                            if v[0] == q:
                                v_not_q = v[1]
                            else:
                                v_not_q = v[0]

                        
                            adjacencies_genomeA_copy.append((u_not_p, v_not_q))

                    

                            op_1 = (u, v) if u[0] < v[0] else (v, u)
                            op_2_1 = (p, q) if p < q else (q, p)
                            op_2_2 = (u_not_p, v_not_q) if u_not_p < v_not_q else (v_not_q, u_not_p)
                            op_2 = (op_2_1, op_2_2) if op_2_1[0] < op_2_2[0] else (op_2_2, op_2_1)
                            ordered_operation = (op_1, op_2)

                        
                            if ordered_operation not in list_of_legal_operations:
                                list_of_legal_operations.append(ordered_operation)
                            else:
                                pass

                        else:
                            adjacencies_genomeA_copy.append(u_not_p)  

                         
                            if p < q:
                                op_2_1 = (p, q)
                            else:
                                op_2_1 = (q, p)

                            op_2 = (op_2_1, u_not_p)  
                            ordered_operation = ((u, v), op_2)   

                            if ordered_operation not in list_of_legal_operations:  
                                list_of_legal_operations.append((ordered_operation)) 
                                pass
                        
                    else:
                       
                        if type(v) is tuple:

                            
                            if v[0] == q:
                                v_not_q = v[1]
                            else:
                                v_not_q = v[0]
                            adjacencies_genomeA_copy.append(v_not_q) 

                       
                            if p < q:
                                op_2_1 = (p, q)
                            else:
                                op_2_1 = (q, p)

                            ordered_operation = ((v, u), (op_2_1, v_not_q))  

                            if ordered_operation not in list_of_legal_operations:  
                                list_of_legal_operations.append(ordered_operation)  
                            else:
                                pass

                       
                        else:
                        
                            if p < q:
                                op_2 = (p, q)
                            else:
                                op_2 = (q, p)

                            
                            if u < v:
                                ordered_operation = (u, v, op_2)
                            else:
                                ordered_operation = (v, u, op_2)

                            if ordered_operation not in list_of_legal_operations:   
                                list_of_legal_operations.append((ordered_operation))  
                            else:
                                pass

                            # Insertion
                            if u == 0:
                                insert_index = adjacencies_genomeA_copy.index(p)
                                insert_operation = (('insert', insert_index, p),)
                                ordered_operation = ordered_operation + insert_operation
                                if ordered_operation not in list_of_legal_operations:
                                    list_of_legal_operations.append(ordered_operation)

                            # Deletion
                            if v == 0:
                                delete_index = adjacencies_genomeA_copy.index(q)
                                delete_operation = (('delete', delete_index),)
                                ordered_operation = ordered_operation + delete_operation
                                if ordered_operation not in list_of_legal_operations:
                                    list_of_legal_operations.append(ordered_operation)

                            # Duplication
                            if type(u) is tuple and u[0] == p:
                                duplication_index = adjacencies_genomeA_copy.index(u[1])
                                duplication_operation = (('duplicate', duplication_index, p),)
                                ordered_operation = ordered_operation + duplication_operation
                                if ordered_operation not in list_of_legal_operations:
                                    list_of_legal_operations.append(ordered_operation)

                            if type(u) is tuple and u[1] == p:
                                duplication_index = adjacencies_genomeA_copy.index(u[0])
                                duplication_operation = (('duplicate', duplication_index, p),)
                                ordered_operation = ordered_operation + duplication_operation
                                if ordered_operation not in list_of_legal_operations:
                                    list_of_legal_operations.append(ordered_operation)

                            if type(v) is tuple and v[0] == q:
                                duplication_index = adjacencies_genomeA_copy.index(v[1])
                                duplication_operation = (('duplicate', duplication_index, q),)
                                ordered_operation = ordered_operation + duplication_operation
                                if ordered_operation not in list_of_legal_operations:
                                    list_of_legal_operations.append(ordered_operation)

                            if type(v) is tuple and v[1] == q:
                                duplication_index = adjacencies_genomeA_copy.index(v[0])
                                duplication_operation = (('duplicate', duplication_index, q),)
                                ordered_operation = ordered_operation + duplication_operation
                                if ordered_operation not in list_of_legal_operations:
                                    list_of_legal_operations.append(ordered_operation)

                else:
                    p = element
                    u = 0

                    for marker in adjacencies_genomeA_copy:  

                        if type(marker) is tuple: 
                            if marker[0] == p or marker[1] == p:
                                u = marker
                                       
                        if u == 0:
                            u = p

                     
                        if u != p:
                         
                            adjacencies_genomeA_copy.append(u[0])
                            adjacencies_genomeA_copy.append(u[1])
                            adjacencies_genomeA_copy.remove(u)

                            operation = ((u), (u[0]), (u[1]))  
                            if operation not in list_of_legal_operations: 
                                list_of_legal_operations.append((operation))

                            # Insertion
                            if u == 0:
                                insert_index = adjacencies_genomeA_copy.index(p)
                                insert_operation = (('insert', insert_index, p),)
                                ordered_operation = ordered_operation + insert_operation
                                if ordered_operation not in list_of_legal_operations:
                                    list_of_legal_operations.append(ordered_operation)

                            # Deletion
                            if u[0] == p:
                                delete_index = adjacencies_genomeA_copy.index(u[1])
                                delete_operation = (('delete', delete_index),)
                                ordered_operation = ordered_operation + delete_operation
                                if ordered_operation not in list_of_legal_operations:
                                    list_of_legal_operations.append(ordered_operation)

                            if u[1] == p:
                                delete_index = adjacencies_genomeA_copy.index(u[0])
                                delete_operation = (('delete', delete_index),)
                                ordered_operation = ordered_operation + delete_operation
                                if ordered_operation not in list_of_legal_operations:
                                    list_of_legal_operations.append(ordered_operation)

                            # Duplication
                            duplication_index = adjacencies_genomeA_copy.index(p)
                            duplication_operation = (('duplicate', duplication_index, p),)
                            ordered_operation = ordered_operation + duplication_operation
                            if ordered_operation not in list_of_legal_operations:
                                list_of_legal_operations.append(ordered_operation)

    return list_of_legal_operations