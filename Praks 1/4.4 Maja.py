from tkinter import *

root = Tk()
root.title("Maja")
c = Canvas(root)
c = Canvas(width = 600, height = 600) # Annab Canvase suuruse
c.pack()

# Maailm
c.create_rectangle(700, 0, 0, 1000, fill='#008fdb', outline="#008fdb")
c.create_rectangle(700, 450, 0, 1000, fill='green')

# Maja
c.create_rectangle(450, 600, 150, 250, fill='#a14e00')
c.create_rectangle(425, 600, 300, 375, fill='#6e3500')
c.create_rectangle(285, 475, 175, 390, fill='#00e6e6')
c.create_polygon(300, 250, 550, 250, 300, 3, fill="#c90000", outline="black")
c.create_polygon(50, 250, 550, 250, 300, 3, fill="#c90000", outline="black")

root.mainloop()
