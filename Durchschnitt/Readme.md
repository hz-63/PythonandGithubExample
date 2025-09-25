# 📊 Durchschnittsberechnung mit Python

Dieses kleine Python-Programm berechnet den Durchschnitt von drei Zahlen, die vom Benutzer eingegeben werden.

## 🧾 Beschreibung

Das Programm fordert den Benutzer auf, drei Zahlen einzugeben. Anschließend werden diese Zahlen addiert und durch 3 geteilt, um den Durchschnitt zu berechnen. Das Ergebnis wird auf der Konsole ausgegeben.

## 💡 Beispielcode


# Berechnung des Durchschnitts

zahl1 = float(input("Gib die erste Zahl ein: "))
zahl2 = float(input("Gib die zweite Zahl ein: "))
zahl3 = float(input("Gib die dritte Zahl ein: "))

durchschnitt = (zahl1 + zahl2 + zahl3) / 3

print("Der Durchschnitt der Zahlen ist:", durchschnitt)
