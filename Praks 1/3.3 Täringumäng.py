import random

x = int(input("Täringute arv: "))

while x > 0:
    a = random.randint(1, 6)
    print(a)
    x -= 1