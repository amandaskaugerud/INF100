# oppg 1
# def will_work(city:str, salary:int)-> bool:
    # if city == "Bergen" and salary >= 400_000:
    #     return True
    # elif city == "Bodø" and salary >= 900_000:
    #     return True
    # elif city == "Verdensrommet":
    #     return True
    # elif salary >= 600_000 and city!= "Bodø":
    #     return True
    # return False


# oppg 2
# def mase_for_is():
    # svar = input("Kan jeg få en is?\n")
    # while True:
    #     if svar == "ja":
    #         print("Tusen takk!")
    #         break
    #     else:
    #         svar = input("Vær så snill, si ja!\n")
# mase_for_is()

# oppg 3
# def rotate(grid:list) -> list:
    # rotated_grid = []
    # for col in range(len(grid[0])):
    #     new_row = list()
    #     for row in range(len(grid)):
    #         new_row.append(grid[row][col])
    #     rotated_grid.append(new_row)
    # return rotated_grid

# oppg 4a
# def shopping_list_to_dict(shopping_list_as_string) -> dict:
#     shopping_list_as_dict = dict()
#     for line in shopping_list_as_string.splitlines():
#         value,key = line.split(" ")
#         shopping_list_as_dict[key] = int(value)
#     return shopping_list_as_dict

# oppg 4b
# def read_file(path):
#     with open(path, "rt", encoding='utf-8') as f:
#         return f.read()

# def shopping_list_file_to_dict(path) -> dict:
#     return shopping_list_to_dict(read_file(path))

# oppg 5
# def collatz_sequence(n):
    # sequence = [n]
    # while n > 1:
    #     if n % 2 == 0:
    #         n = n // 2
    #     else:
    #         n = 3 * n + 1
    #     sequence.append(n)
    # return sequence

# def collect_collatz(a,b):
    # collatz = dict()
    # for i in range(a,b):
    #     collatz[i] = collatz_sequence(i)
    # return collatz

# oppg 6
# def key_value_getter(d:dict):
#     print("Dictionary keys:")
#     for key in d.keys():
#         print(f"{key}")
#     print("\nDictionary values:")
#     for value in d.values():
#         print(f"{value}")
#     print("\nDictionary keys/values:")
#     for key, value in d.items():
#         print(f"{key} {value}")
#     return d
# key_value_getter({
#   "monday": 0,
#   "tuesday": 0.7,
#   "wednesday": 0,
#   "thursday": 4.7,
#   "friday": 10
# })

# oppg 7
# def weather_report(weather_stations, city):
    # wind_speed = weather_stations[city]["Wind speed"]
    # direction = weather_stations[city]["Wind direction"]
    # percipitation = weather_stations[city]["Precipitation"]
    # device = weather_stations[city]["Device"]
    # print(f"The weather in {city}:\nThe wind speed is {wind_speed}s in the {direction} direction and the precipitation is {percipitation}mm.\nThe measurement was done using the {device} weather station.")

# weather_stations = {
#     "Bergen": {
#         "Wind speed": 3.6,
#         "Wind direction": "northeast",
#         "Precipitation": 5.2,
#         "Device": "WeatherMaster500"
#     },
#     "Trondheim": {
#         "Wind speed": 8.2,
#         "Wind direction": "northwest",
#         "Precipitation": 0.2,
#         "Device": "ClimateDiscoverer3000"
#     },
#     "Svalbard": {
#         "Wind speed": 7.5,
#         "Wind direction": "southwest",
#         "Precipitation": 1.1,
#         "Device": "WeatherFinder5.0"
#     },
# }
# weather_report(weather_stations, "Bergen")

# oppg 8
# def word_comparison(s1:str,s2:str)->dict:
    # dict_words = dict()
    # common = set()
    # unique_s1 = set()
    # unique_s2 = set()
    # for i in range(len(s1)):
    #     print(s2[i] not in s1, s2[i])
    #     if s1[i] in s2:
    #         common.add(s1[i])
    #     elif s1[i] not in s2:
    #         unique_s1.add(s1[i])
    #     else:
    #         unique_s2.add(s2[i])
    # dict_words["In common"] = common
    # dict_words["Unique to first word"] = unique_s1
    # dict_words["Unique to second word"] = unique_s2
    # print(dict_words)
    # return dict_words
# print("Tester word_comparison... ", end="")
# assert({
#   "In common": {"e", "c"},
#   "Unique to first word": {"r", "u", "t", "p", "o", "m"},
#   "Unique to second word": {"s", "i", "n"},
# } == word_comparison("computer", "science"))
# print("OK")

# oppg 9
# def displayInventory(inventory:dict):
#     the_sum = 0
#     print("Inventory:")
#     for key, value in inventory.items():
#         print(f"{value} {key}")
#         the_sum += value
#     return the_sum


# oppg 10
# def addToInventory(inventory, addedItems):
#     copy_inventory = inventory.copy()
#     for item in addedItems:
#         if item in copy_inventory:
#             copy_inventory[item] += 1
#         else:
#             copy_inventory[item] = 1
#     return copy_inventory
