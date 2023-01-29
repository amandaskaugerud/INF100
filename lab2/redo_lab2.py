# # oppgave 1
# def find_longest_words(str1, str2, str3):
#     words = [str1, str2, str3]
#     longest = max(len(str1),len(str2),len(str3))
#     for i in range(len(words)):
#         if len(words[i]) >= longest:
#             print(words[i])

# # oppgave 2
# def is_leap_year(year: int) -> bool:
#     if year % 4 == 0:
#         if year % 100 == 0 and year % 400 != 0:
#             return False
#         else:
#             return True 
#     return False

# # oppg 3
# def human_to_dog_years(human):
#     if human <= 2:
#         dog = 10.5 *human
#     else:
#         first_years = 2 * 10.5
#         left_years = (human-2)*4
#         dog = first_years + left_years
#     return dog

# # oppg 4
# def find_first_longest_word(str1, str2, str3):
#     longest = max(len(str1), len(str2), len(str3))
#     if len(str1) == longest:
#         print(str1)
#     elif len(str2) == longest:
#         print(str2)
#     elif len(str3) == longest:
#         print(str3)
#     else:
#         print("nada")

# # oppg 5
# # del A
# def wavelength_to_color(nm: int) -> str:
#     if 380<=nm<=450:
#         return "Violet"
#     elif 450<=nm<=485:
#         return "Blue"
#     elif 485<=nm<=500:
#         return "Cyan"
#     elif 500<=nm<=565:
#         return "Green"
#     elif 565<=nm<=590:
#         return "Yellow"
#     elif 590<=nm<=625:
#         return "Orange"
#     elif 625<=nm<=750:
#         return "Red"
#     else:
#         return None

# # del B
# def frequency_to_color(THz: int) -> str:
#     Hz = THz * (10**12)
#     wavelength = (3e8)/Hz
#     nm_wavelength = wavelength * (10**9)
#     return wavelength_to_color(nm_wavelength)

# # del C
# def frequency_or_wavelength_to_color():
#     unit = input("Enter a unit (nm or THz):\n")
#     if unit == "nm":
#         value_nm = int(input("Enter a value in nm:\n"))
#         print()
#         if 380 <= value_nm <= 750:
#             print(wavelength_to_color(value_nm))
#         else:
#             print(f"There is no color with wavelength {value_nm} nm")
#     elif unit == "THz":
#         value_THz = int(input("Enter a value in THz:\n"))
#         print()
#         if 400 <= value_THz <= 790:
#             print(frequency_to_color(value_THz))
#         else:
#             print(f"There is no frequency {value_THz} THz")
#     else:
#         print()
#         print(f"The unit must be either nm or THz, it can not be {unit}")
# frequency_or_wavelength_to_color()

# # oppg 6
# def is_even_positive_int(x: int) -> bool:
#     if  type(x) == int and x > 0 and x % 2 == 0:
#         return True
#     return False

# # oppg 7
# def is_legal_triangle(side1: int or float, side2: int or float, side3: int or float) -> bool:
#     triangle = [side1, side2, side3]
#     for side in triangle:
#         if type(side) == str:
#             return False
#         else:
#             if side1 < side2 + side3 and side2<side1+side3 and side3< side1+side2:
#                 return True
#             else:
#                 return False

# # oppg 8
# # del A
# def point_in_rectangle(x0,y0,x1,y1,x2,y2):
#     x_left = min(x0,x1)
#     x_right = max(x0,x1)
#     y_top = max(y0,y1)
#     y_bottom = min(y0,y1)
#     if x_left <= x2 <= x_right and y_bottom <= y2 <= y_top:
#         return True
#     return False

