
# ============================================
# POO  – INTRODUÇÃO A CLASSES E OBJETOS
# ============================================

# POO = Programação Orientada a Objetos
# Usamos classes para representar "coisas" com características (atributos) e ações (métodos)

# Criando uma classe simples
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, eu sou {self.nome} e tenho {self.idade} anos.")

# Criando objetos
p1 = Pessoa("João", 30)
p2 = Pessoa("Maria", 25)

# Chamando métodos
p1.apresentar()
p2.apresentar()

# Podemos criar várias classes para representar coisas diferentes
class Musica:
    def __init__(self, titulo, artista):
        self.titulo = titulo
        self.artista = artista

    def tocar(self):
        print(f"Tocando '{self.titulo}' de {self.artista}.")

musica1 = Musica("Imagine", "John Lennon")
musica1.tocar()
