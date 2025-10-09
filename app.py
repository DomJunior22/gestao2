# BIBLIOTECAS IMPORTADAS
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import  SQLAlchemy
from flask_login import LoginManager, login_user, UserMixin, login_required
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#navegador = webdriver.Chrome()
#navegador.get("https://web.whatsapp.com")

#INICIANDO O APP FLASK
app= Flask(__name__)
lm= LoginManager(app)
app.secret_key=" projeto1"
app.config['SQLALCHEMY_DATABASE_URI'] = '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format( SGBD='mysql+pymysql', usuario='root', senha='byqUvTZEpWxZjNTzdVVikmDLjmbajkTL', servidor='hopper.proxy.rlwy.net:10763', database='railway' )


@lm.user_loader
def user_loader(id):
    usuario = db.session.query(Admin).filter_by(id=id).first()
    return usuario


#CONFiRMANDO A CONEXAO
print('conectado')

#BANCO DE DADOS
db=SQLAlchemy(app)


#CRIANDO AS TABELAS NO BANCO DE DADOS

# CRIANDO A TABELA DE MEMBROS COM O NOME TASKS
class Tasks (db.Model):
    matricula = db.Column(db.Integer, unique = True, primary_key = True, nullable = False)
    carteira = db.Column(db.String(15), unique=True, nullable=False)
    funcao= db.Column(db.String(150), nullable = False)

    nome = db.Column(db.String(250), unique = False, nullable=False)
    email = db.Column(db.String(150), unique=False, nullable=False)
    telefone = db.Column(db.String(25), unique=False,  nullable=False)

    sexo = db.Column(db.String(20), unique=False, nullable=False)
    data_nascimento = db.Column(db.String(50),unique=False, nullable=False)
    data_filiacao = db.Column(db.String(50), unique=False, nullable=False)
    cidade = db.Column(db.String(100), unique=False, nullable=False)
    estado = db.Column(db.String(25), unique=False,  nullable=False)
    endereco = db.Column(db.String(250), unique=False, nullable=False)

#CRIANDO TABELA DE ADMINISTRADORES

class Admin(UserMixin, db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False)
    nome = db.Column(db.String(250), unique=True, nullable=False)
    senha = db.Column(db.String(100), nullable=False)

# CRIANDO TABELA CONTAS A Pagar






# CRIANDO A TABELA DE CONTAS A RECEBER

class Receber (db.Model):
    codigo = db.Column(db.Integer, unique = True, primary_key = True, nullable = False, autoincrement=True)
    devedor= db.Column(db.String(150), nullable = False)
    vencimento = db.Column(db.String(50), unique=False, nullable=False)
    valor= db.Column(db.Integer, unique = False, nullable = True)
    descricao= db.Column(db.String(500), unique= False, nullable=False)

@app.route("/receb", methods = ["POST"])
def receb():
    #codigo = request.form['codigo']
    devedor =request.form['devedor']
    vencimento=request.form['vencimento']
    valor = request.form['valor']
    descricao = request.form['descricao']

    novo_receb = Receber(devedor=devedor, vencimento=vencimento, valor=valor, descricao=descricao)
    db.session.add(novo_receb)
    db.session.commit()


    return redirect('/receber')


# query consultar lista receber

@app.route('/receber')
def receb2():
    receber = Receber.query.all()
    return render_template('receber.html', receber=receber)



#contas a pagar
#criando a tabela no banco de dados
class Pagar (db.Model):
    codigo = db.Column(db.Integer, unique = True, primary_key = True, nullable = False, autoincrement=True)
    debito= db.Column(db.String(150), nullable = False)
    #data de vencimento
    diavenci=db.Column(db.Integer, nullable=True)
    mesvenci = db.Column(db.Integer, nullable=True)
    anovenci = db.Column(db.Integer, nullable=True)
    diapag = db.Column(db.Integer)
    mespag = db.Column(db.Integer)
    anopag = db.Column(db.Integer)

    valor= db.Column(db.Integer, unique = False, nullable = True)
    descricao= db.Column(db.String(500), unique= False, nullable=False)
    fornecedor = db.Column(db.String(500), unique=False, nullable=False)
    meiopag = db.Column(db.String(150), nullable=False)
    categoria = db.Column(db.String(500), unique=False)

#VINCULANDO O FORMULARIO HTML A ROTA ATRAVES DO METODO POST
@app.route("/pag", methods = ["POST","GET"])
def pag():
    #codigo = request.form['codigo']
    debito =request.form['debito']
    fornecedor= request.form['fornecedor']

    meiopag= request.form ['meiopag']
    categoria= request.form['categoria']
    #data vencimento
    diavenci= request.form['diavenc']
    mesvenci= request.form['mesvenc']
    anovenci= request.form['anovenc']
    #data de pagamento
    diapag= request.form['diapag']
    mespag= request.form['mespag']
    anopag= request.form['anopag']

    valor = request.form['valor']
    descricao = request.form['descricao']

#CRIANDO NOVO OBJETO/INSTANCIA//LINHA NA TABELA PAGAR
    novo_pagar = Pagar(debito=debito,fornecedor=fornecedor, diavenci=diavenci, mesvenci=mesvenci, anovenci=anovenci,diapag=diapag, mespag=mespag, anopag=anopag,meiopag=meiopag, categoria=categoria, valor=valor, descricao=descricao)
    db.session.add(novo_pagar)
    db.session.commit()


    return redirect('/pagar')
#CRIANDO NOVA CONSULTA/QUERY NA TABELA PAGAR
@app.route('/pagar')
def pagar2():
    pagar = Pagar.query.all()
    return render_template('pagar.html', pagar=pagar)

#PAGINA HTML /PAGAR
@app.route('/pagar')
def pagar():
    return render_template('pagar.html')


#tabela historico pagar

class Histpagar (db.Model):
    hcodigo = db.Column(db.Integer, unique = True, primary_key = True, nullable = False, autoincrement=True)
    hdebito= db.Column(db.String(150), nullable = False)
    hvencimento = db.Column(db.String(50), unique=False, nullable=False)
    hvalor= db.Column(db.Integer, unique = False, nullable = True)
    hdescricao= db.Column(db.String(500), unique= False, nullable=False)

@app.route("/histpag", methods = ["POST"])
def pag2():

    #codigo = request.form['codigo']
    hdebito =request.form['debito']
    hvencimento=request.form['vencimento']
    hvalor = request.form['valor']
    hdescricao = request.form['descricao']

#CRIANDO NOVO OBJETO/INSTANCIA//LINHA NA TABELA histpagar
    novo_pagar2 = Histpagar(hdebito=hdebito, hvencimento=hvencimento, hvalor=hvalor, hdescricao=hdescricao)
    db.session.add(novo_pagar2)
    db.session.commit()












# f pagina adicinar novo admin
@app.route('/novoadmin')
def admin():
    return render_template('cadastro_admin.html')


# adicionando novo admin
@app.route("/registrar", methods = ["POST"])
def registrar():
    nome = request.form['nome']
    senha = request.form['senha']

    novo_admin = Admin(nome=nome, senha=senha)
    db.session.add(novo_admin)
    db.session.commit()

    return redirect('/receber')









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

@app.route('/cadastrados')
def cadastrados():
    tasks = Tasks.query.all()
    return render_template('membroscadastrados.html', tasks=tasks)

#ROTA PARA ADICIONAR NOVO ADMIN
@app.route('/novoadmin')
def admincad():
    admin = Admin.query.all()
    return render_template('cadastro_admin.html', admin=admin)


#ROTA PARA ADICIONAR NOVO A PAGAR





#ROTA PARA DELETAR MEMBRO
@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    task = Tasks.query.get(task_id)

    if task:
        db.session.delete(task)
        db.session.commit()
    return redirect('/excluir')

#pagina de excluir
@app.route('/excluir')
def excluir():
    tasks = Tasks.query.all()
    return render_template('excluir2.html', tasks=tasks)

#ROTA PARA DELETAr Devedor
@app.route('/delete/<int:receber_id>', methods=['POST'])
def delete_receber(receber_id):
    task2 = Recebers.query.get(receber_id)

    if task2:
        db.session.delete(receber)
        db.session.commit()
    return redirect('/excluir')

#pagina de excluir
#@app.route('/excluir')
#def excluir():
#    tasks = Tasks.query.all()
 #   return render_template('excluir2.html', tasks=tasks)





#Rota página de cadastro

@app.route('/formulario')
def index():
    tasks = Tasks.query.all()
    return render_template('formulario.html', tasks=tasks)


# ADICIONAR NOVOS MEMBROS
@app.route('/create', methods = ["POST"])
def create_task():

    nome = request.form['nome']
    carteira = request.form ['carteira']
    funcao = request.form ['funcao']
    email = request.form['email']
    telefone = request.form['telefone']
    sexo = request.form['sexo']
    data_nascimento = request.form['data_nascimento']
    data_filiacao = request.form['data_filiacao']
    cidade = request.form['cidade']
    estado = request.form['estado']
    endereco = request.form['endereco']


    novo_membro = Tasks(nome= nome, carteira= carteira,funcao=funcao, email= email, telefone=telefone, sexo=sexo, data_nascimento=data_nascimento, data_filiacao=data_filiacao,cidade=cidade, estado=estado, endereco=endereco)
    db.session.add(novo_membro)
    db.session.commit()
    return redirect('/formulario')






















if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)

