import re
from collections import Counter

def text_analyzer(text):
    # Remove punctuation and convert to lowercase
    words = re.findall(r'\b\w+\b', text.lower())
    word_count = len(words)
    
    # Character count (excluding spaces)
    char_count = len(re.sub(r'\s+', '', text))
    
    # Sentence count (simple split by sentence-ending punctuation)
    sentences = re.split(r'[.!?]+', text)
    sentence_count = len([s for s in sentences if s.strip()])
    
    # Most common words
    common_words = Counter(words).most_common(5)
    
    # Average word length
    avg_word_len = sum(len(word) for word in words) / word_count if word_count > 0 else 0

    # Output results
    print("Text Analysis:")
    print(f"Words: {word_count}")
    print(f"Characters (no spaces): {char_count}")
    print(f"Sentences: {sentence_count}")
    print(f"Average word length: {avg_word_len:.2f}")
    print("Most common words:")
    for word, freq in common_words:
        print(f"  {word}: {freq}")

# Example usage
sample_text = """
Python is an interpreted, high-level and general-purpose programming language.
Its design philosophy emphasizes code readability with the use of significant indentation.
Python's syntax allows programmers to express concepts in fewer lines of code.
"""
text_analyzer(sample_text)
