import tkinter as tk
import Faculdade.BackEnd.Python.Estudo.Cadastro_produtos.cadastroTkinter.editar as editar
import Faculdade.BackEnd.Python.Estudo.Cadastro_produtos.cadastroTkinter.visualizar as visualizar
import Faculdade.BackEnd.Python.Estudo.Cadastro_produtos.cadastroTkinter.adicionar as adicionar
import Faculdade.BackEnd.Python.Estudo.Cadastro_produtos.cadastroTkinter.conectarsql as conectarsql
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

    opcoes = {
        "Adicionar": (
            15,
            2,
            lambda: adicionar.adicionar_produtos(janela_opcoes, Produtos),
        ),
        "Editar": (15, 2, lambda: editar.produto_editar(Produtos, janela_opcoes)),
        "Ver Info": (15, 2, lambda: visualizar.visualizar_produto(Produtos, janela_opcoes)),
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
        button(
            janela_opcoes, text=f"{i}", width=largura, height=altura, command=funcao
        )

    janela_opcoes.protocol("WM_DELETE_WINDOW", lambda: fechar_programa(janela_opcoes))

    formatar_centro(janela_opcoes, 400, 400)
    janela_opcoes.config(background=BACKGROUND)
    janela_opcoes.title("Opções Gerais")
    janela_opcoes.mainloop()
