'''
Listar todos os arquivos do diretorio
agrupar os arquivos separadamente em pasta especificas
'''

import os
import shutil

#Funções para agrupamento de arquivos...


def listar_arquivos_de_diretorio() -> list():

    lista_de_arquivos = list()
    for elemento in os.listdir():
        if os.path.isfile(elemento):
            lista_de_arquivos.append(elemento)

    return lista_de_arquivos


def agrupar_arquivos(tipo_do_arquivo: str, novo_diretorio: str) -> None:

    if len(os.listdir()) == 1:
        print('zero arquivos!')
        return None
    else:
        lista_de_arquivos = listar_arquivos_de_diretorio()
        for arquivo in lista_de_arquivos:
            if arquivo[arquivo.rfind('.'):] == tipo_do_arquivo:
                if os.path.exists(novo_diretorio):
                    shutil.move(os.path.join(os.getcwd(), arquivo), os.path.join(os.getcwd(), novo_diretorio, arquivo))
                else:
                    os.mkdir(novo_diretorio)
                    shutil.move(os.path.join(os.getcwd(), arquivo), os.path.join(os.getcwd(), novo_diretorio, arquivo))


def executar_agrupamentos() -> None:

    agrupar_arquivos('.txt', 'Documentos de texto')
    agrupar_arquivos('.pdf', 'Documentos de PDF')
    agrupar_arquivos('.PDF', 'Documentos de PDF')
    agrupar_arquivos('.doc', 'Documentos Word')
    agrupar_arquivos('.docx', 'Documentos Word')
    agrupar_arquivos('.jpeg', 'Imagens')
    agrupar_arquivos('.png', 'Imagens')
    agrupar_arquivos('.jpg', 'Imagens')
    agrupar_arquivos('.ppt', 'Arquivos PowerPoint')
    agrupar_arquivos('.xlsx', 'Arquivos Excel')
    agrupar_arquivos('.exe', 'Instaladores de programas')
    agrupar_arquivos('.msi', 'Instaladores de programas')
    agrupar_arquivos('.rar', 'Arquivos compactados')
    agrupar_arquivos('.zip', 'Arquivos compactados')
    agrupar_arquivos('.mp4', 'Vídeos e filmes')
    agrupar_arquivos('.mkv', 'Vídeos e filmes')
    agrupar_arquivos('.mp3', 'Audio e músicas')


#Funções para desagrupar os arquivos...


def listar_diretorios_reservados() -> list:

    diretorios_reservados = ['Documentos de texto', 'Documentos de PDF', 'Documentos Word', 'Imagens',
                             'Arquivos PowerPoint', 'Arquivos Excel', 'Instaladores de programas',
                             'Arquivos compactados', 'Vídeos e filmes', 'Audio e músicas']
                               
    lista_de_diretorios = list()
    for elemento in os.listdir():
        if os.path.isdir(elemento) and elemento in diretorios_reservados:
            lista_de_diretorios.append(elemento)
    return lista_de_diretorios
            
    
def desagrupar_agrupamentos() -> None:

    for diretorio in listar_diretorios_reservados():
        for arquivo in os.listdir(os.path.join(os.getcwd(), diretorio)):
            if os.path.exists(os.path.join(os.getcwd(), arquivo)):
                os.rename(os.path.join(os.getcwd(), diretorio, arquivo), os.path.join(os.getcwd(), diretorio, 'cópia_' + arquivo))                               
                shutil.move(os.path.join(os.getcwd(), diretorio, 'cópia_' + arquivo), os.getcwd())
            else:
                shutil.move(os.path.join(os.getcwd(), diretorio, arquivo), os.getcwd())
            
    print('O desagrupamento funfou...')
    

def remover_diretorios_reservados() -> None:

    for diretorio in listar_diretorios_reservados():
        os.rmdir(os.path.join(os.getcwd(), diretorio))


def executar_desagrupamentos() -> None:

    desagrupar_agrupamentos()
    remover_diretorios_reservados()

    
#main program


def leitura_de_opcoes(txt) -> int:

    while True:
        try:
            opc = int(input(txt))
        except:
            print('opção inválida!')
        else:
            if opc != 1 and opc != 2:
                print('opção inválida!')
            else:
                return opc

opc = leitura_de_opcoes('1 - agrupar arquivos\n2 - desagrupar arquivos\nopção: ')
if opc == 1:
    executar_agrupamentos()
elif opc == 2:
    executar_desagrupamentos()
    
