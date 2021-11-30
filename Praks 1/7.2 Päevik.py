import os

from datetime import datetime
kuupäev_kellaaeg = datetime.today()

file = open("paevik.txt", encoding = "UTF-8")

file.write(str(kuupäev_kellaaeg))
file.write("\n")

file.write(sissekanne = str(input("Sisesta sissekande tekst: ")))
file.close()

