# methods -> predefined set of codes focused to do specific operation.
# in built methods were availble in python while we installing
# these methods were built and vary based on datatypes

# two types -> 1. DataType Methods and 2. Common Methods

# DataTypes Methods -> String alone

#***** 1.capitalize, 2.upper,lower, 3.strip, 4.split, 5.index,count, 6.format, 7.join, 8.replace

########***** capitalize *****#######
name = "thaamarai kannan"
# # name = "Thaamarai kannan"
# capital_version = name.capitalize()

# print(name)
# print(capital_version)

########***** upper  and lower *****#######
# value = "pYthOn cLAsS"

# print(value)
# print(value.upper())
# print(value.lower()) 
# print(value.casefold()) 

########***** strip *****#######

# response = "   i have a benz car.    "
# print(len(response))
# print(response)
# print(len(response.strip()))
# print(response.strip())


########***** split *****#######

# fruits = "apple,orange,mosambi,grape,pineapple,cherry,strawberry"
# fruits_splited = fruits.split(",")
# print(fruits_splited)

########***** index and count *****#######

# value = "zee5"
# res = value.index("5")
# print(res)
value = "zee5ee and techiee"
# res = value.count("ee")
# print(res)

########***** format *****#######
fruits = ["apple", "orange", "grape", "pineapple"]
# count = len(fruits)
# value = "I have totally {} fruits in my basket {}"
# value = "I have totally {num} fruits in my basket {extra}"

# print(value.format(count, "and in my car"))
# print(value.format(extra="and in my car", num=count))

# print(f"I have totally {count} fruits in my basket {name}")


########***** join *****#######

# value = "123"
# response = "kannan"
# print(response.join(value))



########***** replace *****#######

print(value.replace("ee", "i"))