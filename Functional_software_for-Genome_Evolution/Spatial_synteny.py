

import numpy as np
from Intergenic_region_generator import IntergenicGenerator


class SpatialSyntenyConstraint:
    def __init__(self, hic_data):
        self.hic_data = hic_data
        self.spatial_synteny_map = self.build_spatial_synteny_map()

    def build_spatial_synteny_map(self):
        # This function builds a map of spatial synteny based on the Hi-C data.
        # The Hi-C data is a matrix where the entry at position (i, j) represents the
        # frequency of contact between loci i and j. We can use this data to infer
        # which loci are in spatial synteny.
        spatial_synteny_map = {}
        for i in range(self.hic_data.shape[0]):
            for j in range(self.hic_data.shape[1]):
                if self.hic_data[i, j] >= 5:  # change threshold here
                    spatial_synteny_map[(i, j)] = True
        return spatial_synteny_map

    def check_spatial_synteny(self, loci1, loci2):
        # This function checks whether two loci are in spatial synteny.
        # It does this by looking up the loci in the spatial_synteny_map.
        return self.spatial_synteny_map.get((loci1, loci2), False)
    

    def check_intergenic_region(self, loci, genes_with_intergenic_genome):
         # This function checks whether a locus is in an intergenic region.
        # You would need to implement this based on your specific definition of an intergenic region.
        applicable_regions = []
        for i in range(len(genes_with_intergenic_genome)-1):
            if '*' in genes_with_intergenic_genome[i]:
                if loci[i] >= 5:
                    applicable_regions.append(genes_with_intergenic_genome[i])
        return applicable_regions

                

    def apply_constraint(self, source_genome):
        # This function applies the spatial synteny constraint to a proposed genome.
        # It does this by iterating over pairs of loci in the proposed genome,
        # and checking whether they are in spatial synteny using the check_spatial_synteny function.
        # If a pair of loci is not in spatial synteny, this function returns False,
        # indicating that the proposed genome does not satisfy the constraint.
        for i in range(len(source_genome) - 1):
            if not self.check_spatial_synteny(source_genome[i], source_genome[i + 1]):
                return False
        return True



    

    
