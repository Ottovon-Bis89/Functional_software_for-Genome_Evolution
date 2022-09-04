# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 02:48:36 2022

@author: dakur
"""


class Xtremities:

    def __init__(self):
        pass

    def gene_extremity(self, genome):  # find gene extremities in genome for downward action
        genome_gene_extremity = []
        for chromosome in genome:
            chromosome_gene_extremity = []
            for element in chromosome:
                if int(element) >= 0:
                    chromosome_gene_extremity.append(element)
                    chromosome_gene_extremity.append(element + 0.5)
                else:
                    chromosome_gene_extremity.append(abs(element) + 0.5)
                    chromosome_gene_extremity.append(abs(element))
            genome_gene_extremity.append(chromosome_gene_extremity)

        return genome_gene_extremity

        # finding the adjacencies of each gene

    def create_adjacencyList(self, genome):
        adjacencies = []
        gene_extremity = Xtremities.gene_extremity(self, genome)
        for chromosome in gene_extremity:
            i = 0
            while i < len(chromosome):
                if chromosome[i] == chromosome[0] or chromosome[i] == chromosome[-1]:
                    adjacencies.append(chromosome[i])
                    i += 1
                else:
                    adjacencies.append((chromosome[i], chromosome[i + 1]))
                    i += 2

        return adjacencies

        # ordering and sorting the adjacencies of the genes

    def adjacencies_ordered_and_sorted(self, genome):
        adjacencies = []
        telomers = []
        sorted_adjacencies = Xtremities.create_adjacencyList(self, genome)
        for element in sorted_adjacencies:
            if type(element) is tuple:
                if int(element[0]) < int(element[1]):
                    adjacencies.append(element)
                else:
                    adjacencies.append((element[1], element[0]))

            else:
                telomers.append(element)
        adjacencies.sort()
        telomers.sort()
        adjacencies_sorted = telomers + adjacencies
        return adjacencies_sorted, adjacencies, telomers

    '''
    Function : find_next_extremity
    Parameters:
        @current :  holds the genome extremities as signed integers in a list
        @next_extremity : holds the next extremity as signed inetgers in a list
    Purpose:
        Provides extremities for each gene in the genome
    '''
    def find_next_extremity(self, current, next_extremity):
        if current[0] == next_extremity:
            if current[1] % 1 == 0:
                next_extremity = (current[1] + [0.5])
            else:
                next_extremity = (current[1] - [0.5])
        else:
            if current[0][0] % 1 == 0:
                next_extremity = (current[0] + [0.5])
            else:
                next_extremity = (current[0] - [0.5])
        return next_extremity

    def find_next_adjacency(self, next_extremity, chromosome, telomers):
        for element in telomers:
            if element == next_extremity:
                current = element
                chromosome.append(current)
                telomers.remove(current)
                next_extremity = Xtremities.find_next_extremity(self, current, next_extremity)
            return next_extremity, chromosome, telomers
        return [next_extremity]

    def find_adjacency_cycle(self, next_extremity, chromosome, telomers):
        next_adjacency = Xtremities.find_next_adjacency(self, next_extremity, chromosome, telomers)
        while len(next_adjacency) != 1:
            next_extremity = next_adjacency[0]
        else:
            next_extremity = next_adjacency[1]

        return next_extremity, chromosome, telomers

        # find the chromosomes in the genomes

    def find_chromosome(self, adjacencies):
        telomers = [element for element in adjacencies if type(element) is not tuple]
        linear_chromosomes = []
        chromosome = []
        i = 0
        # find linear chromosomes in case there circular chromosomes
        while len(telomers) > 0:
            i += 1
            current = telomers[0]
            telomers.remove(current)
            chromosome.append(current)

            if current % 1 == 0:
                next_extremity = current + 0.5
            else:
                next_extremity = current - 0.5

        # if the chromosome has a single gene
            if next_extremity in telomers:
                current = next_extremity

                telomers.remove(current)
                chromosome.append(current)
                linear_chromosomes.append(chromosome)
                chromosome = []

        # find the adjacency cycle
            else:
                adjacency_cycle = Xtremities.find_next_adjacency(self, next_extremity, chromosome, telomers)
                next_extremity = adjacency_cycle[0]

                if next_extremity in telomers:
                    current = next_extremity
                    telomers.remove(current)
                    chromosome.append(current)
                    linear_chromosomes.append(chromosome)
                    chromosome = []

        return linear_chromosomes, telomers, chromosome

    def adjacencies_to_genome(self, adjacencies):
        genome = []
        chromosomes = Xtremities.find_chromosome(self, adjacencies)
        linear_chromosomes = chromosomes[0]

        for chromosome in linear_chromosomes:
            chromosome = []
            gene = 0
            chromosome_length = len(chromosome)
            for i in range(0, chromosome_length - 1):
                if i == 0:
                    gene = chromosome[i]
                    if gene % 1 == 0:
                        chromosome.append(int(gene))
                    else:
                        chromosome.append(-int(gene))

                else:
                    if int(gene) == int(chromosome[i][0]):
                        gene = chromosome[i][1]
                    else:
                        gene = chromosome[i][0]

                    if gene % 1 == 0:
                        chromosome.append(int(gene))
                    else:
                        chromosome.append(-int(gene))
            genome.append(chromosome)

        return genome

