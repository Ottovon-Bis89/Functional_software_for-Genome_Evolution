from random import randint

class Gen_API:

    def insert_Integenic_Regions(self, source_genome):
        clean_chrom = []
        count_app = 0

        for chromosome in source_genome:
            for i in range(len(chromosome)):
                if "*" in chromosome[i] and len(chromosome[i]) > 1:
                    count_app += 1
                else:
                    clean_chrom.append(chromosome[i])

        new_source_genome = self.generate_integenic_regions(clean_chrom)

        return new_source_genome

    def getIndex(self, int_list, num):
        count = 0
        for i, n in enumerate(int_list):
            if n == num:
                count += 1
            if count == 2:
                return i
        else:
            return 0

    def deletion(self, source_chromosome, position_app_region):
        position_a = False
        position_b = False
        deletion_region = source_chromosome[position_app_region]
        new_source_chromosome = []

        if "_" not in deletion_region:
            position_a = True
            if position_app_region > 0 and source_chromosome[position_app_region-1] == deletion_region:
                position_b = True

        if position_a and position_b:
            for i in range(0, position_app_region-1):
                new_source_chromosome.append(source_chromosome[i])
            for i in range(position_app_region+1, len(source_chromosome)):
                new_source_chromosome.append(source_chromosome[i])
        elif position_a:
            for i in range(0, position_app_region):
                new_source_chromosome.append(source_chromosome[i])
            for i in range(position_app_region+1, len(source_chromosome)):
                new_source_chromosome.append(source_chromosome[i])

        return new_source_chromosome

    def duplication(self, source_chromosome, gene, insertion_position):

        source_chromosome[insertion_position-1] = gene

        return source_chromosome

    def insertion(self, source_chromosome, position_app_region, gene):

        source_chromosome[position_app_region-1] = gene

        return source_chromosome

    def pick_mutation(self, duplication_genome, out_genome, in_genome):
        do_mutation = ()
        mutations = []
        if any(duplication_genome):
            mutations.append('dup')
        if any(out_genome):
            mutations.append('del')
        if any(in_genome):
            mutations.append('insert')

        pick = mutations[randint(0, len(mutations)-1)]
        for i in range(len(in_genome)):
            chromosome = in_genome[i]
            if chromosome != []:
                picker = randint(0, len(chromosome)-1)
                do_mutation = (pick, i, chromosome[picker])
                break

        return do_mutation

    def generate_integenic_regions(self, source_genome):
        new_source_genome = [[] * 1 for i in range(len(source_genome))]

        j = 0
        for index in source_genome:
            value = 0
            while value < (len(index)):
                random_bp = randint(6, 10)

                if not '*' in source_genome[j][value]:
                    new_source_genome[j].append('*'+str(random_bp))
                    new_source_genome[j].append(source_genome[j][value])
                    value += 1
                else:
                    for _ in range(2):
                        try:
                            new_source_genome[j].append(
                                source_genome[j][value])
                            value += 1
                        except:
                            break
            j += 1
        return new_source_genome

    def get_foreign_DNA(self, source_genome):
        largest_gene = 0
        smallest_gene = 10000

        count_genes = 0
        f_DNA_pool = []

        for chromosome in source_genome:
            # temp = [x.replace('_', '') for x in chromosome if "*" not in x]
            temp = [x for x in chromosome if "*" not in x]
            count_genes += len(temp)
            for c in temp:
                largest_gene = max(int(largest_gene), int(c))
                smallest_gene = min(int(smallest_gene), int(c))

        for i in range(int(count_genes//2)):
            random_bp = randint(int(smallest_gene), int(largest_gene))
            chromosome_to_insert = randint(0, int(len(source_genome)-1))

            pool = []
            pool.append(random_bp)
            pool.append(chromosome_to_insert)
            f_DNA_pool.append(pool)

        new_source_genome = [[0] * 1 for i in range(len(source_genome))]

        j = 0
        for index in source_genome:
            count = 0
            for i in range(len(index)-1):
                count += 1
                new_source_genome[j].append("0")
            j += 1

        for i in f_DNA_pool:
            chromosome = i[1]
            f_dna = i[0]

            chosen_chromosome = source_genome[chromosome]
            gene = randint(0, int(len(chosen_chromosome)-1))

            while not '*' in chosen_chromosome[gene]:
                gene = randint(0, int(len(chosen_chromosome)-1))

            new_source_genome[chromosome][gene] = str(f_dna) + "_"

        j = 0
        for index in new_source_genome:
            for value in range(len(index)):
                if new_source_genome[j][value] == 0 or new_source_genome[j][value] == '0':
                    new_source_genome[j][value] = str(source_genome[j][value])
            j += 1

        return self.generate_integenic_regions(new_source_genome)

    def create_record(self,type, chromosome_index, position, gene, source_genome, mutated_chromosome, list_of_mutations):
        operation = {}
        operation['Type'] = type
        operation['Chr'] = chromosome_index + 1
        operation['Pos'] = position
        operation['Gene'] = gene
        source_genome[chromosome_index] = mutated_chromosome
        operation['Genome after mutation'] = source_genome
        list_of_mutations.append(operation)




# def get_legal_operations(self,source_genome, target_genome):
#         list_of_legal_operations = []
#         adjacenciesA = source_genome
#         adjacenciesB = target_genome
#         switch = True
#         loop_counter = 0  # No foreign DNA in first iteration of mutations
#         for_Dna_counter = 0

#         while switch:
#             if loop_counter > 0 :
                
#                 # check number of applicale region, if 0 then create 
#                 adjacenciesA = API.insert_Integenic_Regions(adjacenciesA)
       
#                 # randomly choose to insert foreign dna
#                 choose = randint(0, 10)
#                 if (choose <= 5 and for_Dna_counter != 0) :
#                     series_of_mutation,mutation_required = self.mutation_legal_operations(adjacenciesA, adjacenciesB)
                    
#                     if series_of_mutation == [] and mutation_required !=():
#                         source_genome, mutation_list = self.do_mutation(adjacenciesA, mutation_required)
        
#                         adjacenciesA = source_genome[:]

#                         list_of_legal_operations.append(mutation_list)
#                         switch = True
#                     else:
#                         while (any(series_of_mutation) and mutation_required !=()) or mutation_required !=():
#                             mutations_finale = []
#                             for i in range(len(series_of_mutation)):
#                                 if i == 0:
#                                     mutation_type = 'ins'
#                                 elif i == 1:
#                                     mutation_type = 'del'
#                                 else:
#                                     mutation_type = 'dup'

#                                 mutation = series_of_mutation[i]
#                                 for chromosome_number in range(len(mutation)):
#                                     if mutation[chromosome_number] != []:
#                                         chromosome_index = chromosome_number
#                                         chrom = mutation[chromosome_number]
#                                         for m in range(len(chrom)):
#                                             do_mutation = (mutation_type, chromosome_index, chrom[m])
#                                             source_genome, mutation_list = self.do_mutation(adjacenciesA, do_mutation)
#                                             adjacenciesA = source_genome[:]
#                                             mutations_finale.append(mutation_list)
#                             list_of_legal_operations.append(mutations_finale)

#                             #remove all unapplicable intergenic regions and call intergenerator 
#                             # to insert new applicable regions for mutations to occur
#                             adjacenciesA = API.insert_Integenic_Regions(adjacenciesA)

#                             series_of_mutation,mutation_required = self.mutation_legal_operations(adjacenciesA, adjacenciesB)
                    
#                             if mutation_required ==():
#                                 break
#                         switch = False
#                 elif ((for_Dna_counter < 10 or for_Dna_counter ==0)):
#                     print("\tInserted foreign DNA")
#                     for_Dna_counter += 1

#                     # add foreign dna 
#                     mutation_genome = API.get_foreign_DNA(adjacenciesA)

#                     series_of_mutation, mutation_required = self.mutation_legal_operations(mutation_genome, adjacenciesB)
    
#                     if series_of_mutation == []:
                        
#                         source_genome, mutation_list = self.do_mutation(adjacenciesA, mutation_required)
#                         adjacenciesA = source_genome[:]
#                         list_of_legal_operations.append(mutation_list)
#                         switch = True
        
#                     else:
#                         while (any(series_of_mutation) and mutation_required ==()) or mutation_required !=():
#                             mutations_finale = []
#                             for i in range(len(series_of_mutation)):
#                                 if i == 0:
#                                     mutation_type = 'ins'
#                                 elif i == 1:
#                                     mutation_type = 'del'
#                                 else:
#                                     mutation_type = 'dup'

#                                 mutation = series_of_mutation[i]

#                                 for chromosome_number in range(len(mutation)):
#                                     if mutation[chromosome_number] != []:
#                                         chromosome_index = chromosome_number
#                                         chrom = mutation[chromosome_number]
#                                         for m in range(len(chrom)):
#                                             do_mutation = (mutation_type, chromosome_index, chrom[m])
#                                             source_genome, mutation_list = self.do_mutation(adjacenciesA, do_mutation)
#                                             adjacenciesA = source_genome[:]
#                                             mutations_finale.append(mutation_list)
                            
#                             list_of_legal_operations.append(mutations_finale)
                        
#                             if mutation_required ==():
#                                 break
#                         switch = False
                        
#             elif loop_counter == 0:
#                 series_of_mutation, mutation_required = self.mutation_legal_operations(adjacenciesA, adjacenciesB)
                
#                 if series_of_mutation == [] and mutation_required !=():
#                     switch = True

#                     #Do random mutation
#                     source_genome, mutation_list = self.do_mutation(adjacenciesA, mutation_required)
#                     print("Could not find straight path to get to target_genome so randomly mutated")

#                     adjacenciesA = source_genome[:]
#                     list_of_legal_operations.append(mutation_list)
                    
#                     # check number of applicale region, if 0 then create 
#                     count_app = 0
#                     for chromosome in adjacenciesA:
#                         for i in range(len(chromosome)):
#                             if isinstance(chromosome[i], str) and '*' in chromosome[i] and len(chromosome[i]) > 1 :
#                                 count_app += 1
#                     print(f"Within first iteration after any and all mutations we check applicable reagions, count is : {str(count_app)}")
                   
#                     if count_app <= len(adjacenciesA)-1:
#                         #remove all unapplicable intergenic regions and call intergenerator
#                         adjacenciesA = API.generate_integenic_regions(adjacenciesA)
#                 else:
#                         while (any(series_of_mutation) and mutation_required ==()) or mutation_required !=():
                            
#                             mutations_finale = []
#                             for i in range(len(series_of_mutation)):
#                                 if i == 0:
#                                     mutation_type = 'ins'
#                                 elif i == 1:
#                                     mutation_type = 'del'
#                                 else:
#                                     mutation_type = 'dup'

#                                 mutation = series_of_mutation[i]
#                                 for chromosome_number in range(len(mutation)):
#                                     if mutation[chromosome_number] != []:
#                                         chromosome_index = chromosome_number
#                                         chrom = mutation[chromosome_number]
#                                         for m in range(len(chrom)):
#                                             do_mutation = (mutation_type, chromosome_index, chrom[m])
#                                             source_genome, mutation_list = self.do_mutation(adjacenciesA, do_mutation)
#                                             adjacenciesA = source_genome[:]
#                                             mutations_finale.append(mutation_list)
#                             list_of_legal_operations.append(mutations_finale)

#                             #remove all unapplicable intergenic regions and call intergenerator
#                             adjacenciesA = API.generate_integenic_regions(adjacenciesA)
                                
#                             series_of_mutation,mutation_required = self.mutation_legal_ops(adjacenciesA, adjacenciesB)
                            
#                             if mutation_required ==():
#                                 break
#                         switch = False                
#             else:
#                 break
#             loop_counter += 1

#         return list_of_legal_operations