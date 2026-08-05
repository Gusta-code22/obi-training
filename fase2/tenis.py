# /*
# Problema: Diferença entre Times
# Origem: OBI - Treino
# Status: Resolvido sozinho após estudar a ideia
# Tempo: 15 minutos
# Dificuldade pessoal: 6/10
# Aprendi:
# - Que existem apenas 3 combinações possíveis de duplas.
# #

a = int(input())
b = int(input())
c = int(input())
d = int(input())

poss1 = abs((a + b) - (c + d))
poss2 = abs((a + c) - (b + d))
poss3 = abs((a + d) - (b + c))

print(min(poss1, poss2, poss3))
