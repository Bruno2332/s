from entity.Pessoa import Pessoa


class Funcionario(Pessoa):
    def __init__(self, nome, idade, endereco, rg, cargo, salario):
        Pessoa.__init__(self, nome, idade, endereco, rg)
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return f'Funcionario: {self.nome} - Idade: {self.idade} - Endereço: {self.endereco} - rg: {self.rg} - Cargo: {self.cargo} - Salário: {self.salario}'