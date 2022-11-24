import random

x = random.randint(1, 3)
y = int(input("Угадай меня полностью"))
кол_во_попыток = 0
while x != y:
    кол_во_попыток += 1
    y = int(input("Try again loser"))
else:
    print("you win", кол_во_попыток)
