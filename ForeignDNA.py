from random import randint

class Foreign_DNA:

    def __init__(self):
        self.state = []


    
    def foreign_dna_pool(self, source, target):
        """
        The function finds the difference in genes between the source and target genomes. These genes are added to a pool of random integers and foreign DNA fragments
        are created out of the pool of integers. The fragments are tagged with an underscore(_) to them indentiable in the source genome and also for them to be 
        ignored by the delete function in the transformation process.
        """
        # Check what genes are in target genome but not in source genome. Those genes are needed to create a foreign DNA pool 
        # with fragments that are similar to the two genomes 
        source_genome = []
        target_genome = []

        # create master lists

        for chromosome in source:
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
        
        for chromosome in target:
            for i in range(len(chromosome)):
                if isinstance(chromosome[i],int):
                    target_genome.append(int(chromosome[i]))

        # Find the difference between source genome and target genome
        difference = list(set(target_genome) - set(source_genome))

        if len(difference) > 0:
            # define the ratio (1/5)
            number_of_random_ints = (len(difference) * 3) - (len(difference))  #ratio can be changed here, the ratio is the number of genes to number of random integers in foreign dna fragment. Maximum should be five (5)

            # create foreign dna
            foreign_dna = []
            count = 0
            while count < (number_of_random_ints):
                gene = randint(1, 40)
                if len(foreign_dna) >= 1:
                    if gene not in foreign_dna:
                        foreign_dna.append(gene)
                        count += 1
                else:
                    foreign_dna.append(gene)

            # add difference to foreign dna and check duplicates and add foreign DNA if necessary
            foreign_dna = difference + foreign_dna
            foreign_dna = list(set(foreign_dna))
            if len(foreign_dna) < ((len(difference)) * 3):  #ratio can be changed here, the ratio is the number of genes to number of random integers in foreign dna fragment. Maximum should be five (5)
                count = len(foreign_dna)
                while (len(foreign_dna) < ((len(difference)) * 3)):
                    gene = randint(1, 40)
                    if gene not in foreign_dna:
                        foreign_dna.append(gene)
                        count += 1
            
            #Use foreign_dna list that was created to create foreign dna fragments (random number of fragment and random length of fragments)
            number_of_fragments = randint(1,50)
            len_fragments = 1
            
            #choose randomly from foreign_dna list to add to frags
            list_of_fragments = []
            fragment = []
            for j in range(number_of_fragments):
                for i in range(len_fragments):
                    choice = randint(0,len(foreign_dna)-1)
                    fragment.append(foreign_dna[choice])
                #Ensure unique fragments in list
                if j > 0 and fragment not in list_of_fragments:
                    list_of_fragments.append(fragment)
                else:
                    j -= 1
                fragment = []

            #Check for the difference in genes within at least one fragment in list
            check = True
            for f in list_of_fragments:
                if difference in f:
                    check = False
            if check == True:
                final_fragment = difference[:]
            #add a fragment that does contain the difference
            #Check that the gene does not already exist in the fragment
                while len(final_fragment) <= len(difference)+1:
                    selected_gene =  foreign_dna[randint(0, len(foreign_dna)-1)]
                    if selected_gene not in final_fragment:
                        final_fragment.append(selected_gene)
                list_of_fragments.append(final_fragment)

            #Tag foreign DNA with underscore(_) so that it can easily be identified and te delete function to ignore them
            for i in list_of_fragments:
                fragment = i
                for j in range(len(fragment)):
                    fragment[j] = str(fragment[j])+"_"
            return list_of_fragments

        else:
            # define the ratio (1/5)
            number_of_random_ints = randint(1,5)

            # create foreign dna
            foreign_dna = []
            count = 0
            while count < (number_of_random_ints):
                gene = randint(1, 40)
                if len(foreign_dna) >= 1:
                    if gene not in foreign_dna:
                        foreign_dna.append(gene)
                        count += 1
                else:
                    foreign_dna.append(gene)
            
            #Use foreign_dna list that was created to create foreign dna fragments (random number of frag and random length of fragments)
            number_of_fragments = randint(1,50)
            len_fragments = 1
            #choose randomly from foreign_dna list to add to frags
            list_of_fragments = []
            fragment = []
            for j in range(number_of_fragments):
                for i in range(len_fragments):
                    choice = randint(0,len(foreign_dna)-1)
                    fragment.append(foreign_dna[choice])
                #Ensure unique fragments in list
                if j > 0 and fragment not in list_of_fragments:
                    list_of_fragments.append(fragment)
                else:
                    j -= 1
                fragment = []

            #Tag foreign DNA with underscore
            for i in list_of_fragments:
                fragment = i
                for j in range(len(fragment)):
                    fragment[j] = str(fragment[j])+"_"

            return list_of_fragments
    

    
    def insert_foreign_dna(self, source_genome, fragment):
        """
        This function adds/insert a fragment of foreign DNA to the Source genome. The foreign fragment can be identified with an underscore(_) attached to an integer. 
        The path of foreign DNA fragment can be followed through the evolutionary journey of the source genome into 
        the target genome
        """
        # Count number of applicable intergenic regions to associate to number of mutations
        list_of_mutation_points = []
        list_of_mutation_points_genome = []

        for genes_with_intergenic_approved in source_genome:
            for i in range(len(genes_with_intergenic_approved)):
                if (isinstance(genes_with_intergenic_approved[i], str) and len(genes_with_intergenic_approved[i]) > 1) and '*' in genes_with_intergenic_approved[i]:
                    list_of_mutation_points.append(i+1)

            list_of_mutation_points_genome.append(list_of_mutation_points)
            list_of_mutation_points = []
        
        #insert intergenic regions in foreign dna fragments 
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

        #find applicable intergenic regions in fragment
        for i in range(len(fragment_with_intergenic_regions)):
            if i % 2 == 0 or i == 0:
                region = fragment_with_intergenic_regions[i]
               
                if len(region) > 2:
                    # print("lltr: ", len(region))
                    value = region[1]+region[2]
                else:
                    value = region[1]
                if int(value) < 5:
                    fragment_with_intergenic_regions[i] = '*'


        # Account for chromosomes without intergenic regions
        position_applicable_region_chromosome = []
        source_chromosome = []
        rand_chromosome = []

        while len(position_applicable_region_chromosome) == 0 :
            rand_chromosome = randint(0,len(list_of_mutation_points_genome)-1)
            position_applicable_region_chromosome = list_of_mutation_points_genome[rand_chromosome]
            source_chromosome = source_genome[rand_chromosome]
        
        #randomly pick a position from position of applicable region in the chromsome to position

        rand_position = randint(0, len(position_applicable_region_chromosome)-1)
        position = position_applicable_region_chromosome[rand_position]

        mutated = []
        if position == 0:  # Insert at the beginning
            mutated = fragment_with_intergenic_regions + source_chromosome
        else:  # Insert at the ending
            mutated = source_chromosome + fragment_with_intergenic_regions

        source_genome[rand_chromosome] = mutated
        return source_genome,  ['F_DNA',rand_chromosome, position, fragment_with_intergenic_regions, mutated]


    


