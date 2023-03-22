import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

hand_list = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Pape or 2 for Scrissors.\n"))
computer_choice = random.randint(0, 2)

print(hand_list[user_choice])

print(f"Computer chose: {computer_choice}")
print(hand_list[computer_choice])

if user_choice == 0 and computer_choice == 2 or \
        user_choice == 1 and computer_choice == 0 or \
        user_choice == 2 and computer_choice == 1:
    print("You win.")
else:
    print("You lost.")
