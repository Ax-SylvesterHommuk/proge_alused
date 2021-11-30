import requests

kuu = str(input("Sisestage kuu: "))
päev = int(input("Sisestage päev: "))

url = 'http://kodu.ut.ee/~eno/mooc/' + str(kuu)
output = requests.get(url).text
data = output.splitlines()

x = 0

for line in data:
    x += 1
    if x == päev:
        print("Kuupäeval " + str(päev) + ". " + str(kuu) + " on nimepäevad järgmiste nimedega inimestel:")
        print(line)