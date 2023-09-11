from entity.Disciplina import Disciplina
from entity.Turma import Turma
from controller.AlunoController import AlunoController
from controller.ProfessorController import ProfessorController
from controller.FuncionarioController import FuncionarioController
from controller.EscolaController import EscolaController
from model.Model import *
import os

escola = EscolaController()

def verificador_rg():
    while True:
        entrada = input('Digite o RG: ')
        if entrada.isdigit() and len(entrada) <= 10:
            break
        else:
            print('Digite um numero com até 10 digitos')
            continue
    return entrada


def verificador_id(turma=False, disciplina=False):
    while True:
        if turma:
            entrada = input('Digite o id da turma: ')
        elif disciplina:
            entrada = input('Digite o id da disciplina: ')
        if entrada.isdigit():
            break
        else:
            print('Digite um numero')
    return entrada


def cadastrar_manualmente_pessoas(aluno=False, funcionario=False, professor=False):
    verificar_turma = session.query(func.count(Turma_db.id_turma)).scalar() == 0
    verificar_disciplina = session.query(func.count(Disciplina_db.id_disciplina)).scalar() == 0
    if verificar_turma or verificar_disciplina:
        os.system('cls')
        print('É necessário que primeiro sejam cadastradas as turmas e disciplinas')
        print('')
    else:
        nome = input('Digite o nome: ')
        while True:
            idade = input('Digite a idade: ')
            if idade.isdigit():
                break
            else:
                print('A idade deve ser um numero')
                continue
        endereco = input('Digite o endereço: ')
        rg = verificador_rg()
        if aluno:
            while True:
                turma = verificador_id(turma=True)
                entrada_turma = session.query(Turma_db).filter_by(id_turma=turma).first()
                if entrada_turma:
                    break
                else:
                    os.system('cls')
                    print('Turma inválida')
                    continue
            while True:
                matricula = input('Digite a matricula: ')
                if matricula.isdigit():
                    break
                else:
                    print('A matricula deve ser um numero')
                    continue
            aluno_instancia = AlunoController(nome, idade, endereco, rg, turma, matricula)
            escola.cadastrar_aluno(aluno_instancia)
            os.system('cls')
            print('Aluno cadastrado com sucesso')
            print('')
        elif professor:
            while True:
                disciplina = verificador_id(disciplina=True)
                entrada_disciplina = session.query(Disciplina_db).filter_by(id_disciplina=disciplina).first()
                if entrada_disciplina:
                    break
                else:
                    os.system('cls')
                    print('Disciplina Inválida')
                    continue
            while True:
                salario = input('Digite o salário: ')
                if salario.isdigit():
                    break
                else:
                    print('O salario deve ser um numero')
                    continue
            professor_instancia = ProfessorController(nome, idade, endereco, rg, disciplina, salario)
            escola.cadastrar_professor(professor_instancia)
            os.system('cls')
            print('Professor cadastrado com sucesso')
            print('')
        elif funcionario:
            cargo = input('Digite o cargo: ')
            while True:
                salario = input('Digite o salário: ')
                if salario.isdigit():
                    break
                else:
                    print('O salario deve ser um numero')
                    continue
            funcionario_instancia = FuncionarioController(nome, idade, endereco, rg, cargo, salario)
            escola.cadastrar_funcionario(funcionario_instancia)
            os.system('cls')
            print('Funcionario cadastrado com sucesso')
            print('')


def cadastrar_aleatorio_pessoas(aluno=False, professor=False, funcionario=False):
    verificar_turma = session.query(func.count(Turma_db.id_turma)).scalar() == 0
    verificar_disciplina = session.query(func.count(Disciplina_db.id_disciplina)).scalar() == 0
    if verificar_turma or verificar_disciplina:
        os.system('cls')
        print('É necessário que primeiro sejam cadastradas as turmas e disciplinas')
        print('')
    else:
        while True:
            qtd = input('Digite a quantidade de cadastros desejados: ')
            if qtd.isdigit():
                qtd = int(qtd)
                break
            else:
                print('Digite um numero')
                continue
        if aluno:
            escola.debug_aluno(qtd)
            os.system('cls')
            print('Alunos cadastrados com sucesso')
            print('')
        elif professor:
            escola.debug_professor(qtd)
            os.system('cls')
            print('Professores cadastrados com sucesso')
            print('')
        elif funcionario:
            escola.debug_funcionario(qtd)
            os.system('cls')
            print('Funcionarios cadastrados com sucesso')
            print('')


def cadastrar_turma_disciplina_manualmente(turma=False, disciplina=False):
    if disciplina:
        nome_disciplina = input('Digite o nome da disciplina: ')
        instancia = Disciplina(nome_disciplina)
        escola.cadastrar_disciplina(instancia)
        os.system('cls')
        print('Disciplinas cadastradas com sucesso')
        print('')
    elif turma:
        nome_turma = input('Digite o nome da turma: ')
        instancia = Turma(nome_turma)
        escola.cadastrar_turma(instancia)
        os.system('cls')
        print('Turma cadastrada com sucesso')
        print('')


def cadastrar_prof_por_turma(manual=False, aleatorio=False):
    verificar_turma = session.query(func.count(Turma_db.id_turma)).scalar() == 0
    verificar_prof = session.query(func.count(Professor_db.id_prof)).scalar() == 0
    if verificar_turma or verificar_prof:
        os.system('cls')
        print('Cadastros inexistentes de turma ou professor')
        print('')
    else:
        if manual:
            while True:
                turma = verificador_id(turma=True)
                entrada_turma = session.query(Turma_db).filter_by(id_turma=turma).first()
                if entrada_turma:
                    break
                else:
                    os.system('cls')
                    print('Turma inválida')
                    continue
            while True:
                prof = verificador_rg()
                entrada_professor = session.query(Professor_db).filter_by(id_prof=prof).first()
                if entrada_professor:
                    break
                else:
                    os.system('cls')
                    print('Professor inválido')
                    continue
            escola.cadastrar_professor_turma(prof, turma)
            os.system('cls')
            print('Professor cadastrado para a turma com sucesso')
            print('')
        elif aleatorio:
            while True:
                qtd = input('Digite a quantidade de cadastros a realizar: ')
                if qtd.isdigit():
                    qtd = int(qtd)
                    break
                else:
                    print('Digite um numero')
                    continue
            escola.cadastrar_professores_turmas_aleatoria(qtd)
            os.system('cls')
            print('Turmas cadastradas com sucesso')
            print('')


def cadastrar_notas_aluno(manual=False, aleatorio=False):
    verificar_disciplina = session.query(func.count(Disciplina_db.id_disciplina)).scalar() == 0
    verificar_aluno = session.query(func.count(Aluno_db.id_aluno)).scalar() == 0
    if verificar_aluno or verificar_disciplina:
        os.system('cls')
        print('É necessário que hajam disciplinas e alunos cadastrados')
        print('')
    else:
        if manual:
            while True:
                aluno = verificador_rg()
                entrada_aluno = session.query(Aluno_db).filter_by(id_aluno=aluno).first()
                if entrada_aluno:
                    break
                else:
                    os.system('cls')
                    print('Aluno inválido')
                    continue
            while True:
                disciplina = verificador_id(disciplina=True)
                entrada_disciplina = session.query(Disciplina_db).filter_by(id_disciplina=disciplina).first()
                if entrada_disciplina:
                    break
                else:
                    os.system('cls')
                    print('Disciplina Inválida')
                    continue
            cont = 1
            lista_notas = []
            while cont <= 3:
                nota = input (f'Digite a {cont}ª nota: ')
                if nota.isdigit():
                    nota = int(nota)
                else:
                    print('A nota deve ser um numero de 0 a 10')
                    continue
                if nota <= 10:
                    lista_notas.append(nota)
                    cont += 1
                    continue
                else:
                    print('A nota deve ser um numero de 0 a 10')
                    continue
            escola.cadastrar_notas_aluno(aluno, disciplina, lista_notas[0], lista_notas[1], lista_notas[2])
            os.system('cls')
            print('Notas cadastradas com sucesso')
            print('')
        elif aleatorio:
            qtd = input('Digite a quantidade de cadastros a realizar: ')
            if qtd.isdigit():
                qtd = int(qtd)
            else:
                print('Digite um numero')
            escola.cadastrar_notas_aluno_aleatorio(qtd)
            os.system('cls')
            print('Notas cadastradas com sucesso')
            print('')