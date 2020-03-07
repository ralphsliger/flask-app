from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
from flaskext.mysql import MySQL
import redis
from celery import Celery



app = Flask(__name__)

app.config.from_object("config")
app.secret_key = app.config['SECRET_KEY']


##docker
def getMysqlConnection():
    return mysql.connector.connect(user='root', host='mysql', port='3306', password='secret', database='flaskapp')


# Mysql Connection
app.config['MYSQL_HOST'] = 'localhost' 
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'secret
app.config['MYSQL_DB'] = 'flaskapp'
mysql = MySQL(app)

# settings
app.secret_key = "mysecretkey"


# routes

@app.route('/')
def Index():
    cursor = mysql.get_db().cursor()
    cur.execute('SELECT * FROM data')
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', data = data)


@app.route('/', methods=['POST'])
def add():
    if request.method == 'POST':
        temperature = request.form['temperature']
        date = datetime.strptime(request.form['date'],'%Y-%m-%d %H:%M:%S').strftime('%Y%m%d%H%M%S')
        time  = datetime.now().strftime('%Y%m%d%H%M%S')
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO data (temperature, date) VALUES (%s,%s,%s)", (temperature, date, time))
        mysql.connection.commit()
        flash('Added successfully')
        return redirect(url_for('Index'))


@app.route('/index', methods=['GET'])
def show_ar():
    return redirect(url_for('arquitectura'))


if __name__ == '__main__':
    # host defecto flask, puerto 80
    app.run(host="0.0.0.0", port=80, debug=True)