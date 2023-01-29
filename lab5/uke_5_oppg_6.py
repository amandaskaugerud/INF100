from uke_05_oppg_1 import unique_values
def non_contigous_substrings(s):
    substring_list = [""]
    for c in s:
        len_substring_list = len(substring_list)
        for i in range(len_substring_list):
            ikss = substring_list[i]
            substring_list.append((ikss + c)) 
    return unique_values(substring_list)

# print("Tester non_contigous_substrings... ", end="")
# # Test 1
# # Merk: rekkefølgen på elementene i listen betyr ingenting,
# # siden begge listene sorteres før de sammenlignes
# assert(sorted([
#   "", # Den tomme strengen er alltid en substreng
#   "a", "b", "c", "d",
#   "ab", "ac", "ad", "bc", "bd", "cd",
#   "abc", "abd", "acd", "bcd",
#   "abcd",
# ]) == sorted(non_contigous_substrings("abcd")))

# # Test 2
# assert(sorted([
#   "",
#   "f", "o",  # Merk: "o" opptrer bare én gang
#   "fo", "oo",
#   "foo",
# ]) == sorted(non_contigous_substrings("foo")))
# print("OK")
