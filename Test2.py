import Gen_Node
import Gen_xtremities
import foreign_DNA

gen_n_obj = Gen_Node.Node()

Genome_A = [['*', '1', '*7', '2', '*', '3', '*7', '4', '*', '1', '*7', '5'], ['*6', '8', '*9', '7', '*', '6', '*7',  '12', '*5','13']]
Genome_B = [['*', '1', '*6', '2', '*', '3', '*', '4', '*', '5', '*', '6', '*', '7', '*6', '8'], ['*', '9', '*', '10', '*8', '11' ,'26']] 


fdna  = gen_n_obj.mutation_legal_ops(Genome_A, Genome_B)

