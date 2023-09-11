from entity.Pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome, idade, endereco, rg, disciplina, salario):
        Pessoa.__init__(self, nome, idade, endereco, rg)
        self.disciplina = disciplina
        self.salario = salario

    def __str__(self):
        return f'Professor: {self.nome} - Idade: {self.idade} - Endereço: {self.endereco} - RG: {self.rg} - ID Disciplina: {self.disciplina} - Salario: {self.salario}'
