import csv
def check_criteria(line):
    # sjekker at alle quizene er bestått
    if line[13:17].count("B") == 4:
        # sjekker om bestått kartleggingsprøve
        if line[1] == "B":
            # sjekker at 3 av 5 siste labber er bestått
            if line[8:13].count("B") >= 3:
                return True
        else:
            # sjekker om det er bestått minst 6 av 11 labber
            if line[2:13].count("B") >= 6:
                # sjekker deretter om 3 av 5 siste labber er bestått
                if line[8:13].count("B") >= 3:
                    return True
    else:
        return False

def students_who_passed(path):
    # tom liste som tar vare på student id
    student_id = list()
    # åpner filen
    file_open = open(path)
    # leser filen som liste
    file_read = list(csv.reader(file_open, delimiter=";"))
    for student in file_read:
        # sjekker om student oppfyller kravene
        if check_criteria(student):
            student_id.append(student[0])
    # returnerer en liste med studenter som sto
    return student_id

# print("Tester students_who_passed... ", end="")
# assert(['abc101', 'abc103', 'abc105', 'abc109', 'abc111', 'abc113'] 
#         == students_who_passed("lab6/course_data.csv"))
# print("OK")
