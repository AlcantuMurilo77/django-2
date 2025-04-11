
# ============================================
# MÓDULOS E IMPORTS – EXPLICAÇÃO E EXEMPLO
# ============================================

# Módulos são arquivos .py com funções, variáveis ou classes reutilizáveis.
# Podemos importar módulos padrão do Python ou criar os nossos.

# Módulo padrão
import math
print("Raiz quadrada de 25:", math.sqrt(25))  # Saída: 5.0

# Importando função específica de um módulo
from random import choice
print("Escolha aleatória:", choice(['maçã', 'banana', 'laranja']))

# Criando e usando um módulo próprio (exemplo):
# Suponha que temos um arquivo chamado frases.py com:
# def bom_dia():
#     return "Bom dia!"

# Podemos importar e usar assim:
# from frases import bom_dia
# print(bom_dia())
