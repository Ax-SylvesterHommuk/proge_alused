file_x = open("sisseränne.txt", encoding="UTF-8")
file_y = open("väljaränne.txt", encoding="UTF-8")

sisseränded = []
väljaränded = []
rändesaldo = []

for x in file_x:
    sisseränded.append(x)
file_x.close()

for y in file_y:
    väljaränded.append(y)
file_y.close()

i = 0
while i < 10:
    rändesaldo.append(int(sisseränded[i]) - int(väljaränded[i]))
    i += 1
print(rändesaldo)

if max(rändesaldo) > 0:
    print("Suurim positiivne rändesaldo oli " + str(i) + ". aastal.")
else:
    print("Positiivse rändesaldoga aastaid ei ole.")