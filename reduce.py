#!/usr/bin/env python3
import sys
from collections import defaultdict

frequencia = defaultdict(int)

# leitura igual ao seu reduce
for linha in sys.stdin:
    palavra, valor = linha.strip().split("\t")
    frequencia[palavra] += int(valor)

# ordenar igual seu código
frequencia_ordenada = sorted(frequencia.items(), key=lambda x: x[1], reverse=True)

# saída final
for palavra, freq in frequencia_ordenada:
    print(f"{palavra}\t{freq}")