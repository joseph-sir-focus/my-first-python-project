# Project: Japanese Phonetic Name Generator
# Data Structure: Python Dictionary (Key-Value Pairs)
# Description: Maps English characters to Japanese syllables

japanese_alphabet = {
    'a': 'ka', 'b': 'tu', 'c': 'mi', 'd': 'te', 'e': 'ku', 
    'f': 'lu', 'g': 'ji', 'h': 'ri', 'i': 'ki', 'j': 'zu', 
    'k': 'me', 'l': 'ta', 'm': 'rin', 'n': 'to', 'o': 'mo', 
    'p': 'no', 'q': 'ke', 'r': 'shi', 's': 'ari', 't': 'chye', 
    'u': 'do', 'v': 'ru', 'w': 'mei', 'x': 'na', 'y': 'fu', 'z': 'zi'
}

# 1. Asking users for their name
english_name = input("Type your name: ")

# 2. Make the name lowercase to matches our list of keys
clean_name = english_name.lower()

# 3. Create a blank container to hold the translation
japanese_name = ""

# 4. Loop through every letter in the name and convert it
for letter in clean_name:
    if letter in japanese_alphabet:
        japanese_name += japanese_alphabet[letter]
    else:
        # If there's a space or symbol, keep it as it is
        japanese_name += letter

# 5. Print the final results out to the screen
print(f"Your English name is: {english_name.capitalize()}")
print(f"In Japanese syllables, you are called: {japanese_name.capitalize()}")
