from veiculo import Veiculo, Carro, Moto

# Crie pelo menos 3 veículos (seus dados, não os do exemplo)
v1 = Carro('Ford', 'Focus', 2020, 4)
v2 = Moto('Yamaha', 'MT-07', 2021, 689)
v3 = Carro('Chevrolet', 'Onix', 2022, 4)

garagem = [v1, v2, v3]

# percorra a lista e imprima cada veículo
for v in garagem:
    print(v)

# imprima quantos são Carros e quantos são Motos
carros = [v for v in garagem if isinstance(v, Carro)]
motos = [v for v in garagem if isinstance(v, Moto)]

print(f'Carros: {len(carros)} | Motos: {len(motos)}')