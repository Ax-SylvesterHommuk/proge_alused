ring_arv = int(input("Sisesta ringide arv: "))

a = 1
x = 0
porgandid = 0

while ring_arv > 0:
    x += 1
    porgandid += a
    ring_arv -= 1; a += 1 + x

print("Porgandite kogu arv on " + str(porgandid) + ".")