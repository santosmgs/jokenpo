import random

def get_user_choice():
    choice = input("Escolha pedra, papel, tesoura ou digite SAIR para encerrar: ").strip().lower()
    if choice == "sair":
        return "sair"
    elif choice not in ["pedra", "papel", "tesoura"]:
        print("Escolha inválida, tente novamente.")
        return get_user_choice()
    return choice

def get_computer_choice():
    return random.choice(["pedra", "papel", "tesoura"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Empate"
    elif (
        (user_choice == "pedra" and computer_choice == "tesoura") or
        (user_choice == "tesoura" and computer_choice == "papel") or
        (user_choice == "papel" and computer_choice == "pedra")
    ):
        return "Você"
    else:
        return "Computador"

def play_game():
    user_score = 0
    computer_score = 0
    rounds = 0

    while True:
        user_choice = get_user_choice()
        if user_choice == "sair":
            print("Jogo encerrado!")
            break

        computer_choice = get_computer_choice()
        print(f"Você escolheu: {user_choice}")
        print(f"O computador escolheu: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)

        if result == "Empate":
            print("Foi um empate!")
        elif result == "Você":
            print("Você venceu esta rodada!")
            user_score += 1
        else:
            print("O computador venceu esta rodada!")
            computer_score += 1

        rounds += 1
        print(f"Placar: Você {user_score} x {computer_score} Computador (Rodadas: {rounds})")
        print("-" * 30)

    print(f"Placar final: Você {user_score} x {computer_score} Computador")
    print("Obrigado por jogar!")

if __name__ == "__main__":
    play_game()
