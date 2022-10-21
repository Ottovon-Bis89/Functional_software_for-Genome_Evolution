import Gen_Node
import Gen_xtremities
import Foreign_DNA


Genome_A = [['*', '1', '*7', '2', '*', '3', '*7', '4', '*', '1', '*7', '5'], ['*6', '8', '*9', '7', '*', '6', '*7',  '12', '*5','13']]
Genome_B = [['*', '1', '*6', '2', '*', '3', '*', '4', '*', '5', '*', '6', '*', '7', '*6', '8'], ['*', '9', '*', '10', '*8', '11' ,'26']] 


fdna_1, fdna_2  = Foreign_DNA.foreign_dna(Genome_A, Genome_B)

print(fdna_1)
print(fdna_2)
