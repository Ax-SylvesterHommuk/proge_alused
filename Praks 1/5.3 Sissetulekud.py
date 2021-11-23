fail = open("konto.txt", encoding="UTF-8")
for a in fail:
    if float(a) > 0:
        print(a[:-1])
fail.close()
