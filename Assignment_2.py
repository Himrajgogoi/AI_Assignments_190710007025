# Assignment 2: Write a python program to identify a language.

from langdetect import detect

# Function to identify the language of a text
def identify_language(text):
    try:
        language = detect(text)
        return language
    except:
        return "Language detection failed."

# Example
text = "This is an example text."
language = identify_language(text)
print("Detected language:", language)
