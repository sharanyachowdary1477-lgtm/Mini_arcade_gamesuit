import random

# Individual scores
score_guess = 0
score_rps = 0
score_quiz = 0
score_dice = 0

# ---------------- GAME 1: Guess the Number ----------------
def guess_number():
    global score_guess
    num = random.randint(1, 10)
    guess = int(input("Guess number (1-10): "))
    if guess == num:
        print("Correct!")
        score_guess += 10
    else:
        print("Wrong! Number was", num)

# ---------------- GAME 2: Rock Paper Scissors ----------------
def rps():
    global score_rps
    choices = ["rock", "paper", "scissors"]
    comp = random.choice(choices)
    user = input("Enter rock/paper/scissors: ").lower()

    if user == comp:
        print("Draw!")
    elif (user == "rock" and comp == "scissors") or \
         (user == "paper" and comp == "rock") or \
         (user == "scissors" and comp == "paper"):
        print("You win!")
        score_rps += 10
    else:
        print("You lose! Computer chose", comp)

# ---------------- GAME 3: Simple Quiz ----------------
def quiz():
    global score_quiz
    print("Q: Capital of India?")
    ans = input("Answer: ").lower()
    if ans == "delhi":
        print("Correct!")
        score_quiz += 10
    else:
        print("Wrong!")

# ---------------- GAME 4: Dice Roll ----------------
def dice():
    global score_dice
    user = int(input("Guess dice number (1-6): "))
    roll = random.randint(1, 6)
    print("Dice rolled:", roll)
    if user == roll:
        print("Correct!")
        score_dice += 10
    else:
        print("Try again!")

# ---------------- GAME MENU ----------------
while True:
    print("\n🎮 MINI ARCADE GAME SUITE")
    print("1. Guess Number")
    print("2. Rock Paper Scissors")
    print("3. Quiz")
    print("4. Dice Game")
    print("5. Show Scores")
    print("6. Exit")

    choice = input("Choose game: ")

    if choice == "1":
        guess_number()
    elif choice == "2":
        rps()
    elif choice == "3":
        quiz()
    elif choice == "4":
        dice()
    elif choice == "5":
        print("\n--- Individual Scores ---")
        print("Guess Number Score:", score_guess)
        print("RPS Score:", score_rps)
        print("Quiz Score:", score_quiz)
        print("Dice Score:", score_dice)
        print("Total Score:", score_guess + score_rps + score_quiz + score_dice)
    elif choice == "6":
        print("\nFinal Scores:")
        print("Guess Number:", score_guess)
        print("RPS:", score_rps)
        print("Quiz:", score_quiz)
        print("Dice:", score_dice)
        print("Total:", score_guess + score_rps + score_quiz + score_dice)
        break
    else:
        print("Invalid choice!")