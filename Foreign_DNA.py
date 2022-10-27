import sys
import Gen_Node
import Gen_xtremities



import Evolutionary_events
import copy

#This function is called to insert foreign DNA into a source_genome and transform it into a target_genome using DCJ_indels and duplications. It shows the evolutionary pathway of the foreign DNA fragments in the source genome transformation process.
def foreign_dna(source_genome, target_genome):
    trgt = copy.deepcopy(target_genome)
    #print(trgt)
    # source_genome = []
    # target_genome = []
    # Genome_A = []
    Genome_A1 = []
    Genome_B1 = []
    genome_b1_tot = []
    # check for genes present in Genome_A(source_genome) but absent from Genome_B(target_genome) and insert them into
    # Genome_B to produce Genome_B1
    for j in range(len(source_genome)):
        Genome_A = source_genome[j]
        Genome_B = target_genome[j]
        for i in range(len(Genome_A)):
            if Genome_A[i] not in Genome_B and "*" not in Genome_A:
                Genome_B.append(str(Genome_A[i])+"_")
        Genome_A1.append(Genome_B)
        # genome_b1_tot.append(Genome_B1)
        # Genome_B1 = []
        # return Genome_B1
    #print("g b1")
    #print(Genome_A1)
    # Let Genome_B1 undergo evolutionary events(insertions, deletions and duplications) via normal DCJ operations( call "Do mutations" function) 
    # to sort the "new source genome"(Genome_B1)
    # into the target_genome. in the process it will produce Genome_A1, which will be sorted back to Genome_A
    # Gen_b_obj = Gen_Node.Node()
    eve_obj = Evolutionary_events.Eve()
    #print("trgt")
    #print(trgt)
    #rint(trgt)
    # sys.exit(0)
    Genome_A1, list_of_mutations = eve_obj.get_legal_operations(source_genome, target_genome)
    # Genome_A1, list_of_mutations = Gen_b_obj.mutation_legal_ops(source_genome, Genome_B1)
    #print("g a1")
    #print(Genome_A1)
    #return Genome_A1

    # Check Genome_A1 for genes present in Genome_B but absent in Genome_A. 
    # Remove such genes from Genome_A1 to produce Genome_A which has been transformed into Genome_B with foreign_DNA inserted.
    Genome_A2 = []
    for j in range(len(Genome_A1)):
            if Genome_A1[j] in Genome_B and Genome_A1[j] not in source_genome[j]:
                Genome_A1.remove[j]
            Genome_A2.append(Genome_A1)
            
    return Genome_A1, Genome_A2
        
        
    
