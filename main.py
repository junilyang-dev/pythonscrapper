from random import randint
user_choise = int(input("Enter a number: "))
pc_choise = randint(1,50)

if user_choise == pc_choise:
  print("You won!")
elif user_choise > pc_choise:
  print("Lower! Computer Chosen", pc_choise)
elif user_choise < pc_choise:
  print("Higher! Computer Chosen", pc_choise)