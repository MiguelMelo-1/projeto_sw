from flask import Flask, request, render_template, redirect, flash, url_for
from datetime import datetime
from project import app
from project.models import User, Task
from project.forms import RegistrationForm, LoginForm



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

@app.route("/register", methods = ["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Conta criada para {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route("/", methods = ["GET", "POST"])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

@app.route("/tasks")
def tasks():
    return render_template('tarefas.html')


