def kuu_nimi(järjekorra_number):
    kuu_list  = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    return kuu_list[int(järjekorra_number) - 1]

def kuupäev_sõnana(kuupäev):
    kuupäevad = kuupäev.split(".")
    kuupäev = kuupäevad[0] + "." + kuu_nimi(kuupäevad[1]) + " " + kuupäevad[2] + ". a"
    return kuupäev

a = input("Sisesta kuupäev kujul DD.MM.YYYY: ")
print(str(kuupäev_sõnana(a)))

