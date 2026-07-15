# Study Assistant - Dattatray Bhosale
print("Welcome to AI Study Assistant!")
print("1. Summarize Notes")
print("2. Generate Quiz")
print("3. Chat with Assistant")

choice = input("Choose option: ")

if choice == "1":
    notes = input("Paste your notes: ")
    print("\nSummary:", notes[:200] + "...")  # Simple summary
elif choice == "2":
    print("Quiz generated! (Coming soon)")
elif choice == "3":
    print("Chat mode activated! (Coming soon)")
else:
    print("Invalid option")
