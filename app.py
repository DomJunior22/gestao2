# BIBLIOTECAS IMPORTADAS
from flask import Flask, render_template, request, redirect
#from flask_sqlalchemy import  SQLAlchemy
#from flask_login import LoginManager, login_user, UserMixin, login_required
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.by import By
#navegador = webdriver.Chrome()
#navegador.get("https://web.whatsapp.com")

#INICIANDO O APP FLASK
app= Flask(__name__)
lm= LoginManager(app)
app.secret_key=" projeto1"
#app.config['SQLALCHEMY_DATABASE_URI'] = '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format( SGBD='mysql+pymysql', usuario='root', senha='byqUvTZEpWxZjNTzdVVikmDLjmbajkTL', servidor='hopper.proxy.rlwy.net:10763', database='railway' )


@lm.user_loader
def user_loader(id):
    usuario = db.session.query(Admin).filter_by(id=id).first()
    return usuario


#CONFiRMANDO A CONEXAO
print('conectado')

#BANCO DE DADOS
#db=SQLAlchemy(app)


#CRIANDO AS TABELAS NO BANCO DE DADOS

# CRIANDO A TABELA DE MEMBROS COM O NOME TASKS










# RASCUNHO/ TESTE - ACESSANDO COM UM ADMIN
# @app.route("login", methods= ["GET", "POST"])
# def login():
#     if request.method == "GET":
#         return render_template("gestao.html")
#     elif request.method == "POST":
#         nome =request.form['nome']
#         senha = request.form['senha']
#
#         user = db.session.query(Admin).filter_by(nome=nome, senha=senha).first()
#         if not user:
#             return "Nome ou senha incorretos."
#
#         login_user(user)
#         return redirect("gestao.html")





#ROTAS DAS PÁGINAS

# ROTA PAGINA INICIAL
@app.route('/')
def homepage():
    return render_template('homepage.html')

# ROTA DO MENU
@app.get("/menu1")
def menu1():
    return render_template("menu1.html")

#ROTA PAGINA DE AUTENTICAÇÃO
@app.route('/autenticacao')
def autenticacao():
    return render_template('autenticacao.html')

#CULTOS
@app.route('/cultos')
def cultos():
    return render_template('cultos.html')

#ROTA EVENTOS
@app.route('/eventos')
def eventos():
    return render_template('eventos.html')

#ROTA FINANCEIRO
@app.route('/financeiro')
def financeiro():
    return render_template('financeiro.html')

# FLUXO DE CAIXA
@app.route('/caixa')
def caixa():
    return render_template('caixa.html')

# PÁGINA RECEBER
@app.route('/receber')
def receber():
    return render_template('receber.html')




#PAGINA LEMBRETES

@app.route('/lembretes')
def lembretes():
    return render_template('lembretes.html')


# ROTA PAGINA GESTAO

@app.route('/gestao')
#@login_required #login requirido
def gestao():
    return render_template('gestao.html')



# rota para exibir todos os cadatrados na pagina html




#ROTA PARA ADICIONAR NOVO A PAGAR





#ROTA PARA DELETAR MEMBRO



if __name__ == '__main__':
    with app.app_context():
       

    app.run(debug=True)


