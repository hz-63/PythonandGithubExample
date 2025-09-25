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