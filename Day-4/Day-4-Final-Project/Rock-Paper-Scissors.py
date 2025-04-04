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

computer_choice  = random.randint(1, 3)

man_choice = input("What do you choose?, 0 for Rock, 1 for Paper, and 2 for Scissors ")
man_choice = int(man_choice)
if man_choice == 0:
    print(rock)
elif man_choice == 1:
    print(paper)
elif man_choice == 2:
    print(scissors)
else:
    print("Error PANDCHOO")
    
    
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
elif computer_choice == 2:
    print(scissors)
else:
    print("Error PANDCHOO")
    

if computer_choice == 0 and man_choice == 0:
    print("TIE")
elif computer_choice == 0 and man_choice == 1:
    print("You Win")
elif computer_choice == 0 and man_choice == 2:
    print("You LOOSEEE HEHEHEHHE")
elif computer_choice == 1 and man_choice == 0:
    print("You LOOSEEE HEHEHEHHE")
elif computer_choice == 1 and man_choice == 1:
    print("TIE")
elif computer_choice == 1 and man_choice == 2:
    print("You Win")
elif computer_choice == 2 and man_choice == 0:
    print("You Win")
elif computer_choice == 2 and man_choice == 1:
    print("You LOOSEEE HEHEHEHHE")
elif computer_choice == 2 and man_choice == 2:
    print("TIE")
else:
    print("ERRORRR PANDCHOOOO")