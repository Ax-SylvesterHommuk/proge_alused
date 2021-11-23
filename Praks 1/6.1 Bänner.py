kuvamised = int(input("Mitu korda soovite reklaamlauset kuvad? "))
sõnum = str(input("Sisestage reklaamlause: "))
def banner(sõnum, kuvamised):
    while kuvamised > 0:
        print(sõnum.upper())
        kuvamised -= 1
    
banner(sõnum, kuvamised)
    