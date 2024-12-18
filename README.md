# Functional_software_for-Genome_Evolution
#A software to determine sequence of evolutionary events in transforming a source genome into a target genome

Genolve+ is a Python program that identifies and return the most biologically acceptable series of evolutionary events (rearrangements) that can describe the possible transformation of genome A (source genome) into genome B (target genome).  It can be used to investigate the evolutionary history of two closely related genomes.  Genolve+ uses an ammended version of the double-cut-and-join model [1], and extends this approach with a tree searching algorithm to set an upper bound to the minimum number of evolutionary events required for the observed genomic difference.  Genolve+ identifies evolutionary events such as insertions, deletions, inversions, transpositions, duplications, fissions, fusions, translocations (balanced and unbalanced).  Genolve+ returns a list of all the most biologically acceptable paths that can get the source genome to the target genome.  As input, Genolve+ requires a file with the chromosome number and the order of all identified synonymous sequence blocks.
The files necessary to run Genolve+ include Genome_extremities_and_adjacencies.py, Path_node.py, Path_network.py, Biological_Constraints.py, ForeignDNA.py and Genolve+.py. In addition, two text files containing the input genomes,  a text file containing the weighting ratios and a text file containing the fragments of foreign DNA are required. To generate the fragments of foreign DNA, run the ForeignDNA.py file with the two genomes as input files (e.g python3 ForeignDNA.py source_genome.txt target_genome.txt outputfile.txt --num_fragments (omit fragments arguement to use default value))
Genolve takes as input two lists of synteny blocks representing the two input genomes.MTZ.txt and FJSA.txt are examples of the format in which the input genomes need to be. The synteny blocks confined to separate chromosomes occur on different lines in the file. Synteny blocks on the same chromosome are separated by commas. Synteny blocks in the inverse orientation should be preceded by a negative ('-') sign.
The Weight_ratios.txt file can be altered in accordance with the cost that the user wants to assign to each of the different rearrangements. The order of the weight ratios are inversions, transpositions, balanced translocations, unbalanced translocation, fissions, fusions, insertions, deletions, duplications
Python3 is required to run the Genolve.py file. The following arguments need to be passed to the program in this order: -t your_target_genome.txt -s your_source_genome.txt -r weights_ratios.txt -f foreign_DNA_fragment_list.txt -o name_of_output_file.txt. To run the program. download these files into your working directory
Example of running program on command line:python3 Genolve+.py -t MTZ.txt -s FJSA.txt -r weight_ratios.txt -f frag.txt –o output.txt

The output of the program shows the source and target genomes, number of solutions (paths) in the transformation process, number (average) of events per solution, number (average) of each event in a solution and the Edit distance.


[1]  Yancopoulos S, Attie O, Friedberg R. Efficient sorting of genomic permutations by translocation, inversion and block interchange. Bioinformatics 2005; 21:3340–3346


# Acknowledgement
Helene Fouche -for your immense contribution to the design and implementation of the first part of Genolve+
