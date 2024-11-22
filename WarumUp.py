import time
import random
import webbrowser

def zahlenraten():
    """Ein kleines Zahlenratespiel."""
    print("\nWillkommen zum Zahlenratespiel!")
    print("Ich denke mir eine Zahl zwischen 1 und 10. Kannst du sie erraten?")
    
    # Zufällige Zahl generieren
    geheimzahl = random.randint(1, 10)
    versuche = 0

    while True:
        versuche += 1
        tipp = int(input("Dein Tipp: "))
        
        if tipp == geheimzahl:
            print(f"Glückwunsch! Du hast die Zahl {geheimzahl} nach {versuche} Versuch(en) erraten!")
            break
        elif tipp < geheimzahl:
            print("Zu niedrig! Versuch es noch einmal.")
        else:
            print("Zu hoch! Versuch es noch einmal.")
    
    print("Danke fürs Spielen! Jetzt zurück zum Programm.")

def main():
    # Begrüßung und Erklärung
    print("Willkommen zu deinem Work-Life-Balance-Programm!")
    print("Nach dem Lied kannst du ein Warm-Up spielen, wenn du möchtest.")
    
    # Frage den Benutzer nach Gesamtlernzeit und Intervallen
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
        
        # Pause
        print(f"\nPause {zyklus}: Entspanne dich für {pausendauer} Minuten.")
        print(f"Dein Lieblingslied wird jetzt abgespielt!")
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")  # Link zu deinem Lieblingslied
        time.sleep(pausendauer * 60)  # Pausendauer in Sekunden
        
        # Warm-Up Frage
        spielen = input("\nMöchtest du ein kleines Warm-Up-Spiel spielen? (ja/nein): ").strip().lower()
        if spielen == "ja":
            zahlenraten()
        else:
            print("Kein Problem! Weiter geht's mit dem nächsten Zyklus.")
    
    print("\nLernzeit beendet! Gute Arbeit, du hast es geschafft!")

# Starte das Hauptprogramm
main()
