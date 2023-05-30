from flask import Flask, request, render_template, redirect, flash, url_for
from datetime import datetime
from project import app, db, bcrypt
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
        task_categoria = request.form['idAddCategoria']

        new_task = Task(
            title = task_title,
            desc = task_description,
            category = task_categoria,
            date_start = task_date_start,
            date_end = task_date_end
            )
        db.session.add(new_task)
        db.session.commit()
        return redirect('index')
    else:
        dia = datetime.now()
        return render_template('home.html', dia=dia)

@app.route("/register", methods = ["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email_address=form.email.data, password_hash=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Conta criada com sucesso', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route("/", methods = ["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == '' and form.password.data=='':
            flash('Login com sucesso', 'success')
            return redirect(url_for('index'))
        else:
            flash('Login sem sucesso, verifique o username e password', 'danger')
    return render_template('login.html', form=form)

@app.route("/tasks")
def tasks():
    all_tasks = Task.query.all()
    return render_template('tarefas.html', tasks=all_tasks)


