my_cars = ["tesla", "audi"]

def program1(fname, lname, age, dept= "IMS"):
    # print(fname, lname, age, dept)
    if age > 18:
        print("Major")
    return 200, {"name": f"{fname} {lname}"}, dept


print(my_cars)
function_res = program1("s", "kannan", 20)
print(function_res)
function_res = program1("Vairavel", "V", 20)
print(function_res)
function_res = program1("Dhanush", "M", 20, "Cyber")
print(function_res)