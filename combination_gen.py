import copy
import csv


def gen_comb_list(list_set):
    if len(list_set) == 1:
        start_list = []
        for item in list_set[0]:
            start_list.append([item])
        return start_list
    comb_list_temp = gen_comb_list(list_set[0:-1])
    start_list = []
    for list_item in comb_list_temp:
        for val in list_set[-1]:
            temp_item = copy.deepcopy(list_item)
            temp_item.append(val)
            start_list.append(temp_item)
    return start_list

# print("Test gen_comb_list")
# x = [1, 2, 3]
# y = [4, 5]
# z = [6, 7, 8]
# u = [9, 10]
# comb_list = gen_comb_list([x])
# print(comb_list, len(comb_list), [x])
# comb_list = gen_comb_list([x, y])
# print(comb_list, len(comb_list), [x, y])
# comb_list = gen_comb_list([x, y, z])
# print(comb_list, len(comb_list), [x, y, z])
