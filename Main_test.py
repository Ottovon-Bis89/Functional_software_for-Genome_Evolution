import Gen_xtremities
import Gen_Node

# data_target = []
# data_source = []
# with open("Generated_data.txt") as f:
#      lines = f.readlines()
#      for l in lines:
#          k = l.strip('\n').split(',')
#          data_source.append(k)

# with open("Generated_data_B.txt") as f:
#      lines = f.readlines()
#      for l in lines:
#          k = l.strip('\n').split(',')
#          data_target.append(k)

# print(data_source)
# print(data_target)
'''
gen_obj = Gen_Node.Node()
for_dna = gen_obj.foreign_dna_pool(data_source, data_target)
print(for_dna)
# print(len(for_dna))



#create the object
gen_x_obj = Gen_xtremities.Xtremities()
genome_gene_extremity = gen_x_obj.gene_extremity(data_source)
# print(genome_gene_extremity)
adjacencies_one = gen_x_obj.create_adjacencyList(data_source) #chromosome
# print()
# print((adjacencies_one))
# for i in adjacencies:
#     print(i)

adjacencies_sorted, adjacencies, telomers = gen_x_obj.adjacencies_ordered_and_sorted(data_source)
# print(adjacencies_sorted)
# print()
# print(adjacencies)
# print()
# print(telomers)
next_ext = gen_x_obj.find_next_extremity(adjacencies)
print(next_ext)
print()

next_extrem = gen_x_obj.find_next_adjacency(next_ext, adjacencies_one, telomers)
# print(telomers)
# print()
# print(next_ext)
# print()
# print(next_extrem)
linear_chromosomes, circular_chromosomes, genome = gen_x_obj.find_chromosome_type(adjacencies_one)
print(linear_chromosomes)
'''
#test mutations
#chrom = [1, '*', 2, '*8', 5, '*7', 6, '*6', 7, '*9', 8, '*', 9, '*',10]
# print(chrom)
gen_n_obj = Gen_Node.Node()
# insert_mutation = gen_n_obj.insertion(chrom, 4)
# print(insert_mutation)

# del_mutation = gen_n_obj.deletion(chrom, 4)
# print(del_mutation)
# print(chrom)
# dup_mutation = gen_n_obj.duplication(chrom, 4, 8)
# print(dup_mutation)

# print(data_source)

# for_chrom = gen_n_obj.add_for_dna(data_source, [1,1,1,3])
# print(for_chrom)
# print(data_source)
# print()
# #test do mutation
# mutated_genome, list_of_mutations = gen_n_obj.do_mutation(data_source)
# print(list_of_mutations), [10,11,'*9', 33]
# print(mutated_genome) , [10, '*10', 22, '*9', 33]
# data_source = [['*8', '1', '*6', '5','*6', '4', '*6','3', '*','9_' ], ['*8','10', '*10', '22', '*9', '37', '*9','33']]
# data_target = [['*8','1','*','4','*','5', '*','6'], ['*8','10','*9', '33','*', '33', '*', '40']]

data_source = [['*', '1', '*7', '2', '*', '3', '*7', '4', '*', '1', '*7', '5'], ['*6', '8', '*9', '7', '*', '6', '*', '5', '*', '1', '*', '4', '*9', '1', '*', '3', '*', '1', '*8', '2'], ['*8', '9', '*7', '11'], ['*', '20', '*8', '19', '*', '18', '*', '17', '*', '16', '*6', '32', '*9', '10', '*8', '31', '*', '30', '*', '29', '*8', '28', '*', '27'], ['*', '21', '*', '22', '*7', '23', '*', '24', '*7', '25', '*6', '26'], ['*8', '33'], ['*', '34', '*', '35', '*', '36', '*', '37']]
data_target = [['*', '1', '*6', '2', '*', '3', '*', '4', '*', '5', '*', '6', '*', '7', '*6', '8'], ['*', '9', '*', '10', '*8', '11'], ['*', '12', '*', '13', '*', '14', '*', '15'], ['*', '16', '*6', '17', '*6', '18', '*', '19', '*', '20'], ['*9', '21', '*', '22', '*', '23', '*', '24', '*', '25', '*7', '26'], ['*', '27', '*', '28', '*', '29', '*9', '30', '*8', '31', '*', '32', '*', '33'], ['*', '34', '*6', '35', '*', '36', '*', '37', '*7', '38', '*6', '39', '*', '40']]
# in_g, out, dup = gen_n_obj.mutation_legal_ops(data_source, data_target)
# print(in_g)
# print(out)
# print(dup)
list_of_legal  = gen_n_obj.get_legal_operations(data_source, data_target)
#print(list_of_legal