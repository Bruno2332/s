from controller.EscolaController import EscolaController
from controller.FunctionMenu import *
import os

escola = EscolaController()

class Menu:
    def __init__(self):
        while True:
            print('Selecione uma Opção')
            print('1 - Cadastrar')
            print('2 - Pesquisar')
            print('3 - Exibir Cadastros')
            print('4 - Excluir Cadastros')
            print('5 - Sair')
            op = input()
            os.system('cls')
            if op == '1':
                while True:
                    print('Selecione uma Opção')
                    print('1 - Cadastrar Aluno')
                    print('2 - Cadastrar Professor')
                    print('3 - Cadastrar Funcionario')
                    print('4 - Cadastrar Disciplina')
                    print('5 - Cadastrar Turma')
                    print('6 - Cadastrar Professor por Turma')
                    print('7 - Cadastrar notas por aluno')
                    print('8 - Voltar ao Menu Inicial')
                    opcao = input()
                    os.system('cls')                
                    if opcao == '1':
                        while True:
                            print('Selecione uma Opção')
                            print('1 - Cadastrar Aluno Manualmente')
                            print('2 - Cadastrar Alunos Aleatórios')
                            print('3 - Retornar ao Menu Inicial')
                            escolha = input()
                            if escolha == '1':
                                cadastrar_manualmente_pessoas(aluno=True)
                                continue
                            elif escolha == '2':
                                cadastrar_aleatorio_pessoas(aluno=True)
                                continue
                            elif escolha == '3':
                                os.system('cls')
                                break
                            else:
                                os.system('cls')
                                print('Opção inválida')
                                print('')
                                continue
                    elif opcao == '2':
                        while True:
                            print('Selecione uma Opção')
                            print('1 - Cadastrar Professor Manualmente')
                            print('2 - Cadastrar Professores Aleatórios')
                            print('3 - Retornar ao Menu Inicial')
                            escolha = input()
                            if escolha == '1':
                                cadastrar_manualmente_pessoas(professor=True)
                                continue
                            elif escolha == '2':
                                cadastrar_aleatorio_pessoas(professor=True)
                                continue
                            elif escolha == '3':
                                os.system('cls')
                                break
                            else:
                                os.system('cls')
                                print('Opção inválida')
                                print('')
                                continue
                    elif opcao == '3':
                        while True:
                            print('Selecione uma Opção')
                            print('1 - Cadastrar Funcionario Manualmente')
                            print('2 - Cadastrar Funcionarios Aleatórios')
                            print('3 - Retornar ao Menu Inicial')
                            escolha = input()
                            if escolha == '1':
                                cadastrar_manualmente_pessoas(funcionario=True)
                                continue
                            elif escolha == '2':
                                cadastrar_aleatorio_pessoas(funcionario=True)
                                continue
                            elif escolha == '3':
                                os.system('cls')
                                break
                            else:
                                os.system('cls')
                                print('Opção inválida')
                                print('')
                                continue

                    elif opcao == '4':
                        while True:  
                            print('Selecione uma Opção')
                            print('1 - Cadastrar Disciplina Manualmente')
                            print('2 - Cadastrar Disciplinas Aleatórias')
                            print('3 - Retornar ao Menu Inicial')
                            escolha = input()
                            if escolha == '1':
                                cadastrar_turma_disciplina_manualmente(disciplina=True)
                                continue
                            elif escolha == '2':
                                escola.cadastrar_disciplinas_aleatorias()
                                os.system('cls')
                                print('Disciplinas cadastradas com sucesso')
                                print('')
                                continue
                            elif escolha == '3':
                                os.system('cls')
                                break
                            else:
                                os.system('cls')
                                print('Opção inválida')
                                print('')
                                continue
                    elif opcao == '5':
                        while True:  
                            print('Selecione uma Opção')
                            print('1 - Cadastrar Turma Manualmente')
                            print('2 - Cadastrar Turmas Aleatórias')
                            print('3 - Retornar ao Menu Inicial')
                            escolha = input()
                            if escolha == '1':
                                cadastrar_turma_disciplina_manualmente(turma=True)
                                continue
                            elif escolha == '2':
                                escola.cadastrar_turma_aleatoria()
                                os.system('cls')
                                print('Turmas cadastradas com sucesso')
                                print('')
                                continue
                            elif escolha == '3':
                                os.system('cls')
                                break
                            else:
                                os.system('cls')
                                print('Opção inválida')
                                print('')
                                continue
                    elif opcao == '6':
                        while True:  
                            print('Selecione uma Opção')
                            print('1 - Cadastrar Manualmente')
                            print('2 - Cadastrar Aleatório')
                            print('3 - Retornar ao Menu Inicial')
                            escolha = input()
                            if escolha == '1':
                                cadastrar_prof_por_turma(manual=True)
                                continue
                            elif escolha == '2':
                                cadastrar_prof_por_turma(aleatorio=True)
                                continue
                            elif escolha == '3':
                                os.system('cls')
                                break
                            else:
                                os.system('cls')
                                print('Opção inválida')
                                print('')
                                continue
                    elif opcao == '7':
                        while True:  
                            print('Selecione uma Opção')
                            print('1 - Cadastrar Manualmente')
                            print('2 - Cadastrar Aleatório')
                            print('3 - Retornar ao Menu Inicial')
                            escolha = input()
                            if escolha == '1':
                                cadastrar_notas_aluno(manual=True)
                                continue
                            elif escolha == '2':
                                cadastrar_notas_aluno(aleatorio=True)
                                continue
                            elif escolha == '3':
                                os.system('cls')
                                break
                            else:
                                os.system('cls')
                                print('Opção inválida')
                                print('')
                                continue
                    elif opcao == '8':
                        os.system('cls')
                        break
                    else:
                        os.system('cls')
                        print('Opção inválida')
                        print('')
                        continue
            elif op == '2':
                while True:
                    print('Selecione uma opção')
                    print('1 - Pesquisa por RG')
                    print('2 - Pesquisar Professor por Aluno')
                    print('3 - Pesquisar Aluno por Professor')
                    print('4 - Voltar ao Menu Inicial')
                    opcao = input()
                    os.system('cls')
                    if opcao == '1':
                        escola.pesquisa_rg(verificador_rg())
                        continue
                    elif opcao == '2':
                        escola.pesquisar_professores_por_aluno(verificador_rg())
                        continue               
                    elif opcao == '3':
                        escola.pesquisar_alunos_por_professor(verificador_rg())
                        continue
                    elif opcao == '4':
                        os.system('cls')
                        break
                    else:
                        os.system('cls')
                        print('Opção inválida')
                        print('')
                        continue
            elif op == '3':
                while True:
                    print('Selecione uma Opção')    
                    print('1 - Exibir Lista de Alunos')
                    print('2 - Exibir Lista de Professores')
                    print('3 - Exibir Lista de Funcionarios')
                    print('4 - Exibir Relatorio de Notas')
                    print('5 - Retornar ao Menu Inicial')
                    opcao = input()
                    os.system('cls')
                    if opcao == '1':
                        os.system('cls')
                        escola.listar_aluno()
                        print('')
                        continue
                    elif opcao == '2':
                        os.system('cls')
                        escola.listar_professor()
                        print('')
                        continue
                    elif opcao == '3':
                        os.system('cls')
                        escola.listar_funcionario()
                        print('')
                        continue
                    elif opcao == '4':
                        os.system('cls')
                        escola.relatorio_media_notas_disciplinas()
                        print('')
                        continue
                    elif opcao == '5':
                        os.system('cls')
                        break
                    else:
                        os.system('cls')
                        print('Opção Inválida')
                        print('')
                        continue
            elif op == '4':
                print('1 - Excluir cadastro por RG')
                print('2 - Excluir Turma')
                print('3 - Excluir Disciplina')
                print('4 - Retornar ao menu inicial')
                opcao = input()
                if opcao == '1':
                    escola.excluir_cadastros_pessoas(verificador_rg())
                    continue
                elif opcao == '2':
                    entrada = input('Digite o id da Turma: ')
                    escola.excluir_turma(entrada)
                    continue
                elif opcao == '3':
                    entrada = input('Digite o id da Disciplina: ')
                    escola.excluir_disciplina(entrada)
                    continue
                elif opcao == '4':
                    os.system('cls')
                    break
                else:
                    os.system('cls')
                    print('Opção Inválida')
                    print('')
                    continue
            elif op == '5':
                os.system('cls')
                print('Programa Finalizado')
                break
            else:
                os.system('cls')
                print('Opção Inválida')
                print('')
                continue          