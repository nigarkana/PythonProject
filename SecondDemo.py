#List
values = [1, 2, "Mahid", 4, 5]
print(values)
print(values[0])
print(values[3])
print(values[-1])
print(values[1:3])
values.insert(3, "Shah")
print(values)
values.append("end")
print(values)
values[2] = "MAHID" #updating
print(values)
del values[0] #delete
print(values)

#tuple - same data types like list but immutable
val = (1, 2, 4, "Mahid", 7.5)
print(val)
print(val[1])
print(val[-1])

#Dictionary
dic = {"a":2, 4:"Mahid", 6:9, "c": "EID"}
print(dic)
print(dic["c"])

# Dynamically adding value in dictionary
dict = {}
dict["FirstName"] = "Mahad"
dict["LastName"] = "Mahid"
dict["MiddleName"] = "Uddin"
print(dict)
print(dict["MiddleName"])
