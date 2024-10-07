import random

def jogar():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    print("Adivinhe o número entre 1 e 100!")

    while True:
        palpite = int(input("Seu palpite: "))
        tentativas += 1
        
        if palpite < numero_secreto:
            print("Muito baixo! Tente novamente.")
        elif palpite > numero_secreto:
            print("Muito alto! Tente novamente.")
        else:
            print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
            break

if __name__ == "__main__":
    jogar()
