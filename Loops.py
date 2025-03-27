greetings = "Good Evening!"
a = 4

if a > 2:
    print("Condition matches")
    print("4 is greater than 2")
else:
    print("Condition do not match")
    print(" 2 is greater than 4")
print("if else condition match completed.")

#for loops
obj = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
for i in obj:
    print("Multiple of 2: ", i * 2)
    print("Multiple of 3: ", i * 3)
#Sum of first five natural number 1+2+3+4+5 = 15
summation = 0
for j in range(1, 6):
    summation = summation + j
print("Total is : ", summation)
print("*********************************************************")
for k in range(1, 17, 3):
    print(k)
print("*************Skipping First Index********************")
for m in range(5):
    print(m)