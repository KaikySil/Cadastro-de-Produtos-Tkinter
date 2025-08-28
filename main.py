import opcoes as opcoes
from configs import *


def Login():
    tela_login = tk.Tk()
    formatar_centro(tela_login, 300, 300, "Login")

    usuario = tk.StringVar()
    senha = tk.StringVar()

    label(tela_login, text="Login")

    entry(tela_login, textvariable=usuario).pack(padx=10, pady=20)

    label(tela_login, text="Senha")

    entry(
        tela_login,
        textvariable=senha,
        show="*",
    ).pack(padx=10, pady=10)

    button(
        tela_login,
        text="Entrar",
        command=lambda: verificacao(tela_login, usuario.get(), senha.get()),
    )

    tela_login.config(background=BACKGROUND)
    tela_login.mainloop()


def verificacao(tela_login: tk.Tk, usuario: str, senha: str):
    usuario = usuario.upper().strip()

    def janela_incorreto():
        label_erro(
            tela_login,
            text="Usuário ou senha inválidos!",
        )

    if usuario:
        if senha:
            opcoes.opcoes(tela_login)
        else:
            janela_incorreto()
    else:
        janela_incorreto()

if __name__ == "__main__":
    Login()
