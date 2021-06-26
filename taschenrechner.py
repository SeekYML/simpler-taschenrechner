###############################################################################
#Diese Version beinhaltet keine Farben, wie auch den Dateipfad Fix            #
#aufgrund von Kombabilitätsproblemen mit repl.it und des Ersparen von         #
#herunterladen von Colorama nicht.                                            #
################################################################    imports   #               

import math

################################################################    rechenart auswahl

while True:
    try:
        print(" 1. Addition         2. Subtraktion")
        print(" 3. Multiplikation   4. Division")
        print(" 5. Potenzen         6. Quadratwurzel")
        print(" 7. Kubikwurzel      7. N-te Wurzel")
        print
        print(" 9. Taschenrechner schließen")
        print
        print(" Wähle die Rechenart aus.")
        rechenart = int(input(" USER: "))
        if rechenart not in (1, 2, 3, 4, 5, 6, 7, 8, 9):
            raise ValueError
        break
    except ValueError:
        print(" ERROR: Falscher Input.")
        print

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
            print(" ERROR: Falscher Input.")
            print


wert2 = 1
if rechenart < 6 or rechenart == 8:
    while True:
        try: 
            print(" Gebe den zweiten Wert ein. (n)")
            wert2 = float(input(" USER: "))
            break
        except ValueError:
            print(" ERROR: Falscher Input.")
            print


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
    print("%d + %d = %d" % (wert1,wert2,ergebnis_add))

if rechenart == 2:
    print("%d - %d = %d" % (wert1,wert2,ergebnis_sub))

if rechenart == 3:
    print("%d x %d = %d" % (wert1,wert2,ergebnis_mul))

if rechenart == 4:
    print("%d : %d = %d" % (wert1,wert2,ergebnis_div))

if rechenart == 5:
    print("%d^%d = %d" % (wert1,wert2,ergebnis_pot))

if rechenart == 6:
    print("Die Quadratwurzel aus %d ist %d" % (wert1,ergebnis_qwu))

if rechenart == 7:
    print("Die Kubikwurzel aus %d ist %d" % (wert1,ergebnis_kwu))

if rechenart == 8:
    print("Die %d.-te Wurzel aus %d ist %d" % (wert2,wert1,ergebnis_nwu))

################################################################    ENDE    
