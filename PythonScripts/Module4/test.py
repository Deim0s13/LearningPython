lst = []
with open("text.txt", "r") as f:
    lines = f.readlines()
    for i in range(2):
        lst.append(lines[i].rstrip())
print(lst)