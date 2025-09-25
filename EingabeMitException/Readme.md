# Überprüfung einer Eingabe: Gerade oder Ungerade mit Fehlerbehandlung

Dieses Python-Programm prüft, ob eine vom Benutzer eingegebene Zahl gerade oder ungerade ist. Zusätzlich wird sichergestellt, dass ungültige Eingaben wie Zeichenketten oder leere Eingaben erkannt und mit einer Fehlermeldung behandelt werden.

## Beschreibung

Der Benutzer wird aufgefordert, eine Zahl einzugeben. Das Programm verwendet den Modulo-Operator (`%`), um zu überprüfen, ob die Zahl durch 2 teilbar ist. Ist dies der Fall, handelt es sich um eine gerade Zahl, andernfalls um eine ungerade Zahl.

Ungültige Eingaben wie Buchstaben oder leere Eingaben werden durch eine Fehlerbehandlung (`try-except`) abgefangen und mit einer verständlichen Fehlermeldung ausgegeben.

## Python-Code

````python
# Überprüfung einer Eingabe mit Fehlerbehandlung

try:
    eingabe = input("Gib eine Zahl ein: ")
    
    if eingabe.strip() == "":
        raise ValueError("Keine Eingabe erkannt.")

    zahl = int(eingabe)

    if zahl % 2 == 0:  # Modulo in Python
        print("Die Zahl ist gerade.")
    else:
        print("Die Zahl ist ungerade.")

except ValueError as e:
    print(f"Ungültige Eingabe: {e}")
