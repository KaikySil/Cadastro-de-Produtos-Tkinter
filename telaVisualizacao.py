import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from configs import *


def visualizar_produto(produtos, janela_opcoes):
    if produtos != {}:

        janela_visualizacao = tk.Toplevel(janela_opcoes)

        def ver_produto_existe(ver_produto_info, janela_visualizacao):
            ver_produto_info = ver_produto_info.upper()
            if ver_produto_info in produtos:

                preco = produtos[ver_produto_info][0]
                qtde = produtos[ver_produto_info][1]
                indice = produtos[ver_produto_info][2]

                opcoes = {
                    "Preço": (preco, "reais"),
                    "Quantidade": (qtde, "unidades"),
                    "Indice": (indice, ""),
                }

                for i in opcoes:
                    valor, medida = opcoes[i]
                    label_sucesso(
                        janela_visualizacao,
                        text=f"O {i} atual do produto {ver_produto_info} é {valor} {medida}",
                    )

            else:
                label_erro(
                    janela_visualizacao,
                    text="Produto não existe!",
                )

        ver_produto_info = tk.StringVar()

        label(
            janela_visualizacao,
            text="Digite o nome do produto que deseja visualizar_produto as informações",
        )

        entry(janela_visualizacao, textvariable=ver_produto_info).pack(pady=10)

        botao_produto_buscar = button(
            janela_visualizacao,
            text="Buscar",
            command=lambda: ver_produto_existe(
                ver_produto_info.get(), janela_visualizacao
            ),
        )
        animacao_botao(botao_produto_buscar)
        botao_produto_buscar.pack(pady=10)

        formatar_centro(janela_visualizacao)
        janela_visualizacao.config(background=BACKGROUND)
        janela_visualizacao.title("Nome do Produto")
        janela_visualizacao.geometry("400x300")
        janela_visualizacao.mainloop()

    else:
        label_erro(
            janela_opcoes,
            text="Não há produtos cadastrados!",
        )


def vizualizacao_geral(produtos, janela_opcoes):
    if produtos != {}:
        style = ttk.Style()
        style.configure(
            "Custom.Treeview",
            background=BACKGROUND,
            fieldbackground=BACKGROUND,
            foreground=TEXTO,
        )
        style.configure(
            "Custom.Treeview.Heading",
            background=BACKGROUND,
            foreground=TEXTO,
        )

        janela_visualizacao_geral = tk.Toplevel(janela_opcoes)
        janela_visualizacao_geral.config(background=BACKGROUND)
        colunas = ("Nome Produto", "Preço", "Quantidade", "IdProduto")
        tabela = ttk.Treeview(
            janela_visualizacao_geral,
            columns=colunas,
            show="headings",
            style="Custom.Treeview",
        )
        tabela.heading("Nome Produto", text="Nome Produto")
        tabela.heading("Preço", text="Preço")
        tabela.heading("Quantidade", text="Quantidade")
        tabela.heading("IdProduto", text="IdProduto")

        for nome, (preco, quantidade, idProduto) in produtos.items():
            tabela.insert("", tk.END, values=(nome, preco, quantidade, idProduto))

        def item_selecionado(event):
            l = ["Nome", "Preço", "Quantidade"]
            selecionados = tabela.selection()
            for item_id in selecionados:
                item = tabela.item(item_id)
                valores = item["values"]
                registro = dict(zip(l, valores))
                mensagem = "\n".join(
                    f"{chave}: {valor}" for chave, valor in registro.items()
                )
                showinfo(title="Informação", message=mensagem)

        tabela.bind("<<TreeviewSelect>>", item_selecionado)

        tabela.grid(row=0, column=0, sticky="nsew")

        scrollbar = ttk.Scrollbar(
            janela_visualizacao_geral, orient=tk.VERTICAL, command=tabela.yview
        )

        tabela.configure(
            yscrollcommand=scrollbar.set,
        )

        scrollbar.grid(row=0, column=1, sticky="ns")

        janela_visualizacao_geral.grid_rowconfigure(0, weight=1)

        janela_visualizacao_geral.grid_columnconfigure(0, weight=1)

        formatar_centro(janela_visualizacao_geral)
        janela_visualizacao_geral.geometry("800x800")

    else:
        label_erro(
            janela_opcoes,
            text="Não há produtos cadastrados!",
        )
