# 🐍 Python
Verwendung von if __name__ == "__main__"
Dieses Projekt zeigt die Verwendung einer wichtigen Python-Konstruktion:
if __name__ == "__main__" – ein Mechanismus zur Steuerung der Ausführung von Code, abhängig davon, ob ein Skript direkt ausgeführt oder als Modul importiert wird.

## 📌 Zweck
In Python wird jedes Skript beim Ausführen oder Importieren mit einem speziellen Namen versehen:

Wird das Skript direkt ausgeführt, ist __name__ gleich "__main__".
Wird das Skript importiert, ist __name__ gleich dem Namen des Moduls.
Die Konstruktion if __name__ == "__main__": erlaubt es, Code nur dann auszuführen, wenn das Skript direkt gestartet wird – und nicht, wenn es als Modul in ein anderes Skript eingebunden wird.


