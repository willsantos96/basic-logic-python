class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def myfunc(self):
        print('Olá, meu nome é ' + self.nome)
