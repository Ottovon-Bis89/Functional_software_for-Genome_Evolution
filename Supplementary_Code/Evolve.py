
import random
from Genome_extremities_and_adjacencies import Extremities_and_adjacencies
import time

class Evolve:
    def __init__(self, target_genome):
        get_adjacencies_and_chromosomes = Extremities_and_adjacencies()
        self.state = get_adjacencies_and_chromosomes.create_adjacency_list(target_genome)
        # Track the highest gene number to handle insertions and duplications
        self.max_gene = max(abs(x) if isinstance(x, (int, float)) else max(abs(x[0]), abs(x[1])) for x in self.state)

        # self.max_gene = max([max(abs(x) if isinstance(x, int) else max(abs(x[0]), abs(x[1]))) 
        #                     for x in self.state])

    def evolve_with_random_rearrangements(self, number_of_rearrangements):
        rearrangements = ['inv', 'trp', 'b_trl', 'u_trl', 'fus', 'fis', 'ins', 'dele', 'dup']
        get_adjacencies_and_chromosomes = Extremities_and_adjacencies()
        rearrangement_series = []

        while number_of_rearrangements > 0:
            chromosomes = get_adjacencies_and_chromosomes.find_chromosomes(self.state)
            linear_chromosomes = chromosomes[0]
            
            if len(chromosomes[0]) < 2:
                if len(chromosomes[0][0]) < 5:
                    operation = random.choice(['inv', 'ins', 'dup'])
                else:
                    chr_lens = [len(x) for x in linear_chromosomes]
                    if max(chr_lens) < 4:
                        operation = random.choice(['inv', 'ins', 'dup'])
                    else:
                        operation = random.choice(['inv', 'trp', 'ins', 'dele', 'dup'])
            else:
                chr_lens = [len(x) for x in linear_chromosomes]
                chrm_longer_than_2_SB = [x for x in chr_lens if x > 3]
                chrm_longer_than_1_SB = [x for x in chr_lens if x > 2]

                if len(chrm_longer_than_2_SB) < 2:
                    if len(chrm_longer_than_1_SB) < 2:
                        if len(chrm_longer_than_1_SB) < 1:
                            operation = random.choice(['fus', 'ins', 'dup'])
                        else:
                            operation = random.choice(['inv', 'u_trl', 'fus', 'fis', 'ins', 'dele', 'dup'])
                    else:
                        operation = random.choice(['inv', 'b_trl', 'u_trl', 'fus', 'fis', 'ins', 'dele', 'dup'])
                else:
                    operation = random.choice(rearrangements)
            
            if operation == 'inv':
                execution = self.inversion(linear_chromosomes)
                #print('REACHES THIS POINT')
                rearrangement_series.append(execution)
                number_of_rearrangements -= 1
                #print('NUMBER OF REARRANGEMENTS after: ', number_of_rearrangements)

            elif operation == 'trp':
                execution = self.transposition(linear_chromosomes)
                for element in execution:
                    rearrangement_series.append(element)
                number_of_rearrangements -=1

            elif operation == 'b_trl':
                execution = self.balanced_translocation(linear_chromosomes)
                rearrangement_series.append(execution)
                number_of_rearrangements -=1

            elif operation == 'u_trl':
                execution = self.unbalanced_translocation(linear_chromosomes)
                rearrangement_series.append(execution)
                number_of_rearrangements -=1

            elif operation == 'fus':
                execution = self.fusion(linear_chromosomes)
                rearrangement_series.append(execution)
                number_of_rearrangements -=1

            elif operation == 'fis':
                execution = self.fission(linear_chromosomes)
                rearrangement_series.append(execution)
                number_of_rearrangements -=1

            elif operation == 'ins':
                execution = self.insertion(linear_chromosomes)
                rearrangement_series.append(execution)
                number_of_rearrangements -=1

            elif operation == 'dele':
                execution = self.deletion(linear_chromosomes)
                rearrangement_series.append(execution)
                number_of_rearrangements -=1

            elif operation == 'dup':
                execution = self.duplication(linear_chromosomes)
                rearrangement_series.append(execution)
                number_of_rearrangements -=1

        return rearrangement_series


    def evolve_with_set_rearrangments(self, target_genome, inv, trp, b_trl, u_trl, fus, fis, ins, dele, dup):
        pass

    def inversion(self, linear_chromosomes):
        get_adjacencies_and_chromosomes = Extremities_and_adjacencies()
        chromosome_number = random.randint(0, len(linear_chromosomes) - 1)
        chromosome = linear_chromosomes[chromosome_number]
        chromosome_length = len(chromosome)
        to_exclude = []

        while chromosome_length < 3:
            to_exclude.append(linear_chromosomes.index(chromosome))
            chromosome_number = random.choice([i for i in range(0, len(linear_chromosomes)) if i not in to_exclude])
            chromosome = linear_chromosomes[chromosome_number]
            chromosome_length = len(chromosome)

        if chromosome_length == 3:
            adjacencies = [element for element in chromosome if type(element) is tuple]
            telomeres = [element for element in chromosome if type(element) is not tuple]

            adj = adjacencies[0]
            telo = random.choice(telomeres)
            if int(telo) == int(adj[0]):
                if telo < adj[1]:
                    new_adj = (telo, adj[1])
                else:
                    new_adj = (adj[1], telo)
                new_telo = adj[0]
            else:
                if telo < adj[0]:
                    new_adj = (telo, adj[0])
                else:
                    new_adj = (adj[0], telo)
                new_telo = adj[1]

            operationA = (adj, telo)
            operationB = (new_adj, new_telo)

            self.state.remove(adj)
            self.state.remove(telo)
            self.state.append(new_adj)
            self.state.append(new_telo)

            operation = (operationA, operationB, 'inv')
            intermediate = self.state
        else:
            try:
                adjacencies = [element for element in chromosome if type(element) is tuple]
            except:
                print('There were not any chromosomes with more than 2 sequence blocks')

            adj1_num = random.randint(0, len(adjacencies) - 1)
            adj2_num = random.randint(0, len(adjacencies) - 1)

            while adj1_num == adj2_num:
                adj2_num = random.randint(0, len(adjacencies) - 1)

            adj1 = adjacencies[adj1_num]
            adj2 = adjacencies[adj2_num]

            if adj1[0] < adj2[0]:
                new_adj1 = (adj1[0], adj2[0])
            else:
                new_adj1 = (adj2[0], adj1[0])

            if adj1[1] < adj2[1]:
                new_adj2 = (adj1[1], adj2[1])
            else:
                new_adj2 = (adj2[1], adj1[1])

            self.state.remove(adj1)
            self.state.remove(adj2)
            self.state.append(new_adj1)
            self.state.append(new_adj2)

            chromosomes = get_adjacencies_and_chromosomes.find_chromosomes(self.state)
            if len(chromosomes[1]) != 0:
                self.state.append(adj1)
                self.state.append(adj2)
                self.state.remove(new_adj1)
                self.state.remove(new_adj2)

                if adj1[0] < adj2[1]:
                    new_adj1 = (adj1[0], adj2[1])
                else:
                    new_adj1 = (adj2[1], adj1[0])

                if adj1[1] < adj2[0]:
                    new_adj2 = (adj1[1], adj2[0])
                else:
                    new_adj2 = (adj2[0], adj1[1])

                self.state.remove(adj1)
                self.state.remove(adj2)
                self.state.append(new_adj1)
                self.state.append(new_adj2)

            if adj1[0] < adj2[0]:
                operationA = (adj1, adj2)
            else:
                operationA = (adj2, adj1)

            if new_adj1[0] < new_adj2[0]:
                operationB = (new_adj1, new_adj2)
            else:
                operationB = (new_adj2, new_adj1)

            operation = ((operationA, operationB), 'inv')
            intermediate = self.state[:]

        return (operation, intermediate)

    def transposition(self, linear_chromosomes):
        get_adjacencies_and_chromosomes = Extremities_and_adjacencies()
        chromosome_number = random.randint(0, len(linear_chromosomes) - 1)
        chromosome = linear_chromosomes[chromosome_number]
        chromosome_length = len(chromosome)
        to_exclude = []

        while chromosome_length < 4:
            to_exclude.append(linear_chromosomes.index(chromosome))
            chromosome_number = random.choice([i for i in range(0, len(linear_chromosomes)) if i not in to_exclude])
            chromosome = linear_chromosomes[chromosome_number]
            chromosome_length = len(chromosome)

        try:
            adjacencies = [element for element in chromosome if type(element) is tuple]
        except:
            print('There were not any chromosomes with more than 2 sequence blocks')

        adj1_num = random.randint(0, len(adjacencies) - 1)
        adj2_num = random.randint(0, len(adjacencies) - 1)

        while adj1_num == adj2_num:
            adj2_num = random.randint(0, len(adjacencies) - 1)

        adj1 = adjacencies[adj1_num]
        adj2 = adjacencies[adj2_num]

        if adj1[0] < adj2[0]:
            new_adj1 = (adj1[0], adj2[0])
        else:
            new_adj1 = (adj2[0], adj1[0])

        if adj1[1] < adj2[1]:
            new_adj2 = (adj1[1], adj2[1])
        else:
            new_adj2 = (adj2[1], adj1[1])

        self.state.remove(adj1)
        self.state.remove(adj2)
        self.state.append(new_adj1)
        self.state.append(new_adj2)

        chromosomes = get_adjacencies_and_chromosomes.find_chromosomes(self.state)
        if len(chromosomes[1]) == 0:
            self.state.append(adj1)
            self.state.append(adj2)
            self.state.remove(new_adj1)
            self.state.remove(new_adj2)

            if adj1[0] < adj2[1]:
                new_adj1 = (adj1[0], adj2[1])
            else:
                new_adj1 = (adj2[1], adj1[0])

            if adj1[1] < adj2[0]:
                new_adj2 = (adj1[1], adj2[0])
            else:
                new_adj2 = (adj2[0], adj1[1])

            self.state.remove(adj1)
            self.state.remove(adj2)
            self.state.append(new_adj1)
            self.state.append(new_adj2)

        if adj1[0] < adj2[0]:
            operationA = (adj1, adj2)
        else:
            operationA = (adj2, adj1)

        if new_adj1[0] < new_adj2[0]:
            operationB = (new_adj1, new_adj2)
        else:
            operationB = (new_adj2, new_adj1)

        chromosomes = get_adjacencies_and_chromosomes.find_chromosomes(self.state)
        if new_adj1 in chromosomes[1][0]:
            circular_adjacency = new_adj1
            excision_adjacency = new_adj2
        else:
            circular_adjacency = new_adj2
            excision_adjacency = new_adj1

        operation1 = ((operationA, operationB), 'trp0')
        intermediate1 = self.state[:]

        adj1 = circular_adjacency
        adj2 = excision_adjacency

        counter = 0
        while adj2 == excision_adjacency:
            if counter > 2:
                adj2 = chromosomes[0][0][0]
            else:
                chromosome_number = random.randint(0, len(chromosomes[0]) - 1)
                chromosome = chromosomes[0][chromosome_number]
                chromosome_length = len(chromosome)
                to_exclude = []
                while chromosome_length < 3:
                    to_exclude.append(linear_chromosomes.index(chromosome))
                    chromosome_number = random.choice([i for i in range(0, len(linear_chromosomes)) if i not in to_exclude])
                    chromosome = chromosomes[0][chromosome_number]
                    chromosome_length = len(chromosome)

                adjacencies = [element for element in chromosome if type(element) is tuple]
                adj2_num = random.randint(0, len(adjacencies) - 1)
                adj2 = adjacencies[adj2_num]
                counter += 1

        if type(adj2) is not tuple:
            if adj1[0] < adj2:
                new_adj1 = (adj1[0], adj2)
            else:
                new_adj1 = (adj2, adj1[0])
            new_adj2 = adj1[1]

            self.state.remove(adj1)
            self.state.remove(adj2)
            self.state.append(new_adj1)
            self.state.append(new_adj2)

            if adj1[0] < adj2:
                operationA = (adj1, adj2)
            else:
                operationA = (adj2, adj1)

            if new_adj1[0] < new_adj2:
                operationB = (new_adj1, new_adj2)
            else:
                operationB = (new_adj2, new_adj1)

            operation2 = ((operationA, operationB), 'trp1')
            intermediate2 = self.state[:]
        else:
            if adj1[0] < adj2[0]:
                new_adj1 = (adj1[0], adj2[0])
            else:
                new_adj1 = (adj2[0], adj1[0])

            if adj1[1] < adj2[1]:
                new_adj2 = (adj1[1], adj2[1])
            else:
                new_adj2 = (adj2[1], adj1[1])

            self.state.remove(adj1)
            self.state.remove(adj2)
            self.state.append(new_adj1)
            self.state.append(new_adj2)

            if adj1[0] < adj2[0]:
                operationA = (adj1, adj2)
            else:
                operationA = (adj2, adj1)

            if new_adj1[0] < new_adj2[0]:
                operationB = (new_adj1, new_adj2)
            else:
                operationB = (new_adj2, new_adj1)

            operation2 = ((operationA, operationB), 'trp1')
            intermediate2 = self.state[:]

        return [(operation1, intermediate1), (operation2, intermediate2)]

    def balanced_translocation(self, linear_chromosomes):
        chromosome1_number = random.randint(0, len(linear_chromosomes)-1)
        chromosome1 = linear_chromosomes[chromosome1_number]
        chromosome1_length = len(chromosome1)
        to_exclude = []

        while chromosome1_length < 3:
            to_exclude.append(linear_chromosomes.index(chromosome1))
        
            chromosome1_number = random.choice([i for i in range(0, len(linear_chromosomes)) if i not in to_exclude])
            chromosome1 = linear_chromosomes[chromosome1_number]
            chromosome1_length = len(chromosome1)

        try:
            chromosome2_number = chromosome1_number
        except:
            print('There were not any non-single sequence block chromosomes')

        to_exclude = []

        while chromosome2_number == chromosome1_number:
            to_exclude.append(chromosome2_number)
            chromosome2_number = random.randint(0, len(linear_chromosomes)-1)
            chromosome2 = linear_chromosomes[chromosome2_number]
            chromosome2_length = len(chromosome2)


            while chromosome2_length < 3:

                to_exclude.append(linear_chromosomes.index(chromosome2))
             
                chromosome2_number = random.choice([i for i in range(0, len(linear_chromosomes)) if i not in to_exclude])
                chromosome2 = linear_chromosomes[chromosome2_number]
                chromosome2_length = len(chromosome2)


        try:
            adjacencies1 = [element for element in chromosome1 if type(element) is tuple]
            adjacencies2 = [element for element in chromosome2 if type(element) is tuple]
        except:
            print('There were not any non-single sequence block chromosomes')

        adj1_num = random.randint(0, len(adjacencies1) - 1)
        adj2_num = random.randint(0, len(adjacencies2) - 1)

        adj1 = adjacencies1[adj1_num]
        adj2 = adjacencies2[adj2_num]

        # order extremities in the adjacency tuple
        if adj1[0] < adj2[1]:
            new_adj1 = (adj1[0], adj2[1])
        else:
            new_adj1 = (adj2[1], adj1[0])

        if adj1[1] < adj2[0]:
            new_adj2 = (adj1[1], adj2[0])
        else:
            new_adj2 = (adj2[0], adj1[1])


        # perfrom operation
        self.state.remove(adj1)
        self.state.remove(adj2)
        self.state.append(new_adj1)
        self.state.append(new_adj2)

        if adj1[0] < adj2[0]:
            operationA = (adj1, adj2)
        else:
            operationA = (adj2, adj1)

        if new_adj1[0] < new_adj2[0]:
            operationB = (new_adj1, new_adj2)
        else:
            operationB = (new_adj2, new_adj1)

        operation = ((operationA, operationB), 'b_trl')
        intermediate = self.state[:]

        return (operation, intermediate)

    def unbalanced_translocation(self, linear_chromosomes):  # linear_chromosomes

        chromosome1_number = random.randint(0, len(linear_chromosomes)-1)
        chromosome1 = linear_chromosomes[chromosome1_number]
        chromosome1_length = len(chromosome1)
        to_exclude =[]

        while chromosome1_length < 3:
            to_exclude.append(linear_chromosomes.index(chromosome1))
         
            chromosome1_number = random.choice([i for i in range(0, len(linear_chromosomes)) if i not in to_exclude])

            chromosome1 = linear_chromosomes[chromosome1_number]
            chromosome1_length = len(chromosome1)

        try:
            chromosome2_number = chromosome1_number
        except:
            print('There were not any non-single sequence block chromosomes')

        to_exclude = []
        while chromosome2_number == chromosome1_number:
            to_exclude.append(chromosome2_number)
        
            chromosome2_number = random.choice([i for i in range(0, len(linear_chromosomes)) if i not in to_exclude])

        chromosome2 = linear_chromosomes[chromosome2_number]

        adjacencies = [element for element in chromosome1 if type(element) is tuple]
        telomeres = [element for element in chromosome2 if type(element) is not tuple]

        adj_num = random.randint(0, len(adjacencies) - 1)
        telo_num = random.randint(0, 1)

        adj = adjacencies[adj_num]
        telo = telomeres[telo_num]

        # order extremities in the adjacency tuple
        if adj[0] < telo:
            new_adj = (adj[0], telo)
        else:
            new_adj = (telo, adj[0])

        new_telo = adj[1]


        # perfrom operation
        self.state.remove(adj)
        self.state.remove(telo)
        self.state.append(new_adj)
        self.state.append(new_telo)

        operationA = (adj, telo)
        operationB = (new_adj, new_telo)

        operation = ((operationA, operationB), 'u_trl')
        intermediate = self.state[:]

        return (operation, intermediate)

    def fusion(self, linear_chromosomes):

        chromosome1_number = random.randint(0, len(linear_chromosomes)-1)
        chromosome1 = linear_chromosomes[chromosome1_number]

        chromosome2_number = chromosome1_number
        to_exclude = []
        while chromosome2_number == chromosome1_number:

            to_exclude.append(chromosome2_number)
        
            chromosome2_number = random.choice([i for i in range(0, len(linear_chromosomes)) if i not in to_exclude])


        chromosome2 = linear_chromosomes[chromosome2_number]


        telomeres1 = [element for element in chromosome1 if type(element) is not tuple]
        telomeres2 = [element for element in chromosome2 if type(element) is not tuple]

        telo1_num = random.randint(0, 1)
        telo2_num = random.randint(0, 1)

        telo1 = telomeres1[telo1_num]
        telo2 = telomeres2[telo2_num]

        # order extremities in the adjacency tuple
        if telo1 < telo2:
            new_adj = (telo1, telo2)
            operation = ((telo1, telo2, new_adj),'fus')
        else:
            new_adj = (telo2, telo1)
            operation = ((telo2, telo1, new_adj), 'fus')

        # perfrom operation
        self.state.remove(telo1)
        self.state.remove(telo2)
        self.state.append(new_adj)

        intermediate = self.state[:]

        return (operation, intermediate)

    def fission(self, linear_chromosomes):  # linear_chromosomes

        chromosome_number = random.randint(0, len(linear_chromosomes)-1)
        chromosome = linear_chromosomes[chromosome_number]
        chromosome_length = len(chromosome)
        to_exclude = []
        while chromosome_length < 3:
            to_exclude.append(linear_chromosomes.index(chromosome))
         
            chromosome_number = random.choice([i for i in range(0, len(linear_chromosomes)) if i not in to_exclude])
            chromosome = linear_chromosomes[chromosome_number]
            chromosome_length = len(chromosome)


        adjacencies = [element for element in chromosome if type(element) is tuple]
        adj_num = random.randint(0, len(adjacencies) - 1)
        adj = adjacencies[adj_num]

        new_telo1 = adj[0]
        new_telo2 = adj[1]

        # perfrom operation
        self.state.remove(adj)
        self.state.append(new_telo1)
        self.state.append(new_telo2)

        operation = ((adj, new_telo1, new_telo2), 'fis')
        intermediate = self.state[:]

        return (operation, intermediate)
    
    def insertion(self, linear_chromosomes):
        """Insert a new gene into the genome"""
        # Create new gene number
        new_gene = self.max_gene + 1
        self.max_gene = new_gene

        # Select random chromosome and position
        chromosome_number = random.randint(0, len(linear_chromosomes) - 1)
        chromosome = linear_chromosomes[chromosome_number]
        
        # Select random insertion point
        if len(chromosome) <= 2:  # Single gene chromosome
            insert_at_telomere = True
            telomere = random.choice([x for x in chromosome if isinstance(x, int)])
        else:
            insert_at_telomere = random.choice([True, False])
            if insert_at_telomere:
                telomere = random.choice([x for x in chromosome if isinstance(x, int)])
            else:
                adjacency = random.choice([x for x in chromosome if isinstance(x, tuple)])

        # Perform insertion
        if insert_at_telomere:
            if telomere < 0:  # Left end
                new_adj = (-new_gene, telomere)
                new_telo = new_gene
            else:  # Right end
                new_adj = (telomere, new_gene)
                new_telo = -new_gene
            
            self.state.remove(telomere)
            self.state.append(new_adj)
            self.state.append(new_telo)
            
            operation = ((telomere, (new_adj, new_telo)), 'ins')
        else:
            # Insert between two genes
            if random.random() < 0.5:
                new_adj1 = (adjacency[0], new_gene)
                new_adj2 = (-new_gene, adjacency[1])
            else:
                new_adj1 = (adjacency[0], -new_gene)
                new_adj2 = (new_gene, adjacency[1])
            
            self.state.remove(adjacency)
            self.state.append(new_adj1)
            self.state.append(new_adj2)
            
            operation = ((adjacency, (new_adj1, new_adj2)), 'ins')

        intermediate = self.state[:]

        return (operation, intermediate)

    def deletion(self, linear_chromosomes):
        """Delete a gene from the genome"""
        # Select chromosome with more than one gene
        valid_chromosomes = [c for c in linear_chromosomes if len(c) > 2]
        if not valid_chromosomes:
            return self.insertion(linear_chromosomes)  # Fallback if no valid chromosomes
        
        chromosome = random.choice(valid_chromosomes)
        
        # Find gene to delete (avoiding telomeres)
        internal_genes = set()
        for adj in chromosome:
            if isinstance(adj, tuple):
                internal_genes.add(abs(adj[0]))
                internal_genes.add(abs(adj[1]))
        
        if not internal_genes:
            return self.insertion(linear_chromosomes)
        
        gene_to_delete = random.choice(list(internal_genes))
        
        # Find adjacencies containing the gene
        adj_to_remove = []
        for adj in self.state:
            if isinstance(adj, tuple):
                if abs(adj[0]) == gene_to_delete or abs(adj[1]) == gene_to_delete:
                    adj_to_remove.append(adj)
        
        if len(adj_to_remove) != 2:
            return self.insertion(linear_chromosomes)
        
        # Create new adjacency
        remaining_ends = []
        for adj in adj_to_remove:
            if abs(adj[0]) == gene_to_delete:
                remaining_ends.append(adj[1])
            else:
                remaining_ends.append(adj[0])
        
        if remaining_ends[0] < remaining_ends[1]:
            new_adj = (remaining_ends[0], remaining_ends[1])
        else:
            new_adj = (remaining_ends[1], remaining_ends[0])
        
        # Perform deletion
        for adj in adj_to_remove:
            self.state.remove(adj)
        self.state.append(new_adj)
        
        operation = ((adj_to_remove[0], adj_to_remove[1], new_adj), 'dele')
        intermediate = self.state[:]

        return (operation, intermediate)

    def duplication(self, linear_chromosomes):
        """Duplicate a gene in the genome"""
        # Select random chromosome and gene to duplicate
        chromosome_number = random.randint(0, len(linear_chromosomes) - 1)
        chromosome = linear_chromosomes[chromosome_number]
        
        # Get all genes in chromosome
        genes = set()
        for element in chromosome:
            if isinstance(element, tuple):
                genes.add(abs(element[0]))
                genes.add(abs(element[1]))
            else:
                genes.add(abs(element))
        
        if not genes:
            return self.insertion(linear_chromosomes)
        
        gene_to_duplicate = random.choice(list(genes))
        new_gene = self.max_gene + 1
        self.max_gene = new_gene
        
        # Find adjacencies containing the gene
        adj_with_gene = []
        for adj in self.state:
            if isinstance(adj, tuple):
                if abs(adj[0]) == gene_to_duplicate or abs(adj[1]) == gene_to_duplicate:
                    adj_with_gene.append(adj)
        
        # Duplicate after the gene
        if len(adj_with_gene) == 2:  # Internal gene
            # Find the adjacency where the gene is the first element
            for adj in adj_with_gene:
                if abs(adj[0]) == gene_to_duplicate:
                    target_adj = adj
                    break
            else:
                target_adj = adj_with_gene[0]
            
            # Create new adjacencies
            if target_adj[0] < 0:
                new_adj1 = (target_adj[0], -new_gene)
                new_adj2 = (new_gene, target_adj[1])
            else:
                new_adj1 = (target_adj[0], new_gene)
                new_adj2 = (-new_gene, target_adj[1])
            
            # Perform duplication
            self.state.remove(target_adj)
            self.state.append(new_adj1)
            self.state.append(new_adj2)
            
            operation = ((target_adj, (new_adj1, new_adj2)), 'dup')
        else:  # Telomeric gene
            telomere = next(x for x in chromosome if isinstance(x, int) and abs(x) == gene_to_duplicate)
            if telomere < 0:
                new_adj = (-new_gene, telomere)
                new_telo = new_gene
            else:
                new_adj = (telomere, new_gene)
                new_telo = -new_gene
            
            self.state.remove(telomere)
            self.state.append(new_adj)
            self.state.append(new_telo)
            
            operation = ((telomere, (new_adj, new_telo)), 'dup')
        
        intermediate = self.state[:]

        return (operation, intermediate)


