#read the file and store all the lines you read
#reverse the list
#write the list back to the file


with open("text.txt", 'r') as reader:
    content = reader.readlines()
    reversed(content)
    #print("Reversed file: ", content)
    with open("text.txt", 'w') as writer:
        for line in reversed(content):
           writer.write(line)
           print("Back to the original file: ", line)


