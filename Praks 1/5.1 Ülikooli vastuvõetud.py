file = open("rebased.txt", encoding="UTF-8")
aasta = int(input("Palun sisestage, millise aasta andmeid vajate: "))

x_aasta = 2011

if aasta >= 2020:
    print(aasta, " aasta kohta ei ole veel andmeid.")
    
for aasta_rida in file:
    if aasta == x_aasta:
        print(x_aasta, " aastal oli vastuvõetuid ", aasta_rida)
        break
    x_aasta += 1
    
file.close()
            