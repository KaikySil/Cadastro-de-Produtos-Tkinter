import tkinter as tk


BACKGROUND = "#212121"
BACKGROUND_ENTRY = "#e8e8e8"
BACKGROUND_BUTTON = "#2b2b2b"
TEXTO_ENTRY = "#0f0f0f"
TEXTO = "white"
TEXTO_INCORRETO = "#c20000"
TEXTO_SUCESSO = "#398503"


def formatar_centro(tela):
    w = 50
    h = 400

    ws = tela.winfo_screenwidth()
    hs = tela.winfo_screenheight()
        
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    return tela.geometry('%dx%d+%d+%d' % (w, h, x, y))


def passar_mouse(event):
    event.widget.config(bg = '#262626')  


def sair_mouse(event):
    event.widget.config(bg = BACKGROUND_BUTTON)


def animacao_botao(button):
    button.bind("<Enter>", passar_mouse)
    button.bind("<Leave>", sair_mouse)


def button(janela_pai, **kwargs):
    configuracoes = {
        "bg": BACKGROUND_BUTTON,
        "fg": TEXTO,
        "bd": False,
        "activebackground": BACKGROUND,
        "activeforeground": TEXTO,
        "cursor": "hand2"
    }
    configuracoes.update(kwargs)
    return tk.Button(janela_pai, **configuracoes)


def label(janela_pai, **kwargs):
    configuracoes = {
        "background": BACKGROUND,
        "fg": TEXTO
    }

    configuracoes.update(kwargs)
    return tk.Label(janela_pai, **configuracoes).pack(pady = 10, padx = 10)


def label_sucesso(janela_pai, **kwargs):
    configuracoes = {
        "background": BACKGROUND,
        "fg": TEXTO_SUCESSO
    }

    configuracoes.update(kwargs)
    return tk.Label(janela_pai, **configuracoes).pack(pady = 10, padx = 10)


def label_erro(janela_pai, **kwargs):
    configuracoes = {
        "background": BACKGROUND,
        "fg": TEXTO_INCORRETO
    }

    configuracoes.update(kwargs)
    return tk.Label(janela_pai, **configuracoes).pack(pady = 10, padx = 10)


def entry(janela_pai, **kwargs):
    configuracao = {
        "background": BACKGROUND_ENTRY,
        "fg": TEXTO_ENTRY,
        "border": False,
    }
    configuracao.update(kwargs)
    return tk.Entry(janela_pai, **configuracao)