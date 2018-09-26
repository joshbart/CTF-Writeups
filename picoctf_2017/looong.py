letter = raw_input("Enter the letter specified: ")
number = raw_input("Enter the number of interations: ")

for n in range(int(number) - 1):
    string += letter

print(string)