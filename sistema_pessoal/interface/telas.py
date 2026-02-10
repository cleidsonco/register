import tkinter as tk
from sistema_pessoal.interface.botoes import (
    limpar,
    botao_cadastrar,
    botao_buscar,
    botao_editar,
    botao_deletar
)

# ---------- CORES ----------
AZUL_PRINCIPAL = "#1E3A8A"
AZUL_SECUNDARIO = "#3B82F6"
FUNDO = "#EFF6FF"
BRANCO = "#FFFFFF"
TEXTO = "#374151"


# ---------- BOTÃO MODERNO ----------
def botao_moderno(parent, texto, comando):
    btn = tk.Button(
        parent,
        text=texto,
        bg=AZUL_PRINCIPAL,
        fg="white",
        activebackground=AZUL_SECUNDARIO,
        activeforeground="white",
        relief="flat",
        font=("Segoe UI", 11, "bold"),
        width=20,
        height=2,
        cursor="hand2",
        command=comando
    )
    return btn


# ---------- CAMPO MODERNO ----------
def campo_moderno(parent):
    entry = tk.Entry(
        parent,
        font=("Segoe UI", 11),
        bd=1,
        relief="solid",
        width=30
    )
    return entry


# ---------- MENU ----------
def mostrar_menu(window):
    limpar(window)
    window.configure(bg=FUNDO)

    card = tk.Frame(window, bg=BRANCO, padx=40, pady=40)
    card.pack(pady=40)

    titulo = tk.Label(
        card,
        text="Sistema de Cadastro",
        font=("Segoe UI", 18, "bold"),
        bg=BRANCO,
        fg=AZUL_PRINCIPAL
    )
    titulo.pack(pady=20)

    botao_moderno(card, "Cadastrar", lambda: tela_cadastro(window)).pack(pady=8)
    botao_moderno(card, "Buscar", lambda: tela_buscar(window)).pack(pady=8)
    botao_moderno(card, "Editar", lambda: tela_editar(window)).pack(pady=8)
    botao_moderno(card, "Deletar", lambda: tela_deletar(window)).pack(pady=8)


# ---------- TELA CADASTRO ----------
def tela_cadastro(window):
    limpar(window)
    window.configure(bg=FUNDO)

    card = tk.Frame(window, bg=BRANCO, padx=40, pady=40)
    card.pack(pady=30)

    tk.Label(card, text="Cadastro de Pessoa",
             font=("Segoe UI", 16, "bold"),
             bg=BRANCO, fg=AZUL_PRINCIPAL).pack(pady=15)

    tk.Label(card, text="Nome", bg=BRANCO, fg=TEXTO).pack(anchor="w")
    nome = campo_moderno(card)
    nome.pack(pady=5)

    tk.Label(card, text="Idade", bg=BRANCO, fg=TEXTO).pack(anchor="w")
    idade = campo_moderno(card)
    idade.pack(pady=5)

    tk.Label(card, text="Email", bg=BRANCO, fg=TEXTO).pack(anchor="w")
    email = campo_moderno(card)
    email.pack(pady=5)

    tk.Label(card, text="Telefone", bg=BRANCO, fg=TEXTO).pack(anchor="w")
    telefone = campo_moderno(card)
    telefone.pack(pady=5)

    botao_moderno(
        card,
        "Salvar",
        lambda: botao_cadastrar(
            window.caminho_banco,
            nome,
            idade,
            email,
            telefone
        )
    ).pack(pady=15)

    botao_moderno(card, "Voltar", lambda: mostrar_menu(window)).pack()


# ---------- BUSCAR ----------
def tela_buscar(window):
    limpar(window)
    window.configure(bg=FUNDO)

    card = tk.Frame(window, bg=BRANCO, padx=40, pady=40)
    card.pack(pady=30)

    tk.Label(card, text="Buscar Registro",
             font=("Segoe UI", 16, "bold"),
             bg=BRANCO, fg=AZUL_PRINCIPAL).pack(pady=15)

    tk.Label(card, text="ID", bg=BRANCO, fg=TEXTO).pack(anchor="w")
    codigo = campo_moderno(card)
    codigo.pack(pady=5)

    resultado = tk.Label(card, text="", bg=BRANCO, fg=TEXTO)
    resultado.pack(pady=10)

    botao_moderno(
        card,
        "Buscar",
        lambda: botao_buscar(
            window.caminho_banco,
            codigo,
            resultado
        )
    ).pack(pady=10)

    botao_moderno(card, "Voltar", lambda: mostrar_menu(window)).pack()


# ---------- EDITAR ----------
def tela_editar(window):
    limpar(window)
    window.configure(bg=FUNDO)

    card = tk.Frame(window, bg=BRANCO, padx=40, pady=40)
    card.pack(pady=30)

    tk.Label(card, text="Editar Registro",
             font=("Segoe UI", 16, "bold"),
             bg=BRANCO, fg=AZUL_PRINCIPAL).pack(pady=15)

    tk.Label(card, text="ID", bg=BRANCO, fg=TEXTO).pack(anchor="w")
    codigo = campo_moderno(card)
    codigo.pack(pady=5)

    tk.Label(card, text="Nome", bg=BRANCO, fg=TEXTO).pack(anchor="w")
    nome = campo_moderno(card)
    nome.pack(pady=5)

    tk.Label(card, text="Idade", bg=BRANCO, fg=TEXTO).pack(anchor="w")
    idade = campo_moderno(card)
    idade.pack(pady=5)

    tk.Label(card, text="Email", bg=BRANCO, fg=TEXTO).pack(anchor="w")
    email = campo_moderno(card)
    email.pack(pady=5)

    tk.Label(card, text="Telefone", bg=BRANCO, fg=TEXTO).pack(anchor="w")
    telefone = campo_moderno(card)
    telefone.pack(pady=5)

    botao_moderno(
        card,
        "Salvar",
        lambda: botao_editar(
            window.caminho_banco,
            codigo,
            nome,
            idade,
            email,
            telefone
        )
    ).pack(pady=15)

    botao_moderno(card, "Voltar", lambda: mostrar_menu(window)).pack()


# ---------- DELETAR ----------
def tela_deletar(window):
    limpar(window)
    window.configure(bg=FUNDO)

    card = tk.Frame(window, bg=BRANCO, padx=40, pady=40)
    card.pack(pady=30)

    tk.Label(card, text="Deletar Registro",
             font=("Segoe UI", 16, "bold"),
             bg=BRANCO, fg=AZUL_PRINCIPAL).pack(pady=15)

    tk.Label(card, text="ID", bg=BRANCO, fg=TEXTO).pack(anchor="w")
    codigo = campo_moderno(card)
    codigo.pack(pady=5)

    botao_moderno(
        card,
        "Deletar",
        lambda: botao_deletar(
            window.caminho_banco,
            codigo
        )
    ).pack(pady=15)

    botao_moderno(card, "Voltar", lambda: mostrar_menu(window)).pack()
