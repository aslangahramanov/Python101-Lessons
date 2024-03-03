a = {"key": "value"}
a = {2: "value"}
a = {(1, 2, 3): "value"}

a = {(1, 2, 3): "Python"}
b = {"hobbies": {1,2,3}}


person = {"name": "Zehra", "age": 25}


# print(person.get("surname"))

# print(person)


person["name"] = "Revan"
person["age"] = 20
person["hobbies"] = ["Programming", "Football", "Music"]


hobbies = person.get("hobbies")


hobbies.append("Traveling")




# for k, v in person.items():
#     print(k , v)


# print(person)

# print(person.clear())

# print(person)




# x = ('key1', 'key2', 'key3')
# y = "0"

# thisdict = dict.fromkeys(y, x)

# print(thisdict)


# items = person.items()


# # print(list(items))

# for i in list(items):
#     print(i)


# print(person)


# person_surname = person.setdefault("surname", "Zulfizade")


# a = [1, 2, 3]

# print(a)
# print(a.pop())
# print(a)

# print(person.pop())
# print(person)


# print(person)
# print(person.popitem())
# print(person)


# print(person)
# person.update({"name": "Zulfizade"})
# # person["surname"] = "Zulfizade"
 
# print(person)


# person2 = person.copy()


# person3 = person

# print(id(person))
# print(id(person2))



# print(id(person))
# print(id(person3))



# a = [1, 2, 1, 3, 4]
# print(a)
# print(type(a))


# a = {1, 2, 1, 3, 4}
# print(a)
# print(type(a))


# print(set(a))


# a = {1, 2, 3, 4}
# print(a)


# a.add(5)
# a.add(6)


# a.pop()
# a.pop()


names = {"Revan", "Turqut", "Elnure"}

names2 = {"Zehra", "Aslan", "Ramal", "Revan"}

# names.remove("Zehra")

# a = names.discard("Zehra")


# # names.update(names2)
# names2.update(names)


# print(names)
# print(names2)



print(names2.intersection(names))
print(names2.union(names))
print(names2.difference(names))

