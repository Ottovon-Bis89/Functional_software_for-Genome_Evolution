from My_curse import Xtremities
from DCJ_Node import Node

# find extremities of genomeA and genomeB
from txyy import find_chromosome

genomeA = []
genomeB = []
with open("D:/Bioinformatics/python_work/genA0.txt") as csv:
    line = [element.strip('\n').split(',') for element in csv]
    for element in line:
        element = list(map(int, element))
        genomeA.append(element)

with open("D:/Bioinformatics/python_work/genB0.txt") as csv:
    line = [element.strip('\n').split(',') for element in csv]
    for element in line:
        element = list(map(int, element))
        genomeB.append(element)

    get_extremities = Xtremities()

    gene_extremities_genomeA = get_extremities.gene_extremity(genomeA)
    adjacencies_genomeA = get_extremities.create_adjacencyList(genomeA)
    adjacencies_sorted_genomeA = get_extremities.adjacencies_ordered_and_sorted(genomeA)
    next_extremity_genomeA = get_extremities.find_next_extremity(gene_extremities_genomeA, genomeA)
    next_adjacency_genomeA = get_extremities.find_next_adjacency(next_extremity_genomeA, genomeA,
                                                                 adjacencies_sorted_genomeA)
    Linear_chromosomes_genomeA = get_extremities.find_chromosome(adjacencies_genomeA)
    chromosome_genomeA = Node.find_chromosomes(genomeA,adjacencies_genomeA)
print("adjacencies_genomeA: ", adjacencies_genomeA)
print("adjacencies_sorted_genomeA: ", adjacencies_sorted_genomeA)
print("next_extremity_genomeA: ", next_extremity_genomeA)
print("next_adjacency_genomeA: ", next_adjacency_genomeA)
print("Linear_chromosomes_genomeA: ", Linear_chromosomes_genomeA)
print("chromosome_genomeA: ", chromosome_genomeA)
