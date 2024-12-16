print("Code execution started")


def sum_of_num(data1):
    try:
        print("Function execution started")
        # c= data1/0
        # print(data2)
        c = data1[10]
        print("next line excuted.......")
    # except NameError:
    #     print("Name error in program")
    # except ZeroDivisionError:
    #     print("divide by zero error")
    except Exception as error:
        print(error)
    return 200

# my_val = sum_of_num(10)
my_val = sum_of_num("100")

print(my_val)
print("end of program")