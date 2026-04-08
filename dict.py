
dog = {
    "name":"maciek",
    "bread":"husky",
    "legs":4,
    "age":10
}
values = dog.values()
print(values)


students_dict = {
    "first_name": "Szymon", 
    "last_name":"Zowczak", 
    "gender":"male", 
    "age":27, 
    "marital status":"middle", 
    "skills":["Python","C++"],  
    "country":"Poland", 
    "city":"Poznań", 
    "address":"Kasprowicza 12"
}

print(len(students_dict))

print(students_dict.get("skills"))

students_dict["skills"].append("C")

print(students_dict.get("skills"))

print(students_dict.values())
print(students_dict.keys())

list_of_tuples = list(students_dict.items())
print(list_of_tuples)

students_dict["skills"].pop()

print(students_dict.get("skills"))