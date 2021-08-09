user_word = input("Enter your word: ")
user_word = user_word.upper()

for letter in user_word:
    if letter == "E" or letter =="A" or letter =="I" or letter =="O" or letter == "U":
        continue
    else:
        print(letter)
