from Aluguel import Aluguel

print('-------------------------------------------')
print('Esta aplicação usa a API Web aluguebug')
print('Info: https://aluguebug.herokuapp.com/ajuda')
print('-------------------------------------------')

aluguel = Aluguel()

print(aluguel.calcular_aluguel(1200, 4))
