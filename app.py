from flask import Flask, render_template, request, redirect, url_for, flash
from flaskext.mysql import MySQL


app = Flask(__name__)

# Mysql Connection
app.config['MYSQL_HOST'] = 'localhost' 
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Supreme22'
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
        date = request.form['date']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO data (temperature, date) VALUES (%s,%s)", (temperature, date))
        mysql.connection.commit()
        flash('Added successfully')
        return redirect(url_for('Index'))


if __name__ == '__main__':
    # host defecto flask, puerto 80
    app.run(host="0.0.0.0", port=80, debug=True)