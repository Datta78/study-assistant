# Simple Quiz Generator - Dattatray Bhosale

def generate_quiz(topic):
    print(f"\nQuiz on: {topic}")
    print("Q1. What is the main concept of", topic, "?")
    print("Q2. Give one example related to", topic)
    print("Q3. Why is", topic, "important?")
    print("\n(Answers can be expanded later)")

if __name__ == "__main__":
    topic = input("Enter study topic: ")
    generate_quiz(topic)
