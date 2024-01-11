name = input("What is your fist name?")

letter_count = 0

print(name, "is spelt:")
for x in name:
    print(x, end = ' ')
    letter_count += 1

print("")
print(letter_count, "letters in the name", name)
