from flask import Flask, render_template, request, url_for,redirect
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
import pandas as pd
import hashlib, pymysql
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id

def write_message(name, email, phone, message):
    try:
        connection = pymysql.connect(
        host='127.0.0.1',  # 数据库主机名
        port=3306,               # 数据库端口号，默认为3306
        user='shiyu',             # 数据库用户名
        passwd='Flask123!',         # 数据库密码
        autocommit=True,
        charset='utf8'           # 字符编码
        )
        cursor = connection.cursor()
        connection.select_db("ci4tutorial")
        sql = "insert into flaskmessages (email,phone,message,name) values ('" + email + "','" + phone + "','" + message + "','" + name +"');"
        cursor.execute(sql)
        cursor.close()
        connection.close()
        return "Send message successfully!"
    except Exception as e:
        return e
    
def write_users(name, email, password):
    try:
        connection = pymysql.connect(
        host='127.0.0.1',  # 数据库主机名
        port=3306,               # 数据库端口号，默认为3306
        user='shiyu',             # 数据库用户名
        passwd='Flask123!',         # 数据库密码
        autocommit=True,
        charset='utf8'           # 字符编码
        )
        cursor = connection.cursor()
        connection.select_db("ci4tutorial")
        sql = "insert into flaskusers (username,password,email) values ('" + name + "','" + password + "','" + email + "');"
        cursor.execute(sql)
        cursor.close()
        connection.close()
        return f"congratulations, {name}. Register successfully!"
    except Exception as e:
        return e
    
def search_users(email):
    try:
        connection = pymysql.connect(
        host='127.0.0.1',  # 数据库主机名
        port=3306,               # 数据库端口号，默认为3306
        user='shiyu',             # 数据库用户名
        passwd='Flask123!',         # 数据库密码
        autocommit=True,
        charset='utf8'           # 字符编码
        )
        cursor = connection.cursor()
        connection.select_db("ci4tutorial")
        sql = f"select * from  flaskusers where email like '{email}';"
        cursor.execute(sql)
        results = cursor.fetchone()
        print(type(results))
        print(results==None)
        cursor.close()
        connection.close()
        return results
    except Exception as e:
        return e
    

def hashmd5(password):
    hash_object = hashlib.md5()
    hash_object.update(password.encode('ascii'))
    return hash_object.hexdigest()

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route("/")
def hello():
    return render_template('home.html')

@app.route("/home", methods=['GET'])
def about():
    return render_template('home.html')

@app.route("/tutorial", methods=['GET'])
def tutorial():
    return render_template('tutorial.html')

@app.route("/services", methods=['GET'])
def service():
    return render_template('service.html')

@app.route("/contacts", methods=['GET'])
def contacts():
    return render_template('contacts.html')

@app.route("/result", methods=['POST'])
@login_required
def run_script():
    smiles = request.form['smiles']
    smiles_list = []
    idx_list = []
    for i in range(10):
        smiles_list.append(smiles)
        idx_list.append(i)
    df = pd.DataFrame()
    df["SMILES"] = smiles_list
    df["index"] = idx_list
    return render_template('result.html', dataframe=df.to_html(index=None), smiles=smiles)

@app.route("/result", methods=['GET'])
def redi():
    return redirect(url_for('about'))

@app.route("/login", methods=['GET'])
def login():
    message_tmp="Login is required before you use our website."
    return render_template('login.html', message=message_tmp)

@app.route("/login", methods=['POST'])
def login_post():
    email = request.form['email']
    password = hashmd5(request.form['password'])
    result = search_users(email)
    message_tmp = "Wrong Password or Email address."
    try:
        search_password = result[2]
        if password == search_password:
            user_id = result[0]
            user = load_user(user_id)
            login_user(user)
            return render_template('home.html')
        if password != search_password:
            return render_template('login.html', message=message_tmp)
    except:
        return render_template('login.html', message=message_tmp)
  

@app.route("/register", methods=["GET"])
def register():
    result=""
    return render_template('register.html', result=result)

@app.route("/register", methods=['POST'])
def register_post():
    name = request.form['name']
    email = request.form['email']
    password = hashmd5(request.form['password'])
    result = search_users(email)
    if result != None:
        return render_template('register.html', result="This email has already been used!")
    result = write_users(name, email, password)
    return render_template('register.html', result=result)

@app.route("/ketcher", methods=['GET'])
def run_ketcher():
    return render_template('ketcher2/index.html')

@app.route("/contacts", methods=['POST'])
def contacts_post():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['message']
    result = write_message(name, email, phone, message)
    return result

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return 'Logged out successfully!'

if __name__ == "__main__":
    app.run(host = '0.0.0.0' ,port = 5000, debug = 'True')