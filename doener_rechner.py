# Begrüßung
print("🌯 Willkommen beim verbesserten Döner-Rechner! 🌯")

# 1. Döner-Typ auswählen
print("\n### Wähle deinen Döner ###")
print("1. Hähnchen-Döner")
print("2. Kalb-Döner")
print("3. Veggie-Döner")
doener_typ = int(input("Gib die Nummer des gewünschten Dönertyps ein (1, 2, 3): "))

# Döner-Namen basierend auf der Auswahl
if doener_typ == 1:
    doener_name = "Hähnchen-Döner"
elif doener_typ == 2:
    doener_name = "Kalb-Döner"
elif doener_typ == 3:
    doener_name = "Veggie-Döner"
else:
    doener_name = "Unbekannter Döner"
    print("Ungültige Auswahl. Wir machen trotzdem weiter!")

# 2. Anzahl der Döners eingeben
anzahl = int(input("\nWie viele Döner möchtest du bestellen? "))

# 3. Preis berechnen (unterschiedliche Preise)
if doener_typ == 1:
    preis_pro_doener = 6  # Hähnchen kostet 6 Euro
elif doener_typ == 2:
    preis_pro_doener = 7  # Kalb kostet 7 Euro
elif doener_typ == 3:
    preis_pro_doener = 5  # Veggie kostet 5 Euro
else:
    preis_pro_doener = 0  # Unbekannter Döner

total = anzahl * preis_pro_doener

# 4. Ausgabe der Bestellung und abschließende Nachricht
if preis_pro_doener > 0:
    print(f"\nDu hast {anzahl}x {doener_name} bestellt. Der Gesamtpreis beträgt: {total}€")
else:
    print(f"\n{anzahl}x {doener_name}. Leider konnte kein Preis berechnet werden, da die Auswahl ungültig war.")

name = input("\nWie heißt du? ")
print(f"Danke, {name}, für deine Bestellung! Afiyet olsun! 🍽️")

