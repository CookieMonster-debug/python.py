import time
import random
import webbrowser

def zahlenraten():
    """Ein kleines Zahlenratespiel."""
    print("\nWillkommen zum Zahlenratespiel!")
    print("Ich denke mir eine Zahl zwischen 1 und 10. Kannst du sie erraten?")
    
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
    print("Nach jeder Pause kannst du ein Warm-Up-Spiel spielen, wenn du möchtest.")
    
    # Eingabe von Arbeitszeit, Pausendauer und Gesamtlernzeit
    gesamtlernzeit = int(input("Wie viele Minuten möchtest du insgesamt lernen? "))
    arbeitszeit = int(input("Wie viele Minuten möchtest du am Stück arbeiten? "))
    pausendauer = int(input("Wie viele Minuten soll eine Pause dauern? "))
    
    # Berechnung der Anzahl der Zyklen
    zyklen = gesamtlernzeit // (arbeitszeit + pausendauer)
    print(f"\nDu wirst insgesamt {zyklen} Arbeits- und Pausenzyklen absolvieren.")
    print("Das Programm beginnt jetzt. Viel Erfolg!")
    
    # Zähler für Pausen und Arbeitszeit
    pausen_zaehler = 0
    gesamte_arbeitszeit = 0
    
    # Start der Pomodoro-Zyklen
    for zyklus in range(1, zyklen + 1):
        print(f"\nZyklus {zyklus}: Arbeite jetzt {arbeitszeit} Minuten.")
        time.sleep(arbeitszeit * 60)  # Arbeitszeit in Sekunden
        gesamte_arbeitszeit += arbeitszeit  # Addiere die Arbeitszeit
        
        # Pause
        print(f"\nPause {zyklus}: Entspanne dich für {pausendauer} Minuten.")
        print("Dein Lieblingslied wird jetzt abgespielt!")
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")  # Link zu deinem Lieblingslied
        time.sleep(pausendauer * 60)  # Pausendauer in Sekunden
        pausen_zaehler += 1  # Erhöhe den Pausenzähler
        
        # Warm-Up Spiel Option
        spielen = input("\nMöchtest du ein kleines Warm-Up-Spiel spielen? (ja/nein): ").strip().lower()
        if spielen == "ja":
            zahlenraten()
        else:
            print("Kein Problem! Weiter geht's mit dem nächsten Zyklus.")
    
    # Abschlussnachricht
    print("\nLernzeit beendet! Gute Arbeit, du hast es geschafft!")
    print(f"Du hast insgesamt {pausen_zaehler} Pausen gemacht.")
    print(f"Deine gesamte konzentrierte Arbeitszeit beträgt {gesamte_arbeitszeit} Minuten.")

# Starte das Hauptprogramm
main()
