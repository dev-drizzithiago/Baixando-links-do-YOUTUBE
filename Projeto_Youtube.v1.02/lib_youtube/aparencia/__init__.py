import datetime
import tkinter as tk
from time import sleep
from tkinter import messagebox
from datetime import datetime, date
from lib_youtube.downloads import *
from lib_youtube.checagem import *

time_certo = datetime.now()
data = time_certo.strftime('%d-%m-%Y - %H-%M')



# Janelas adicionar links
# Responsável por dar uma melhor interação com usuário.
def janela_link(msg_arq_link):
    """
    Janela responsável por interagir melhor com o usuário.
    """
    class janelaLinks:
        def __init__(self):
            # Abrindo a janela
            self.janela_principal = tk.Tk()
            self.fonte_Padrao = ['Arial', '12']
            self.titulo = tk.Label(self.janela_principal, text='Bem vindo ao programa para baixar videos e audios do '
                                                               'YouTube', font=self.fonte_Padrao)
            self.titulo.pack(side='top')
            # Frame 1
            self.frame_1 = tk.Frame(self.janela_principal, height=50, width=700, padx=10, pady=10)
            self.frame_1.pack(fill=tk.X)

            self.frame_2 = tk.Frame(self.janela_principal, padx=10, pady=10)
            self.frame_2.pack(fill=tk.X)

            self.caixa_link = tk.Label(self.frame_1, text='Cole no campo abaixo', pady=3)
            self.caixa_link.pack(anchor='center')

            # Entrada de dados
            self.entrada_link = tk.Entry(self.frame_1, width=100, font=self.fonte_Padrao)
            self.entrada_link.pack(anchor='center')  # fill faz ajustar conforme mexe na janela

            # Botão adicionar
            self.botao_add = tk.Button(self.frame_2, text='CLIQUE AQUI PARA ADICIONAR O LINK NA BASE DE DADOS', command=self.link_add, pady=10)
            self.botao_add.pack(anchor='center')

            # Botão sair
            self.botao_limpar = tk.Button(self.frame_2, text='Sair', command=self.janela_principal.destroy)
            self.botao_limpar.pack(side='right')
            tk.mainloop()

        # Função para adicionar o link
        def link_add(self):
            from lib_youtube.checagem import add_links  # Chama a função para add link.
            link = self.entrada_link.get()  # add o link que foi colado na variável.

            # Filtra o que foi colado na caixa de texto, para evitar erros
            if link[:23] != 'https://www.youtube.com':
                log_arquivo_erro('Entre com um link valido do YouTube')  # Caso entre com algum dado incorreto.
                sleep(1)
                self.limpar()
            else:
                add_links(msg_arq_link, link)
                self.limpar()

        def limpar(self):
            self.entrada_link.delete('0', 'end')

    janelaLinks()


def arquivos():
    return 'C:/Youtube/Arquivos/links_youtube.txt'


def log():
    return 'C:/Youtube/Arquivos/_log_.log'


def log_arquivo_ok(msg_ok):
    msg = f' ==> {data} \n{msg_ok}'
    open_log = open(log(), 'a')
    open_log.write(f' Sem erro ==> {msg}\n')
    print(f'AVISO!!', f'{msg_ok}')


def log_arquivo_erro(msg_log):
    msg = f' ERRO ==> {data} \n{msg_log}'
    open_log = open(log(), 'a')
    open_log.write(f' Com erro ==> {msg}\n')
    messagebox.showwarning(f'AVISO!', f'{msg}')


def pasta_audio():
    return 'C:/YouTube/Audios'


def pasta_video():
    return 'C:/YouTube/Videos'


def linhas(msg_linhas=100):
    return '~' * msg_linhas


def janela_info(msg_info):
    messagebox.showinfo(f'YouTube', f'{msg_info}')



