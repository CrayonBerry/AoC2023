import re

puzzleFile = open("C:\Users\NimbusDDOS\AoC-Projects\Day1\puzzle.txt", 'r')
lines = puzzleFile.readlines()

total = 0
for line in lines:
    #returns a list of each number in each line
    num = re.findall(r'\d+', line)
    #combine the numbers of the list into a single string
    numstring = ''.join(num)
    #pull out the first and last numbers of the string
    first = numstring[0]
    last = numstring[-1]
    #sum the first and last digits for each line together and add them to total
    total += int(first + last)
    print(total)