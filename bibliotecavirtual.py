import os
import shutil
from datetime import datetime

# Diretório base da biblioteca
BASE_DIR = "biblioteca_digital"
LOG_PATH = os.path.join(BASE_DIR, "log.txt")

# Garante que a pasta da biblioteca exista
os.makedirs(BASE_DIR, exist_ok=True)

# Função para registrar logs de atividade
def registrar_log(acao, caminho):
    with open(LOG_PATH, "a", encoding="utf-8") as log:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"[{timestamp}] {acao.upper()}: {caminho}\n")

# Lista documentos organizados por tipo e ano
def listar_documentos():
    documentos = {}
    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            if file == "log.txt":
                continue
            tipo = file.split('.')[-1].lower()
            ano = root.split(os.sep)[-1]
            if tipo not in documentos:
                documentos[tipo] = {}
            if ano not in documentos[tipo]:
                documentos[tipo][ano] = []
            documentos[tipo][ano].append(file)
    return documentos

# Adiciona novo documento ao sistema (com verificação de duplicação)
def adicionar_documento(caminho_arquivo, ano):
    if not os.path.exists(caminho_arquivo):
        print("Arquivo não encontrado.")
        return

    tipo = caminho_arquivo.split('.')[-1].lower()
    destino_dir = os.path.join(BASE_DIR, str(ano), tipo)
    os.makedirs(destino_dir, exist_ok=True)

    nome_arquivo = os.path.basename(caminho_arquivo)
    destino_caminho = os.path.join(destino_dir, nome_arquivo)

    if os.path.exists(destino_caminho):
        print("⚠Já existe um documento com esse nome e tipo neste ano.")
        return

    shutil.copy(caminho_arquivo, destino_dir)
    print("Documento adicionado com sucesso.")
    registrar_log("adicionado", destino_caminho)

# Renomeia documento existente
def renomear_documento(ano, tipo, nome_antigo, novo_nome):
    caminho = os.path.join(BASE_DIR, str(ano), tipo, nome_antigo)
    novo_caminho = os.path.join(BASE_DIR, str(ano), tipo, novo_nome)

    if not os.path.exists(caminho):
        print("Arquivo não encontrado.")
        return
    if os.path.exists(novo_caminho):
        print("⚠Já existe um arquivo com o novo nome.")
        return

    os.rename(caminho, novo_caminho)
    print("Documento renomeado com sucesso.")
    registrar_log("renomeado", f"{caminho} → {novo_caminho}")

# Remove documento com confirmação
def remover_documento(ano, tipo, nome_arquivo):
    caminho = os.path.join(BASE_DIR, str(ano), tipo, nome_arquivo)
    if os.path.exists(caminho):
        confirm = input(f"Tem certeza que deseja remover '{nome_arquivo}'? (s/n): ")
        if confirm.lower() == 's':
            os.remove(caminho)
            print("Documento removido com sucesso.")
            registrar_log("removido", caminho)
        else:
            print("Ação cancelada.")
    else:
        print("Arquivo não encontrado.")

# Menu interativo principal
def menu_interativo():
    while True:
        print("\n--- MENU DA BIBLIOTECA DIGITAL ---")
        print("1. Listar documentos")
        print("2. Adicionar documento")
        print("3. Renomear documento")
        print("4. Remover documento")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

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

        elif escolha == '2':
            caminho = input("Caminho do arquivo: ")
            ano = input("Ano de publicação: ")
            adicionar_documento(caminho, ano)

        elif escolha == '3':
            ano = input("Ano do documento: ")
            tipo = input("Tipo do arquivo (ex: pdf): ")
            antigo = input("Nome atual do arquivo: ")
            novo = input("Novo nome para o arquivo: ")
            renomear_documento(ano, tipo, antigo, novo)

        elif escolha == '4':
            ano = input("Ano do documento: ")
            tipo = input("Tipo do arquivo (ex: pdf): ")
            nome = input("Nome do arquivo a remover: ")
            remover_documento(ano, tipo, nome)

        elif escolha == '5':
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Execução principal
if __name__ == '__main__':
    menu_interativo()
