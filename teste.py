import re

# Ler stopwords
with open("stopwords.txt", "r", encoding="utf-8") as f:
    stopwords = set(f.read().split())

# Ler arquivo original
with open("propostas/CELSO-RUSSOMANNO.txt", "r", encoding="utf-8") as file:
    texto = file.read()

# Limpeza
texto = texto.lower()
texto = re.sub(r'[^\w\s]', '', texto)

palavras = texto.split()

# Remover stopwords
palavras_filtradas = [p for p in palavras if p not in stopwords]

# Salvar arquivo limpo
with open("limpo.txt", "w", encoding="utf-8") as f:
    f.write(" ".join(palavras_filtradas))

print("Arquivo limpo gerado com sucesso!")