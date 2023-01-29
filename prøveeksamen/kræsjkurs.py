# xs = [12, 34, 15, 23, 11, 64]
# # list comprehension
# odde_x = [x for x in xs if x%2==1]
# print(odde_x)

# navn = "Amanda"
# alder = 18
# print(f"My name is {navn} and I am {alder} years")

# # printer både variabel og verdi
# print(f"{navn = }{alder = }")

# import math
# pi = math.pi
# # printer med f-string kun 4 desimaler for math.pi
# print(f"Pi er {pi:.4f}")

# def info(name:str, age: int):
#     return f"My name is {name} and I am {age} years"
# print(info("Christoffer", 24))
# # Try/except 
# def divide(x,y):
#     return x/y
# try:
#     print(divide(10,0))
# except ZeroDivisionError:
#     print(f"Error, kan ikke dele på null")

# try:
#     print(divide(10,0))
# except Exception as e:
#     print(f"Error: {e}")
# path = "handleliste.txt"
# with open(path, "rt", encoding='utf-8') as file:
#     read = file.read()
# print(read)
# input("Trykk enter for neste")
# # åpner og leser filen til en liste
# with open(path, "rt", encoding='utf-8') as file:
#     linjer = file.readlines()
#     # linjer = [s.strip() for s in file.readlines()]
# print(linjer)
# input("Trykk enter for list comprehension")
# print([s.strip() for s in linjer])

def les_fil(path):
    with open(path, "r") as file:
        linjer = file.readlines()
    linjer = [linje.strip().split(";") for linje in linjer]
    return linjer
# kommune/fylke er 5
# ADMIN1 er 7
# befolkning er 9

def get_admin_code(fylke,data):
    admin1 = str()
    for linje in data:
        if linje[1] == fylke:
            admin1 = linje[7]
    return admin1

def get_county_name(admin1, data):
    admin = str()
    for linje in data:
        if linje[7] == admin1:
            return linje[1]
    return admin

if __name__ == "__main__":
    fil = "prøveeksamen/NO_ADM12.csv"
    data = les_fil(fil)
    print(get_county_name(data[440][7], data))
