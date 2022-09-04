class Biological_constraints:
    def __init__(self):
        pass

    def intergenic_region(self, filename, intergenic_length=5):
        genic_record = SeqIO.parse(open(filename), "genome").next()
        intergenic_region = []

        # Find gene features over entire genome

        for feature in genic_record.features:
            if feature.type == "*":
                gen_start = feature.location._start.position
                gen_end = feature.location._end.position
                if intergenic_length >= 5:
                    intergenic_region.append(gene)

                else:
                    intergenic_region.remove(gene)

        return intergenic_region

    def proximity_of_DNA_segments(self):
        pass