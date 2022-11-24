name = input("enter you name")
while True:
    try:
        age=int()
    except ValueError:
        print("try again")
    age = int(input("enter you age"))
    if  age <= 0:
        print("mistake")
    elif age<10:
        print ("junior")
        break
    elif age<20:
        print("Hello old men")
        break
    elif age>20:
        print("what do you want?")
        break
    elif age<=100:
        print("what do you want?")
        break
    else:
        print ("end")








