import flaskext.mysql import MySQL
from flask import Flask, render_template, request

mysql= MySQL()
app = Flask(__name__)
app.url_map.strict_slashes = False



    # Criar Conexão com Banco SQLILITE
 app.config ['MYSQL_DATABASE_USER'] = 'root'
 app.config ['MYSQL_DATABASE_PASSWORD'] =' 'user1234'
 app.config ['MYSQL_DATABASE_DB] = 'atividade'
 app.config ['MYSQL_DATABASE_HOST'] = '172.17.0.7'
 
 mysql.init_app(app)
             
conexao = mysql.connector.connect(database='db_usuario', user='root', password='user1234')
criar_tabela_sql = """CREATE TABLE IF NOT EXISTS tb_usuarios(
                        id int(11) NOT NULL AUTO_INCREMENT,
                        nome VARCHAR(255) NOT NULL,
                        email VARCHAR(255) NOT NULL,
                        senha VARCHAR(255) NOT NULL,
                        PRIMARY KEY (id))"""


cursor = conexao.cursor()
cursor.execute(criar_tabela_sql)
print("Tabela criada :)")


@app.route('/')
def main():
    return render_template('home.html')

@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/leitores.html')
def leitores():
    return render_template('leitores.html')

@app.route('/books')
def leitores():
    return render_template('books.html')





@app.route("/fazerlogin", methods=['POST', 'GET'])
def incluir_usuario():
    cursor = conexao.cursor()
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    cursor.execute("""INSERT INTO tb_usuarios(nome, email, senha) VALUES(%s, %s, %s)""", (nome, email, senha))
    conexao.commit()
    cursor.close()
    conexao.close()
    return render_template('login.html')
    

if __name__ == '__main__':
   port = int(os.environ.get("PORT", 5000))
   app.run(host='0.0.0.0', port=port)
