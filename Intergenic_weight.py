from new_Node import  Node
import Network_wrDCJ
from Rearrangement_extremities_and_adjacencies import Extremities_and_adjacencies





list_of_legal_operations = Node.get_legal_operations()


def intergenic_weight(intergenic_length, list_of_legal_operations, operation_weight):

    for operation in list_of_legal_operations:
        if intergenic_length in operation >= 5:
            new_operation_weight =  0.6 *[operation_weight]
        else:
            new_operation_weight = 0.4 * [operation_weight]
            print(new_operation_weight)

    return new_operation_weight




