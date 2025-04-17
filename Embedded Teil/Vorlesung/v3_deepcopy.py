import copy


def modify_list(lst):
    lst_copy = copy.deepcopy(lst)
    lst_copy.append(4)
    return lst_copy


# Ursprüngliche Liste
my_list = [1, 2, 3]

# Aufruf der Funktion
modified_list = modify_list(my_list)

# Ausgabe der veränderten Liste und der ursprünglichen Liste
print("Modified List:", modified_list)
print("Original List:", my_list)
