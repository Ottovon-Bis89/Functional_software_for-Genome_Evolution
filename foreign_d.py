import random

# define the source and target genomes
source_genome = "ATCGATCG"
target_genome = "TGCATGCA"

# create a list of possible mutations for the foreign DNA
mutations = ["A", "T", "C", "G"]

# insert the foreign DNA into the source genome at a random position
foreign_dna = "ATCG"
insert_pos = random.randint(0, len(source_genome))
source_genome = source_genome[:insert_pos] + foreign_dna + source_genome[insert_pos:]

# create a population of genomes with the foreign DNA
population = [source_genome]

# apply a genetic algorithm to evolve the foreign DNA towards the target genome
generation = 0
while True:
    # create a new generation of genomes by mutating the current generation
    new_population = []
    for genome in population:
        for i in range(len(genome)):
            if genome[i] in mutations:
                # mutate the genome at the current position
                new_genome = genome[:i] + random.choice(mutations) + genome[i+1:]
                new_population.append(new_genome)
    population = new_population

    # check if any genome in the population matches the target genome
    for genome in population:
        if genome == target_genome:
            print(f"Foreign DNA evolved to target genome in generation {generation}")
            break
    else:
        generation += 1
    print(population)
