# class weight:

#     def __init__(self):
#         self.ins = 0.15
#         self.delete = 0.05
#         self.dup = 0.3
#         self.Fdna = 0.5

#     def calc_cumulative_ratio(self,list_of_operations):
#         cumulative_weight = 0
#         for operation in list_of_operations:
#             mutation = operation[0]
#             mutation_type = mutation['Mut']
#             print(mutation_type)
#             #change to if statement, only works with python 3.10 and up
#             # match mutation_type:
#             if 'ins':
#                 cumulative_weight += self.ins
#             elif 'del':
#                 cumulative_weight += self.delete
#             elif 'dup':
#                 cumulative_weight += self.dup
#             elif 'FDNA':
#                 cumulative_weight += self.Fdna

#             #cumulative value for each mutation type?
#             #why are you such a bitch?

#         return cumulative_weight

class Cost:
    def __init__(self):
        self.weights = {'ins': 0.15, 'del': 0.05, 'dup': 0.3, 'F_DNA': 0.5}

    def calc_cumulative_ratio(self, list_of_operations):
        cumulative_weight = 0
        
        for operation in list_of_operations:

            mutation_type = operation[0]['Mut']

            cumulative_weight += self.weights.get(mutation_type, 0)

        return cumulative_weight



