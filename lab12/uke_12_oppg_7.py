def read_file_to_list(path):
    with open(path, "rt", encoding='utf-8') as f:
        file_content = f.read()
        list_content = list()
        for row in file_content.split("\n"):
            row = row.strip()
            list_content.append(row.split(" "))
    return list_content

def fastest_runner(path):
    list_runners = read_file_to_list(path)
    fastest = 10000
    for i in range(len(list_runners)):
        if int(list_runners[i][1]) < fastest:
            fastest = int(list_runners[i][1])
            answer = f"{list_runners[i][0]} {list_runners[i][1]}"
    return answer
