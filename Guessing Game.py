
import time

secret_word = "python"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("\nOut Of Guesses, YOU LOSE!")
    time.sleep(5)
else:
    print("\nCongrats, You Win!!!!")
    time.sleep(5)