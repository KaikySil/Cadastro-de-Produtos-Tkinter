import tkinter as tk
from configs import *


def produto_editar(produtos: dict, janela_opcoes: tk.Tk):
    if produtos != {}:
        janela_editar = tk.Toplevel(janela_opcoes)

        def produto_verificar(nome_produto_editar, janela_editar_nome):
            nome_produto_editar = nome_produto_editar.upper()
            if nome_produto_editar in produtos:
                janela_opcoes_edicao = tk.Toplevel(janela_editar_nome)
                janela_opcoes_edicao.config(background=BACKGROUND)
                formatar_centro(janela_opcoes_edicao)
                janela_opcoes_edicao.title("Opções de Edição")
                janela_opcoes_edicao.geometry("300x300")

                opcoes = {
                    "Editar Nome": (
                        lambda: nome_editar(nome_produto_editar, janela_opcoes_edicao)
                    ),
                    "Editar Preço": (
                        lambda: preco_editar(nome_produto_editar, janela_opcoes_edicao)
                    ),
                    "Editar Qtde": (
                        lambda: quantidade_editar(
                            nome_produto_editar, janela_opcoes_edicao
                        )
                    ),
                    "Remover": (
                        lambda: produto_remover(
                            nome_produto_editar, janela_opcoes_edicao, janela_editar
                        )
                    ),
                }

                for i in opcoes:
                    funcao = opcoes[i]
                    botao_opcoes_edicao = button(
                        janela_opcoes_edicao, text=i, width=10, command=funcao
                    )
                    animacao_botao(botao_opcoes_edicao)
                    botao_opcoes_edicao.pack(pady=15)

            else:
                label_erro(
                    janela_editar_nome,
                    text="Produto não existe",
                )

        def nome_editar(nome_produto_editar, janela_opcoes_edicao):

            def nome_alterar(nome_novo_produto, produto_editar, janela_nome_existe):
                nome_novo_produto = nome_novo_produto.upper()
                if nome_novo_produto != produto_editar and nome_novo_produto != "":
                    try:
                        nome_novo_produto = int(nome_novo_produto)
                        label_erro(
                            janela_editar_nome,
                            text="Nome não pode ser um número!",
                        )
                    except ValueError:
                        try:
                            produtos[nome_novo_produto] = produtos[produto_editar]
                            del produtos[produto_editar]
                            label_sucesso(
                                janela_nome_existe,
                                text=f"Produto {produto_editar} editado para {nome_novo_produto} com sucesso",
                            )
                            janela_opcoes_edicao.destroy()
                        except KeyError:
                            label_erro(
                                janela_nome_existe,
                                text="Nome do produto ja alterado",
                            )
                else:
                    label_erro(
                        janela_nome_existe,
                        text="Novo nome não pode ser o mesmo que o nome anterior ou um valor vazio",
                    )

            if nome_produto_editar in produtos:
                janela_editar_nome = tk.Toplevel(janela_editar)
                nome_editar_string = tk.StringVar()

                label(
                    janela_editar_nome,
                    text=f"Digite o novo nome do produto {nome_produto_editar}",
                )

                entry(janela_editar_nome, textvariable=nome_editar_string).pack(pady=10)

                botao_nome_alterar = button(
                    janela_editar_nome,
                    text="Alterar",
                    command=lambda: nome_alterar(
                        nome_editar_string.get(),
                        nome_produto_editar,
                        janela_editar_nome,
                    ),
                )
                animacao_botao(botao_nome_alterar)
                botao_nome_alterar.pack(pady=10)

                janela_editar_nome.config(background=BACKGROUND)
                formatar_centro(janela_editar_nome)
                janela_editar_nome.title("Editar Nome")
                janela_editar_nome.geometry("500x200")
                janela_editar_nome.mainloop()
            else:
                label_erro(
                    janela_opcoes_edicao,
                    text="Produto removido!",
                )

        def preco_editar(nome_produto_editar, janela_opcoes_edicao):

            def preco_alterar(nome_produto_editar, novoPreco):
                try:
                    novoPreco = float(novoPreco)
                    quantidade = produtos[nome_produto_editar][1]
                    indice = produtos[nome_produto_editar][2]
                    del produtos[nome_produto_editar]
                    produtos[nome_produto_editar] = novoPreco, quantidade, indice

                    label_sucesso(
                        janela_preco_editar,
                        text="Preço alterado com sucesso!",
                    )

                except ValueError:
                    label_erro(
                        janela_preco_editar,
                        text="Preço não pode ser uma letra!",
                    )

            if nome_produto_editar in produtos:
                janela_preco_editar = tk.Toplevel(janela_editar)
                label(
                    janela_preco_editar,
                    text=f"Preço atual do Produto: {nome_produto_editar} = R${produtos[nome_produto_editar][0]}, Digite um novo valor",
                )

                novoPreco = tk.StringVar()

                entry(janela_preco_editar, textvariable=novoPreco).pack(pady=10)

                botao_preco_alterar = button(
                    janela_preco_editar,
                    text="Alterar",
                    command=lambda: preco_alterar(nome_produto_editar, novoPreco.get()),
                )
                animacao_botao(botao_preco_alterar)
                botao_preco_alterar.pack(pady=10)

                janela_preco_editar.config(background=BACKGROUND)
                formatar_centro(janela_preco_editar)
                janela_preco_editar.title("Editar Preço")
                janela_preco_editar.geometry("400x200")

            else:
                label_erro(janela_opcoes_edicao, text="Produto removido!")

        def quantidade_editar(nome_produto_editar, janela_opcoes_edicao):
            def quantidade_alterar(nome_produto_editar, qtde_nova, janela_qtde_editar):
                try:
                    int(qtde_nova)
                    valor = produtos[nome_produto_editar][0]
                    indice = produtos[nome_produto_editar][2]
                    del produtos[nome_produto_editar]
                    produtos[nome_produto_editar] = valor, qtde_nova, indice
                    label_sucesso(
                        janela_qtde_editar,
                        text="Quantidade Alterada com sucesso!",
                    )

                except ValueError:
                    label_erro(
                        janela_qtde_editar,
                        text="Preço não pode ser uma letra!",
                    )

            if nome_produto_editar in produtos:
                janela_qtde_editar = tk.Toplevel(janela_editar)
                label(
                    janela_qtde_editar,
                    text=f"Quantidade atual do Produto: {nome_produto_editar} = {produtos[nome_produto_editar][1]} unidades, Digite um novo valor",
                )

                qtde_nova = tk.StringVar()

                entry(janela_qtde_editar, textvariable=qtde_nova).pack(pady=10)

                botao_qtde_editar = button(
                    janela_qtde_editar,
                    text="Alterar",
                    command=lambda: quantidade_alterar(
                        nome_produto_editar, qtde_nova.get(), janela_qtde_editar
                    ),
                )
                animacao_botao(botao_qtde_editar)
                botao_qtde_editar.pack(pady=10)

                janela_qtde_editar.config(background=BACKGROUND)
                formatar_centro(janela_qtde_editar)
                janela_qtde_editar.title("Editar Quantidade")
                janela_qtde_editar.geometry("450x200")
            else:
                label_erro(
                    janela_opcoes_edicao,
                    text="Produto removido!",
                )

        def produto_remover(produto_retirar, janela_opcoes_edicao, janela_produto_nome):
            if produto_retirar in produtos:
                produto = produto_retirar
                del produtos[produto_retirar]
                label_sucesso(
                    janela_opcoes_edicao,
                    text=f"Produto {produto} removido!",
                )
                janela_opcoes_edicao.destroy()
                janela_produto_nome.destroy()

            else:
                label_erro(
                    janela_opcoes_edicao,
                    text=f"Produto já removido!",
                )

        label(
            janela_editar,
            text="Digite o nome do Produto que deseja editar, seu Nome, Preço ou Quantidade",
        )

        nome_produto_editar = tk.StringVar()

        entry(janela_editar, textvariable=nome_produto_editar).pack(pady=10)

        botao_verificar = button(
            janela_editar,
            text="Verificar",
            command=lambda: produto_verificar(nome_produto_editar.get(), janela_editar),
        )
        animacao_botao(botao_verificar)
        botao_verificar.pack(pady=10)

        formatar_centro(janela_editar)
        janela_editar.config(background=BACKGROUND)
        janela_editar.geometry("500x200")
        janela_editar.title("Nome do Produto")
        janela_editar.mainloop()
    else:
        label_erro(
            janela_opcoes,
            text="Não há Produtos cadastrados!",
        )
