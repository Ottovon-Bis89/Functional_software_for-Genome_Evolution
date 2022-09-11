import Gen_xtremities
import Gen_Node

data_target = []
data_source = []
with open("Generated_data.txt") as f:
    lines = f.readlines()
    for l in lines:
        k = l.strip('\n').split(',')
        data_source.append(k)

with open("Generated_data_B.txt") as f:
    lines = f.readlines()
    for l in lines:
        k = l.strip('\n').split(',')
        data_target.append(k)

# print(data_source)
# print(data_target)

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
