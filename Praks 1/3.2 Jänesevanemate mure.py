ringide_arv = int(input("Sisesta ringide arv: "))

a = 1
b = 0
porgandid = 0

while a < ringide_arv:
    a = a + 2
    porgandid = porgandid + 2 + b
    b = b + 2
    
print("Porgandite koguarv on " + str(porgandid) + " .")