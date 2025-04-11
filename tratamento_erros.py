# ================================================================
# TRATAMENTO DE ERROS EM PYTHON 
# ================================================================

# ----------------------------------------
# 1. ZeroDivisionError
# ----------------------------------------
# Ocorre quando tentamos dividir por zero.
try:
    x = int(input("Digite um número para dividir 10: "))
    print(10 / x)
except ZeroDivisionError:
    print("Erro: divisão por zero!")

# ----------------------------------------
# 2. ValueError
# ----------------------------------------
# Ocorre quando tentamos converter algo que não pode ser convertido.
try:
    numero = int(input("Digite um número inteiro: "))
except ValueError:
    print("Erro: valor inválido. Digite apenas números inteiros.")

# ----------------------------------------
# 3. TypeError
# ----------------------------------------
# Ocorre quando usamos tipos incompatíveis em uma operação.
try:
    print("Idade: " + 20)
except TypeError:
    print("Erro: tipo de dado incompatível.")

# ----------------------------------------
# 4. IndexError
# ----------------------------------------
# Ocorre quando tentamos acessar um índice que não existe na lista.
try:
    lista = [1, 2, 3]
    print(lista[10])
except IndexError:
    print("Erro: índice fora do intervalo da lista.")

# ----------------------------------------
# 5. KeyError
# ----------------------------------------
# Ocorre quando acessamos uma chave que não existe em um dicionário.
try:
    dados = {"nome": "João"}
    print(dados["idade"])
except KeyError:
    print("Erro: chave não encontrada no dicionário.")

# ----------------------------------------
# 6. FileNotFoundError
# ----------------------------------------
# Ocorre quando tentamos abrir um arquivo que não existe.
try:
    with open("arquivo_inexistente.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("Erro: arquivo não encontrado.")

# ----------------------------------------
# 7. NameError
# ----------------------------------------
# Ocorre quando usamos uma variável que não foi definida.
try:
    print(variavel_nao_definida)
except NameError:
    print("Erro: variável não definida.")

# ----------------------------------------
# 8. AttributeError
# ----------------------------------------
# Ocorre quando usamos um atributo ou método que não existe para o tipo.
try:
    x = 10
    x.append(5)
except AttributeError:
    print("Erro: atributo ou método inválido para este tipo.")

# ----------------------------------------
# 9. ModuleNotFoundError
# ----------------------------------------
# Ocorre quando tentamos importar um módulo inexistente.
try:
    import modulo_que_nao_existe
except ModuleNotFoundError:
    print("Erro: módulo não encontrado.")

# ----------------------------------------
# 10. RuntimeError
# ----------------------------------------
# Erro genérico que ocorre em tempo de execução.
try:
    raise RuntimeError("Erro em tempo de execução")
except RuntimeError:
    print("Erro: problema em tempo de execução.")
