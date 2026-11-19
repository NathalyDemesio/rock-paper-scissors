import random

user_points = 0
computer_points = 0

options_computer = ["R", "T", "P"]
options_user = ["R", "T", "P", "Q"]

# Loop Infinito
while True:
    user_choice = input("Escolha R(Pedra) / T(Tesoura) / P(Papel) ou Q para sair: ").upper()

    # Caso de saída
    if user_choice == 'Q':
        break

    if user_choice not in options_computer:
         continue
         
    # 0 : R, 1 : T, 2 : P
    computer_choice = random.randint(0, 2)

    computer_choice = options_computer[computer_choice]

    print(f"O computador escolheu {computer_choice}")

    if user_choice == computer_choice:
        print("Empate!")
    elif user_choice == "R" and computer_choice == "T":
        print("Você ganhou da tesoura!")
        user_points += 1

    elif user_choice == "P" and computer_choice == "R":
            print("Você ganhou da pedra!")
            user_points += 1

    elif user_choice == "T" and computer_choice == "P":
            print("Você ganhou do papel!")
            user_points += 1

    else:
         print("Você perdeu!")
         computer_points += 1

print()

# Resultado
print("---------PONTUAÇÃO---------")
print(f"Sua pontuação: {user_points}")
print(f"A pontuação do computador: {computer_points}")

print()

print("---------RESULTADO---------")
if computer_points > user_points:
    print("Derrota!")
elif computer_points == user_points:
    print("Empate!")
else:
    print("Você venceu dele!!")