import webbrowser

# Brave-Browser registrieren (MacOS)
brave_path = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
webbrowser.register('brave', None, webbrowser.BackgroundBrowser(brave_path))

# Begrüßung und Erklärung
print("Willkommen! Gib 'suche' ein, um die Startseite von Google im Brave-Browser zu öffnen.")
print("Gib etwas anderes ein, um das Programm zu beenden.")

# Benutzereingabe
command = input("Was möchtest du tun? ").strip().lower()

# Überprüfen der Eingabe
if command == "suche":
    print("Öffne die Startseite von Google im Brave-Browser...")
    webbrowser.get('brave').open("https://www.google.com")
else:
    print("Programm wird beendet. Auf Wiedersehen!")
