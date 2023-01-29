# del A
def compress(raw_binary):
    telle = 0
    for i in range(0,len(raw_binary)):
        if raw_binary[i] == raw_binary[i-1]:
            telle += 1
            
print(compress("0011100001111"))
print(compress("110111111110"))
