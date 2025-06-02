import os

documentos = []

#Funcao para adicionar documentos na biblioteca virtual

def adicionar_documento():
    print('Adicionar novo documento!')
    titulo = input('Informe o titulo:')
    autor = input('Informe o nome do autor:')
    ano = input('Informe o ano de publicacao:')
    tipo = input('Informe o tipo do arquivo (pdf, txt, etc):')

    novo_documento = {
        'titulo': titulo,
        'autor': autor,
        'ano': ano,
        'tipo': tipo
    }

    documentos.append(novo_documento)
    print('Documento incluido com sucesso!')