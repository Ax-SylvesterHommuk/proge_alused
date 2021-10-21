inimesed = int(input("Sisesta inimeste arv: "))
kohad_ühes_bussis = int(input("Sisesta kohtade arv ühes bussis: "))

bussid = inimesed // kohad_ühes_bussis

maha_jäänud = inimesed % kohad_ühes_bussis

print(maha_jäänud)