import random

vaja_õunu = int(input("Mitu pöialpoissi tahab õunu? "))

õunad = 14

while vaja_õunu > 0:
    x = random.randint(1, 2)
    print(x)
    õunad -= x; vaja_õunu -= 1
    
print("Lumivalgekesele jäi " + str(õunad))
