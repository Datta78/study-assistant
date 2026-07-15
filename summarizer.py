# Note Summarizer - Dattatray Bhosale

def summarize_notes(notes):
    words = notes.split()
    summary = ' '.join(words[:100])  # Simple summary: first 100 words
    return summary + "..." if len(words) > 100 else summary

# Test
if __name__ == "__main__":
    text = input("Paste your study notes: ")
    print("\nSummary:")
    print(summarize_notes(text))
