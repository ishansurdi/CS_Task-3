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
user_score = 0
comp_score = 0

print("What do you choose?")
ask_rounds = int(input("How many round do you want to play? -"))
while ask_rounds != 0:
    choice_user = int(input("Type 0 for Rock, 1 for paper or 2 for Scissors:- "))

    if (choice_user == 0):
        print(rock)
    elif (choice_user == 1):
        print(paper)
    elif (choice_user == 2):
        print(scissors)



    comp_choice = ["rock", "paper", "scissors"]
    num_cc = len(comp_choice)

    random_comp_choice = random.randint(0, 2)
    #print(random_comp_choice)
    if random_comp_choice == 0:
        print(rock)
    elif random_comp_choice == 1:
        print(paper)
    elif random_comp_choice == 2:
        print(scissors)

    if (choice_user != random_comp_choice):

        user_score += 1
        ask_rounds -= 1
    elif (random_comp_choice != choice_user):
        comp_score += 1
        ask_rounds -=1

    elif (choice_user == random_comp_choice):
        user_score = 0
        comp_score = 0
        ask_rounds -=1

print(f"User score is {user_score}")
print(f"Computer score is {comp_score}")
if user_score > comp_score:
    print("Congrats! You won!")
else:
    print("Sad! You lost!")