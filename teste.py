from testeclasses import Pessoa

p1 = Pessoa('Fulano', str(30))
p1.myfunc

p2 = Pessoa('Ciclano', str(20))

print('Olá, meu nome é ' + p1.nome, ' e eu tenho ' + p1.idade)
print('Olá, meu nome é ' + p2.nome, ' e eu tenho ' + p2.idade)
