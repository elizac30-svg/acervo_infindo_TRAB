def conectar():

    import sqlite3

    conn = sqlite3.connect("acervo_trab/zacervo.db")
    conn.row_factory = sqlite3.Row
    return conn

def limpa_tela():

    import sys
    import subprocess

    if sys.platform == 'win32':
        subprocess.run(['cmd', '/c', 'cls'])
    else:
        subprocess.run(['clear'])

