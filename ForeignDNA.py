from random import randint

class Foreign_DNA:

    def __init__(self):
        self.state = []


    
    def foreign_dna_pool(self, source_genome, target_genome):
        
        """
        Finds the difference in genes between the source and target genomes. Creates a pool of random integers and
        generates foreign DNA fragments from the pool. Fragments are tagged with an underscore(_) for identification
        in the source genome and to be ignored by the delete function during the transformation process.
        
        :param source: The source genome.
        :param target: The target genome.
        :return: A list of foreign DNA fragments.
        """
       
        source_genome = []
        target_genome = []


        for chromosome in source_genome:
            for i in range(len(chromosome)):
                if isinstance(chromosome[i],int):
                    source_genome.append(int(chromosome[i]))
                elif isinstance(chromosome[i],str) and "_" in chromosome[i]:
                    if len(chromosome[i])==2:
                        gene = chromosome[i]
                        source_genome.append(int(gene[:1]))
                    elif len(chromosome[i])==3:
                        gene = chromosome[i]
                        source_genome.append(int(gene[:2]))
        
        for chromosome in target_genome:
            for i in range(len(chromosome)):
                if isinstance(chromosome[i],int):
                    target_genome.append(int(chromosome[i]))

       
        difference = list(set(target_genome) - set(source_genome))

        if len(difference) > 0:
            # define the ratio (1/5)
            number_of_random_ints = (len(difference) * 2) - (len(difference))  #ratio can be changed here, the ratio is the number of genes to number of random integers in foreign dna fragment.
            
            foreign_dna = []
            count = 0
            while count < (number_of_random_ints):
                gene = randint(1, 25)
                if len(foreign_dna) >= 1:
                    if gene not in foreign_dna:
                        foreign_dna.append(gene)
                        count += 1
                else:
                    foreign_dna.append(gene)

           
            foreign_dna = difference + foreign_dna
            foreign_dna = list(set(foreign_dna))
            if len(foreign_dna) < ((len(difference)) * 2):  
                count = len(foreign_dna)
                while (len(foreign_dna) < ((len(difference)) * 2)):
                    gene = randint(1, 25)
                    if gene not in foreign_dna:
                        foreign_dna.append(gene)
                        count += 1
            
            number_of_fragments = randint(1,5)
            len_fragments = 1
            
           
            list_of_fragments = []
            fragment = []
            for j in range(number_of_fragments):
                for i in range(len_fragments):
                    choice = randint(0,len(foreign_dna)-1)
                    fragment.append(foreign_dna[choice])
               
                if j > 0 and fragment not in list_of_fragments:
                    list_of_fragments.append(fragment)
                else:
                    j -= 1
                fragment = []

            check = True
            for fragmt in list_of_fragments:
                if difference in fragmt:
                    check = False
            if check == True:
                final_fragment = difference[:]
           
                while len(final_fragment) <= len(difference)+1:
                    selected_gene =  foreign_dna[randint(0, len(foreign_dna)-1)]
                    if selected_gene not in final_fragment:
                        final_fragment.append(selected_gene)
                list_of_fragments.append(final_fragment)

            for i in list_of_fragments:
                fragment = i
                for j in range(len(fragment)):
                    fragment[j] = str(fragment[j])+"_"
            return list_of_fragments

        else:
           
            number_of_random_ints = randint(1,5)

            
            foreign_dna = []
            count = 0
            while count < (number_of_random_ints):
                gene = randint(1, 25)
                if len(foreign_dna) >= 1:
                    if gene not in foreign_dna:
                        foreign_dna.append(gene)
                        count += 1
                else:
                    foreign_dna.append(gene)
            
            number_of_fragments = randint(1,5)
            len_fragments = 1
            list_of_fragments = []
            fragment = []
            for j in range(number_of_fragments):
                for i in range(len_fragments):
                    choice = randint(0,len(foreign_dna)-1)
                    fragment.append(foreign_dna[choice])
                
                if j > 0 and fragment not in list_of_fragments:
                    list_of_fragments.append(fragment)
                   
                else:
                    j -= 1
                fragment = []

            for i in list_of_fragments:
                fragment = i
                for j in range(len(fragment)):
                    fragment[j] = str(fragment[j])+"_"

            return list_of_fragments
    

    
    def insert_foreign_dna(self, source_genome, fragment):
        """
        Adds/inserts a fragment of foreign DNA to the source genome. The foreign fragment is identified with an
        underscore(_) attached to an integer. The path of foreign DNA fragments can be traced through the evolutionary
        journey of the source genome into the target genome.
        
        :param source_genome: The source genome.
        :param fragment: The foreign DNA fragment to insert.
        :return: The updated source genome and information about the insertion.
        """
        list_of_mutation_points = []
        list_of_mutation_points_genome = []

        for genes_with_intergenic_approved in source_genome:
            for i in range(len(genes_with_intergenic_approved)):
                if (isinstance(genes_with_intergenic_approved[i], str) and len(genes_with_intergenic_approved[i]) > 1) and '*' in genes_with_intergenic_approved[i]:
                    list_of_mutation_points.append(i+1)

            list_of_mutation_points_genome.append(list_of_mutation_points)
            list_of_mutation_points = []
        
        fragment_with_intergenic_regions = []
        length = len(fragment)
        for j in range(len(fragment)):
            if j == 0 :
                random_bp = randint(6,10)
                region = '*' + str(random_bp)
                fragment_with_intergenic_regions.append(region)
            random_bp = randint(6,10)
            start = fragment[j]
            region = '*' + str(random_bp)
            fragment_with_intergenic_regions.append(start)
            if j != length-1:
                fragment_with_intergenic_regions.append(region)

        
        for i in range(len(fragment_with_intergenic_regions)):
            if i % 2 == 0 or i == 0:
                region = fragment_with_intergenic_regions[i]
               
                if len(region) > 2:
                    value = region[1]+region[2]
                else:
                    value = region[1]
                if int(value) < 5:
                    fragment_with_intergenic_regions[i] = '*'


        position_applicable_region_chromosome = []
        source_chromosome = []
        rand_chromosome = []

        while len(position_applicable_region_chromosome) == 0 :
            rand_chromosome = randint(0,len(list_of_mutation_points_genome)-1)
            position_applicable_region_chromosome = list_of_mutation_points_genome[rand_chromosome]
            source_chromosome = source_genome[rand_chromosome]
        

        rand_position = randint(0, len(position_applicable_region_chromosome)-1)
        position = position_applicable_region_chromosome[rand_position]

        mutated = []
        if position == 0: 
            mutated = fragment_with_intergenic_regions + source_chromosome
        else:  
            mutated = source_chromosome + fragment_with_intergenic_regions

        source_genome[rand_chromosome] = mutated
        return source_genome,  ['F_DNA',rand_chromosome, position, fragment_with_intergenic_regions, mutated]


    


