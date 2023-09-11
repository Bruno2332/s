from entity.Pessoa import Pessoa

class Aluno(Pessoa):  
    def __init__(self, nome, idade, endereco, rg, turma, matricula):
        Pessoa.__init__(self, nome, idade, endereco, rg)
        self.matricula = matricula
        self.turma = turma
        self.lista_disciplinas = []
        self.lista_notas = []
        self.notas_disciplina = {}

    def __str__(self):
        return f'Aluno: {self.nome} - Idade: {self.idade} - Endereço: {self.endereco} - RG: {self.rg} - Turma: {self.turma} - Matricula: {self.matricula}'