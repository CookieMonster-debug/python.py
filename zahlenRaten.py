import random

# Begrüßung und Erklärung des Spiels
print("Ahoy, Matrose! Käpt’n Hook hat eine Zahl zwischen 1 und 100 versteckt.")
print("Errätst du die Zahl in 6 Versuchen, bekommst du seinen Schatz!")
print("Los geht's!")

# Zufällige Zahl zwischen 1 und 100 generieren
geheime_zahl = random.randint(1, 100)

# Anzahl der Versuche festlegen
versuche = 6

# Spiel starten
for i in range(versuche):
    print(f"\nVersuch {i + 1} von {versuche}")
    tipp = int(input("Gib deinen Tipp ein: "))

    if tipp < geheime_zahl:
        print("Zu niedrig, du Landratte!")
    elif tipp > geheime_zahl:
        print("Zu hoch!")
    else:
        print("Arrr! Du hast die geheime Zahl erraten! Käpt’n Hook gratuliert dir!")
        break
else:
    # Wenn alle Versuche verbraucht sind
    print(f"Game over! Die geheime Zahl war {geheime_zahl}. Käpt’n Hook lacht dich aus!")
5