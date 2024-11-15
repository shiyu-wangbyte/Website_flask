# 安装配置
## mysql配置：
    1. 在服务器上安装mysql服务器，并且开启mysql数据库
    2. 创建用户shiyu, 并且修改用户的密码为Flask123!
    3. 在mysql软件中创建数据库：ci4tutorial
    4. 在ci4tutorial数据库中创建数据表（flaskusers）用于存储用户登录的数据
        该数据表一共有4列，分别为：
        +----------+-------------+------+-----+---------+----------------+
        | Field    | Type        | Null | Key | Default | Extra          |
        +----------+-------------+------+-----+---------+----------------+
        | id       | int         | NO   | PRI | NULL    | auto_increment |
        | username | varchar(50) | NO   |     | NULL    |                |
        | password | varchar(60) | NO   |     | NULL    |                |
        | email    | varchar(50) | NO   |     | NULL    |                |
        +----------+-------------+------+-----+---------+----------------+
    5. 在ci4tutorial数据库中创建数据表（flaskmessages）用于存储用户留言的数据
        该数据表有5列，分别为：
        +---------+--------------+------+-----+---------+----------------+
        | Field   | Type         | Null | Key | Default | Extra          |
        +---------+--------------+------+-----+---------+----------------+
        | id      | int          | NO   | PRI | NULL    | auto_increment |
        | email   | varchar(50)  | NO   |     | NULL    |                |
        | phone   | varchar(50)  | NO   |     | NULL    |                |
        | message | varchar(150) | NO   |     | NULL    |                |
        | name    | varchar(20)  | NO   |     | NULL    |                |
        +---------+--------------+------+-----+---------+----------------+


## PYTHON环境
    flask==2.1.3
    pandas==2.0.3
    python==3.8.18
    pymysql==1.0.2
    flask_login==0.6.3

# 软件启动（请确保5000端口是开放的）
    python app.py
    服务启动之后，直接在浏览器中访问：http://127.0.0.1:5000
