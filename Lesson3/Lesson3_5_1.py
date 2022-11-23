import random

while True:
    y = int(input("enter"))
    x = random.randint(1, 2)

    if y == x:
        print("god job")
        break
    else:
        input("try again loser")
