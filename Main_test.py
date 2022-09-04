import Gen_xtremities

data = []
with open("Generated_data.txt") as f:
    lines = f.readlines()
    for l in lines:
        k = l.strip('\n').split(',')
        data.append(k)
# print(data)

#create the object
gen_x_obj = Gen_xtremities.Xtremities()
genome_gene_extremity = gen_x_obj.gene_extremity(data)
# print(genome_gene_extremity)
adjacencies_one = gen_x_obj.create_adjacencyList(data) #chromosome
# print()
# print((adjacencies_one))
# for i in adjacencies:
#     print(i)

adjacencies_sorted, adjacencies, telomers = gen_x_obj.adjacencies_ordered_and_sorted(data)
# print(adjacencies_sorted)
# print()
# print(adjacencies)
# print()
# print(telomers)
next_ext = gen_x_obj.find_next_extremity(adjacencies)
# print(next_ext)
# print()

next_extrem = gen_x_obj.find_next_adjacency(next_ext, adjacencies_one, telomers)
# print(telomers)
# print()
# print(next_ext)
# print()
# print(next_extrem)
linear_chromosomes, telomers, chromosome = gen_x_obj.find_chromosome(adjacencies_one)