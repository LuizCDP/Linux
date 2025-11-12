import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw
import subprocess

NOME = "Luiz"
with open("password.txt", "r") as f:
    SENHA_CORRETA = f.read().strip()

def criar_imagem_redonda(imagem_path, tamanho=(150, 150)):
    imagem = Image.open(imagem_path).resize(tamanho, Image.Resampling.LANCZOS).convert("RGBA")
    mask = Image.new('L', tamanho, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + tamanho, fill=255)
    imagem.putalpha(mask)
    return ImageTk.PhotoImage(imagem)

def verificar():
    if entrada_senha.get() == SENHA_CORRETA:
        messagebox.showinfo("Acesso Permitido", f"Bem-vindo, {NOME}!")
        root.destroy()
        subprocess.Popen(["conf.cmd"], shell=True)
    else:
        messagebox.showerror("Erro", "Senha incorreta. Tente novamente.")
        entrada_senha.delete(0, tk.END)

root = tk.Tk()
root.title("Lunix")
root.attributes('-fullscreen', True)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
wallpaper_img = Image.open("wallpaper.jpg").resize((screen_width, screen_height), Image.Resampling.LANCZOS)
wallpaper = ImageTk.PhotoImage(wallpaper_img)

background_label = tk.Label(root, image=wallpaper)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

try:
    foto = criar_imagem_redonda("user.jpg", (200, 200))
    label_foto = tk.Label(root, image=foto, bg="black")
    label_foto.pack(pady=40)
except Exception as e:
    messagebox.showerror("Erro", f"Não foi possível carregar a imagem.\n{e}")

label_nome = tk.Label(root, text=NOME, font=("Arial", 24), fg="white", bg="black")
label_nome.pack(pady=10)

label_senha = tk.Label(root, text="Senha:", font=("Arial", 18), fg="white", bg="black")
label_senha.pack(pady=(20,5))

entrada_senha = tk.Entry(root, show="*", font=("Arial", 16), width=25)
entrada_senha.pack()

btn_verificar = tk.Button(root, text="Entrar", command=verificar, font=("Arial", 16), width=15)
btn_verificar.pack(pady=30)

root.mainloop()

