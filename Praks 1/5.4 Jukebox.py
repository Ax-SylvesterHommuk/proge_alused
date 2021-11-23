open_file = str(input("Palun sisestage failinimi: "))
file = open(open_file, encoding="UTF-8")

laulude_arv = 0
laulu_list = []
rida = 0

for i in file:
    laulude_arv += 1
    laulu_list.append(str(i))
    print(str(laulude_arv) + ". " + i[:-1])
    
vali_laul = int(input("\nValige laulu järjekorranumber: "))

for i in laulu_list:
    rida += 1
    if vali_laul == rida:
        print("Mängitav muusikapala on " + i)
        
file.close()
    
    