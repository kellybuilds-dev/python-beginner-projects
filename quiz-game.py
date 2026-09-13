print("🎯 Welcome to the Python Quiz Game!")
print("Answer the questions and see how much you know.\n")

score = 0

questions = [
    {
        "question": "What does CPU stand for?",
        "answer": "central processing unit"
    },
    {
        "question": "What programming language are we learning?",
        "answer": "python"
    },
    {
        "question": "What symbol is used to start a comment in Python?",
        "answer": "#"
    },
    {
        "question": "What function is used to display text in Python?",
        "answer": "print"
    },
    {
        "question": "What keyword is used to define a function in Python?",
        "answer": "def"
    }
]

for item in questions:
    answer = input(item["question"] + " ").strip().lower()

    if answer == item["answer"]:
        print("✅ Correct!\n")
        score += 1
    else:
        print("❌ Incorrect!")
        print("Correct answer:", item["answer"], "\n")

print("🏆 Quiz Complete!")
print("Your score:", score, "/", len(questions))

if score == len(questions):
    print("🔥 Perfect score!")
elif score >= 3:
    print("👏 Great job!")
else:
    print("💪 Keep practicing!")
