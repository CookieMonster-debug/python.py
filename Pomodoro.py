import time
import webbrowser

# Begrüßung und Erklärung
print("Willkommen zur Pomodoro-Methode!")
print("Du kannst deine Lernzeit und die Länge der Lern- und Pausenzeiten individuell einstellen.")

# Benutzereingaben für die Einstellungen
gesamtlernzeit = int(input("Wie viele Minuten möchtest du insgesamt lernen? "))
arbeitszeit = int(input("Wie viele Minuten möchtest du am Stück arbeiten? "))
pausendauer = int(input("Wie viele Minuten soll eine Pause dauern? "))

# Berechnung der Anzahl der Pomodoro-Zyklen
zyklen = gesamtlernzeit // (arbeitszeit + pausendauer)

print(f"\nDu wirst insgesamt {zyklen} Arbeits- und Pausenzyklen absolvieren.")
print("Das Programm beginnt jetzt. Viel Erfolg!")

# Start der Pomodoro-Zyklen
for zyklus in range(1, zyklen + 1):
    print(f"\nZyklus {zyklus}: Arbeite jetzt {arbeitszeit} Minuten.")
    time.sleep(arbeitszeit * 60)  # Arbeitszeit in Sekunden

    print(f"\nPause {zyklus}: Entspanne dich für {pausendauer} Minuten.")
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")  # Link zu deinem Lieblingslied
    time.sleep(pausendauer * 60)  # Pausendauer in Sekunden

print("\nLernzeit beendet! Gute Arbeit, du hast es geschafft!")
