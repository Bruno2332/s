from sqlalchemy.sql import func
from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine('postgresql://bruno:pass@localhost:5432/escola')

Session = sessionmaker(bind=engine)

session = Session()

class Disciplina_db(Base):
    __tablename__ = 'disciplina'
    id_disciplina = Column(Integer, primary_key=True)
    disciplina = Column(String(100), nullable=False)
    professores = relationship('Professor_db', back_populates='disciplina', cascade='all, delete-orphan')
    notas_disciplina = relationship('NotasDisciplina_db', back_populates='disciplina', cascade='all, delete-orphan')
    

class Turma_db(Base):
    __tablename__ = 'turma'
    id_turma = Column(Integer, primary_key=True)
    turma = Column(String(100), nullable=False)
    alunos = relationship('Aluno_db', backref='turma', cascade='all, delete-orphan')
    prof_turma = relationship('Professor_Turma_db', back_populates='turma', cascade='all, delete-orphan')


class Aluno_db(Base):
    __tablename__ = 'aluno'
    id_aluno = Column(Integer, primary_key=True)
    id_turma = Column(Integer, ForeignKey('turma.id_turma'), nullable=False)
    nome = Column(String(150), nullable=False)
    idade = Column(String(10), nullable=False)
    matricula = Column(Integer, nullable=False)
    enderecos = relationship('EndAluno_db', back_populates='aluno', cascade='all, delete-orphan')
    notas_disciplina = relationship('NotasDisciplina_db', back_populates='aluno', cascade='all, delete-orphan')
    

class Professor_db(Base):
    __tablename__ = 'professor'
    id_prof = Column(Integer, primary_key=True)
    id_disciplina = Column(Integer, ForeignKey('disciplina.id_disciplina'), nullable=False)
    nome = Column(String(150), nullable=False)
    idade = Column(String(10), nullable=False)
    salario = Column(Integer, nullable=False)
    prof_turma = relationship('Professor_Turma_db', back_populates='professor')
    enderecos = relationship('EndProf_db', back_populates='professor', cascade='all, delete-orphan')
    disciplina = relationship('Disciplina_db', back_populates='professores')


class Professor_Turma_db(Base):
    __tablename__ = 'professor_turma'
    id_prof_turma = Column(Integer, primary_key=True)
    id_turma = Column(Integer, ForeignKey('turma.id_turma') ,nullable=False)
    id_professor = Column(Integer, ForeignKey('professor.id_prof'), nullable=True)
    professor = relationship('Professor_db', back_populates='prof_turma')
    turma = relationship('Turma_db', back_populates='prof_turma')



class Funcionario_db(Base):
    __tablename__ = 'funcionario'
    id_func = Column(Integer, primary_key=True)
    nome = Column(String(150), nullable=False)
    idade = Column(String(10), nullable=False)
    enderecos = relationship('EndFunc_db', back_populates='funcionario', cascade='all, delete-orphan')
    cargo = relationship('Cargo_db', back_populates='funcionario', cascade='all, delete-orphan')
    salario = relationship('Cargo_db', back_populates='funcionario', cascade='all, delete-orphan')
    

class Cargo_db(Base):
    __tablename__ = 'cargo'
    id_cargo = Column(Integer, primary_key=True)
    id_func = Column(Integer, ForeignKey('funcionario.id_func'), nullable=False)
    cargo = Column(String(50), nullable=False)
    salario = Column(Float, nullable=False)
    funcionario = relationship('Funcionario_db', back_populates='cargo')


class EndAluno_db(Base):
    __tablename__ = 'end_aluno'
    id_end_aluno = Column(Integer, primary_key=True)
    id_aluno = Column(Integer, ForeignKey('aluno.id_aluno'), nullable=False)
    endereco = Column(String(200), nullable=False)
    aluno = relationship('Aluno_db', back_populates='enderecos')


class EndProf_db(Base):
    __tablename__ = 'end_prof'
    id_end_prof = Column(Integer, primary_key=True)
    id_prof = Column(Integer, ForeignKey('professor.id_prof'), nullable=False)
    endereco = Column(String(200), nullable=False)
    professor = relationship('Professor_db', back_populates='enderecos')


class EndFunc_db(Base):
    __tablename__ = 'end_func'
    id_end_func = Column(Integer, primary_key=True)
    id_func = Column(Integer, ForeignKey('funcionario.id_func'), nullable=False)
    endereco = Column(String(200), nullable=False)
    funcionario = relationship('Funcionario_db', back_populates='enderecos')


class NotasDisciplina_db(Base):
    __tablename__ = 'notas_disciplina'
    id_nota = Column(Integer, primary_key=True)
    id_disciplina = Column(Integer, ForeignKey('disciplina.id_disciplina'), nullable=False)
    id_aluno = Column(Integer, ForeignKey('aluno.id_aluno'), nullable=False)
    nota_1 = Column(Integer, nullable=False)
    nota_2 = Column(Integer, nullable=False)
    nota_3 = Column(Integer, nullable=False)
    media = Column(Float, nullable=False)
    aluno = relationship('Aluno_db', back_populates='notas_disciplina')
    disciplina = relationship('Disciplina_db', back_populates='notas_disciplina')



    
Base.metadata.create_all(bind=engine)