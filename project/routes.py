from project import app
from flask import render_template, request, redirect, request
from datetime import datetime
from project.models import User, Task


# Rota página principal do programa
@app.get("/", METHODS=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task_title = request.form['idAddTaskTitle']
        task_description = request.form['idAddTaskDescription']
        task_date_start = request.form['idAddTaskDateStart']
        task_date_end = request.form['idAddTaskDateEnd']
    else:
        dia = datetime.now()
        return render_template('home.html', dia=dia)

@app.route("/tasks")
def tasks():
    return render_template('tarefas.html')


@app.post("/create_task")
def create_task():
    