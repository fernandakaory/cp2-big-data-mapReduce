import re
import os

# Lista de arquivos de candidatos
arquivos = [
    "propostas/celso-russomanno.txt",
    "propostas/levy-fidelix.txt",
    "propostas/ana-luiza.txt",
    "propostas/carlos-giannazi.txt",
    "propostas/soninha.txt"
]

pasta_saida = "propostas-limpas"
os.makedirs(pasta_saida, exist_ok=True)

# Ler arquivo separado com as palavras que devem ser ignoradas
with open("stopwords.txt", "r", encoding="utf-8") as f:
    stopwords = set(f.read().split())

# Tratamento de cada arquivo
for caminho in arquivos:
    with open(caminho, "r", encoding="utf-8") as file:
        texto = file.read()

    # Limpeza
    texto = texto.lower()
    texto = re.sub(r"[^\w\s]", "", texto)

    palavras = [p for p in texto.split() if p not in stopwords]

    texto_limpo = " ".join(palavras)
    # Pegar nome original
    nome_arquivo = os.path.basename(caminho)

    # Separar nome e extensão
    nome, extensao = os.path.splitext(nome_arquivo)

    # Criar novo nome do arquivo tratado
    novo_nome = f"{nome}-limpo{extensao}"

    # Caminho final
    caminho_saida = os.path.join(pasta_saida, novo_nome)

    # Salvar arquivo limpo
    with open(caminho_saida, "w", encoding="utf-8") as f:
        f.write(texto_limpo)

    print(f"Arquivo salvo: {caminho_saida}")