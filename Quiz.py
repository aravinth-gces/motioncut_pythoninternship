# Python quiz game

questions = ("Which is the largest state in India interms of population?: ",
                       "Who took more wickets in IPL?: ",
                       "Which is the most watched Anime in the world?: ",
                       "How many territories are there in India?: ",
                       "Who is the most followed person on Instagram?: ")

options = (("A. Rajasthan", "B. Maharastra", "C. Uttarpradesh", "D. Tamilnadu"),
                   ("A. Piyush Chawala", "B. Yuzvendra Chahal", "C. Dwayne Bravo", "D. Amit Mishra"),
                   ("A. One piece", "B. Jujutsu Kaisen", "C. Naruto shippuden", "D. Spy X family"),
                   ("A. 9", "B. 8", "C. 10", "D. 7"),
                   ("A. Lionel Messi", "B. Christiano Ronaldo", "C.Selena Gomex", "D. Virat kohli"))

answers = ("C", "B", "A", "B", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("----------------------")
print("       RESULTS        ")
print("----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")
