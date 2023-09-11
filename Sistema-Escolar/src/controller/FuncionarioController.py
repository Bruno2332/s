from entity.Funcionario import Funcionario

class FuncionarioController(Funcionario):
    def __init__(self, nome, idade, endereco, rg, cargo, salario):
        Funcionario.__init__(self, nome, idade, endereco, rg, cargo, salario)

    def __str__(self):
        return f'Funcionario: {self.nome} - Idade: {self.idade} - Endereço: {self.endereco} - RG: {self.rg} - Cargo: {self.cargo} - Salário: {self.salario}'