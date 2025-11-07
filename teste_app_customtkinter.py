import customtkinter as ctk

ctk.set_appearance_mode("dark")

app= ctk.CTk()
app.title('Divisor de salário')
app.geometry('300x300')

def validar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()
    




#Label
label_usuario = ctk.CTkLabel(app,text="Usuário")
label_usuario.pack(pady=10)

#entry
campo_usuario = ctk.CTkEntry(app,placeholder_text="Digite seu Usuário")
campo_usuario.pack(pady=10)

label_senha = ctk.CTkLabel(app,text="senha")
label_senha.pack(pady=10)

campo_senha = ctk.CTkEntry(app,placeholder_text="Digite sua senha")
campo_senha.pack(pady=10)

ctk.CTkButton(app,text="Login", command=validar_login)


app.mainloop()