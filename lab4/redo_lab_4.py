# #  oppg 1
# def insert_at(source_string: str, index: int, insertion_string: str) -> str:
#     split_start = source_string[:index]
#     split_end = source_string[index:]
#     return split_start + insertion_string + split_end

# # oppg 2
# def rotate_string(s,k):
#     k = k%len(s)
#     return s[k:] + s[:k]

# # oppg 3
def find_nth_occurence(search_string: str, character: str, n: int) -> str:
    occurence = 0
    for i in range(len(search_string)):
        if search_string[i] == character:
            occurence += 1
            if occurence == n:
                return i
    return -1

# # oppg 4a
# def good_style(source_code) -> bool:
#     for line in source_code.splitlines():
#         if len(line) >= 80:
#             return False
#     return True

# # oppg 4b
# def good_style_from_file(filename) -> bool:
#     with open(filename, "rt", encoding='utf-8') as f:
#         file = f.read()
#     return good_style(file)

# # oppg 5
# def get_common_symbols(s1, s2) -> str:
#     common_symbols = str()
#     for i in range(len(s1)):
#         if s1[i] in s2:
#             if s1[i] not in common_symbols:
#                 common_symbols += s1[i]
#     return common_symbols

# # oppg 6
# def mix(s1: str, s2: str) -> str:
#     mix_string = str()
#     longest_str = max(len(s1), len(s2))
#     for i in range(longest_str):
#         if i in range(len(s1)):
#             mix_string += s1[i]
#         if i in range(len(s2)):
#             mix_string += s2[i]
#     return mix_string

# oppg 7a
def get_impact(line: str) -> str:
    second_occur = find_nth_occurence(line,";",2)
    third_occur = find_nth_occurence(line, ";", 3)
    impact = line[second_occur+1:third_occur]
    return float(impact)

# oppg 7b
def filter_earthquakes(earthquake_csv_string, threshold):
    title_line = int(earthquake_csv_string.find("\n"))
    no_title_earthquake_csv_string = earthquake_csv_string[title_line+1:]
    answer = earthquake_csv_string[0:title_line+1]
    for line in no_title_earthquake_csv_string.splitlines():
        if get_impact(line) > threshold:
            answer += line + "\n"
    return answer

# oppg 7c

def read_file(path):
    """ Given the file path (file name) of a plain text file, returns
    the content of the file as a string. """
    with open(path, "rt", encoding='utf-8') as f:
        return f.read()

def write_file(path, contents):
    """ Writes the contents to the file with the given file path. If
    the file does not exist, it will be created. If the file does
    exist, its old content will be overwritten. """
    with open(path, "wt", encoding='utf-8') as f:
        f.write(contents)

def filter_earthquakes_file(source_filename, target_filename, threshold):
    file_content = read_file(source_filename)
    write_file(target_filename, filter_earthquakes(file_content, threshold))

print("Tester filter_earthquakes_file... ", end="")
filter_earthquakes_file("lab4/earthquakes_simple.csv",
                        "lab4/earthquakes_above_7.csv", 7.0)
expected_value = """\
id;location;impact;time
us100068jg;Northern Mariana Islands;7.7;2016-07-29 17:18:26
us10006d5h;New Caledonia;7.2;2016-08-11 21:26:35
us10006exl;South Georgia Island region;7.4;2016-08-19 03:32:22
"""
assert(expected_value == read_file("lab4/earthquakes_above_7.csv"))
print("OK")

# Manuell test: Finn earthquakes_above_7.csv, åpne og se at innholdet stemmer
