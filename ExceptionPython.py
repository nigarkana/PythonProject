from logging import exception

itemInCart = 0

if itemInCart!= 2:
    #raise Exception("Cart is empty and count does not match")
    pass
assert(itemInCart == 0)

try:
    with open("text1.txt", 'r') as reader:
        reader.read()
except:
    print("this code will pass though it has issue in the file name")

try:
    with open("text1.txt", 'r') as reader:
        reader.read()
except Exception as e:
    print(e)

finally:
    print("Cleaning up resources")
