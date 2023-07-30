import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
Sten
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
papir
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
saks
'''

#Write your code below this line 👇
game = [rock, paper, scissors]

my_input = int(input('''Hi, velkommen til sten, saks, papir. 
Vælger du sten skriv 0,vælger du papir skriv 1 og vælger du saks skriv 2: '''))
print("-------------------------------------")
if my_input == 0:
    print(f"\n du har valgt {game[0]}")

elif my_input == 1:
    print(f"du har valgt {game[1]}")

elif my_input > 2:
    print("Hvad laver du? er du helt væk, du skal vælge et tal mellem 0-2")

elif my_input == 2:
    print(f"du har valgt {game[2]}")


random_int = random.randint(0,2)
print ("----------------------------")
print("Computeren har valgt")
if random_int == 0:
    print(f"{game[0]}")

    if random_int == 0 and my_input == 0:
        print("Uafgjort")

    if random_int == 0 and my_input == 1:
        print("Du vinder")

    if random_int == 0 and my_input == 2:
        print("Computer vinder")

if random_int == 1 :
    print(f"{game[1]}")

    if random_int == 1 and my_input == 1:
        print("Uafgjort")

    if random_int == 1 and my_input == 2:
        print("Du vinder")

    if random_int == 1 and my_input == 0:
        print("Computer vinder")


if random_int == 2:
    print(f"{game[2]}")

    if random_int == 2 and my_input == 2:
        print("Uafgjort")

    if random_int == 2 and my_input == 0:
        print("Du vinder")

    if random_int == 2 and my_input == 1:
        print("Computer vinder")





