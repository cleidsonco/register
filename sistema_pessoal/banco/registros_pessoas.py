import sqlite3
import os


def criar_banco(nome):
    pasta = "database"
    os.makedirs(pasta, exist_ok=True)

    caminho = os.path.join(pasta, f"{nome}.db")

    try:
        sqlite3.connect(caminho).close()
    except sqlite3.Error:
        return None

    return caminho


def criar_tabelas(caminho):
    try:
        conn = sqlite3.connect(caminho)
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS registros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER NOT NULL,
                email TEXT NOT NULL,
                telefone TEXT NOT NULL
            )
        """)

        conn.commit()
        conn.close()
        return True

    except sqlite3.Error:
        return False


def inserir(caminho, nome, idade, email, telefone):
    try:
        conn = sqlite3.connect(caminho)
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO registros (nome, idade, email, telefone) VALUES (?, ?, ?, ?)",
            (nome, int(idade), email, telefone)
        )

        conn.commit()
        conn.close()
        return True

    except sqlite3.Error:
        return False


def ler(caminho, id_registro):
    try:
        conn = sqlite3.connect(caminho)
        cursor = conn.cursor()

        cursor.execute(
            "SELECT id, nome, idade, email, telefone FROM registros WHERE id = ?",
            (id_registro,)
        )

        resultado = cursor.fetchone()
        conn.close()

        if resultado:
            return {
                "id": resultado[0],
                "nome": resultado[1],
                "idade": resultado[2],
                "email": resultado[3],
                "telefone": resultado[4]
            }

        return None

    except sqlite3.Error:
        return None


def mudar(caminho, id_registro, nome, idade, email, telefone):
    try:
        conn = sqlite3.connect(caminho)
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE registros
            SET nome=?, idade=?, email=?, telefone=?
            WHERE id=?
        """, (nome, int(idade), email, telefone, id_registro))

        alterado = cursor.rowcount

        conn.commit()
        conn.close()

        return alterado > 0

    except sqlite3.Error:
        return False


def apagar(caminho, id_registro):
    try:
        conn = sqlite3.connect(caminho)
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM registros WHERE id=?",
            (id_registro,)
        )

        apagado = cursor.rowcount

        conn.commit()
        conn.close()

        return apagado > 0

    except sqlite3.Error:
        return False
