class Atributos:
    def __init__(self,nome,idade,tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    golpe = {
'Guerreiro': 'Espada',
'Mago': 'Magia',
'Monge': 'Artes Marciais',
'Ninja': 'Shurikens'
 }
    
    def attack(self):
       golpe_tipo = self.golpe.get(self.tipo, 'Golpe')
       print (f'O {self.nome} atacou utilizando {golpe_tipo}')

    def __str__(self):
       return f'Nome: {self.nome}, Idade: {self.idade}, Tipo: {self.tipo}'
    
herois = [
Atributos('Guts', 24, 'Guerreiro'),
Atributos('Patolino', 86, 'Mago'),
Atributos('Mestre Miyagi', 73, 'Monge'),
Atributos('Naruto', 12, 'Ninja')
]

for heroi in herois:
    print (heroi)
    heroi.attack()
    print()