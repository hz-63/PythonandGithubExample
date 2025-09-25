import random

# Rechenoperationen als Funktionen
def addiere(x, y):
    return x + y

def subtrahiere(x, y):
    return x - y

def multipliziere(x, y):
    return x * y

def dividiere(x, y):
    return round(x / y, 2) if y != 0 else None

# Mapping der Operatoren zu den Funktionen
operations = {
    '+': addiere,
    '-': subtrahiere,
    '*': multipliziere,
    '/': dividiere
}

# Quiz generieren
def generate_quiz(num_questions=10):
    quiz = []
    for _ in range(num_questions):
        op = random.choice(['+', '-', '*', '/'])

        if op == '/':
            y = random.randint(1, 10)
            x = y * random.randint(1, 10)  # garantiert teilbar
            answer = round(x / y, 2)
        elif op == '+':
            x = random.randint(1, 100)
            y = random.randint(1, 100)
            answer = x + y
        elif op == '-':
            x = random.randint(1, 100)
            y = random.randint(1, 100)
            answer = x - y
        elif op == '*':
            x = random.randint(1, 20)
            y = random.randint(1, 20)
            answer = x * y

        quiz.append((x, op, y, answer))
    return quiz

# Quiz durchführen
def run_quiz(quiz):
    score = 0
    for i, (x, op, y, correct_answer) in enumerate(quiz, 1):
        user_input = input(f"Frage {i}: Was ist {x} {op} {y}? ")
        try:
            user_answer = float(user_input)
            if abs(user_answer - correct_answer) < 0.01:
                print("✅ Richtig!")
                score += 1
            else:
                print(f"❌ Falsch. Die richtige Antwort ist {correct_answer}.")
        except ValueError:
            print(f"⚠️ Ungültige Eingabe. Die richtige Antwort ist {correct_answer}.")
    print(f"\n📊 Du hast {score} von {len(quiz)} Fragen richtig beantwortet.")

if __name__ == "__main__":
    quiz = generate_quiz()
    run_quiz(quiz)