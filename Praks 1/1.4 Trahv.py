nimi = str(input("Sisestage oma nimi: "))

a = int(input("Sisestage lubatud kiirus (km/h): "))
b = int(input("Sisestage tegelik kiirus (km/h): "))

c = min(190, ((b - a) * 3))

print(nimi + ", kiiruse ületamise eest on teie trahv " + str(c) + " eurot.")