from easygui import *

# Arvud mida kalkuleerida
x1 = 0
x2 = 0
tulemus = 0

title = "Kalkulaator"

nupp_list = ["+", "-", "*"]

x1 = integerbox("Sisestage esimene täisarv lõigus 1-10:")
x2 = integerbox("Sisestage teine täisarv lõigus 1-10:")

tehe = buttonbox("Valige tehe:", title, nupp_list)
if tehe == "+":
    tulemus = x1 + x2
elif tehe == "-":
    tulemus = x1 - x2
elif tehe == "*":
    tulemus = x1 * x2

msgbox("Tehte tulemus on " + str(tulemus), title)