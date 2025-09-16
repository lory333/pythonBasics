zahl1 = float(input("Bitte die erste Zahl eingeben: "))
zahl2 = float(input("Bitte die zweite Zahl eingeben: "))

# Berechnungen
addition = round(zahl1 + zahl2, 2)
subtraktion = round(zahl1 - zahl2, 2)
multiplikation = round(zahl1 * zahl2, 2)

# Division prüfen, um Division durch Null zu vermeiden
if zahl2 != 0:
    division = round(zahl1 / zahl2, 2)
else:
    division = "nicht definiert (Division durch 0)"

# Ergebnisse ausgeben
print("Addition:", addition)
print("Subtraktion:", subtraktion)
print("Multiplikation:", multiplikation)
print("Division:", division)