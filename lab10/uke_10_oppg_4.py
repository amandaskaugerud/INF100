def read_file(path):
    with open(path,"rt",encoding="utf-8") as f:
        return f.read()

def people_with_age(path,age):
    names = set()
    file_content = read_file(path)
    for line in file_content.splitlines():
        name_file, age_file = line.split()
        age_file = int(age_file)
        if age_file == age:
            names.add(name_file)
    return names
