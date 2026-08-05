"""
Problema: Recordes
Origem: OBI - Treino
Status: Resolvido sozinho
Tempo: < 5 minutos
Dificuldade pessoal: 1/10

Aprendi:
- Interpretar corretamente o enunciado.
- Comparar o resultado com dois recordes independentes.
- Resolver um problema simples utilizando condicionais.
"""

r = int(input())
m = int(input())
l = int(input())

if r < m:
    print("RM")
else:
    print("*")

if r < l:
    print("RO")
else:
    print("*")
