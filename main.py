import tkinter as tk
from tkinter import messagebox
import subprocess

def abrir_projeto_maquina_de_doces():
    subprocess.Popen(['python', 'case2-elevador/maquina-de-doces/main.py'])

def abrir_projeto_elevador():
    subprocess.Popen(['python', 'case2-elevador/elevador/tela.py'])

def abrir_projeto_analisador_lexico():
    subprocess.Popen(['python', 'case3-analisador-lexico/codigo/analisador.py'])

def criar_interface():
    root = tk.Tk()
    root.geometry("300x250")
    root.title("Escolha o projeto")

    # Função para abrir o projeto da máquina de doces ao clicar no botão
    botao_maquina_de_doces = tk.Button(root, text="Máquina de Doces", command=abrir_projeto_maquina_de_doces)
    botao_maquina_de_doces.pack(pady=25)

    # Função para abrir o projeto do elevador ao clicar no botão
    botao_elevador = tk.Button(root, text="Elevador", command=abrir_projeto_elevador)
    botao_elevador.pack(pady=25)

    botao_analisador_lexico = tk.Button(root, text="Analisador léxico", command=abrir_projeto_analisador_lexico)
    botao_analisador_lexico.pack(pady=25)

    root.mainloop()

if __name__ == "__main__":
    criar_interface()