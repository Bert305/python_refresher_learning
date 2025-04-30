student = {"Name" : "Bert", "age" : 30, "email" : "bert@gmail.com", "enrolled" : True}


print(student["Name"])

print(student["age"])

print(len(student))


for data in student:
    print(f"{data} : {student[data]}")
    
    
    
colors = {"color1" : "red" , "color2" : "green", "color3" : "black"}

colors["color3"] = "orange"

print(colors)


# keys and values

shopping_list = {'jewelry': 'earrings', 'clothes': 'jeans', 'budget': 200}
 
print(shopping_list.keys()) # returns dict_keys(['jewelry', 'clothes', 'budget'])
print(list(shopping_list.keys())) # returns ['jewelry', 'clothes', 'budget']
print(shopping_list.values()) # returns dict_values(['earrings', 'jeans', 200])