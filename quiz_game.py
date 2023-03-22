print("Welcome to my computer quiz!")
print("=" * 30)

playing = input("Do you want to play? Y/N ")

if playing.lower() != "y":
    quit()

print("Okay! Let's play :)")
score = 0

print("=" * 30)

answer = input("What does CPU stand for?\n    1.central processing unit\n    2.center processing unit\n"
               "    3.central progressing unit\n    4.central processing unity\n")
if answer == "1":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("=" * 30)

answer = input("What does GPU stand for?\n    1.grapics processing unit\n    2.graphics procession unitt\n"
               "    3.graphics processing unit\n    4.graphics processing unity\n")
if answer == "3":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("=" * 30)

answer = input("What does RAM stand for?\n    1.random acess memory\n    2.randomly access memory\n"
               "    3.random acess memo\n    4.random access memory\n")
if answer == "4":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("=" * 30)

answer = input("What does PSU stand for?\n    1.powerly supply unit\n    2.power supply unit\n"
               "    3.power suply unit\n    4.power supply unity\n")
if answer == "2":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print(f"You got {score} questions correct!")
print(f"You got {(score / 4) * 100}% questions correct!")
