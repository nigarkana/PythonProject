

str1 = "Mahid is sleeping"
str2 = "Mahid has a sound and good dream"
str3 = "Mahid&has"
print(str1[1])
print(str1 + "," +" "+ str2)

print(str1[3])
print("String range printing Mahid to Mah:", str1[:3])
print("String range printing for index 1 to index 7: ", str1[1:7])
print(str3 in str2) #to check the string is present or not in the main string

str1.insert(6, "Shah")
print(str1)

splitTest = str3.split("&")
print(splitTest[0])
str4 = " Masud "

print(str4.strip()) #lstrip and rstrip means to remove space from left and right


