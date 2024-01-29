
import Evolutionary_events

#This function inserts foreign DNA into a source_genome and transform it into a target_genome using DCJ_indels and duplications. 
# It shows the evolutionary pathway of the foreign DNA fragments in the source genome transformation process.

def foreign_dna(source_genome : list, target_genome: list):
    # check for genes present in Genome_A(source_genome) but absent from Genome_B(target_genome) and insert such genes into
    # Genome_B to produce Genome_B1

    Genome_A = [x for x in source_genome if '*' not in x]
    #TODO PRint what source & target is & print how to get steps
    Genome_B = [x for x in target_genome if '*' not in x]
    genes_to_add = [f'{x}_'for x in Genome_A if x not in Genome_B]
    Genome_B1 = (*genes_to_add, *Genome_B)


    # Let Genome_B1 undergo evolutionary events(insertions, deletions and duplications) via normal DCJ operations( call "get legal operations" function) 
    # to sort the "new source genome"(Genome_B1)
    # into the target_genome. in the process it will produce Genome_A1, which will be sorted back to Genome_A
    eve_obj = Evolutionary_events.Evolutionary()

    #Genome_A1  = eve_obj.get_legal_operations(source_genome, target_genome)
    list_of_mutations = eve_obj.get_legal_operations(Genome_B1, target_genome)

    # Check Genome_B1 for genes present in Target genome but absent in Source_genome. 
    # Remove such genes from Genome_B1 to produce Source genome which has been transformed into Target genome with foreign_DNA inserted.
    Genome_A1 = []
    for j in range(len(Genome_B1)):
            if Genome_B1[j] in target_genome and Genome_B1[j] not in source_genome:
                Genome_B1.remove[j]
            Genome_A1.append(Genome_B1)
            
    return Genome_A1, Genome_B1, source_genome, target_genome, list_of_mutations
    

        
        
    
