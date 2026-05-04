# PASSO 1 — CLASSE PAI: VEÍCULO

class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano

    @property
    def marca(self):
        return self.__marca

    @property
    def modelo(self):
        return self.__modelo

    @property
    def ano(self):
        return self.__ano

    def descrever(self):
        return f'{self.__marca} {self.__modelo} ({self.__ano})'

    def __str__(self):
        return self.descrever()


# PASSO 2 — SUBCLASSES: CARRO E MOTO

class Carro(Veiculo):  # herda Veiculo
    def __init__(self, marca, modelo, ano, num_portas):
        # super() chama o __init__ do Pai
        super().__init__(marca, modelo, ano)
        self.__num_portas = num_portas

    @property
    def num_portas(self):
        return self.__num_portas

    def descrever(self):  # SOBRESCREVE o Pai
        base = super().descrever()
        return f'{base} | {self.__num_portas} portas'


class Moto(Veiculo):  # herda Veiculo
    def __init__(self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano)
        self.__cilindradas = cilindradas

    @property
    def cilindradas(self):
        return self.__cilindradas

    def descrever(self):  # SOBRESCREVE o Pai
        base = super().descrever()
        return f'{base} | {self.__cilindradas}cc'


# PASSO 3 — TESTES

if __name__ == '__main__':
    c = Carro('Toyota', 'Corolla', 2023, 4)
    m = Moto('Honda', 'CG 160', 2022, 160)

    print(c)  # Toyota Corolla (2023) | 4 portas
    print(m)  # Honda CG 160 (2022) | 160cc
    print(c.marca)  # Toyota
    print(isinstance(c, Veiculo))  # True -> Carro É UM Veículo
    print(isinstance(m, Carro))  # False -> Moto NÃO é um Carro