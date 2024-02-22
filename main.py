from random import randint
print("Welcome to the Python Casino!")

pc_choise = randint(1,50) # I imported this

playing = True

while playing:
  user_choise = int(input("Enter a number: "))
  if user_choise == pc_choise:
    print("You won!")
    playing = False
  elif user_choise > pc_choise:
    print("Lower!")
  elif user_choise < pc_choise:
    print("Higher!")
  