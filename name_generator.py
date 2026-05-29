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

print("=== JAPANESE NAME GENERATOR STARTED ===")
print("(Type 'quit' at any time to exit the program)\n")

# This loop runs forever until it hits a 'break' statement
while True: 
   # 1. Ask the user for their name
    english_name = input("Type a name: ")
    
    # 2. Check if the user wants to exit the program
    if english_name.lower() == 'quit':
        print("Thank you for using the generator. Goodbye!")
        break  # This exits the while loop immediately
        
    # 3. Clean the input and prepare the container
    clean_name = english_name.lower()
    japanese_name = ""
    
    # 4. Loop through every letter in the name and convert it
    for letter in clean_name:
        if letter in japanese_alphabet:
            japanese_name += japanese_alphabet[letter]
        else:
            japanese_name += letter
            
    # 5. Print the final results out to the screen with spacing
    print(f"-> English: {english_name.capitalize()}")
    print(f"-> Japanese: {japanese_name.capitalize()}\n")
