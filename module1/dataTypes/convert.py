# Type Conversion:

# converting one data type into another data type

# tuple -> unchangeable ---> ** I NEED TO DO MODIFICATION **
# type conversion -> tuple -> list -> modification -> tuple


class_rooms = "cr-01", "cr-02", "cr-03", "cr-04", "cr-05"
print(class_rooms)
print(type(class_rooms))

print("\n")
# converting tuple into list

class_list = list(class_rooms)
class_list.append("cr-06")
print(class_list)
print(type(class_list))