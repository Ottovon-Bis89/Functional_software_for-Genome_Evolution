import pandas as pd


def extract_elements(gff_file, output_file):
    chromosomes = {}
    genes = []
    mRNA = []
    exons = []
    CDS = []

    with open(gff_file, 'r') as file:
        for line in file:
            if line.startswith('##sequence-region'):
                _, chromosome, start, end = line.strip().split()
                chromosomes[chromosome] = {'start': int(start), 'end': int(end)}
            elif not line.startswith('#'):
                data = line.strip().split('\t')
                feature_type = data[2]
                attributes = data[8].split(';')

                if feature_type == 'chromosome':
                    continue  # Skip chromosome features

                start_pos = int(data[3])
                end_pos = int(data[4])

                if feature_type == 'gene':
                    gene_attributes = {
                        attr.split('=')[0]: attr.split('=')[1] for attr in attributes if '=' in attr
                    }
                    genes.append([chromosome, start_pos, end_pos,
                                  gene_attributes.get('ID', ' '), gene_attributes.get('Name', ' '),
                                  gene_attributes.get('gbkey', ' '), gene_attributes.get('gene', ' '),
                                  gene_attributes.get('gene_biotype', ' '), gene_attributes.get('locus_tag', ' ')])
                elif feature_type == 'mRNA':
                    mrna_attributes = {
                        attr.split('=')[0]: attr.split('=')[1] for attr in attributes if '=' in attr
                    }
                    mRNA.append([chromosome, start_pos, end_pos,
                                 mrna_attributes.get('ID', ''), mrna_attributes.get('Parent', ''),
                                 mrna_attributes.get('gbkey', ''), mrna_attributes.get('locus_tag', ''),
                                 mrna_attributes.get('product', '')])
                elif feature_type == 'exon':
                    exon_attributes = {
                        attr.split('=')[0]: attr.split('=')[1] for attr in attributes if '=' in attr
                    }
                    exons.append([chromosome, start_pos, end_pos,
                                  exon_attributes.get('ID', ''), exon_attributes.get('Parent', ''),
                                  exon_attributes.get('gbkey', ''), exon_attributes.get('gene', ''),
                                  exon_attributes.get('locus_tag', ''), exon_attributes.get('product', '')])
                elif feature_type == 'CDS':
                    cds_attributes = {
                        attr.split('=')[0]: attr.split('=')[1] for attr in attributes if '=' in attr
                    }
                    CDS.append([chromosome, start_pos, end_pos,
                                cds_attributes.get('ID', ''), cds_attributes.get('Parent', ''),
                                cds_attributes.get('gbkey', ''), cds_attributes.get('gene', ''),
                                cds_attributes.get('locus_tag', ''), cds_attributes.get('product', ''),
                                cds_attributes.get('Dbxref', ''), cds_attributes.get('Note', '')])

    with open(output_file, 'w') as file:
        for chromosome, region in chromosomes.items():
            file.write(f'Chromosome: {chromosome} ({region["start"]}-{region["end"]})\n\n')

            file.write('Genes:\n')
            file.write('Chromosome, Start, End,  D, Name, gbkey, gene, gene_biotype, locus_tag\n')
            for gene in genes:
                if gene[0] == chromosome:
                    file.write(','.join(str(value) for value in gene) + '\n')

            file.write('\nmRNA:\n')
            file.write('Chromosome, Start, End, ID, Parent, gbkey, locus_tag, product\n')
            for mrna in mRNA:
                if mrna[0] == chromosome:
                    file.write(','.join(str(value) for value in mrna) + '\n')

            file.write('\nExons:\n')
            file.write('Chromosome, Start, End, ID, Parent, gbkey, gene, locus_tag, product\n')
            for exon in exons:
                if exon[0] == chromosome:
                    file.write(','.join(str(value) for value in exon) + '\n')

            file.write('\nCDS:\n')
            file.write('Chromosome, Start, End, ID, Parent, gbkey, gene, locus_tag, product, Dbxref, Note\n')
            for cds in CDS:
                if cds[0] == chromosome:
                    file.write(','.join(str(value) for value in cds) + '\n')

    print(f'Data extracted and written to {output_file}')


gff_file_path = '/home/22204911/Downloads/ncbi_dataset.zip_yeast/ncbi_dataset/data/GCF_000146045.2/genomic.gff'
output_file_path = '/home/22204911/Downloads/ncbi_dataset.zip_yeast/ncbi_dataset/data/GCF_000146045.2/output.csv'

extract_elements(gff_file_path, output_file_path)


