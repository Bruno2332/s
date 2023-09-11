#Sistema de Cadastro Escolar
##Descrição
Projeto voltado para a prática de programação orientada a objetos com python e integração de com banco de dados PostgreSQL.

##Funcionalidades
Cadastro de alunos, professores e funcionarios com objetos Python
Cadastro e gerenciamento de disciplinas e turmas
Cadastros aleatórios para testar as funcionalidades do sistema
Armazenamento de dados em Banco de Dados Relacional
Pesquisa relacionando alunos e professores
Registro de notas e médias dos alunos por disciplina
Relatório de média de notas por turma em cada disciplina
##Tecnologias Utilizadas
Python
Sqlalchemy
PostgreSQL
Docker
#Executando o Projeto

# Criando e rodando o Container 
$ docker run --name some-postgres -e POSTGRES_PASSWORD=password -e POSTGRES_USER=user-e POSTGRES_DB=database -p 5432:5432 -d postgres

# Instale as dependencias do Python
$ pip install -r requeriments.txt

# Rode o Model.py para criar as tabelas do banco de dados
$ python3 Model.py

# Rode o arquivo main.py
$ python3 main.py
