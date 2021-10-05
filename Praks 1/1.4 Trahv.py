print("Sisestage oma nimi: ")
nimi = input()

print("Sisestage lubatud kiirus (km/h): ")
a = int(input())

print("Sisestage tegelik kiirus (km/h): ")
b = int(input())

if b > a:
    c = b - a
    d = c * 3
else:
    d = 0

if d > 190:
    d = 190

print(nimi + ", kiiruse ületamise eest on teie trahv " + str(d) + " eurot.")