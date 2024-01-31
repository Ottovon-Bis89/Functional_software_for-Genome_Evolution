class weight:

    def __init__(self):
        self.ins = 0.15
        self.delete = 0.05
        self.dup = 0.3
        self.fdna = 0.5

    def calc_cumulative_ratio(self,list_of_operations):
        cumulative_weight = 0
        for operation in list_of_operations:
            mutation = operation[0]
            mutation_type = mutation['Mut']
            print(mutation_type)
            #change to if statement, only works with python 3.10 and up
            # match mutation_type:
            #     case 'ins':
            #         cumulative_weight += self.ins
            #     case 'del':
            #         cumulative_weight += self.delete
            #     case 'dup':
            #         cumulative_weight += self.dup
            #     case 'FDNA':
            #         cumulative_weight += self.fdna

        return cumulative_weight




