import Gen_Node
import Gen_xtremities
import Foreign_DNA
import sys


source_genome= [['*6', '1', '*7', '2', '*7', '3', '*7', '4', '*8', '1', '*7', '5'],['*6', '8', '*9', '7', '*9', '6', '*7',  '12', '*9','13']]
target_genome= [['*7', '1', '*6', '2', '*7', '3', '*6', '4', '*7', '5', '*9', '6', '*6', '7', '*6', '8'],['*9', '9', '*10', '10', '*8', '11' , '*6', '26']] 


fdna_1 = Foreign_DNA.foreign_dna(source_genome, target_genome)

print(fdna_1) 
print(len(fdna_1))
all_fsrc = []
all_solutions = []
for sub in fdna_1:
    print("solution")
    print(sub[0])
    print()
    all_fsrc.append(sub[0])
    all_solutions.append(sub[1])
    for op in sub[1]:
        print(op)
        print()
    print('\n')

print(all_fsrc)
print(all_solutions)
sys.exit(0)
#f = open("collection_final_source.txt", "w")
#for item in all_fsrc:
    #f.write(str(item))
    #f.write('\n')
#f.close()

#f1 = open("collection_final_solutions.txt", "w")
#for item in all_solutions:
    #f1.write(str(item))
    #f1.write('\n')
#f1.close()