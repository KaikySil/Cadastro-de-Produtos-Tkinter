import tkinter as tk


BACKGROUND = "#212121"
BACKGROUND_ENTRY = "#e8e8e8"
BACKGROUND_BUTTON = "#2b2b2b"
TEXTO_ENTRY = "#0f0f0f"
TEXTO = "#ffffff"
TEXTO_INCORRETO = "#c20000"
TEXTO_SUCESSO = "#398503"


def formatar_centro(tela, width, height, nome):
    ws = tela.winfo_screenwidth()
    hs = tela.winfo_screenheight()

    x = (ws / 2) - (width / 2)
    y = (hs / 2) - (height / 2)
    tela.title(nome)
    tela.config(background = BACKGROUND)
    return tela.geometry("%dx%d+%d+%d" % (width, height, x, y))


def passar_mouse(event):
    event.widget.config(bg="#262626")


def sair_mouse(event):
    event.widget.config(bg=BACKGROUND_BUTTON)


def button(janela_pai, **kwargs):
    configuracoes = {
        "bg": BACKGROUND_BUTTON,
        "fg": TEXTO,
        "bd": False,
        "activebackground": BACKGROUND,
        "activeforeground": TEXTO,
        "cursor": "hand2",
        "width": 10,
        "height": 1,
    }
    configuracoes.update(kwargs)
    botao = tk.Button(janela_pai, **configuracoes)
    botao.bind("<Enter>", passar_mouse)
    botao.bind("<Leave>", sair_mouse)
    return botao.pack(pady=10, padx=10)


def label(janela_pai, **kwargs):
    configuracoes = {"background": BACKGROUND, "fg": TEXTO}

    configuracoes.update(kwargs)
    return tk.Label(janela_pai, **configuracoes).pack(pady=10, padx=10)


def label_sucesso(janela_pai, **kwargs):
    configuracoes = {"background": BACKGROUND, "fg": TEXTO_SUCESSO}

    configuracoes.update(kwargs)
    return tk.Label(janela_pai, **configuracoes).pack(pady=10, padx=10)


def label_erro(janela_pai, **kwargs):
    configuracoes = {"background": BACKGROUND, "fg": TEXTO_INCORRETO}

    configuracoes.update(kwargs)
    return tk.Label(janela_pai, **configuracoes).pack(pady=10, padx=10)


def entry(janela_pai, **kwargs):
    configuracao = {
        "background": BACKGROUND_ENTRY,
        "fg": TEXTO_ENTRY,
        "border": False,
    }
    configuracao.update(kwargs)
    return tk.Entry(janela_pai, **configuracao)
