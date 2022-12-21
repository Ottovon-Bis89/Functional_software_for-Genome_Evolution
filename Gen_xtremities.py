# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 02:48:36 2022

@author: dakur
"""


import string


class Xtremities:

    def __init__(self):
        pass

    def gene_extremity(self, genome):  # find gene extremities in genome for downward action
        genome_gene_extremity = []
        for chromosome in genome:
            chromosome_gene_extremity = []
            for element in chromosome:
                if '*' not in element:
                    if int(element) >= 0:
                        chromosome_gene_extremity.append(int(element))
                        chromosome_gene_extremity.append(int(element) + 0.5)
                    else:
                        chromosome_gene_extremity.append(abs(int(element)) + 0.5)
                        chromosome_gene_extremity.append(abs(int(element)))
                else:
                    chromosome_gene_extremity.append(((element)))
            genome_gene_extremity.append(chromosome_gene_extremity)

        return genome_gene_extremity

        # finding the adjacencies of each gene

    def create_adjacencyList(self, genome):
        adjacencies = []
        gene_extremity = Xtremities.gene_extremity(self, genome)
       
        for chromosome in gene_extremity:
            i = 0
            chrom = []
            while i < len(chromosome):
                if(isinstance(chromosome[i], str) == True):
                 
                    chrom.append(chromosome[i])
                    i += 1
                elif chromosome[i] == chromosome[0] or chromosome[i] == chromosome[-1]:
                    chrom.append(chromosome[i])
                    i += 1
                elif i < len(chromosome) - 3 and isinstance(chromosome[i+1], str) == True: 
                    chrom.append((chromosome[i], chromosome[i + 2]))
                    i += 1
                elif(isinstance(chromosome[i+1], str) == False):
                    chrom.append((chromosome[i], chromosome[i + 1]))
                    i+=1
                else:
                    print("problem occurred")
            adjacencies.append(chrom)
            chrom = []
                    
                   

        return adjacencies

        # ordering and sorting the adjacencies of the genes

    def adjacencies_ordered_and_sorted(self, genome):
        adjacencies = []
        c_adj = []
        telomers = []
        c_tel = []
        sorted_adjacencies = Xtremities.create_adjacencyList(self, genome)
        for element in sorted_adjacencies:
            for i in range(len(element)):
                if type(element[i]) is tuple:
                    tup = element[i]
                    if int(tup[0]) < int(tup[1]):
                        c_adj.append(tup)
                    else:
                        c_adj.append((tup[1], tup[0]))

                else:
                    c_tel.append(str(element[i]))
            c_adj.sort()
            adjacencies.append(c_adj)
            c_adj = []
            c_tel.sort()
            telomers.append(c_tel)
            c_tel = []
        # adjacencies.sort()
        # telomers.sort()
        adjacencies_sorted = telomers + adjacencies
        return adjacencies_sorted, adjacencies, telomers #Telomers arent actually telomers but end point genes and intergenic regions

    '''
    Function : find_next_extremity
    Parameters:
        @current :  holds the genome extremities as signed integers in a list(tuples)
        @next_extremity : holds the next extremity as signed inetgers in a list
    Purpose:
        Provides extremities for each gene in the genome
    '''
    def find_next_extremity(self, current):
        next_extremity = []
        c_next = []
        # if current[0] == next_extremity:
        for sub in current:
            for cur in sub:
                left = cur[0]
                right = cur[1]
                c_next.append((left-0.5, right+0.5))
            next_extremity.append(c_next)
            c_next  = []
            # if cur[1] % 1 == 0:
            #     next_extremity.append(cur[1] + 0.5)
            # else:
            #     next_extremity.append(cur[1] - 0.5)
            # # else:
            # if current[0][0] % 1 == 0:
            #     next_extremity.append(cur[0] + 0.5)
            # else:
            #     next_extremity.append(cur[0] - 0.5)
        return next_extremity


    #Next to functions fpr checks and validation - no functionality changes
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

        return next_extremity, chromosome, telomers#Telomers arent actually telomers but end point genes and intergenic regions


        # find the chromosomes in the genomes


    '''
    Gives only linear chromosomes from a genome, due to mixture of both circular and linear chromosomes
    '''
    def find_chromosome_type(self, adjacencies):
        linear_chromosomes = []
        circular_chromosomes = []
        genome = []
        genome = [element for element in adjacencies if type(element) is not tuple and type(element) is not string]
        for chromosome in genome:
            if type(chromosome[0]) is not tuple and type(chromosome[len(chromosome)-1]) is not str:
                if chromosome[0] < 0:
                    #circular
                    circular_chromosomes.append(chromosome)
                    genome.append(chromosome)
                elif (chromosome[0] > 0 and chromosome[len(chromosome)-1] < 0) or (chromosome[0] > 0 and chromosome[len(chromosome)-1] > 0):
                    #linear 
                    chromosome.insert(0, 'o')
                    chromosome.append('o')
                    linear_chromosomes.append(chromosome)
                    genome.append(chromosome)
        return linear_chromosomes, circular_chromosomes, genome


    '''
    takes linear chromosomes and outputs the genome (signed integers per chromosome)
    
    def adjacencies_to_genome(self, adjacencies):
        genome = []
        chromosomes = Xtremities.find_chromosome_type(adjacencies)
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
    '''

