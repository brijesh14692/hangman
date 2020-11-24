import random

secret_list = ('python', 'java', 'kotlin', 'javascript')
secret_word = random.choice(secret_list)
user_list = len(secret_word) * "-"
guessed_letters = []
attempts = 8

print("H A N G M A N")
user_want = input('Type "play" to play the game, "exit" to quit: ')
if user_want == "play":

    while attempts != 0 and secret_word != user_list:
        print()
        print(user_list)
        user_input = input("Input a letter: ")

        if user_input in guessed_letters:
            print("You've already guessed this letter")
        elif len(user_input) != 1:
            print("You should input a single letter")
        elif ord(user_input) < 97 or ord(user_input) > 122:
            print("Please enter a lowercase English letter")
        else:
            if user_input in secret_word:
                for i in range(0, len(secret_word)):
                    if secret_word[i] == user_input:
                        user_list = list(user_list)
                        user_list[i] = secret_word[i]
                        user_list = "".join(user_list)
                    else:
                        continue
            else:
                print("That letter doesn't appear in the word")
                attempts -= 1
        if len(user_input) == 1:
            guessed_letters.append(user_input)
        else:
            continue
    if attempts > 0:
        print("You guessed the word " + secret_word + "!")
        print("You survived!")
        print()
        user_want = input('Type "play" to play the game, "exit" to quit: ')
    else:
        print("You lost!")
        print()
        user_want = input('Type "play" to play the game, "exit" to quit: ')
elif user_want == "exit":
    pass
else:
    user_want = input('Type "play" to play the game, "exit" to quit: ')

