import tkinter as tk
from tkinter import messagebox
from sistema_pessoal.interface.telas import mostrar_menu
from sistema_pessoal.banco.registros_pessoas import criar_banco, criar_tabelas


def main():
    window = tk.Tk()
    window.geometry('400x350')
    window.title('Sistema')

    caminho_banco = criar_banco('pessoas')

    if not caminho_banco:
        messagebox.showerror("Erro", "Falha ao criar banco de dados")
        window.destroy()
        return

    if not criar_tabelas(caminho_banco):
        messagebox.showerror("Erro", "Falha ao criar tabelas")
        window.destroy()
        return

    window.caminho_banco = caminho_banco

    mostrar_menu(window)

    window.mainloop()


if __name__ == '__main__':
    main()

