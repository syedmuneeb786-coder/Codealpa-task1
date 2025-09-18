import random

def hangman():
    words = ["python", "code", "alpha", "intern", "program"]
    word = random.choice(words)
    guessed = []
    attempts = 6
    print("🎮 Welcome to Hangman!")

    while attempts > 0:
        display_word = "".join([letter if letter in guessed else "_" for letter in word])
        print("\nWord:", display_word)

        if display_word == word:
            print("🎉 Congratulations! You guessed the word:", word)
            break

        guess = input("Guess a letter: ").lower()

        if guess in guessed:
            print("⚠️ Already guessed.")
        elif guess in word:
            guessed.append(guess)
            print("✅ Correct guess!")
        else:
            attempts -= 1
            print("❌ Wrong guess. Attempts left:", attempts)

    else:
        print("💀 Game Over! The word was:", word)

if __name__ == "__main__":
    hangman()
