def check_adulthood():
    # Frage die Person nach ihrem Alter
    ageCheck = int(input("Wie alt bist du? "))
    
    # Frage, ob die Volljährigkeit in diesem Land ab 18 gilt
    law = input("Ist man in deinem Land ab 18 volljährig? (ja/nein) ").strip().lower()
    
    # Überprüfe die Volljährigkeitsgrenze
    if law == "ja":
        legal_age = 18
    else:
        print("Ich kann die Umfrage nur durchführen, wenn ab 18 die Volljährigkeit gilt.")
        return

    # Überprüfe, ob die Person volljährig ist
    if ageCheck >= legal_age:
        adult = True
    else:
        adult = False

    # Zeige den Volljährigkeitsstatus an
    if adult:
        print("Du bist volljährig!")
        # Frage, ob die Person Horrorfilme mag
        horrormovie = input("Magst du Horrorfilme ab 18? (ja/nein) ").strip().lower()
        if horrormovie == "ja":
            print("Cool! Viel Spaß beim Anschauen von Horrorfilmen.")
        else:
            print("Kein Problem, es gibt auch andere tolle Genres!")
    else:
        print("Du bist noch nicht volljährig.")
        print(f"Komm in {18 - ageCheck} Jahr(en) zurück, um den Rest der Umfrage zu beantworten!")

# Starte das Programm
check_adulthood()
