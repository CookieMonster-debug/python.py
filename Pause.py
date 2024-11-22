import time
import webbrowser

# Begrüßung und Erklärung
print("Willkommen zu deinem Lernrhythmus Programm!")
print("Das Programm erinnert dich daran, nach 90 Minuten eine Pause zu machen.")
print("Während der Pause wird dein Lieblingslied abgespielt. Viel Erfolg beim Lernen!")

# Gesamtdauer des Arbeitstags
arbeitszeit = 8 * 60  # 8 Stunden in Minuten
pausenintervall = 90  # Alle 90 Minuten eine Pause
pausendauer = 7.5  # Pause dauert 7,5 Minuten

# Berechnung der Anzahl der Pausen
anzahl_pausen = arbeitszeit // pausenintervall

# Start des Lernprogramms
for pause_nummer in range(1, anzahl_pausen + 1):
    print(f"Arbeite jetzt {pausenintervall} Minuten lang.")
    time.sleep(pausenintervall * 60)  # Wartezeit für die Arbeitsphase (90 Minuten)

    # Pause
    print(f"Pause {pause_nummer}! Zeit, dich zu entspannen.")
    print(f"Dein Lieblingslied wird jetzt abgespielt!")
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")  # Link zu deinem Lieblingslied
    time.sleep(pausendauer * 60)  # Wartezeit für die Pausenphase (7,5 Minuten)

    print("Die Pause ist vorbei. Weiter geht's!")

# Ende des Programms
print("Dein Arbeitstag ist beendet. Gut gemacht!")
