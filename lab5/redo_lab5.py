# # oppg 1a
# def remove_threes(a):
#     while (3 in a):
#         a.remove(3)
#     return a

# # oppg 1b
# def every_fourth(a):
#     new_list = list()
#     for i in range(0,len(a),4):
#         new_list.append(a[i])
#     return new_list

# # oppg 1c
# def halve_values(a):
#     for i, item in enumerate(a):
#         a[i] = item*0.5
#     return a

# # oppg 1d
# def unique_values(a):
#     unique_value_list = list()
#     for value in a:
#         if value not in unique_value_list:
#             unique_value_list.append(value)
#     return unique_value_list

# # oppg 1e
# def add_list(a,b):
#     for i in range(len(a)):
#         a[i] = a[i] + b[i]
#     return a, b

# # oppg 3
# def sort_by_sign(a: list) -> list:
#     sorted_by_sign = list()
#     negative_values = list()
#     zero_values = list()
#     positive_values = list()
#     for i in range(len(a)):
#         if a[i] < 0:
#             negative_values.append(a[i])
#         if a[i] == 0:
#             zero_values.append(a[i])
#         if a[i] > 0:
#             positive_values.append(a[i])
#     sorted_by_sign.extend(negative_values)
#     sorted_by_sign.extend(zero_values)
#     sorted_by_sign.extend(positive_values)
#     return sorted_by_sign

# # oppg 4
# def read_and_sort():
#     unsorted_list = list()
#     while True:
#         answer = int(input())
#         if answer == 0:
#             print()
#             break
#         else:
#             unsorted_list.append(answer)
#     sorted_list = sorted(unsorted_list)
#     for element in sorted_list:
#         print(element)
# read_and_sort()

# # oppg 5
# def complement(seq):
#     complement_seq = " "
#     for letter in seq:
#         if letter == "A":
#             complement_seq += "T"
#         elif letter == "C":
#             complement_seq += "G"
#         elif letter == "T":
#             complement_seq += "A"
#         elif letter == "G":
#             complement_seq += "C"
#     return complement_seq[::-1].strip()

# # oppg 6
# def non_contigous_substrings(s):
#     # tom liste som skal returneres
#     substring_list = [""]
#     # løper gjennom s, bokstav for bokstav
#     for c in s:
#         # finner lengden av resultat listen
#         len_substring_list = len(substring_list)
#         # løper gjennom indeksene til listen
#         for i in range(len_substring_list):
#             # substrengen er lik elementet på indeks i
#             ikss = substring_list[i]
#             # legger til substrengen + bokstaven fra iterasjon
#             substring_list.append((ikss + c)) 
#     return unique_values(substring_list)

