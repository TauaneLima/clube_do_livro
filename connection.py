from flask import Flask, render_template, request
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
app.url_map.strict_slashes = False

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'admin'
app.config['MYSQL_DATABASE_DB'] = 'teste'
app.config['MYSQL_DATABASE_HOST'] = '172.17.0.2'
#app.config['MYSQL_DATABASE_HOST'] = ''
mysql.init_app(app)


conexao = mysql.connect()
cursor = conexao.cursor()


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

@app.route("/adicionar_usuario", methods=['POST', 'GET'])
def incluir_usuario():
    cursor = conexao.cursor()
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    cursor.execute("""INSERT INTO tbl_user(user_name, user_username, user_password) VALUES(%s, %s, %s)""", (nome, email, senha))
    conexao.commit()
    cursor.close()
    return render_template('login.html')


@app.route("/listar_usuario", methods=['POST', 'GET'])
def listar_usuario():
    consulta_bd = "select * from tb_user"
    cursor = conexao.cursor()
    cursor.execute(consulta_bd)
    details = cursor.fetchall()
    print("Quantidade de registros: ", cursor.rowcount)

    for x in range(len(details)):
        print(details[x])
    conexao.commit()
    cursor.close()
    conexao.close()
    return render_template('usuarios.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
