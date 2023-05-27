from flask import Flask, request, render_template, redirect
from datetime import datetime
from project import app
from project.models import User, Task


# Rota página principal do programa
@app.route("/index", methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_title = request.form['idAddTaskTitle']
        task_description = request.form['idAddTaskDescription']
        task_date_start = request.form['idAddTaskDateStart']
        task_date_end = request.form['idAddTaskDateEnd']

        new_task = Task(
            title = task_title,
            desc = task_description,
            date_start = task_date_start,
            date_end = task_date_end
            )
        
        return redirect('index')
    else:
        dia = datetime.now()
        return render_template('home.html', dia=dia)

@app.route("/", methods = ["GET", "POST"])
def login():
    return render_template("login.html")

@app.route("/tasks")
def tasks():
    return render_template('tarefas.html')

