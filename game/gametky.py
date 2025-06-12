import tkinter as tk
from tkinter import messagebox, simpledialog
import random

# Função para iniciar ou reiniciar o jogo
def novo_jogo():
    global numero_secreto, tentativas, nome_jogador

    # Pergunta o nome do jogador
    nome_jogador = simpledialog.askstring("Nome do Jogador", "Digite seu nome:")
    if not nome_jogador:
        nome_jogador = "Jogador Anônimo"

    numero_secreto = random.randint(1, 100)
    tentativas = 0
    entrada.delete(0, tk.END)
    label_resultado.config(text="Tente adivinhar o número entre 1 e 100.")
    label_tentativas.config(text="Tentativas: 0")

# Função para verificar o palpite do jogador
def verificar_palpite():
    global tentativas

    palpite = entrada.get()
    if not palpite.isdigit():
        messagebox.showwarning("Entrada inválida", "Por favor, digite um número válido.")
        return

    palpite = int(palpite)
    tentativas += 1
    label_tentativas.config(text=f"Tentativas: {tentativas}")

    if palpite < numero_secreto:
        label_resultado.config(text="🔻 Muito baixo!")
    elif palpite > numero_secreto:
        label_resultado.config(text="🔺 Muito alto!")
    else:
        label_resultado.config(text=f"✅ Acertou! O número era {numero_secreto}.")
        salvar_no_ranking(nome_jogador, tentativas)
        messagebox.showinfo("Parabéns!", f"{nome_jogador}, você acertou em {tentativas} tentativas!")
        mostrar_ranking()
        novo_jogo()

# Salva o jogador no ranking (arquivo texto)
def salvar_no_ranking(nome, tentativas):
    with open("ranking.txt", "a") as arquivo:
        arquivo.write(f"{nome} - {tentativas} tentativas\n")

# Lê e exibe o ranking
def mostrar_ranking():
    try:
        with open("ranking.txt", "r") as arquivo:
            conteudo = arquivo.readlines()
            conteudo = sorted(conteudo, key=lambda x: int(x.strip().split(" - ")[1].split()[0]))
            ranking_texto = "".join(conteudo[:10])  # Mostra os 10 melhores
    except FileNotFoundError:
        ranking_texto = "Nenhum ranking ainda."

    messagebox.showinfo("🏆 Ranking", ranking_texto)

# Janela principal
janela = tk.Tk()
janela.title("Jogo da Adivinhação")
janela.geometry("400x240")

# Interface
label_instrucoes = tk.Label(janela, text="Digite um número entre 1 e 100:")
label_instrucoes.pack(pady=5)

entrada = tk.Entry(janela)
entrada.pack()

botao_adivinhar = tk.Button(janela, text="Adivinhar", command=verificar_palpite)
botao_adivinhar.pack(pady=5)

label_resultado = tk.Label(janela, text="Tente adivinhar o número entre 1 e 100.")
label_resultado.pack(pady=5)

label_tentativas = tk.Label(janela, text="Tentativas: 0")
label_tentativas.pack()

botao_novo = tk.Button(janela, text="Novo Jogo", command=novo_jogo)
botao_novo.pack(pady=5)

botao_ranking = tk.Button(janela, text="Ver Ranking", command=mostrar_ranking)
botao_ranking.pack(pady=5)

# Inicia o primeiro jogo
novo_jogo()
janela.mainloop()
