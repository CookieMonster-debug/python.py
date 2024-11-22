import time

# Liste mit 10 Fragen
questions = [
    "Was ist dein Lieblingsessen?",
    "Welche Farbe magst du am liebsten?",
    "Wie heißt dein bester Freund oder deine beste Freundin?",
    "Welches Land möchtest du unbedingt bereisen?",
    "Welches Tier findest du am interessantesten?",
    "Was ist dein Lieblingsfilm?",
    "Welche Musikrichtung hörst du am meisten?",
    "Wie lautet dein Traumberuf?",
    "Was ist dein Lieblingsbuch?",
    "Was würdest du mit einer Million Euro machen?"
]

# Programm, um die Fragen zu stellen
for i, question in enumerate(questions):
    print(f"Frage {i+1}: {question}")
    print("Du hast 30 Sekunden Zeit, um nachzudenken...")
    time.sleep(30)  # Warte 30 Sekunden
    answer = input("Deine Antwort: ")
    print(f"Antwort gespeichert: {answer}\n")

print("Danke für deine Teilnahme am 30 Sec. Tester!")
