import sys
import Bio
from Bio import SeqIO, SeqFeature
from Bio.SeqRecord import SeqRecord
import os


def get_intergenic_regions(filename, intergenic_length=4):
    seq_record = SeqIO.parse(open(filename), "genome").next()
    gene_list_plus = []
    gene_list_minus = []
    intergenic_region = []
    # Loop over the genome file, get the gene features
    for feature in seq_record.features:
        if feature.type == "gene":
            gen_start = feature.location._start.position
            gen_end = feature.location._end.position
            if feature.strand == -1:
                gene_list_minus.append((gen_start, gen_end, -1))
            elif feature.strand == 1:
                gene_list_plus.append((gen_start, gen_end, 1))
            else:
                sys.stderr.write(
                    "No strand indicated %d-%d. Assuming +\n" % (gen_start, gen_end)
                )
                gene_list_plus.append((gen_start, gen_end, 1))

    for i, pospair in enumerate(gene_list_plus[1:]):
        # Compare current start position to previous end position
        last_end = gene_list_plus[i][1]
        this_start = pospair[0]
        strand = pospair[2]
        if this_start - last_end >= intergenic_length:
            intergenic_seq = seq_record.seq[last_end:this_start]
            strand_string = "+"
            intergenic_records.append(
                SeqRecord(
                    intergenic_seq,
                    id="%s-ign-%d" % (seq_record.name, i),
                    description="%s %d-%d %s"
                                % (seq_record.name, last_end + 1, this_start, strand_string),
                )
            )
    for i, pospair in enumerate(gene_list_minus[1:]):
        last_end = gene_list_minus[i][1]
        this_start = pospair[0]
        strand = pospair[2]
        if this_start - last_end >= intergenic_length:
            intergenic_seq = seq_record.seq[last_end:this_start]
            strand_string = "-"
            intergenic_records.append(
                SeqRecord(
                    intergenic_seq,
                    id="%s-ign-%d" % (seq_record.name, i),
                    description="%s %d-%d %s"
                                % (seq_record.name, last_end + 1, this_start, strand_string),
                )
            )
    outpath = os.path.splitext(os.path.basename(filename))[0] + "_ign.fasta"
    SeqIO.write(intergenic_records, open(outpath, "w"), "fasta")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        get_intergenic_regions(sys.argv[1])
    elif len(sys.argv) == 3:
        get_intergenic_regions(sys.argv[1], int(sys.argv[2]))
    else:
        print("Usage: get_intergenic.py gb_file [intergenic_length]")
        sys.exit(0)
