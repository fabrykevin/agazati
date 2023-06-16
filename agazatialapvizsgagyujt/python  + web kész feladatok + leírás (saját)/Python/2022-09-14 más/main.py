# menüvezérelt program
# testek (pl.: gömb, hasáb... stb) felszínét és térfogatát
# számolja ki

# from menu import *
from menu import foMenu, felszinVagyTerfogat
from teglatest import teglatestFelszin, teglatestTerfogat
from gomb import gombFelszin, gombTerfogat

tipus = -1
while tipus != 0:
    tipus = foMenu()

    if tipus != 0:
        va = felszinVagyTerfogat()

        if va != 'X':
            if tipus == 1 and va == 'A':
                teglatestFelszin()
            elif tipus == 1 and va == 'V':
                teglatestTerfogat()
            elif tipus == 2 and va == 'A':
                gombFelszin()
            elif tipus == 2 and va == 'V':
                gombTerfogat()

