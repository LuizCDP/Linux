import tkinter as tk
from tkinter import messagebox
import os
import subprocess
import sys

ARQUIVO_SENHA = "password.txt"

# Cria o arquivo de senha se não existir
if not os.path.exists(ARQUIVO_SENHA):
    with open(ARQUIVO_SENHA, "w") as f:
        f.write("1234")  # senha padrão

def carregar_senha():
    with open(ARQUIVO_SENHA, "r") as f:
        return f.read().strip()

def salvar_senha(nova_senha):
    with open(ARQUIVO_SENHA, "w") as f:
        f.write(nova_senha)

def alterar_senha():
    atual = entrada_atual.get()
    nova = entrada_nova.get()
    confirma = entrada_confirmar.get()

    if atual != carregar_senha():
        messagebox.showerror("Erro", "Senha atual incorreta.")
        return

    if nova != confirma:
        messagebox.showerror("Erro", "A nova senha não coincide com a confirmação.")
        return

    if nova.strip() == "":
        messagebox.showerror("Erro", "A nova senha não pode estar vazia.")
        return

    salvar_senha(nova)
    messagebox.showinfo("Sucesso", "Senha alterada com sucesso!")
    subprocess.Popen(["main.cmd"])
    root.destroy()

# Interface
root = tk.Tk()
root.title("Lunix")
root.geometry("350x300")
root.resizable(False, False)
root.attributes('-fullscreen', True)
tk.Label(root, text="Senha atual:", font=("Arial", 12)).pack(pady=(20, 5))
entrada_atual = tk.Entry(root, show="*", font=("Arial", 12), width=25)
entrada_atual.pack()

tk.Label(root, text="Nova senha:", font=("Arial", 12)).pack(pady=(15, 5))
entrada_nova = tk.Entry(root, show="*", font=("Arial", 12), width=25)
entrada_nova.pack()

tk.Label(root, text="Confirmar nova senha:", font=("Arial", 12)).pack(pady=(15, 5))
entrada_confirmar = tk.Entry(root, show="*", font=("Arial", 12), width=25)
entrada_confirmar.pack()

tk.Button(root, text="Alterar senha", font=("Arial", 12), command=alterar_senha).pack(pady=25)
def abrir_nova_janela():
    root.destroy()
    subprocess.Popen(["main.cmd"])

tk.Button(root, text="Tela de bloqueio", font=("Arial", 12), command=abrir_nova_janela).pack()
root.mainloop()