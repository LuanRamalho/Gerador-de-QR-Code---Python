import qrcode
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def generate_qr_code():
    text = entry.get()
    if not text:
        messagebox.showwarning("Atenção", "Por favor, digite algo para gerar o QR Code.")
        return
    
    qr = qrcode.make(text)
    qr_image = ImageTk.PhotoImage(qr)

    qr_label.config(image=qr_image)
    qr_label.image = qr_image  # Mantém uma referência para a imagem

# Configurações da janela principal
root = tk.Tk()
root.title("Gerador de QR Code")
root.geometry("400x450")
root.configure(bg="#f0f0f0")

# Estilo das fontes
font_entry = ('Arial', 14)
font_button = ('Arial', 12, 'bold')

# Caixa de texto para entrada
entry = tk.Entry(root, width=40, font=font_entry, bd=2, relief="solid", justify="center")
entry.pack(pady=20)

# Botão para gerar o QR Code
generate_button = tk.Button(root, text="Gerar QR Code", command=generate_qr_code, font=font_button, bg="#4CAF50", fg="white", relief="raised", bd=3)
generate_button.pack(pady=10)

# Rótulo para exibir o QR Code
qr_label = tk.Label(root, bg="#f0f0f0")
qr_label.pack(pady=20)

# Inicia a interface
root.mainloop()
