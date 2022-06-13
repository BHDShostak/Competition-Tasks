
#RANK_LIST
#Everyone saw that James won. But nobody noticed who finished the run on second place. Fortunately, we have logs with names and positions.
#The problem is that there were thousands of runners and we need you to write a program that can find a runner-up for us.

#Input Format
#A single file "list.txt" having name and place on each line. Name is separated from place with semicolon.

#Output Format
#Name of runner-up

#Sample Input
#Peter Hass;3 , Julia Tiny;4 , Tomas Novak;2

#Sample Output
#Tomas Novak

#Explanation
#According to input file Tomas finished the run on second place therefore we print Tomas to the output.


runner_number = input(int())
filename = "list.txt"
newDict = {}

with open(filename) as f:
    for line in f:
        lst = line.strip().split(';')
        (key, val) = lst[0], " ".join(lst[1:])
        newDict[key] = val
print(newDict)
for key, value in newDict.items():
    if value == runner_number:
        print(key)
