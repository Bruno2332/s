from entity.Escola import Escola
from entity.Disciplina import Disciplina
from entity.Turma import Turma
from controller.AlunoController import AlunoController
from controller.ProfessorController import ProfessorController
from controller.FuncionarioController import FuncionarioController
from model.Model import *
import random
import names
import os



class EscolaController(Escola):
    def __init__(self):
        Escola.__init__(self)


    def cadastrar_turma(self, turma):
        db_turma = Turma_db(turma=turma.nome)
        session.add(db_turma)
        session.commit()
        session.close()


    def cadastrar_turma_aleatoria(self):
        for i in self.lista_turmas:
            instancia = Turma(i)
            db_disciplina = Turma_db(turma=instancia.nome)
            session.add(db_disciplina)
            session.commit()
        session.close()
        

    def cadastrar_disciplina(self, disciplina):
        db_disciplina = Disciplina_db(disciplina=disciplina.disciplina)
        session.add(db_disciplina)
        session.commit()
        session.close()


    def cadastrar_disciplinas_aleatorias(self):
        for i in self.lista_materias:
            instancia = Disciplina(i)
            db_disciplina = Disciplina_db(disciplina=instancia.disciplina)
            session.add(db_disciplina)
            session.commit()
        session.close()


    def cadastrar_aluno(self, aluno):
        db_aluno = Aluno_db(id_aluno=aluno.rg, nome=aluno.nome, idade=aluno.idade, id_turma=aluno.turma, matricula=aluno.matricula)
        end_aluno = EndAluno_db(id_aluno=aluno.rg, endereco=aluno.endereco)
        session.add_all([db_aluno, end_aluno])
        session.commit()
        session.close()

        
    def cadastrar_professor(self, professor):
        db_prof = Professor_db(id_prof=professor.rg, nome=professor.nome, idade=professor.idade, id_disciplina=professor.disciplina, salario=professor.salario)
        end_prof = EndProf_db(id_prof=professor.rg, endereco=professor.endereco)
        session.add_all([db_prof, end_prof])
        session.commit()
        session.close()


    def cadastrar_funcionario(self, funcionario):
        db_func = Funcionario_db(id_func=funcionario.rg, nome=funcionario.nome, idade=funcionario.idade)
        end_func = EndFunc_db(id_func=funcionario.rg, endereco=funcionario.endereco)
        cargo_func = Cargo_db(id_func=funcionario.rg, cargo=funcionario.cargo, salario=funcionario.salario)
        session.add_all([db_func, end_func, cargo_func])
        session.commit()
        session.close()


    def listar_aluno(self):
        query = session.query(Aluno_db, EndAluno_db).\
        join(EndAluno_db, Aluno_db.id_aluno == EndAluno_db.id_aluno)
        resultados = query.all()                
        for aluno, endereco in resultados:
            print(f'RG: {aluno.id_aluno} - Nome: {aluno.nome} - Idade: {aluno.idade} - Endereço: {endereco.endereco} - Matricula: {aluno.matricula} - Turma: {aluno.id_turma}')
        session.close()


    def listar_funcionario(self):
        query = session.query(Funcionario_db, EndFunc_db, Cargo_db).\
        join(EndFunc_db, Funcionario_db.id_func == EndFunc_db.id_func).\
        join(Cargo_db, Funcionario_db.id_func == Cargo_db.id_func)
        resultados = query.all()  
        for funcionario, endereco, cargo in resultados:
            print(f'RG: {funcionario.id_func} - Nome: {funcionario.nome} - Idade: {funcionario.idade} - Endereço: {endereco.endereco} - Cargo: {cargo.cargo} - Salario: {cargo.salario}')
        session.close()


    def listar_professor(self):
        query = session.query(Professor_db, EndProf_db).\
            join(EndProf_db, Professor_db.id_prof == EndProf_db.id_prof)
        resultados = query.all()  
        for professor, endereco in resultados:
            print(f'RG: {professor.id_prof} - Nome: {professor.nome} - Idade: {professor.idade} - Endereço: {endereco.endereco} - Disciplina: {professor.id_disciplina} - Salario: {professor.salario}')
        session.close()


    def pesquisa_rg(self, rg):
        aluno = session.query(Aluno_db, EndAluno_db).\
        join(EndAluno_db, Aluno_db.id_aluno == EndAluno_db.id_aluno).\
        filter_by(id_aluno=rg).first()

        professor = session.query(Professor_db, EndProf_db).\
        join(EndProf_db, Professor_db.id_prof == EndProf_db.id_prof).\
        filter_by(id_prof=rg).first()

        funcionario = session.query(Funcionario_db, EndFunc_db, Cargo_db).\
        join(EndFunc_db, Funcionario_db.id_func == EndFunc_db.id_func).\
        join(Cargo_db, Funcionario_db.id_func == Cargo_db.id_func).\
        filter_by(id_func=rg).first()

        if aluno:
            aluno_info, endereco = aluno
            os.system('cls')
            print('Aluno:')
            print(f'RG: {aluno_info.id_aluno} - Nome: {aluno_info.nome} - Idade: {aluno_info.idade} - Endereço: {endereco.endereco} - Matricula: {aluno_info.matricula} - Turma: {aluno_info.id_turma}')
            print('')
        elif professor:
            prof, endereco = professor
            os.system('cls')
            print('Professor:')
            print(f'RG: {prof.id_prof} - Nome: {prof.nome} - Idade: {prof.idade} - Endereço: {endereco.endereco} - Disciplina: {prof.id_disciplina} - Salario: {prof.salario}')
            print('')
        elif funcionario:
            func, endereco, cargo = funcionario
            os.system('cls')
            print('Funcionário:')
            print(f'RG: {func.id_func} - Nome: {func.nome} - Idade: {func.idade} - Endereço: {endereco.endereco} - Cargo: {cargo.cargo} - Salario: {cargo.salario}')
            print('')
        else:
            os.system('cls')
            print('RG não encontrado')
        session.close()            


    def cadastrar_professor_turma(self, id_professor, id_tur):
        prof = session.query(Professor_db).filter_by(id_prof=id_professor).first()
        turma = session.query(Turma_db).filter_by(id_turma=id_tur).first()
        if prof and turma:
            res = Professor_Turma_db(id_turma=turma.id_turma, id_professor=prof.id_prof)
            session.add(res)
            session.commit()
            session.close()
        else:
            print('Dados inválidos')


    def cadastrar_professores_turmas_aleatoria(self, quantidade):
        professores = session.query(Professor_db).all()
        turmas = session.query(Turma_db).all()

        for x in range(quantidade):
            professor = random.choice(professores)
            turma = random.choice(turmas)
            professor_turma = Professor_Turma_db(id_turma=turma.id_turma, id_professor=professor.id_prof)
            session.add(professor_turma)

        session.commit()
        session.close()
        

    def cadastrar_notas_aluno(self, aluno, disciplina, nota1, nota2, nota3):
        aluno_query = session.query(Aluno_db).filter_by(id_aluno=aluno).first()
        disciplina_query = session.query(Disciplina_db).filter_by(id_disciplina=disciplina).first()
        if aluno and disciplina:
            nota1, nota2, nota3 = int(nota1), int(nota2), int(nota3)
            media = round((nota1 + nota2 + nota3) / 3, 1)
            cadastro_nota = NotasDisciplina_db(id_disciplina=disciplina_query.id_disciplina, id_aluno=aluno_query.id_aluno, nota_1=nota1, nota_2=nota2, nota_3=nota3, media=media)
            session.add(cadastro_nota)
            session.commit()
            session.close()
        else:
            print('Cadastro não encontrado')

    def cadastrar_notas_aluno_aleatorio(self, quantidade):
        alunos = session.query(Aluno_db).all()
        disciplinas = session.query(Disciplina_db).all()

        for x in range(quantidade):
            aluno = random.choice(alunos)
            disciplina = random.choice(disciplinas)
            nota1 = random.randint(0, 11)
            nota2 = random.randint(0, 11)
            nota3 = random.randint(0, 11)
            media = round((nota1 + nota2 + nota3) / 3, 1)
            notas_aluno = NotasDisciplina_db(id_disciplina=disciplina.id_disciplina, id_aluno=aluno.id_aluno, nota_1=nota1, nota_2=nota2, nota_3=nota3, media=media)
            session.add(notas_aluno)

        session.commit()
        session.close()

    def debug_professor(self, quantidade):
        for i in range(quantidade):
            nome = names.get_full_name()
            idade = random.randint(0, 65)
            endereco = f'Rua {names.get_full_name()}, nº {random.randint(0, 1500)}'
            rg = random.randint(1000000, 99999999)
            random_value = session.query(func.array_agg(Disciplina_db.id_disciplina)).scalar()
            disciplina = random.choice(random_value)
            salario = random.randint(1000, 5000)
            professor = ProfessorController(nome, idade, endereco, rg, salario)

            db_prof = Professor_db(id_prof=professor.rg, id_disciplina=disciplina, nome=professor.nome, idade=professor.idade, salario=professor.salario)
            end_prof = EndProf_db(id_prof=professor.rg, endereco=professor.endereco)
            session.add_all([db_prof, end_prof])
            session.commit()
        session.close()

    
    def debug_aluno(self, quantidade):
        for i in range(quantidade):
            nome = names.get_full_name()
            idade = random.randint(0, 65)
            endereco = f'Rua {names.get_full_name()}, nº {random.randint(0, 1500)}'
            rg = random.randint(1000000, 99999999)
            
            random_value = session.query(func.array_agg(Turma_db.id_turma)).scalar()
            turma = random.choice(random_value)
            matricula = random.randint(1000, 5000)
            aluno = AlunoController(nome, idade, endereco, rg, turma, matricula)

            db_aluno = Aluno_db(id_aluno=aluno.rg, id_turma=turma, nome=aluno.nome, idade=aluno.idade, matricula=aluno.matricula)
            end_aluno = EndAluno_db(id_aluno=aluno.rg, endereco=aluno.endereco)
            
            session.add_all([db_aluno, end_aluno])
            session.commit()
            session.close()
            

    def debug_funcionario(self, quantidade):
        for i in range(quantidade):
            nome = names.get_full_name()
            idade = random.randint(0, 65)
            endereco = f'Rua {names.get_full_name()}, nº {random.randint(0, 1500)}'
            Rg = random.randint(1000000, 99999999)
            rg_str = str(Rg)
            cargo = random.choice(self.lista_cargos)
            salario = random.randint(1000, 5000)
            funcionario = FuncionarioController(nome, idade, endereco, rg_str, cargo, salario)

            db_func = Funcionario_db(id_func=funcionario.rg, nome=funcionario.nome, idade=funcionario.idade)
            end_func = EndFunc_db(id_func=funcionario.rg, endereco=funcionario.endereco)
            cargo_func = Cargo_db(id_func=funcionario.rg, cargo=funcionario.cargo, salario=funcionario.salario)
            session.add_all([db_func, end_func, cargo_func])
            session.commit()
            session.close()


    def pesquisar_professores_por_aluno(self, id_aluno):
        aluno = session.query(Aluno_db).filter_by(id_aluno=id_aluno).first()

        if aluno:
            turma = session.query(Turma_db).filter_by(id_turma=aluno.id_turma).first()
            if turma:
                professores_disciplina_turma = (
                    session.query(Professor_db, Disciplina_db.disciplina)
                    .join(Professor_Turma_db)
                    .join(Disciplina_db, Professor_db.id_disciplina == Disciplina_db.id_disciplina)
                    .filter(Professor_Turma_db.id_turma == turma.id_turma)
                    .all()
                )

                if professores_disciplina_turma:
                    os.system('cls')
                    print("Professores e suas disciplinas na turma do aluno:")
                    for professor, disciplina in professores_disciplina_turma:
                        print(f"{disciplina}: {professor.nome}")
                    print('')
                else:
                    os.system('cls')
                    print("Não há professores nesta turma.\n")
            else:
                os.system('cls')
                print("Turma não encontrada para o aluno.\n")
        else:
            os.system('cls')
            print("Aluno não encontrado.\n")


    def pesquisar_alunos_por_professor(self, id_professor):
        professor = session.query(Professor_db).filter_by(id_prof=id_professor).first()

        if professor:
            turmas_do_professor = (
                session.query(Professor_Turma_db.id_turma)
                .filter(Professor_Turma_db.id_professor == professor.id_prof)
                .subquery()
            )

            alunos_turmas = (
                session.query(Aluno_db, Turma_db.turma)
                .join(turmas_do_professor, Aluno_db.id_turma == turmas_do_professor.c.id_turma)
                .join(Turma_db, Aluno_db.id_turma == Turma_db.id_turma)
                .all()
            )

            if alunos_turmas:
                os.system('cls')
                print(f"Alunos e suas turmas do professor {professor.nome}:")
                for aluno, turma in alunos_turmas:
                    print(f"Aluno: {aluno.nome}, Turma: {turma}")
            else:
                os.system('cls')
                print("O professor não ministra aulas para nenhum aluno.")
        else:
            os.system('cls')
            print("Professor não encontrado.")


    def relatorio_media_notas_disciplinas(self):
        media_notas = session.query(
            Disciplina_db.id_disciplina,
            Disciplina_db.disciplina,
            func.avg(NotasDisciplina_db.media).label('media_disciplina')
        ).select_from(Disciplina_db).join(NotasDisciplina_db, NotasDisciplina_db.id_disciplina == Disciplina_db.id_disciplina).group_by(Disciplina_db.id_disciplina, Disciplina_db.disciplina).all()
        os.system('cls')
        print("Relatório de Média de Notas por Disciplina:")
        print('')
        for disciplina_id, nome_disciplina, media_disciplina in media_notas:
            print(f"Disciplina: {nome_disciplina}")
            print(f"Média de Notas: {media_disciplina:.2f}\n")


    def excluir_cadastros_pessoas(self, rg):
        aluno = session.query(Aluno_db).filter_by(id_aluno=rg).first()
        prof = session.query(Professor_db).filter_by(id_prof=rg).first()
        funcionario = session.query(Funcionario_db).filter_by(id_func=rg).first()
        if aluno:
            session.delete(aluno)
            session.commit()
            print('Aluno excluído com sucesso')
            print('')
        elif prof:
            session.delete(prof)
            registros_professores_turma = session.query(Professor_Turma_db).filter_by(id_professor=rg).all()
            for registro in registros_professores_turma:
                session.delete(registro)
            session.commit()
            print('Professor excluído com sucesso')
            print('')
        elif funcionario:
            session.delete(funcionario)
            print('Funcionário excluído com sucesso')
            print('')
            session.commit()
            session.close()
        else:
            print('RG não encontrado')
            print('')
    

    def excluir_turma(self, turma):
        cadastro = session.query(Turma_db).filter_by(id_turma=turma).first()
        if cadastro:
            session.delete(cadastro)
            session.commit()
            print('Turma excluída com sucesso')
            print('')
            session.close()
        else:
            print('Turma não encontrada')


    def excluir_disciplina(self, disciplina):
        cadastro = session.query(Disciplina_db).filter_by(id_disciplina=disciplina).first()
        if cadastro:
            session.delete(cadastro)
            registro_prof = session.query(Professor_db).filter_by(id_disciplina=disciplina).all()
            for reg in registro_prof:
                session.delete(reg)
            registros_notas = session.query(NotasDisciplina_db).filter_by(id_disciplina=disciplina).all()
            for registro in registros_notas:
                session.delete(registro)
            session.commit()
            print('Disciplina excluída com sucesso')
            print('')
            session.close()
        else:
            print('Disciplina não encontrada')

        