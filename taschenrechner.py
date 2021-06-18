################################################################    imports
import sys, os
import math
from colorama import Fore,  Style
from colorama import init
init()

################################################################    clearconsole
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

clearConsole()

################################################################    rechenart auswahl
while True:
    try:
        print(Style.BRIGHT + Fore.BLUE + "1. Addition")
        print("2. Subtraktion")
        print("3. Multiplikation")
        print("4. Divison")
        print("5. Potenzen")
        print("6. Quadratwurzel")
        print("7. Kubikwurzel")
        print("8. N-te Wurzel")
        print()
        print("Wähle die Rechenart aus.")
        rechenart = int(input(Fore.WHITE + "USER: "))
        if rechenart not in (1, 2, 3, 4, 5, 6, 7, 8):
            raise ValueError
        break
    except ValueError:
        clearConsole()
        print(Fore.RED + "ERROR: Falscher Input.")
        print()
clearConsole()

################################################################    werte abfrage
while True:
    try:
        print(Style.BRIGHT + Fore.BLUE + "Gebe den ersten Wert ein. (x)")
        wert1 = float(input(Fore.WHITE + "USER: "))
        break
    except ValueError:
        clearConsole()
        print(Fore.RED + "ERROR: Falscher Input.")
        print()

clearConsole()

wert2 = 1
if rechenart == 6 or 7:
    while True:
        try: 
            print(Style.BRIGHT + Fore.BLUE + "Gebe den zweiten Wert ein. (n)")
            wert2 = float(input(Fore.WHITE + "USER: "))
            break
        except ValueError:
            clearConsole()
            print(Fore.RED + "ERROR: Falscher Input.")
            print()

clearConsole()

################################################################    rechnung
ergebnis_add = wert1 + wert2
ergebnis_sub = wert1 - wert2
ergebnis_mul = wert1 * wert2
ergebnis_div = wert1 / wert2
ergebnis_pot = wert1 ** wert2
ergebnis_qwu = math.sqrt(wert1)
ergebnis_kwu = wert1**(1/3)
ergebnis_nwu = wert1**(1/float(wert2))

################################################################    output 
if rechenart == 1:
    print(Fore.WHITE,wert1, "+", wert2, "=",Fore.GREEN, ergebnis_add)

if rechenart == 2:
    print(Fore.WHITE,wert1, "-", wert2, "=",Fore.GREEN, ergebnis_sub)

if rechenart == 3:
    print(Fore.WHITE,wert1, "x", wert2, "=",Fore.GREEN, ergebnis_mul)

if rechenart == 4:
    print(Fore.WHITE,wert1, ":", wert2, "=",Fore.GREEN, ergebnis_div)

if rechenart == 5:
    print(Fore.WHITE,wert1, "hoch", wert2, "=",Fore.GREEN, ergebnis_pot)

if rechenart == 6:
    print(Fore.WHITE,"Die Quadratwurzel aus", wert1, "ist",Fore.GREEN, ergebnis_qwu)

if rechenart == 7:
    print(Fore.WHITE, "Die Kubikwurzel aus", wert1, "ist",Fore.GREEN, ergebnis_kwu)

if rechenart == 8:
    print(Fore.WHITE, "Die", wert2,"-te Wurzel aus", wert1, "ist",Fore.GREEN, ergebnis_nwu)

print()

################################################################    restart?
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
        break

################################################################    ENDE    ################################################################