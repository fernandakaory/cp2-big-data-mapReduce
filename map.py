#!/usr/bin/env python3
import sys

for linha in sys.stdin:
    palavras = linha.strip().split()
    
    # mantém sua lógica de map
    mapped = [(p, 1) for p in palavras]

    for palavra, count in mapped:
        print(f"{palavra}\t{count}")