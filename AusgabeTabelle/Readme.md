# Quadratzahlen-Tabelle in Python

Dieses Programm gibt eine Tabelle mit den Quadratzahlen von 1 bis 10 aus.

## Beispielcode
````python
print("Zahl\t| Quadrat")
print("-----------------")

for zahl in range(1, 11):
    quadrat = zahl ** 2  # Operator ** für Potenzen
    print(zahl, "\t|", quadrat)
