file = open('text.txt')

#print only two character from the beginning of the line
#print(file.read(2))

#read a single line at a time
# print(file.readline())
# print(file.readline())


#print all the lines using while loop
# line = file.readline()
# while line!= "":
#     print(line)
#     line = file.readline()


#print all lines using the below method and it will generate a LIST data type
for line in file.readlines():
    print(line)

file.close()

