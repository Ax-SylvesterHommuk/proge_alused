from tkinter import *

root = Tk()
myCanvas = Canvas(root)
myCanvas = Canvas(width = 600, height = 600) # Annab Canvase suuruse
myCanvas.pack()

def liiklusmärk(x, y, r, canvasName): # Function mis teeb liiklusmärgi (võta vastu x, y, r)
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    canvasName.create_oval(x0, y0, x1, y1, fill="red",outline ="black")
    canvasName.create_rectangle(500, 350, 100, 250, fill='white')


liiklusmärk(300, 300, 250, myCanvas)
root.mainloop()