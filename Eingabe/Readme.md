# Überprüfung einer Eingabe: Gerade oder Ungerade

Dieses Python-Programm prüft, ob eine vom Benutzer eingegebene Zahl gerade oder ungerade ist.

## Beschreibung

Der Benutzer wird aufgefordert, eine Zahl einzugeben. Das Programm verwendet den Modulo-Operator (`%`), um zu überprüfen, ob die Zahl durch 2 teilbar ist. Ist dies der Fall, handelt es sich um eine gerade Zahl, andernfalls um eine ungerade Zahl.

## Python-Code

````python
# Überprüfung einer Eingabe
zahl = int(input("Gib eine Zahl ein: "))

if zahl % 2 == 0:  # Modulo in Python
    print("Die Zahl ist gerade.")
else:
    print("Die Zahl ist ungerade.")
````
