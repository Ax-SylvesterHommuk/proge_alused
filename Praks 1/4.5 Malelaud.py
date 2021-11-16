from tkinter import *
raam = Tk()
raam.title("Malelaud")

tahvel = Canvas(raam, width = 800, height = 800)

# Sätted malele
x1 = 0
y1 = 0

x2 = 100
y2 = 100

# i on vaja mustade ja valgede ruudude vahetamiseks, j sama moodi.
i = 0
j = 1

# OR listid, lihtsalt, et kood pikk ei oleks.
list_x = [0, 2, 4, 6, 8]
list_y = [0, 2, 4, 6]

while y2 <= 800:
    while x2 <= 800:
        if (i in list_x):
            tahvel.create_rectangle(x1, y1, x2, y2, fill="white", outline="white")
        else:
            tahvel.create_rectangle(x1, y1, x2, y2, fill="black", outline="black")

        i += 1
        x1 += 100
        x2 += 100
        
    y1 += 100
    y2 += 100
    
    x1 = 0
    x2 = 100
    
    if (j in list_y):
        i = 0
    else:
        i = 1
    
    j += 1
        
tahvel.pack()
raam.mainloop()