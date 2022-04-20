from flask import Flask, render_template, json, request
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

    # Criar Conexão com Banco SQLILITE
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'admin'
app.config['MYSQL_DATABASE_DB'] = 'teste'
app.config['MYSQL_DATABASE_HOST'] = '172.17.0.2'

mysql.init_app(app)

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
            cursor.callproc('sp_createUser',(_name,_email,_hashed_password))
            data = cursor.fetchall()
            conn.commit()
            print(data);
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
    app.run(host='0.0.0.0', port=5050, debug=True)
