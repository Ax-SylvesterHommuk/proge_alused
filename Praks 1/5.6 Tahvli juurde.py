from datetime import *
file = open(input("Sisestage failinimi: "), encoding="UTF-8")
nimekiri = []
for i in file:
    nimekiri.append(i)
print("Vastama tuleb: " + str(nimekiri[int(datetime.now().day) - 1]))
file.close()