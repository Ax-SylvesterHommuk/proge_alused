ring_arv = int(input("Sisesta ringide arv: "))

a = 1
b = 0
porgandid = 0

while a < ring_arv:
    a = a + 5
    porgandid = porgandid + 5 + b
    b = b + 5

print("Porgandite kogu arv on " + str(porgandid) + ".")