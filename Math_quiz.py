lives = 3
correctAnswer = 150

while lives > 0:
    answer = int(input("100 + 50: "))
    if answer == correctAnswer:
        print("Correct!")
        break
    else:
        lives = lives - 1
        print(f"You have {lives} left")

else:
    print("Nice try")