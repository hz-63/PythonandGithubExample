# Anleitung: Text-Adventure-Spiel in Python programmieren

Dieses Tutorial zeigt dir, wie du ein einfaches Text-Adventure-Spiel in Python erstellen kannst. Du lernst, wie du mit Benutzereingaben arbeitest, Entscheidungen triffst und eine einfache Spielstruktur aufbaust.

## Voraussetzungen

- Grundkenntnisse in Python
- Python 3 installiert auf deinem Computer

## Schritt-für-Schritt-Anleitung

### 1. Spielstruktur planen

Ein Text-Adventure besteht aus Szenen oder Räumen, in denen der Spieler Entscheidungen trifft. Jede Szene kann durch eine Funktion oder ein Datenobjekt dargestellt werden.

### 2. Benutzereingaben verarbeiten

Nutze `input()` um Eingaben vom Spieler zu erhalten und mit `if`-Abfragen darauf zu reagieren.

### 3. Beispielcode

Im folgenden Beispiel betritt der Spieler eine Höhle und muss Entscheidungen treffen, um zu entkommen.

````Python
def start():
    print("Du betrittst eine dunkle Höhle.")
    choice = input("Gehst du nach links oder rechts? (links/rechts): ")
    if choice == "links":
        left_path()
    elif choice == "rechts":
        right_path()
    else:
        print("Ungültige Eingabe. Das Spiel endet.")

def left_path():
    print("Du findest einen Schatz! Du hast gewonnen.")

def right_path():
    print("Ein Drache erscheint und du wirst gefressen. Spiel vorbei.")

start()
