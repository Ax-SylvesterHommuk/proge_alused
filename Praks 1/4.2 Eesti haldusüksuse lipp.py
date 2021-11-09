from tkinter import *

# Sätted
title = Tk()
title.title("Maardu Lipp")
canvas = Canvas(width = 500, height = 500)

# Programm

title.geometry("700x660")
a = Canvas(title, width=700, height=230, bg="blue")
a.grid(row=0,column=0)
b = Canvas(title, width=700, height=230, bg="snow")
b.grid(row=1,column=0)
c = Canvas(title, width=700, height=230, bg="blue")
c.grid(row=2,column=0)

title.mainloop()
# Programmi Startimine
canvas.pack()