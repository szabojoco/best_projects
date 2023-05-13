from art import logo, vs
from game_data import data
from random import randint

random_nr_A = randint(1, 50)
random_nr_B = randint(1, 50)
score = 0

name_A = data[random_nr_A]["name"]
description_A = data[random_nr_A]["description"]
country_A = data[random_nr_A]["country"]
follower_A = data[random_nr_A]["follower_count"]

name_B = data[random_nr_B]["name"]
description_B = data[random_nr_B]["description"]
country_B = data[random_nr_B]["country"]
follower_B = data[random_nr_B]["follower_count"]

print(logo)
while True:

    print(f"Compare A: {name_A}, {description_A}, {country_A}.")
    print(vs)
    print(f"Against B: {name_B}, {description_B}, {country_B}")

    a_or_b = input("Who has more followers? Type 'A' or 'B': ")

    if follower_A > follower_B and a_or_b == "A":
        score += 1
        print(f"You're right! Current score: {score}")
    elif follower_A < follower_B and a_or_b == "B":
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        exit()
