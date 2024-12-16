

try:
    print("hello team!!")
    print(10/0)
    print("hello panels!!")
except Exception as err:
    print(err)
else:
    print("no error in program, so its excuted")
finally:
    print("always i execute....")