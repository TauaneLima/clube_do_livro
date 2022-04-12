import flaskext.mysql import MySQL
from flask import Flask, render_template, request

mysql= MySQL()
app = Flask(__name__)
app.url_map.strict_slashes = False



    # Criar Conexão com Banco SQLILITE
 app.config ['MYSQL_DATABASE_USER'] = 'root'
 app.config ['MYSQL_DATABASE_PASSWORD'] ='user1234'
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
def fazerlogin():
    try:
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']

        print(_name)
        print(_email)
        print(_password)

        # validate the received values
        if _name and _email and _password:
            
            conn = mysql.connect()
            cursor = conn.cursor()
            _hashed_password = _password
            cursor.execute('insert into tbl_user (user_name, user_username, user_password) VALUES (%s, %s, %s)', ( _name,_email,_hashed_password))
            conn.commit()
        return render_template('login.html')
  
@app.route('/list',methods=['POST','GET'])
def list():
    try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute ('select user_name, user_username from tbl_user')
            data = cursor.fetchall()
            print(data[0]);

            conn.commit()
            return render_template('leitores.html', datas=data)
    

if __name__ == '__main__':
   port = int(os.environ.get("PORT", 5000))
   app.run(host='0.0.0.0', port=port)
