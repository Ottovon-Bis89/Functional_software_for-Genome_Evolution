class Extremities_and_adjacencies:

    def __init__(self):

        pass

    def gene_extremities(self, genome):
        genome_gene_ext = []
        for chromosome in genome:
            chromosome_gene_ext = []
            for marker in chromosome:
                if int(marker) >= 0:
                    chromosome_gene_ext.append(marker)
                    chromosome_gene_ext.append(marker + 0.5)
                else:
                    chromosome_gene_ext.append(abs(marker) + 0.5)
                    chromosome_gene_ext.append(abs(marker))
            genome_gene_ext.append(chromosome_gene_ext)

        return genome_gene_ext

    def create_adjacency_list(self, genome):
        adjacencies = []
        gene_extremities = Extremities_and_adjacencies.gene_extremities(self, genome)
        for chromosome in gene_extremities:
            i = 0
            while i < len(chromosome):
                if chromosome[i] == chromosome[0] or chromosome[i] == chromosome[-1]:
                    adjacencies.append((chromosome[i]))
                    i += 1
                else:
                    adjacencies.append((chromosome[i], chromosome[i + 1]))
                    i += 2
        return adjacencies

    def adjacencies_ordered_and_sorted(self, genome):
        adjacencies = Extremities_and_adjacencies.create_adjacency_list(self, genome)
        adjs = []
        telomeres = []
        for element in adjacencies:
            if type(element) is tuple:
                if int(element[0]) < int(element[1]):
                    adjs.append(element)
                else:
                    adjs.append((element[1], element[0]))
            else:
                telomeres.append(element)
        adjs.sort()
        telomeres.sort()
        sorted_adjacencies = telomeres+adjs


        return sorted_adjacencies


    def find_next_extremity(self, current, next_extremity):
        if current[0] == next_extremity:
            if current[1] % 1 == 0:
                next = current[1] + 0.5
            else:
                next = current[1] - 0.5
        else:
            if current[0] % 1 == 0:
                next = current[0] + 0.5
            else:
                next = current[0] - 0.5
        return next

    def find_next_adjacency(self, next_extremity, chromosome, not_telomeres):
        for element in not_telomeres:
            if element[0] == next_extremity or element[1] == next_extremity:
                current = element
                chromosome.append(current)
                not_telomeres.remove(current)
                next_extremity = Extremities_and_adjacencies.find_next_extremity(self, current, next_extremity)
                return next_extremity, chromosome, not_telomeres
        return [next_extremity]

    def find_adjacency_cycle(self, next_extremity, chromosome, not_telomeres):


        next_adjacency = Extremities_and_adjacencies.find_next_adjacency(self, next_extremity, chromosome, not_telomeres)

        while len(next_adjacency) != 1:

            next_extremity = next_adjacency[0]
            next_adjacency = Extremities_and_adjacencies.find_next_adjacency(self, next_extremity, chromosome, not_telomeres)


        else:
            next_extremity = next_adjacency[0]

            return next_extremity, chromosome, not_telomeres

    def find_chromosomes(self, adjacencies):

        telomeres = [element for element in adjacencies if type(element) is not tuple]
        not_telomeres = [element for element in adjacencies if type(element) is tuple]

        linear_chromosomes = []
        circular_chromosomes = []
        chromosome = []
        i = 0

        # find linear chromosomes
        while len(telomeres) > 0:

            i += 1
            current = telomeres[0]

            telomeres.remove(current)
            chromosome.append(current)

            if current % 1 == 0:
                next_extremity = current + 0.5
            else:
                next_extremity = current - 0.5

            # if single gene chromosome
            if next_extremity in telomeres:
                current = next_extremity

                telomeres.remove(current)
                chromosome.append(current)
                linear_chromosomes.append(chromosome)
                chromosome = []

            # else find adjacency cycle
            else:
                adjacency_cycle = Extremities_and_adjacencies.find_adjacency_cycle(self, next_extremity, chromosome, not_telomeres)
                next_extremity = adjacency_cycle[0]

                if next_extremity in telomeres:
                    current = next_extremity
                    telomeres.remove(current)
                    chromosome.append(current)
                    linear_chromosomes.append(chromosome)
                    chromosome = []

        # find circular chromosomes
        while len(not_telomeres) > 0:
            current = not_telomeres[0]
            not_telomeres.remove(current)
            chromosome.append(current)

            # find next extremity:
            if current[0] % 1 == 0:
                next_extremity = current[0] + 0.5
            else:
                next_extremity = current[0] - 0.5

            # if it is a single gene chromosome:
            if next_extremity == current[1]:
                ordered_circular_chromosome = []

                circular_chromosomes.append(chromosome)
                chromosome = []

            # go find adjacency cycle
            else:
                adjacency_cycle = Extremities_and_adjacencies.find_adjacency_cycle(self, next_extremity, chromosome, not_telomeres)
                next_extremity = adjacency_cycle[0]

                # if at end of circular chromosome
                if next_extremity == chromosome[0][1]:
                    ordered_circular_chromosome =[]

                    circular_chromosomes.append(chromosome)
                    chromosome = []

        return linear_chromosomes, circular_chromosomes

    def adjacencies_to_genome(self, adjacencies):
        genome = []
        chromosomes = Extremities_and_adjacencies.find_chromosomes(self, adjacencies)
        linear_chromosomes = chromosomes[0]
        circular_chromosomes = chromosomes[1]

        for chromosome in linear_chromosomes:
            chr = []
            gene=0
            chromosome_length = len(chromosome)

            for i in range(0, chromosome_length-1):


                if i==0:
                    gene = chromosome[i]
                    if gene%1 == 0:
                        chr.append(int(gene))
                    else:
                        chr.append(-int(gene))


                else:

                    if int(gene) == int(chromosome[i][0]):

                        gene=chromosome[i][1]
                    else:
                        gene = chromosome[i][0]

                    if gene%1 == 0:
                        chr.append(int(gene))
                    else:
                        chr.append(-int(gene))


            genome.append(chr)


        for chromosome in circular_chromosomes:
            chr =[]
            gene = []
            chromosome_length = len(chromosome)

            chr.append('o')
            for i in range(0, chromosome_length):

                if i==0:
                    gene = chromosome[i][0]
                    if gene%1 == 0:
                        chr.append(int(gene))
                    else:
                        chr.append(-int(gene))

                else:
                    if int(gene) == int(chromosome[i][0]):

                        gene=chromosome[i][1]
                    else:
                        gene = chromosome[i][0]

                    if gene%1 == 0:
                        chr.append(int(gene))
                    else:
                        chr.append(-int(gene))

            genome.append(chr)

        return genome


