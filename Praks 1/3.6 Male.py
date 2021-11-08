ruut_arv = int(input("Sisestage täisarv: "))

i = ruut_arv
nisuteri = 1

while ruut_arv > 0:
    nisuteri += nisuteri * 2
    ruut_arv -= 1

print("Nisuteri " + str(i) + ". ruudu eest: " + str(nisuteri))
    