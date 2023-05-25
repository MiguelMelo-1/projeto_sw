from project import app

# Verifica se o ficheiro run.py foi executado diretamente e não importado
if __name__ == '__main__':
    # Ativa o debugger
    app.run(debug = True)