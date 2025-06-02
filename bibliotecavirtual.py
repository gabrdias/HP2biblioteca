import os
import shutil

# Define o diretório base onde os arquivos da biblioteca serão organizados
BASE_DIR = "biblioteca_digital"

# Função que lista todos os documentos organizados por tipo e ano
def listar_documentos():
    documentos = {}
    for root, dirs, files in os.walk(BASE_DIR):  # percorre todas as pastas e arquivos
        for file in files:
            tipo = file.split('.')[-1].lower()  # extrai a extensão do arquivo
            ano = root.split(os.sep)[-1]        # extrai o ano da estrutura de diretórios
            if tipo not in documentos:
                documentos[tipo] = {}
            if ano not in documentos[tipo]:
                documentos[tipo][ano] = []
            documentos[tipo][ano].append(file)  # organiza por tipo e ano
    return documentos

# Função para adicionar um novo documento ao sistema
def adicionar_documento(caminho_arquivo, ano):
    if not os.path.exists(caminho_arquivo):  # verifica se o arquivo existe
        print("Arquivo não encontrado.")
        return
    tipo = caminho_arquivo.split('.')[-1].lower()  # pega a extensão do arquivo
    destino_dir = os.path.join(BASE_DIR, str(ano), tipo)  # monta o caminho de destino
    os.makedirs(destino_dir, exist_ok=True)  # cria as pastas se não existirem
    shutil.copy(caminho_arquivo, destino_dir)  # copia o arquivo para o destino
    print("Documento adicionado com sucesso.")

# Função para renomear um documento existente
def renomear_documento(ano, tipo, nome_antigo, novo_nome):
    caminho = os.path.join(BASE_DIR, str(ano), tipo, nome_antigo)
    novo_caminho = os.path.join(BASE_DIR, str(ano), tipo, novo_nome)
    if not os.path.exists(caminho):  # verifica se o arquivo original existe
        print("Arquivo não encontrado.")
        return
    os.rename(caminho, novo_caminho)  # renomeia o arquivo
    print("Documento renomeado com sucesso.")

# Função para remover um documento existente, com confirmação
def remover_documento(ano, tipo, nome_arquivo):
    caminho = os.path.join(BASE_DIR, str(ano), tipo, nome_arquivo)
    if os.path.exists(caminho):  # verifica se o arquivo existe
        confirm = input(f"Tem certeza que deseja remover '{nome_arquivo}'? (s/n): ")
        if confirm.lower() == 's':
            os.remove(caminho)  # remove o arquivo
            print("Documento removido com sucesso.")
        else:
            print("Ação cancelada.")
    else:
        print("Arquivo não encontrado.")

# Menu interativo principal, exibido quando o programa é executado
def menu_interativo():
    while True:
        print("\n--- MENU DA BIBLIOTECA DIGITAL ---")
        print("1. Listar documentos")
        print("2. Adicionar documento")
        print("3. Renomear documento")
        print("4. Remover documento")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        # Lista os documentos organizados
        if escolha == '1':
            documentos = listar_documentos()
            if not documentos:
                print("Nenhum documento encontrado.")
            else:
                for tipo, anos in documentos.items():
                    print(f"\nTipo: .{tipo}")
                    for ano, arquivos in anos.items():
                        print(f"  Ano: {ano}")
                        for nome in arquivos:
                            print(f"    - {nome}")

        # Solicita os dados e adiciona o documento
        elif escolha == '2':
            caminho = input("Caminho do arquivo: ")
            ano = input("Ano de publicação: ")
            adicionar_documento(caminho, ano)

        # Solicita dados e renomeia o documento
        elif escolha == '3':
            ano = input("Ano do documento: ")
            tipo = input("Tipo do arquivo (ex: pdf): ")
            antigo = input("Nome atual do arquivo: ")
            novo = input("Novo nome para o arquivo: ")
            renomear_documento(ano, tipo, antigo, novo)

        # Solicita dados e remove o documento
        elif escolha == '4':
            ano = input("Ano do documento: ")
            tipo = input("Tipo do arquivo (ex: pdf): ")
            nome = input("Nome do arquivo a remover: ")
            remover_documento(ano, tipo, nome)

        # Encerra o programa
        elif escolha == '5':
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Ponto de entrada do programa – executa o menu quando o script é iniciado
if __name__ == '__main__':
    menu_interativo()
