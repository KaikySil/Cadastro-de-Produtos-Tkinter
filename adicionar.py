import tkinter as tk
import opcoes as opcoes
from configs import *


def adicionar_produtos(janela_opcoes: tk.Tk, produtos: dict):
    """Tela que apresenta as entradas para adicionar produtos"""

    janela_adicionar = tk.Toplevel(janela_opcoes)
    add_nome_string = tk.StringVar()
    add_valor_string = tk.StringVar()
    add_qtde_string = tk.StringVar()

    campos = [
        ("Nome do Produto:", add_nome_string),
        ("Preço do produto:", add_valor_string),
        ("Quantidade do produto:", add_qtde_string),
    ]

    entradas = []
    for titulo, valor_titulo in campos:
        label(
            janela_adicionar,
            text=titulo,
        )

        entrada = entry(
            janela_adicionar,
            textvariable=valor_titulo,
        )
        entrada.pack(padx=10, pady=5)
        entradas.append(entrada)

    button(
        janela_adicionar,
        text="Adicionar",
        command=lambda: lancar_produtos(
            add_nome_string.get(),
            add_valor_string.get(),
            add_qtde_string.get(),
            entradas,
            janela_adicionar,
        ),
    )

    button(
        janela_adicionar,
        text="voltar",
        width=7,
        command=lambda: opcoes.fechar_janela(janela_adicionar, janela_opcoes),
    )

    formatar_centro(janela_adicionar, 550, 400, "Adicionar Produtos")

    def lancar_produtos(
        nome: str, valor: float, quantidade: int, entradas: int, janela_adicionar
    ):
        def limpar_entrada(entradas):
            for entrada in entradas:
                entrada.delete(0, tk.END)

        try:
            if nome and valor and quantidade != "":
                if nome.isdecimal():
                    label_erro(
                        janela_adicionar,
                        text="Nome do Produto não pode ser um número!",
                    )

                else:
                    nome = nome.upper()
                    produtos[nome] = float(valor), int(quantidade)
                    for indice, chave in enumerate(produtos):
                        if chave == nome:
                            indice += 1
                            produtos[nome] = produtos[nome] + (indice,)
                            break
                    label_sucesso(
                        janela_adicionar,
                        text=f"Produto {nome} adicionado com sucesso!",
                    )
            else:
                label_erro(
                    janela_adicionar,
                    text="Valores não podem ficar vazios!",
                )

        except ValueError:
            label_erro(
                janela_adicionar,
                text="Erro de valor, por favor adicione somente números nos campos Preço e Quantidade",
            )
        limpar_entrada(entradas)
