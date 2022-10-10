

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
data_source = [['*8', '1', '*6', '5','*6', '4', '*6','3', '*8','9_' ], ['*8','10', '*10', '22', '*9', '37', '*9','33']]
data_target = [['*8','1','*','4','*','5', '*','6'], ['*8','10','*9', '33','*', '33', '*', '40']]
source = data_source[:]

chromo = []
source_genome = []
for chrom in source:
    for i in range(len(chrom)):
        print(chrom[i])
        print(type(chrom[i]))
        if isinstance(chrom[i], str) and '_' in chrom[i]:
            if len(chrom[i])==3:
                gene = chrom[i]
                chromo.append(int(gene[:2]))
            elif len(chrom[i])==2:
                gene = chrom[i]
                chromo.append(int(gene[:1]))
        elif isinstance(chrom[i], str):
            chromo.append((chrom[i]))
        elif ((isinstance(chrom[i], str) and '*' in chrom[i])):
            chromo.append((chrom[i]))
    source_genome.append(chromo)
    chromo = []
print(source_genome)
target_genome = data_target[:]
in_genome = []
in_target = []
# for chromosome in source_genome:
#     for t_chrom in target_genome:
for j in range(len(target_genome)):
    chromosome = source_genome[j]
    t_chrom = target_genome[j]
    # print(chromosome)
    # print(source_genome)
    for i in range(len(t_chrom)):
        # print(t_chrom[i])
        # print(chromosome)
        if '*' not in str(t_chrom[i]) and (t_chrom[i]) not in chromosome:
            in_target.append((i,t_chrom[i]))
    in_genome.append(in_target)
    in_target = []
print("in_genome")
print(in_genome)

out_genome = []
out_target = []
occured = []
# for chromosome in source_genome:
#     for t_chrom in target_genome:
for j in range(len(target_genome)):
    chromosome = source_genome[j]
    t_chrom = target_genome[j]
    for i in range(len(chromosome)):
        if ((isinstance(chromosome[i], int) and chromosome[i] not in t_chrom)) or (((isinstance(chromosome[i], str) and '*' not in chromosome[i])) and chromosome[i] not in t_chrom):
            print(chromosome[i])
            print(t_chrom)
            out_target.append((i,chromosome[i]))
        elif (((isinstance(chromosome[i], str) and '*' not in chromosome[i])) and chromosome[i] in t_chrom) and (chromosome.count(chromosome[i])) > t_chrom.count(chromosome[i]) and (isinstance(chromosome[i],str) and '*' not in chromosome[i]) and (chromosome[i] not in occured):
            print(chromosome.count(chromosome[i]))
            print(t_chrom)
            out_target.append((i,chromosome[i]))
            occured.append(chromosome[i])
    out_genome.append(out_target)
    out_target = []
print("out_genome")
print(out_genome)

# print(any(out_genome))
# print(not any(out_genome))

# tam = [[],[],[],[]]
# print(any(tam))