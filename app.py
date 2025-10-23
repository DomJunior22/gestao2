# BIBLIOTECAS IMPORTADAS
from flask import Flask, render_template, request, redirect
#from flask_sqlalchemy import  SQLAlchemy
#from flask_login import LoginManager, login_user, UserMixin, login_required


#INICIANDO O APP FLASK
app= Flask(__name__)
lm= LoginManager(app)

#CONFiRMANDO A CONEXAO
print('conectado')

#BANCO DE DADOS
#db=SQLAlchemy(app)


#CRIANDO AS TABELAS NO BANCO DE DADOS

# CRIANDO A TABELA DE MEMBROS COM O NOME TASKS




# ROTA PAGINA INICIAL
@app.route('/')
def homepage():
    return render_template('homepage.html')



if __name__ == '__main__':
    with app.app_context():
       

    app.run(debug=True)



