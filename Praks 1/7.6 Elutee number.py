def elutee(s):
    n = 0
    for i in s:
        if i != ".":
            n += int(i)
    if n < 10:
        return n
    else:
        return elutee(str(n))
    
# Elutee numbri vaatamine kuhu faili see panna
fail = open("sunnikuupaevad.txt", "r")
rida = fail.readlines()

for line in rida:
    elutee_num = elutee(str(line).replace("\n", ""))
    elutee_fail = open("eluteenumber" + str(elutee_num) + ".txt", "a")
    elutee_fail.write(str(line))
    elutee_fail.close()
    
    