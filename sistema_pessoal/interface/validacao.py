import re


def validar_dados(nome, idade, email, telefone):
    nome = nome.strip()
    email = email.strip()
    telefone = telefone.strip()

    if not nome:
        return False, "Nome vazio"

    if not idade.isdigit() or int(idade) <= 0 or int(idade) > 130:
        return False, "Idade inválida"

    padrao_email = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not re.match(padrao_email, email):
        return False, "Email inválido"

    telefone_limpo = re.sub(r"\D", "", telefone)

    if len(telefone_limpo) < 8 or len(telefone_limpo) > 15:
        return False, "Telefone inválido"

    return True, ""
