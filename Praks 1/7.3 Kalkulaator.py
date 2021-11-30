from easygui import *

# Arvud mida kalkuleerida
x1 = 0
x2 = 0
tulemus = 0

title = "Kalkulaator"
tekst_1 = "Sisestage esimene täisarv lõigus 1-10:"
tekst_2 = "Sisestage teine täisarv lõigus 1-10:"
nuppOK = "OK"

nupp_list = ["+", "-", "*"]

x1 = integerbox(tekst_1)
x2 = integerbox(tekst_2)

tehe = buttonbox("Valige tehe:", title, nupp_list)
if tehe == "+":
    tulemus = x1 + x2
elif tehe == "-":
    tulemus = x1 - x2
elif tehe == "*":
    tulemus = x1 * x2

msgbox("Tehte tulemus on " + str(tulemus), title)