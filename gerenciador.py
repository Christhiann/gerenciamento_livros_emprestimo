import tkinter as tk
from tkinter import messagebox
import datetime

# Classe para armazenar dados dos usuários
class Usuario:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, E-mail: {self.email}"

# Classe para armazenar dados dos livros
class Livro:
    def __init__(self, titulo, autor, codigo):
        self.titulo = titulo
        self.autor = autor
        self.codigo = codigo

    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Código: {self.codigo}"

# Classe para armazenar dados dos empréstimos
class Emprestimo:
    def __init__(self, usuario, livro, data_emprestimo, data_devolucao=None):
        self.usuario = usuario
        self.livro = livro
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao

    def registrar_devolucao(self):
        self.data_devolucao = datetime.datetime.now()
        
    def __str__(self):
        devolvido = self.data_devolucao if self.data_devolucao else "Em aberto"
        return f"Empréstimo: {self.livro.titulo} | Usuário: {self.usuario.nome} | Empréstimo: {self.data_emprestimo.strftime('%d/%m/%Y')} | Devolução: {devolvido}"

# Função para realizar o empréstimo
def realizar_emprestimo():
    try:
        nome = entry_nome.get()
        idade = int(entry_idade.get())
        email = entry_email.get()

        titulo = entry_titulo.get()
        autor = entry_autor.get()
        codigo = entry_codigo.get()

        if not nome or not email or not titulo or not autor or not codigo:
            messagebox.showwarning("Entrada inválida", "Todos os campos devem ser preenchidos!")
            return

        usuario = Usuario(nome, idade, email)
        livro = Livro(titulo, autor, codigo)
        data_emprestimo = datetime.datetime.now()

        emprestimo = Emprestimo(usuario, livro, data_emprestimo)

        # Adiciona o empréstimo na lista
        emprestimos.append(emprestimo)

        # Exibe uma mensagem de sucesso
        messagebox.showinfo("Sucesso", "Empréstimo realizado com sucesso!")

        # Atualiza a lista de empréstimos na interface
        atualizar_lista_emprestimos()

        #dar reset na lista
        entry_nome.delete(0, tk.END)
        entry_idade.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_titulo.delete(0, tk.END)
        entry_autor.delete(0, tk.END)
        entry_codigo.delete(0, tk.END)


    except ValueError:
        messagebox.showwarning("Entrada inválida", "Por favor, insira um valor numérico válido para a idade!")

# Função para atualizar a lista de empréstimos na interface
def atualizar_lista_emprestimos():
    lista_emprestimos.delete(0, tk.END)  # Limpa a lista
    for emp in emprestimos:
        lista_emprestimos.insert(tk.END, str(emp))  # Adiciona cada empréstimo à lista

# Função para exibir os empréstimos registrados
def mostrar_emprestimos():
    # Função para exibir os empréstimos em uma nova janela
    # Cria uma nova janela (campo sobreposto)
    janela_emprestimos = tk.Toplevel(root)
    janela_emprestimos.title("Empréstimos Realizados")
    
    # Cria uma lista para exibir os empréstimos
    listbox_emprestimos = tk.Listbox(janela_emprestimos, width=80, height=15)
    listbox_emprestimos.pack(padx=10, pady=10)

    # Preenche a lista com todos os empréstimos
    for emp in emprestimos:
        listbox_emprestimos.insert(tk.END, str(emp))

    # Botão para fechar a janela
    btn_fechar = tk.Button(janela_emprestimos, text="Fechar", command=janela_emprestimos.destroy)
    btn_fechar.pack(pady=10)
# Função para sair
def sair():
    root.quit()

# Lista para armazenar os empréstimos
emprestimos = []

# Criando a interface gráfica
root = tk.Tk()
root.title("Sistema de Empréstimos de Livros")

# Criando os widgets (caixas de texto, botões, etc.)
tk.Label(root, text="Nome do Usuário").grid(row=0, column=0, padx=10, pady=5)
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Idade do Usuário").grid(row=1, column=0, padx=10, pady=5)
entry_idade = tk.Entry(root)
entry_idade.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="E-mail do Usuário").grid(row=2, column=0, padx=10, pady=5)
entry_email = tk.Entry(root)
entry_email.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Título do Livro").grid(row=3, column=0, padx=10, pady=5)
entry_titulo = tk.Entry(root)
entry_titulo.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Autor do Livro").grid(row=4, column=0, padx=10, pady=5)
entry_autor = tk.Entry(root)
entry_autor.grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="Código do Livro").grid(row=5, column=0, padx=10, pady=5)
entry_codigo = tk.Entry(root)
entry_codigo.grid(row=5, column=1, padx=10, pady=5)

# Botões
btn_emprestimo = tk.Button(root, text="Realizar Empréstimo", command=realizar_emprestimo)
btn_emprestimo.grid(row=6, column=0, columnspan=2, pady=10)

btn_mostrar_emprestimos = tk.Button(root, text="Mostrar Empréstimos", command=mostrar_emprestimos)
btn_mostrar_emprestimos.grid(row=7, column=0, columnspan=2, pady=10)

btn_sair = tk.Button(root, text="Sair", command=sair)
btn_sair.grid(row=8, column=0, columnspan=2, pady=10)

# Lista para exibir os empréstimos realizados
lista_emprestimos = tk.Listbox(root, width=60, height=10)
lista_emprestimos.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

# Rodando a interface gráfica
root.mainloop()
