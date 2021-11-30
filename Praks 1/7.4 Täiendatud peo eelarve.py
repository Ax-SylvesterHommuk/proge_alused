def eelarve(külalised):
    rent = 55
    summa = külalised * 10 + rent
    return summa

tulijad = 0
ma_ei_tea_inimesed = 0

file = open(input("Sisestage failinimi: "), "r")

for line in file:
    for char in line:
        if char == "+":
            tulijad += 1
        elif char == "?":
            ma_ei_tea_inimesed += 1

kokku_inimesed = tulijad + ma_ei_tea_inimesed

print("Kutsutud on", kokku_inimesed, "inimest")
print(tulijad, "inimest tuleb")
print("Maksimaalne eelarve:", eelarve(kokku_inimesed), "EUR")
print("Minimaalne eelarve:", eelarve(tulijad), "EUR")            