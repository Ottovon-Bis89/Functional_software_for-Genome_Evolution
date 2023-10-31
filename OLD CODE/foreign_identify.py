# from Bio import SeqIO
# from Bio.Seq import Seq
# from Bio.Alphabet import generic_dna

# # Load source and target genomes
# source_genome = SeqIO.read("source_genome.fasta", "fasta")
# target_genome = SeqIO.read("target_genome.fasta", "fasta")

# # Perform sequence alignment
# alignments = source_genome.seq.align(target_genome.seq)

# # Identify foreign DNA
# for alignment in alignments:
#     for start, end in alignment.aligned:
#         if start is not None and end is not None and (end - start) > 0:
#             segment = target_genome.seq[start:end]
#             if segment not in source_genome.seq:
#                 print("Found foreign DNA: ", segment)

# # Identify deletions
# for alignment in alignments:
#     for start, end in alignment.aligned:
#         if start is not None and end is None:
#             deletion = source_genome.seq[start:alignment.aln_span[1]]
#             print("Found deletion: ", deletion)

# # Identify insertions
# for alignment in alignments:
#     for start, end in alignment.aligned:
#         if start is None and end is not None:
#             insertion = target_genome.seq[end - 1]
#             print("Found insertion: ", insertion)

# # Identify duplications
# for alignment in alignments:
#     for start, end in alignment.aligned:
#         if start is not None and end is not None and (end - start) > 0:
#             segment = target_genome.seq[start:end]
#             if segment in target_genome.seq[end:]:
#                 print("Found duplication: ", segment)

# Load source and target genomes
# source_genome = [1, 2, 3, 6, 8, 15, 8, 10]
# target_genome = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # Perform gene-to-gene sequence alignment
# from difflib import SequenceMatcher
# alignments = SequenceMatcher(None, source_genome, target_genome).get_opcodes()

# # Identify foreign genes, deletions, insertions, and duplications
# for alignment in alignments:
#     operation, start1, end1, start2, end2 = alignment
#     if operation == "replace":
#         segment1 = source_genome[start1:end1]
#         segment2 = target_genome[start2:end2]
#         for gene in segment2:
#             if gene not in segment1:
#                 print("Found foreign DNA: ", gene)
#     elif operation == "delete":
#         deletion = source_genome[start1:end1]
#         for gene in deletion:
#             print("Found deletion: ", gene)
#     elif operation == "insert":
#         insertion = target_genome[start2:end2]
#         for gene in insertion:
#             print("Found insertion: ", gene)
#     elif operation == "equal":
#         segment1 = source_genome[start1:end1]
#         segment2 = target_genome[start2:end2]
#         if segment1 == segment2:
#             continue
#         elif set(segment1) <= set(segment2):
#             duplication = segment1
#             print("Found duplication: ", duplication)

# Load source and target genomes
source_genome = [1, 2, 3, 6, 8, 15, 8, 10]
target_genome = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Perform gene-to-gene sequence alignment
from difflib import SequenceMatcher
alignments = SequenceMatcher(None, source_genome, target_genome).get_opcodes()

# Identify foreign genes, deletions, insertions, and duplications
for alignment in alignments:
    operation, start1, end1, start2, end2 = alignment
    if operation == "replace":
        segment1 = source_genome[start1:end1]
        segment2 = target_genome[start2:end2]
        for gene in segment2:
            if gene not in segment1:
                position = target_genome.index(gene)
                print("Found foreign DNA:", gene, "at position:", position)
    elif operation == "delete":
        deletion = source_genome[start1:end1]
        for gene in deletion:
            position = start1 + source_genome[start1:end1].index(gene)
            print("Found deletion:", gene, "at position:", position)
    elif operation == "insert":
        insertion = target_genome[start2:end2]
        for gene in insertion:
            position = start2 + target_genome[start2:end2].index(gene)
            print("Found insertion:", gene, "at position:", position)
    elif operation == "equal":
        segment1 = source_genome[start1:end1]
        segment2 = target_genome[start2:end2]
        if segment1 == segment2:
            continue
        elif set(segment1) <= set(segment2):
            duplication = segment1
            position = start2 + target_genome[start2:end2].index(duplication[0])
            print("Found duplication:", duplication, "at position:", position)

