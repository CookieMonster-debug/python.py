# Import des Zufallsmoduls
import random

print("🎲 Drücke Enter, um zu würfeln. Beende das Spiel mit 'q'.\n")

# Endlosschleife für wiederholtes Würfeln
while True:
    # Benutzer wartet auf Eingabe (Enter-Taste)
    eingabe = input()
    
    # Wenn "q" eingegeben wird, bricht das Spiel ab
    if eingabe == 'q':
        print("Spiel beendet. Danke fürs Spielen! 🎲")
        break
    
    # Zufallszahl zwischen 1 und 6 generieren
    wuerfel = random.randint(1, 6)
    
    # Ergebnis ausgeben
    print(f"Du hast eine {wuerfel} gewürfelt!")

