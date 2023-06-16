from tkinter.ttk import Sizegrip


elozo=1
elozo_elotti=1

print(elozo)
print(elozo_elotti)

db=2
for i in range(2,41):
    osszeg=elozo+elozo_elotti
    print(osszeg, end='  ')
    elozo_elotti=elozo
    elozo=osszeg