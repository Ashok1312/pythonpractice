from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__, template_folder='render html')

# config
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'your user name'
app.config['MYSQL_PASSWORD'] = 'your password'
app.config['MYSQL_DB'] = 'name of database'


mysql = MySQL(app)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        userDetails = request.form
        name = userDetails['name']
        email = userDetails['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(NAME, EMAIL) VALUES(%s, %s)", (name, email))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index1.html')


if __name__ == '__main__':
    app.run(debug=True)
