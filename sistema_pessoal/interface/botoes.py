from tkinter import messagebox
from sistema_pessoal.banco.registros_pessoas import inserir, ler, mudar, apagar
from sistema_pessoal.interface.validacao import validar_dados


def limpar(window):
    for widget in window.winfo_children():
        widget.destroy()


def botao_cadastrar(caminho, nome, idade, email, telefone):
    valido, erro = validar_dados(
        nome.get(),
        idade.get(),
        email.get(),
        telefone.get()
    )

    if not valido:
        messagebox.showerror("Erro", erro)
        return

    sucesso = inserir(
        caminho,
        nome.get(),
        idade.get(),
        email.get(),
        telefone.get()
    )

    if sucesso:
        messagebox.showinfo("Sucesso", "Cadastro realizado")
    else:
        messagebox.showerror("Erro", "Falha ao cadastrar")


def botao_buscar(caminho, codigo, label):
    if not codigo.get().isdigit():
        label.config(text="ID inválido")
        return

    resultado = ler(caminho, int(codigo.get()))

    if resultado:
        texto = (
            f"ID: {resultado['id']}\n"
            f"Nome: {resultado['nome']}\n"
            f"Idade: {resultado['idade']}\n"
            f"Email: {resultado['email']}\n"
            f"Telefone: {resultado['telefone']}"
        )
        label.config(text=texto)
    else:
        label.config(text="Não encontrado")


def botao_editar(caminho, codigo, nome, idade, email, telefone):
    if not codigo.get().isdigit():
        messagebox.showerror("Erro", "ID inválido")
        return

    valido, erro = validar_dados(
        nome.get(),
        idade.get(),
        email.get(),
        telefone.get()
    )

    if not valido:
        messagebox.showerror("Erro", erro)
        return

    sucesso = mudar(
        caminho,
        int(codigo.get()),
        nome.get(),
        idade.get(),
        email.get(),
        telefone.get()
    )

    if sucesso:
        messagebox.showinfo("Sucesso", "Registro atualizado")
    else:
        messagebox.showerror("Erro", "Registro não encontrado ou falha ao atualizar")


def botao_deletar(caminho, codigo):
    if not codigo.get().isdigit():
        messagebox.showerror("Erro", "ID inválido")
        return

    sucesso = apagar(caminho, int(codigo.get()))

    if sucesso:
        messagebox.showinfo("Sucesso", "Registro removido")
    else:
        messagebox.showerror("Erro", "Registro não encontrado")
