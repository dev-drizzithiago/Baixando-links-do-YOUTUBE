from lib_youtube.aparencia import *
from os import makedirs, listdir
from pytube import YouTube
from re import search


# Criando pastas para o funcionamento programa.
def criando_pasta():
    try:
        makedirs('c:/YouTube/Arquivos')
        makedirs('c:/YouTube/Audios')
        makedirs('c:/YouTube/Videos')
        log_arquivo_ok('Programa executado pela primeiro vez - Pastas foram criadas')
    except FileExistsError:
        # Caso alguma pasta seja deletada, o programa ira verificar e cria outra automaticamente.
        vrf_arquivo()  # Função
        vrf_audios()  # Função
        vrf_videos()  # Função
        print('Iniciando o Programa...')  # Se todas as pastas estiverem corretas, programa inicia


# Verificador de pasta, caso alguma pasta seja deletada, ela refaz.
# Casa a pasta arquivos seja deletado, o arquivo.txt é refeita.
def vrf_arquivo():
    try:
        listdir('c:/YouTube/Arquivos')
    except FileNotFoundError:
        makedirs('c:/YouTube/Arquivos')
        log_arquivo_erro('Pasta não foi encontrada. Uma nova foi criada!')


def vrf_audios():
    try:
        listdir('c:/YouTube/Audios')
    except FileNotFoundError:
        makedirs('c:/YouTube/Audios')
        log_arquivo_erro('Pasta não foi encontrada. Uma nova foi criada!')


def vrf_videos():
    try:
        listdir('c:/YouTube/Videos')
    except FileNotFoundError:
        makedirs('c:/YouTube/Videos')
        log_arquivo_erro('Pasta não foi encontrada. Uma nova foi criada!')


# Filtro para números inteiros, não continua se não for número inteiro
def leiaInt(msg_int):
    while True:
        try:
            opcao_int = int(input(msg_int))
            return opcao_int
        except ValueError:
            log_arquivo_erro('Você entrou com um valor invalido. Digite novamente!')


# Função responsável por verificar se arquivo links_youtube.txt esta ok
def criando_txt():
    if not VRF_TXT(arquivos()):  # Se arquivo não estiver criado ou foi deletado
        ADD_TXT(arquivos())  # Se não tiver o arquivo.txt, ele é criado.


def criando_log():
    if not VRF_TXT(log()):
        ADD_LOG(log())


# Verifica se o arquivo links_youtube.txt esta criado. Se for a primeira vez que abre o programa
# ele vai retornar para ADD_TXT
def VRF_TXT(msg_vrf):
    try:
        open_vrf = open(msg_vrf, 'r')
        open_vrf.close()
        return True
    except FileNotFoundError:
        return False


# Caso seja a primeiro vez que abra o programa. A verificação retorna a solicitação;
def ADD_TXT(msg_add):
    try:
        open_add = open(msg_add, 'w')
        open_add.close()
        log_arquivo_ok('Arquivo links_youtube.txt foi criado!')
    except FileExistsError:
        log_arquivo_ok('Arquivo já esta criado!')


def verif_log(msg_log):
    try:
        open_log = open(msg_log, 'r')
        open_log.close()
        return True
    except FileExistsError:
        return False


def ADD_LOG(arq_erro):
    try:
        open_erro = open(arq_erro, 'w')
        open_erro.close()
        log_arquivo_ok('Arquivo LOG foi criado')
    except FileExistsError:
        log_arquivo_erro('Log de erros já esta criado!')


# Função responsável por adicionar os links do YouTube.
def add_links(msg_add, link):
    try:
        open_add = open(msg_add, 'a')  # Abre o arquivo links_youtube.txt
        open_add.write(f'{link}\n')  # Adiciona o link na linha e pula para proxima linha, para add futuros.
        open_add.close()  # Fecha o arquivo txt
        lista_link = YouTube(link)  # Prepara o link para printar na tela com título.
        print(lista_link.title)  # Mostra o título do link que foi adicionado.
        log_arquivo_ok('Link adicionado com sucesso!')
    except:
        log_arquivo_erro('ERRO não foi possível adicionar o link dentro do arquivo links_youtube.txt')


# Função responsável por lista os links no arquivo links_youtube.txt
def listagem_links(arq_listagem):
    try:
        listagem_open = open(arq_listagem, 'r')
        links_listagem = listagem_open
        try:
            print(f'Listando arquivo {arq_listagem}')
            for indice, valor in enumerate(links_listagem):
                titulo = YouTube(valor)
                print(f'{indice} - {titulo.title}')  # Lista o título do link.
                print(f'{valor}')  # Lista o link youtube.
        except ValueError:
            log_arquivo_erro('ERRO! Listagem não conseguiu abrir o arquivo de texto')
        listagem_open.close()
    except FileNotFoundError:
        log_arquivo_erro(f'Arquivo {arq_listagem} não foi encontrado!')


# Função responsável por listagem dos arquivos nas pastas.
def listagem_pastas(msg_pastas):
    cont = 0
    # Opção para escolher qual pasta lista. (Audio/Videos)
    opc_listagem = menu_modelo(['Listar pasta de Audios', 'Listar pasta de Videos'])
    log_arquivo_ok(f'Você escolheu a opção: {opc_listagem}')
    # Listagem Audio
    if opc_listagem == 1:
        pasta_audio = msg_pastas + 'Audios'
        print('Listando diretorio c:/YouTube/Audios')
        for music in listdir(pasta_audio):  # Lista a pasta por completo
            if search('mp3', music):  # Lista apenas os arquivos mp3
                print(f'    ==> {music}')
                cont += 1
        if cont == 0:
            print('Não foi encontrado nenhum arquivo de audio')
            sleep(0.5)
        print(linhas())

    # Listagem Videos
    elif opc_listagem == 2:
        pasta_videos = msg_pastas + 'Videos'
        print('Listando diretorio c:/YouTube/Videos')
        for movie in listdir(pasta_videos):
            if search('mp4', movie):
                print(f'    ==> {movie}')
                cont += 1
        if cont == 0:
            print('Nenhum arquivo de Video foi encontrado!')
        print(linhas())


# Função responsável por todos os menus do programa.
def menu_modelo(msg_menu):
    for indice, valor in enumerate(msg_menu):
        print(f'{indice + 1} - {valor}')
    while True:
        print(linhas())
        opcao_menu = leiaInt('Escolha uma opcao: ')
        if opcao_menu >= len(msg_menu) + 1:
            print('Voce escolheu uma opção invalida. Digite novamente!')
        else:
            return opcao_menu
