import tkinter as tk
import mysql.connector
from configs import *
from datetime import datetime


def importar_sql(produtos: dict, janela_opcoes: tk.Tk):
    if produtos != {}:
        janela_sql = tk.Toplevel(janela_opcoes)
        formatar_centro(janela_sql, 400, 400)
        nome_host = tk.StringVar()
        nome_user = tk.StringVar()
        senha_base = tk.StringVar()
        base_dados = tk.StringVar()

        campos = [
            ("Nome do Host:", nome_host),
            ("User:", nome_user),
            ("Senha:", senha_base),
            ("Base de Dados:", base_dados),
        ]

        for nome, valor in campos:
            label(janela_sql, text=nome, width=20)
            if nome == "Senha:":
                entry(janela_sql, textvariable=valor, show="*").pack()
            else:
                entry(janela_sql, textvariable=valor).pack()

        button(
            janela_sql,
            text="Adicionar",
            width=10,
            command=lambda: verificar_base(
                nome_host.get(),
                nome_user.get(),
                senha_base.get(),
                base_dados.get(),
                janela_sql,
            ),
        )

        janela_sql.config(bg=BACKGROUND)
        janela_sql.title("Informações do Banco SQL")

        def verificar_base(
            nome_host: str,
            nome_user: str,
            senha_base: str,
            base_dados: str,
            janela_sql: str,
        ):
            try:
                conectar = mysql.connector.connect(
                    host=nome_host,
                    user=nome_user,
                    password=senha_base,
                    database=base_dados,
                )
                if conectar.is_connected():
                    label_sucesso(
                        janela_sql,
                        text="CONECTADO!",
                    )

                    cursor = conectar.cursor()
                    cursor.execute(
                        "CREATE TABLE IF NOT EXISTS Produtos (idProduto INT PRIMARY KEY, nomeProduto VARCHAR(255), Preco DECIMAL(10,2), Quantidade INT, Data DATE)"
                    )

                    valores = produtos.items()

                    for nome, valores in valores:
                        tempo = datetime.now()
                        horario = tempo.strftime("%Y-%m-%d")
                        cursor.execute(
                            f"INSERT INTO Produtos (idProduto, nomeProduto, Preco, Quantidade, Data) VALUES ('{valores[2]}', '{nome}', '{valores[0]}', '{valores[1]}', '{horario}')"
                        )

                    conectar.commit()
                    label_sucesso(
                        janela_sql,
                        text="Adicionado com sucesso!",
                    )
                    conectar.close()
                    cursor.close()

            except mysql.connector.errors.DatabaseError as error:
                label_erro(
                    janela_sql,
                    text="ERRO!",
                )
                print(error)

    else:
        label_erro(
            janela_opcoes,
            text="Não há Produtos cadastrados!",
        )
