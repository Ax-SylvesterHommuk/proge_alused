from datetime import datetime
kuupäev_kellaaeg = datetime.today()

file = open("paevik.txt", "a")

file.write(str(kuupäev_kellaaeg))
file.write("\n")
file.write(str(input("Sisesta sissekande tekst: ")))
file.write("\n\n")

file.close()

