import sys

x = dict()
with open(sys.argv[1], "r") as file1:
    for line in file1:
        line = line.strip()
        line = line.split(":")
        x[line[0]] = line[1]
    for student in sys.argv[2].split(","):
        try:
            print(f"Name: {student}, University: {x[student]}", end=" ")
            assert student in x.keys()
        except:
            print(f"No record of '{student}' was found!", end="")
