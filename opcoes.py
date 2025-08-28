import tkinter as tk
import editar as editar
import visualizar as visualizar
import adicionar as adicionar
import conectarsql as conectarsql
from configs import *


Produtos = {}


def fechar_janela(janela: tk.Tk, janela_opcoes: tk.Toplevel):
    janela.withdraw()
    janela_opcoes.deiconify()


def fechar_programa(janela: tk.Tk):
    janela.destroy()
    exit()


def opcoes(tela_login: tk.Tk):
    janela_opcoes = tk.Toplevel(tela_login)
    try:
        tela_login.withdraw()
    except tk.TclError:
        pass
    finally:
        opcoes = {
            "Adicionar": (
                15,
                2,
                lambda: adicionar.adicionar_produtos(janela_opcoes, Produtos),
            ),
            "Editar": (
                15, 
                2, 
                lambda: editar.produto_editar(Produtos, janela_opcoes)
            ),
            "Ver Info": (
                15,
                2,
                lambda: visualizar.visualizar_produto(Produtos, janela_opcoes),
            ),
            "Infos Gerais": (
                15,
                2,
                lambda: visualizar.vizualizacao_geral(Produtos, janela_opcoes),
            ),
            "Adicionar ao SQL": (
                15,
                2,
                lambda: conectarsql.importar_sql(Produtos, janela_opcoes),
            ),
        }

        for i in opcoes:
            largura, altura, funcao = opcoes[i]
            button(janela_opcoes, text=f"{i}", width=largura, height=altura, command=funcao)

        janela_opcoes.protocol("WM_DELETE_WINDOW", lambda: fechar_programa(janela_opcoes))

        formatar_centro(janela_opcoes, 400, 400, "Opções Gerais")
        janela_opcoes.mainloop()
