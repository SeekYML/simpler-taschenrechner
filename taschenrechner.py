###############################################################################
#Diese Version beinhaltet keine Farben, wie auch den Dateipfad Fix            #
#aufgrund von Kombabilitätsproblemen mit repl.it und des Ersparen von         #
#herunterladen von Colorama nicht.                                            #
################################################################    imports   #               

import os, sys, math

################################################################    gui

os.system("title Simpler Taschenrechner")

cmd = 'mode 67,14'
os.system(cmd)

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
        print(" 1. Addition")
        print(" 2. Subtraktion")
        print(" 3. Multiplikation")
        print(" 4. Divison")
        print(" 5. Potenzen")
        print(" 6. Quadratwurzel")
        print(" 7. Kubikwurzel")
        print(" 8. N-te Wurzel")
        print(" 9. Taschenrechner schließen")
        print(" Wähle die Rechenart aus.")
        print()
        rechenart = int(input(" USER: "))
        if rechenart not in (1, 2, 3, 4, 5, 6, 7, 8, 9):
            raise ValueError
        break
    except ValueError:
        clearConsole()
        print(" ERROR: Falscher Input.")
        print()
clearConsole()

################################################################    werte abfrage

if rechenart == 9:
    exit(0)

if rechenart < 9:
    while True:
        try:
            print(" Gebe den ersten Wert ein. (x)")
            wert1 = float(input(" USER: "))
            break
        except ValueError:
            clearConsole()
            print(" ERROR: Falscher Input.")
            print()

clearConsole()

wert2 = 1
if rechenart < 6 or rechenart == 8:
    while True:
        try: 
            print(" Gebe den zweiten Wert ein. (n)")
            wert2 = float(input(" USER: "))
            break
        except ValueError:
            clearConsole()
            print(" ERROR: Falscher Input.")
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
    print(wert1, "+", wert2, "=",ergebnis_add)

if rechenart == 2:
    print(wert1, "-", wert2, "=",ergebnis_sub)

if rechenart == 3:
    print(wert1, "x", wert2, "=",ergebnis_mul)

if rechenart == 4:
    print(wert1, ":", wert2, "=",ergebnis_div)

if rechenart == 5:
    print(wert1, "hoch", wert2, "=",ergebnis_pot)

if rechenart == 6:
    print("Die Quadratwurzel aus", wert1, "ist",ergebnis_qwu)

if rechenart == 7:
    print("Die Kubikwurzel aus", wert1, "ist",ergebnis_kwu)

if rechenart == 8:
    print("Die", wert2,"-te Wurzel aus", wert1, "ist",ergebnis_nwu)

print()

################################################################    restart?

while True:
    while True:
        answer = str(input(" Neu starten? (y/n): "))
        if answer in ('y', 'n'):
            break
        clearConsole()
        print(" ERROR: Falscher Input.")
        print()
    if answer == 'y':
        print("Restarting ...")
        os.execl(sys.executable, sys.executable, *sys.argv)
    else:
        exit()

################################################################    ENDE    
