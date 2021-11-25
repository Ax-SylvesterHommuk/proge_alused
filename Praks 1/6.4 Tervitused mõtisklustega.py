def tervitus(külaliste_arv):
    for x in range(1, külaliste_arv + 1):
        print('Võõrustaja: "Tere!"')
        print("Täna " + str(x) + ". kord tervitada, mõtiskleb võõrustaja.")
        print('Külaline: "Tere, suur tänu kutse eest!"')
    
    
külaliste_arv = int(input("Sisestage külaliste arv: "))
tervitus(külaliste_arv)