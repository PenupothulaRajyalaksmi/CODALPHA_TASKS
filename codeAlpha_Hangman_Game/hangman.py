import random

# List of predefined words
words = ["python", "laptop", "college", "computer", "developer"]

# Select a random word
word = random.choice(words)

# Create a list to display guessed letters
guessed_word = ["_"] * len(word)

# Store guessed letters
guessed_letters = []

# Maximum wrong attempts
attempts = 6

print("=" * 40)
print("🎮 Welcome to Hangman Game 🎮")
print("=" * 40)

while attempts > 0 and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Wrong Attempts Left:", attempts)
    print("Guessed Letters:", " ".join(guessed_letters))

    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter only one alphabet.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct Guess!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        print("❌ Wrong Guess!")
        attempts -= 1

# Final Result
print("\n" + "=" * 40)

if "_" not in guessed_word:
    print("🎉 Congratulations! You guessed the word:", word)
else:
    print("💀 Game Over!")
    print("The correct word was:", word)

print("=" * 40)