from pessoa import Pessoa

p1 = Pessoa('Fulano', 30)
p2 = Pessoa('Ciclano', 20)

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())

p1.comer('.')
p2.falar('assunto')
p1.parar_comer()
p2.comer('.')
p1.falar('assunto')
p2.parar_comer()
