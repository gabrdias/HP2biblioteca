import os

documentos = []

# Funcao para adicionar documentos na biblioteca virtual

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

# Função para listar todos os documentos

def listar_documentos():
    print('Lista de documentos:')
    if not documentos:
        print('Nenhum documento encontrado.')
        return
    for doc in documentos:
        print(f"{doc['titulo']} ({doc['ano']}) - {doc['autor']} [{doc['tipo_arquivo'].upper()}]")
