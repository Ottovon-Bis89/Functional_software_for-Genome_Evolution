
import random
import argparse
import os

class Foreign_DNA:
	"""
	A class that creates and insert a fragment of foreign DNA into the source genome
	"""
	
def __init__(self):
        pass

def foreign_dna_pool(self, genomeA, genomeB, num_fragments=5):
        """
        Finds the difference in genes between the source and target genomes. Creates a pool of random integers and
        generates foreign DNA fragments from the pool. Fragments are tagged with an underscore (_) for identification.

        :param genomeA: The source genome.
        :param genomeB: The target genome.
        :param num_fragments: The number of fragments to produce.
        :return: A list of foreign DNA fragments.
        """
        def clean_gene(gene):
            """Converts gene to positive integer ignoring any underscore or negative sign."""
            return abs(int(gene.replace("_", ""))) if isinstance(gene, str) else abs(gene)

        # Flatten the source and target genomes, considering only the integer part
        genomeA_flat = [clean_gene(gene) for chrom in genomeA for gene in chrom]
        genomeB_flat = [clean_gene(gene) for chrom in genomeB for gene in chrom]

        difference = list(set(genomeB_flat) - set(genomeA_flat))

        foreign_dna = []
        if len(difference) > 0:
            foreign_dna = difference[:]
            while len(foreign_dna) < 2 * len(difference):
                gene = random.randint(1, 10)
                if gene not in foreign_dna:
                    foreign_dna.append(gene)
        else:
            while len(foreign_dna) < num_fragments:
                gene = random.randint(1, 10)
                if gene not in foreign_dna:
                    foreign_dna.append(gene)

        list_of_fragments = []
        while len(list_of_fragments) < num_fragments:
            fragment = random.sample(foreign_dna, 1)
            fragment = [f"{fragment[0]}_"]
            if fragment not in list_of_fragments:
                list_of_fragments.append(fragment)

        return list_of_fragments

def write_fragments_to_file(self, list_of_fragments, filepath):
        """
        Writes the list of fragments to a specified file.

        :param list_of_fragments: The list of foreign DNA fragments.
        :param filepath: The path to the file where fragments will be written.
        """
        with open(filepath, 'w') as file:
            for fragment in list_of_fragments:
                file.write(f"{fragment[0]}\n")

def run(self, source_filepath, target_filepath, output_filepath, num_fragments=5):
        """
        Executes the process of reading genomes from files, finding foreign DNA fragments,
        and writing them to an output file.

        :param source_filepath: The file path of the source genome.
        :param target_filepath: The file path of the target genome.
        :param output_filepath: The file path where the fragments will be written.
        :param num_fragments: The number of fragments to produce.
        """
        def read_genome(filepath):
            with open(filepath) as file:
                return [list(map(int, line.strip().split(','))) for line in file]

        genomeA = read_genome(source_filepath)
        genomeB = read_genome(target_filepath)

        list_of_fragments = self.foreign_dna_pool(genomeA, genomeB, num_fragments)
        self.write_fragments_to_file(list_of_fragments, output_filepath)

def main():
        parser = argparse.ArgumentParser(description='Process genomes and find foreign DNA fragments.')
        parser.add_argument('source_genome', type=str, help='File name for the source genome')
        parser.add_argument('target_genome', type=str, help='File name for the target genome')
        parser.add_argument('output_file', type=str, help='File name to write the output fragments')
        parser.add_argument('--num_fragments', type=int, default=5, help='Number of fragments to produce (default is 5)')

        args = parser.parse_args()

        # Get the directory where the script is located
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Create full file paths
        source_filepath = os.path.join(script_dir, args.source_genome)
        target_filepath = os.path.join(script_dir, args.target_genome)
        output_filepath = os.path.join(script_dir, args.output_file)

        dna = Foreign_DNA()
        dna.run(source_filepath, target_filepath, output_filepath, args.num_fragments)

if __name__ == "__main__":
        main()


# commandline use
# python3 scriptname source_genome.txt target_genome.txt outputfile.txt --num_fragments (omit fragments arguement to use default value)
