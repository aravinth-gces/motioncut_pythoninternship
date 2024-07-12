def count_words(text):
    # Split the text by whitespace to get individual words
    words = text.split()
    # Return the number of words
    return len(words)

# Example usage
text = "This is an example sentence with several words."
word_count = count_words(text)
print(f"The number of words in the text is: {word_count}")
