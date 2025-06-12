import random  # Importa o módulo 'random', que permite gerar números aleatórios

# Mensagem de boas-vindas ao jogador
print("🎮 Bem-vindo ao Jogo da Adivinhação!")
print("Tente adivinhar o número entre 1 e 100.")

# Gera um número aleatório entre 1 e 100 e armazena na variável 'numero_secreto'
numero_secreto = random.randint(1, 100)

# Inicializa a contagem de tentativas do jogador
tentativas = 0

# Início do laço principal do jogo — ele continuará até o jogador acertar
while True:
    # Recebe a tentativa do usuário como string
    tentativa = input("Digite seu palpite: ")

    # Verifica se o valor digitado é um número (composto apenas por dígitos)
    if not tentativa.isdigit():
        print("⚠️ Por favor, digite um número válido.")
        continue  # Volta para o início do loop sem contar como tentativa

    # Converte a entrada de texto para inteiro
    tentativa = int(tentativa)

    # Incrementa o número de tentativas
    tentativas += 1

    # Compara a tentativa com o número secreto
    if tentativa < numero_secreto:
        print("🔻 Muito baixo!")  # Informa que o palpite foi menor que o número secreto
    elif tentativa > numero_secreto:
        print("🔺 Muito alto!")  # Informa que o palpite foi maior que o número secreto
    else:
        # Se o palpite estiver correto, mostra mensagem de acerto e encerra o loop
        print(f"✅ Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
        break  # Sai do laço 'while'

