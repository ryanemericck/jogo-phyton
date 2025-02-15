import random

# Lista de palavras para o jogo
palavras = ["python", "desenvolvimento", "forca", "computador", "programacao", "jogo", "aplicativo"]

# Função para escolher uma palavra aleatória
def escolher_palavra():
    return random.choice(palavras)

# Função para mostrar a palavra com as letras adivinhadas e os underscores
def mostrar_palavra(palavra, letras_corretas):
    palavra_mostrada = ""
    for letra in palavra:
        if letra in letras_corretas:
            palavra_mostrada += letra
        else:
            palavra_mostrada += "_"
    return palavra_mostrada

# Função principal do jogo
def jogar():
    palavra = escolher_palavra()  # Palavra aleatória
    letras_corretas = []  # Letras que o jogador acertou
    tentativas = 6  # Número de tentativas restantes
    letras_erradas = []  # Letras erradas que o jogador tentou

    print("Bem-vindo ao Jogo da Forca!")
    print("Adivinhe a palavra:")

    # Loop do jogo
    while tentativas > 0:
        print(f"\nPalavra: {mostrar_palavra(palavra, letras_corretas)}")
        print(f"Tentativas restantes: {tentativas}")
        print(f"Letras erradas: {', '.join(letras_erradas)}")
        
        # Jogador escolhe uma letra
        tentativa = input("Escolha uma letra: ").lower()

        # Validação da entrada
        if len(tentativa) != 1 or not tentativa.isalpha():
            print("Por favor, insira apenas uma letra.")
            continue

        # Verifica se a letra foi tentada antes
        if tentativa in letras_corretas or tentativa in letras_erradas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        # Se a letra estiver na palavra
        if tentativa in palavra:
            letras_corretas.append(tentativa)
            print(f"Boa! A letra '{tentativa}' está na palavra.")
        else:
            letras_erradas.append(tentativa)
            tentativas -= 1
            print(f"Ops! A letra '{tentativa}' não está na palavra.")

        # Verifica se o jogador adivinhou toda a palavra
        if set(palavra) == set(letras_corretas):
            print(f"\nParabéns! Você adivinhou a palavra '{palavra}'!")
            break

    # Se o jogador ficar sem tentativas
    if tentativas == 0:
        print(f"\nVocê perdeu! A palavra era '{palavra}'.")

    # Perguntar se o jogador deseja jogar novamente
    jogar_novamente = input("\nVocê gostaria de jogar novamente? (s/n): ").lower()

    if jogar_novamente == "s":
        jogar()  # Chama a função para reiniciar o jogo
    else:
        print("Obrigado por jogar! Até a próxima!")

# Inicia o jogo
if __name__ == "__main__":
    jogar()
