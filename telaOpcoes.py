import tkinter as tk
import telaEdicao
import telaVisualizacao
import telaAdicionar
import telaSql
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
            lambda: telaAdicionar.adicionar_produtos(janela_opcoes, Produtos),
        ),
        "Editar": (15, 2, lambda: telaEdicao.produto_editar(Produtos, janela_opcoes)),
        "Ver Info": (15, 2, lambda: telaVisualizacao.visualizar_produto(Produtos, janela_opcoes)),
        "Infos Gerais": (
            15,
            2,
            lambda: telaVisualizacao.vizualizacao_geral(Produtos, janela_opcoes),
        ),
        "Adicionar ao SQL": (
            15,
            2,
            lambda: telaSql.importar_sql(Produtos, janela_opcoes),
        ),
    }

    for i in opcoes:
        largura, altura, funcao = opcoes[i]
        botao = button(
            janela_opcoes, text=f"{i}", width=largura, height=altura, command=funcao
        )
        animacao_botao(botao)
        botao.pack(pady=15)

    janela_opcoes.protocol("WM_DELETE_WINDOW", lambda: fechar_programa(janela_opcoes))

    formatar_centro(janela_opcoes)
    janela_opcoes.config(background=BACKGROUND)
    janela_opcoes.geometry("400x400")
    janela_opcoes.title("Opções Gerais")
    janela_opcoes.mainloop()
