import random

# Tamil-to-English word list
words = [
    {"tamil": "வணக்கம்", "english": "hello"},
    {"tamil": "நன்றி", "english": "thank you"},
    {"tamil": "ஆமாம்", "english": "yes"},
    {"tamil": "இல்லை", "english": "no"},
    {"tamil": "எப்படி", "english": "how"},
    {"tamil": "எப்போது", "english": "when"},
    {"tamil": "நீங்கள்", "english": "you"},
    {"tamil": "என் பெயர்", "english": "my name"},
    {"tamil": "நண்பர்", "english": "friend"},
    {"tamil": "புத்தகம்", "english": "book"},
    {"tamil": "அம்மா", "english": "mother"},
    {"tamil": "அப்பா", "english": "father"},
    {"tamil": "காலை வணக்கம்", "english": "good morning"},
    {"tamil": "மாலை வணக்கம்", "english": "good evening"},
    {"tamil": "தயவுசெய்து", "english": "please"},
]

def quiz_user(words):
    """Quiz the user with Tamil words."""
    random.shuffle(words)  # Shuffle the list of words
    score = 0

    for word in words:
        print(f"What is the English translation of '{word['tamil']}'?")
        user_answer = input("Your answer: ").strip().lower()
        correct_answer = word['english'].lower()

        if user_answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is '{word['english']}'.\n")

    print(f"Quiz complete! Your score: {score}/{len(words)}")

def main():
    print("Welcome to the Tamil-to-English Flashcards App!")
    input("Press Enter to start the quiz...")
    quiz_user(words)

if __name__ == "__main__":
    main()
