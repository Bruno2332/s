from entity.Aluno import Aluno


class AlunoController(Aluno):
    def __init__(self, nome, idade, endereco, rg, turma, matricula):
        Aluno.__init__(self, nome, idade, endereco, rg, turma, matricula)
        
    
    
    def __str__(self):
        return f'Aluno: {self.nome} - Idade: {self.idade} - Endereço: {self.endereco} - RG: {self.rg} - Turma: {self.turma} - Matricula: {self.matricula}'
