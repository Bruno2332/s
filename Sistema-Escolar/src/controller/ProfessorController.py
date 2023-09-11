from entity.Professor import Professor


class ProfessorController(Professor):
    def __init__(self, nome, idade, endereco, rg, disciplina, salario):
        Professor.__init__(self, nome, idade, endereco, rg, disciplina, salario)

    def __str__(self):
        return f'Professor: {self.nome} - Idade: {self.idade} - Endereço: {self.endereco} - RG: {self.rg} ID Disciplina: {self.disciplina}- Salario: {self.salario}'
