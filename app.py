from flask import Flask, render_template, request, redirect
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'username'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE'] = 'database'

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=app.config['MYSQL_HOST'],
            user=app.config['MYSQL_USER'],
            password=app.config['MYSQL_PASSWORD'],
            database=app.config['MYSQL_DATABASE']
        )
        if connection.is_connected():
            return connection
    except Error as err:
        print(f'Error: {err}')
        return None

@app.get('/')
def index():
    return render_template('index.html')

@app.post('/submit_form')
def submit_form():
    location = request.form.get('location')
    snacks = request.form.get('vending_type_snacks')
    drinks = request.form.get('vending_type_drinks')
    return redirect('/')