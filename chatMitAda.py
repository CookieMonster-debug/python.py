# Begrüßung
print("Hi! Ich bin Ada. Wie heißt du?")
benutzer_name = input("Name: ")
print(f"Freut mich, {benutzer_name}!")

# Frage nach Adas Namen
frage = input(f"Was möchtest du wissen, {benutzer_name}? ")
if "Name" in frage:
    print("Ich bin Ada. ")

# Alter abfragen
alter = int(input("Wie alt bist du? "))
if alter < 18:
    print("Oh, du bist ja noch jung!")
else:
    print("Cool, du hast bestimmt schon viel erlebt!")

# Ja/Nein-Frage
antwort = input("Magst du Programmieren? (ja/nein): ").lower()
if antwort == "ja":
    print("Super, Programmieren ist echt spannend! 🚀")
elif antwort == "nein":
    print("Vielleicht ändert sich das ja noch.")
else:
    print("Hmm, das habe ich nicht verstanden.")

# Verabschiedung
print(f"Tschüss, {benutzer_name}! Bis bald!")
