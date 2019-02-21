'''
f = open("learningpython.txt", "w+")

f.write("In python, you can create lists.")
f.write("In python, you can create dictionaries.")
f.write("In python, you can create classese.")

f.close()
'''
with open("learningpython.txt", "r") as x:
    for z in x:
        print(z)

with open("learningpython.txt","r") as x:
    print(x.read)

list_stuff = [] 
with open("learningpython.txt","r") as learningpython:
    for line in learningpython:
        list_stuff.append(line)

for x in list_stuff:
    print(x)
