import sys, os
import math 
from colorama import Fore,  Style
from colorama import init
init()

#clearconsole
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

clearConsole()

#rechenart auswahl
while True:
    try:
        print(Style.BRIGHT + Fore.BLUE + "1. Addition")
        print("2. Subtraktion")
        print("3. Multiplikation")
        print("4. Divison")
        print("5. Potenzen")
        print("6. Quadratwurzel")
        print()
        rechenart = int(input("Wähle deine Rechenart."))
        if rechenart not in (1, 2, 3, 4, 5, 6):
            raise ValueError
        break
    except ValueError:
        clearConsole()
        print(Fore.RED + "ERROR: Falscher Input.")
        print()
clearConsole()

#werte abfrage
while True:
    try:
        wert1 = float(input(Style.BRIGHT + Fore.BLUE + "Gebe den ersten Wert ein."))
        break
    except ValueError:
        clearConsole()
        print(Fore.RED + "ERROR: Falscher Input.")
        print()

clearConsole()

wert2 = 1
if rechenart < 5:
    while True:
        try: 
            wert2 = float(input(Style.BRIGHT + Fore.BLUE + "Gebe den zweiten Wert ein."))
            break
        except ValueError:
            clearConsole()
            print(Fore.RED + "ERROR: Falscher Input.")
            print()

clearConsole()

#rechnung
ergebnis_add = wert1 + wert2
ergebnis_sub = wert1 - wert2
ergebnis_mul = wert1 * wert2
ergebnis_div = wert1 / wert2
ergebnis_pot = wert1 ** wert2
ergebnis_wur = math.sqrt(wert1)

#output
if rechenart == 1:
    print(Fore.GREEN,wert1, "+", wert2, "=", ergebnis_add)

if rechenart == 2:
    print(Fore.GREEN,wert1, "-", wert2, "=", ergebnis_sub)

if rechenart == 3:
    print(Fore.GREEN,wert1, "x", wert2, "=", ergebnis_mul)

if rechenart == 4:
    print(Fore.GREEN,wert1, ":", wert2, "=", ergebnis_div)

if rechenart == 5:
    print(Fore.GREEN,wert1, "hoch", wert2, "=", ergebnis_pot)

if rechenart == 6:
    print(Fore.GREEN,"Die Quadratwurzel aus", wert1, "ist", ergebnis_wur)

print()

#restart?
while True:
    while True:
        answer = str(input(Fore.LIGHTMAGENTA_EX + "Neu starten? (y/n): "))
        if answer in ('y', 'n'):
            break
        clearConsole()
        print(Fore.RED + "ERROR: Falscher Input.")
        print()
    if answer == 'y':
        os.execl(sys.executable, sys.executable, *sys.argv)
    else:
        print("Tschüss.")
        break