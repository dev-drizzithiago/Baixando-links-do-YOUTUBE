from lib_youtube.downloads import *
from lib_youtube.checagem import *
from lib_youtube.aparencia import *
import tkinter as tk

# criando pastas necessárias
criando_pasta()
criando_txt()
criando_log()


# Menu principal
def menu_principal(msg_menu):
    opcao_menu_principal = msg_menu
    if opcao_menu_principal == 1:
        janela_link(arquivos())

    elif opcao_menu_principal == 2:
        resp = menu_modelo(['Downloads Audios?', 'Downloads Videos?'])
        if resp == 1:
            download_audio(arquivos())
        elif resp == 2:
            download_video(arquivos())

    elif opcao_menu_principal == 3:
        pasta = 'c:/youTube/'
        opc_listagem = menu_modelo([f'Listar links: ', 'Listar Pastas: '])
        if opc_listagem == 1:
            listagem_links(arquivos())
        elif opc_listagem == 2:
            listagem_pastas(pasta)

    elif opcao_menu_principal == 5:
        janela_info('Muito obrigado!!! Finalizando o programa!!')


# menu principal
class botao_radio:
    def __init__(self):
        self.janele_radio = tk.Tk()
        self.label_1 = tk.Label(self.janele_radio, text='>>> Downloads Videos YOUTUBE <<<')
        self.label_1.pack(side='top')
        self.frame_1 = tk.Frame(self.janele_radio, height=5, width=40)
        self.frame_1.pack(side='left')
        self.frame_2 = tk.Frame(self.janele_radio, height=5, width=40)
        self.frame_2.pack(side='left')

        self.radio_valor = tk.IntVar()
        self.radio_valor.set(0)
        # Botão radio
        self.add_link = tk.Radiobutton(self.frame_1, text='==> Adicionar Link ',
                                       variable=self.radio_valor, value=1)
        self.add_link.pack(anchor='w')
        self.download = tk.Radiobutton(self.frame_1, text='==> Downloads ',
                                       variable=self.radio_valor, value=2)
        self.download.pack(anchor='w')
        self.listagem = tk.Radiobutton(self.frame_1, text='==> Listagem',
                                       variable=self.radio_valor, value=3)
        self.listagem.pack(anchor='w')
        # Botoes
        self.botao = tk.Button(self.frame_2, text='Selecionar', height=2, width=10,
                               command=self.opcao)
        self.botao.pack(side='top')
        self.botao.sair = tk.Button(self.frame_2, text='Sair', height=2, width=10,
                                    command=self.janele_radio.destroy)
        self.botao.sair.pack()
        tk.mainloop()

    def opcao(self):
        opcao = int(self.radio_valor.get())
        if opcao == 1:
            log_arquivo_ok('Adicionando link...')
        elif opcao == 2:
            log_arquivo_ok('Realizando downloads...')
        elif opcao == 3:
            log_arquivo_ok('\bListando arquivos...')
        menu_principal(opcao)


botao_radio()
