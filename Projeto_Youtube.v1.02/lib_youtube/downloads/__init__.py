from os import path, remove
from lib_youtube.checagem import *
from lib_youtube.aparencia import *


# (Função) downloads audio.
def download_audio(msg_audio):
    global audio_titulo
    cont = 1
    try:
        open_audio_arq = open(msg_audio, 'r')  # Abre o arquivo que esta no formata .txt
        lista_links = open_audio_arq.readlines()  # Coloca as informações em uma 'lista'
        opc_audio = menu_modelo(['Baixar todos os links?', 'Escolher um link'])  # Opção
        if opc_audio == 1:
            print('Downloads em andamento...')
            for links in lista_links:
                try:
                    downloads_audio_all = YouTube(links)  # Modulo YouTube que prepara a variável
                    audio_titulo = downloads_audio_all.title
                    downloads_audio_all.streams.filter(only_audio=True).first().download(pasta_audio())
                    log_arquivo_ok(f'Downloads {audio_titulo} completo!')  # Janela informação
                    cont += 1
                except:
                    log_arquivo_erro(f'Não foi possível realizar o download do audio {audio_titulo}')
                log_aquivo_ok(f'{cont} baixados')
            print('Convertendo arquivos para MP3')
            converter()  # Converter arquivo audio.mp4 para .mp3 / modulo

        elif opc_audio == 2:
            while True:
                listagem_links(msg_audio)  # Lista os links para fazer o downloads.
                opc_download = leiaInt('Escolha um link para downloads: ')  # Opção do link
                if opc_download > len(lista_links):  # Não permite escolher opções que não existam.
                    log_arquivo_erro('Esse link não existe!')
                else:
                    downloads_audio_only = YouTube(lista_links[opc_download])
                    audio_titulo = downloads_audio_only.title
                    print('Downloads em andamento...')
                    try:
                        downloads_audio_only.streams.filter(only_audio=True).first().download(pasta_audio())
                    except:
                        log_arquivo_erro(f'Erro ao realizar o downloads do arquivo {audio_titulo}')
                    converter()
                    log_arquivo_ok(f'Downloads {audio_titulo} finalizado!')

    except FileNotFoundError:
        log_arquivo_erro(f'Arquivo {msg_audio} não encontrado!! (downloads_audio)')


# (Função) downloads Video
def download_video(msg_video):
    global downloads_videos_all
    try:
        open_video = open(msg_video, 'r')
        lista_videos = open_video.readlines()
        opc_videos = menu_modelo(['Baixar todos os videos?',
                                  'Escolher um video para baixar?'])
        if opc_videos == 1:
            print('Downloads em andamento...')
            for links in lista_videos:
                try:
                    downloads_videos_all = YouTube(links)
                    downloads_videos_all.streams.filter(adaptive=True).first().download(pasta_video())
                    log_arquivo_ok(f'Downloads {downloads_videos_all.title} concluído!')
                except:
                    log_arquivo_erro(f'Não foi possível realizar o downloads do videos {downloads_videos_all.title} (downloads_videos)')
            log_arquivo_ok('Todos os arquivos foram baixados')
        elif opc_videos == 2:
                listagem_links(msg_video)
                opc_downloads = leiaInt('Escolha um um link para downloads: ')
                downloads_videos_only = YouTube(lista_videos[opc_downloads])
                try:
                    print(f'Downloads {downloads_videos_only.title} em andamento...')
                    downloads_videos_only.streams.filter(adaptive=True).first().download(pasta_video())
                    log_arquivo_ok(f'Downloads {downloads_videos_only.title} concluído!')
                except:
                    log_arquivo_erro(f'{data} ==> Não foi possível realizar o downloads do videos {downloads_videos_only.title} (downloads_videos')
        open_video.close()
    except FileNotFoundError:
        log_arquivo_erro('Não foi encontrado o arquivo de texto')


def converter():
    """
    ==> Converte o arquivo .mp4 na pasta Audio, para .mp3
    Obs.: Quando programa é compilado, essa função não funciona.
    """
    global mp4_file
    try:
        from moviepy.editor import AudioFileClip
        from re import search
        for file in listdir(pasta_audio()):
            if search('mp4', file):
                try:
                    mp4_file = path.join(pasta_audio(), file)
                    mp3_file = path.join(pasta_audio(), path.splitext(file)[0] + '.mp3')
                    novo_mp3 = AudioFileClip(mp4_file)
                    novo_mp3.write_audiofile(mp3_file)
                    remove(mp4_file)
                    log_arquivo_ok(f'Arquivo {mp4_file} convertido com sucesso')
                except:
                    log_arquivo_erro(f'Não foi possível converter o arquivo {mp4_file} para mp3')
    except AttributeError:
        log_arquivo_erro('''Modulo moviepy não funciona quando o programa é compilado.
        Downloads do arquivo .mp4 foi concluído''')
    except:
        log_arquivo_erro('Não foi possível converter o arquivo .mp4 para .mp3')
