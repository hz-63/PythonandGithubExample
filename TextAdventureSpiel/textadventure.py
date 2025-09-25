# Raumdefinitionen
raeume = {
    "Eingang": {
        "beschreibung": "Du stehst am Eingang eines alten Gebäudes.",
        "norden": "Flur"
    },
    "Flur": {
        "beschreibung": "Ein langer Flur mit knarrendem Boden.",
        "süden": "Eingang",
        "osten": "Bibliothek",
        "westen": "Labor"
    },
    "Bibliothek": {
        "beschreibung": "Regale voller staubiger Bücher.",
        "westen": "Flur",
        "norden": "Geheimzimmer"
    },
    "Labor": {
        "beschreibung": "Ein Raum voller seltsamer Geräte und Flüssigkeiten.",
        "osten": "Flur"
    },
    "Geheimzimmer": {
        "beschreibung": "Ein versteckter Raum mit einem alten Schatz.",
        "süden": "Bibliothek"
    }
}

# Startposition
aktueller_raum = "Eingang"

print("Willkommen zum Textadventure! Gib 'beenden' ein, um das Spiel zu verlassen.\n")

# Spielschleife
while True:
    print(f"\nDu bist im Raum: {aktueller_raum}")
    print(raeume[aktueller_raum]["beschreibung"])
    
    befehl = input("Was möchtest du tun? (z. B. 'gehe nach Norden') ").strip().lower()
    
    if befehl == "beenden":
        print("Spiel beendet. Danke fürs Spielen!")
        break
    
    elif befehl.startswith("gehe nach "):
        richtung = befehl.split("gehe nach ")[1]
        if richtung in raeume[aktueller_raum]:
            aktueller_raum = raeume[aktueller_raum][richtung]
        else:
            print("Du kannst in diese Richtung nicht gehen.")
    else:
        print("Unbekannter Befehl. Versuche z. B. 'gehe nach Norden'.")