
# ============================================
#  TRATAMENTO DE ERROS – EXPLICAÇÃO E EXEMPLO
# ============================================

# Usamos try/except para lidar com erros que podem ocorrer em tempo de execução
# Isso evita que o programa "quebre" e permite tratarmos o erro de forma controlada.

# Exemplo 1: erro de divisão por zero
try:
    x = int(input("Digite um número para dividir 10: "))
    print("Resultado:", 10 / x)
except ZeroDivisionError:
    print("Erro: divisão por zero!")
except ValueError:
    print("Erro: valor inválido! Digite apenas números.")
finally:
    print("Fim da operação.")

# Exemplo 2: acessando arquivos
try:
    with open("exemplo.txt", "r") as arquivo:
        print(arquivo.read())
except FileNotFoundError:
    print("Erro: arquivo não encontrado.")
