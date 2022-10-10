import Gen_Node
<<<<<<< HEAD
import Gen_xtremities

#This function is called to insert foreign DNA into a source_genome and transform it into a target_genome using DCJ_indels and duplications. It shows the evolutionary pathway of the foreign DNA fragments in the source genome transformation process.
def foreign_dna():
    source_genome = []
    target_genome = []
=======

def foreign_dna(source_genome, target_genome):
    Genome_A = []
    Genome_B = []
>>>>>>> 329dcab9db2a762e624d5379b220453b362950b1
    Genome_A1 = []
    Genome_B1 = []
    # check for genes present in Genome_A(source_genome) but absent from Genome_B(target_genome) and insert them into
    # Genome_B1
    for j in range(len(source_genome)):
        Genome_A = source_genome[j]
        Genome_B = target_genome[j]
        for i in range(len(Genome_A)):
            if Genome_A(i) not in Genome_B:
                Genome_B.append(i, Genome_A(i))
            Genome_B1.append(Genome_B)
        return Genome_B1
    # Let Genome_B1 undergo mutations via normal DCJ operations( call "Do mutations" function) to sort
    # the source_genome into the target_genome. in the process it will produce Genome_A1, which will be converted
    # to Genome_back into the source_genome
    Gen_b_obj = Gen_Node.Node()
<<<<<<< HEAD
    Genome_A1 = Gen_b_obj.Do mutations(Genome_B1)
    return Genome_A1
=======
    Genome_A1, list_of_mutations = Gen_b_obj.mutation_legal_ops(Genome_A, Genome_B1)
    # return Genome_A1
>>>>>>> 329dcab9db2a762e624d5379b220453b362950b1

    # Check Genome_A1 for genes present in Genome_B but absent in Genome_A. Remove such genes from Genome_A1 to produce Genome_A which has been transformed into Genome_B with foreign_DNA inserted.
    Genome_A2 = []
    for j in range(len(Genome_A1)):
<<<<<<< HEAD
            if genome_A1[j] in Genome_B and not in source_genome():
                Genome_A1.remove(j)
            Genome_A2.append(Genome_A1)
            return Genome_A2
        
        
    pass
=======
            if Genome_A1[j] in Genome_B and Genome_A1[j] not in Genome_A:
                Genome_A1.remove(j)
            Genome_A2.append(Genome_A1)
            # return Genome_A2

    return Genome_A1, Genome_A2
>>>>>>> 329dcab9db2a762e624d5379b220453b362950b1
