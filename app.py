import mysql.connector
from flask import Flask, render_template
from sqlalchemy import create_engine, Column, String, Integer, Boolean, Date
from sqlalchemy.orm import sessionmaker, declarative_base

app = Flask(__name__)


@app.get("/")

def homepage():
    return render_template("homepage.html")

@app.get("/autenticacao")
def autenticacao():
    return render_template("autenticacao.html")


@app.get("/gestao")
def gestao():
    return render_template("gestao.html")


@app.get("/formulario")
def formulario():
    return render_template("formulario.html")


@app.get("/buscar")
def buscar():
    return render_template("buscar.html")


@app.get("/excluir")
def excluir():
    return render_template("excluir.html")


# Criar a conexão com o banco de dados

# enderço do servidor
db = create_engine('mysql+pymysql://root:byqUvTZEpWxZjNTzdVVikmDLjmbajkTL@hopper.proxy.rlwy.net:10763/railway')

# criar a seção
Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()


# criar as tabelas

class Usuario(Base):  # classe Membro, equivale a tabela
    __tablename__ = "Membros"  # Nome da Tabela
    matricula = Column("Matricula", Integer, primary_key=True, autoincrement=True)
    nome = Column("Nome", String(150))
    telefone = Column("Telefone", Integer)
    email = Column("Email", String(150))
    sexo = Column("Sexo", String(150))
    nasc = Column("Data Nascimento", Date)
    filiacao = Column("Data Filiação", Date)
    cidade = Column("Cidade", String(150))
    estado = Column("Estado", String(50))
    endereco = Column("Endereço", String(150))


    def __init__(self, nome, telefone, email, nasc,filiacao, cidade, estado,endereco):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.nasc = nasc
        self.filiacao = filiacao
        self.cidade = cidade
        self.estado = estado
        self.endereco = endereco


Base.metadata.create_all(bind=db)

# Cadastrar novo membro

#usuario = Usuario(nome="Helena", telefone="6969", email="5555@marcia", endereco="33", data_nasc="90887",data_filiacao="763")
#session.add(usuario)
#session.commit()


# membro3 = Membro (nome= " Paulo" , telefone= "123", email="5555", endereco="33", data_nasc="90887", data_filiacao="763")
# session.add(membro3)
# session.commit()

@app.get("/cadastrados")
def cadastrados():
     #usuario = session.query(Usuarios).all()
    return render_template("membroscadastrados.html", usuario=usuario)


print(' conectado!!')

usuario = session.query(Usuario).first()

#print('Matricula:',usuario.matricula, 'Nome:', usuario.nome, 'Telefone:',usuario.telefone)




# membros_um = session.query(Tasks).filter_by(email="5555").first()
# print()

# print(membros_um)
# print('Matrícula:', membros_um.matricula)
# print('Nome:', membros_um.nome)
# print('Telefone:',membros_um.telefone)
# print('Email: ',membros_um.email)


if __name__ == '__main__':
    app.run(debug=True)
