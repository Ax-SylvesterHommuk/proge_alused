def pronksikarva_summa(täisarv):
    sentide_arv = 0
    for i in täisarv:
        if int(i) <= 5:
            sentide_arv += int(i)
    return sentide_arv

file = open(input("Sisestage failinimi: "), encoding="UTF-8")
print("Hoiupõrsasse läheb", pronksikarva_summa(file), "senti.")
file.close()
