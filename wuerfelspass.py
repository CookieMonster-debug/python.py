# Import des Zufallsmoduls
import random

# Initialisierung des Counters
counter = 0

# Unendliche Würfelschleife, bis 30 Würfe erreicht sind
while counter < 30:
    # Würfeln und Ergebnis anzeigen
    wuerfel = random.randint(1, 6)
    print(f"Wurf {counter + 1}: Du hast eine {wuerfel} gewürfelt!")
    
    # Counter erhöhen
    counter += 1

# Nachricht, wenn die maximale Anzahl erreicht wurde
print("\nDas war's! Du hast 30-mal gewürfelt. 🎲")