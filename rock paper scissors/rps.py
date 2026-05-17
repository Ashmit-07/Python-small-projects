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





choice = input("What do you choose? Type 1 for rock, 2 for paper and 3 for scissors!\n")
comp_choice = random.randint(1,3)
choice = int(choice)

if choice == 1:
    print ("You choose:", rock) 

    if comp_choice == 1:
        print ("The computer choose:", rock)
        print ("That was a Tie!!") 
    if comp_choice == 2:
        print ("The computer choose:", paper)
        print ("You lost! Skill issue!") 
    if comp_choice == 3:
        print ("The computer choose:", scissors)
        print ("You won by luck!!")     

if choice == 2:
    print ("You choose:", paper) 

    if comp_choice == 1:
        print ("The computer choose:", rock)
        print ("You won by luck!!")    

    if comp_choice == 2:
        print ("The computer choose:", paper)
        print ("That was a Tie!!") 

    if comp_choice == 3:
        print ("The computer choose:", scissors)
        print ("You lost! Skill issue!") 

if choice == 3:
    print ("You choose:", scissors) 

    if comp_choice == 1:
        print ("The computer choose:", rock)
        print ("You lost! Skill issue!")    

    if comp_choice == 2:
        print ("The computer choose:", paper)
        print ("You won by luck!!")   

    if comp_choice == 3:
        print ("The computer choose:", scissors)
        print ("That was a Tie!!")        
