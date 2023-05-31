from flask import Flask, request, render_template, redirect, flash, url_for
from datetime import datetime
from project import app, db, bcrypt
from project.models import User, Task
from project.forms import RegistrationForm, LoginForm
from flask_login import login_user, current_user, logout_user

# Rota página principal do programa
@app.route("/index", methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_title = request.form['idAddTaskTitle']
        task_description = request.form['idAddTaskDescription']
        task_date_start = request.form['idAddTaskDateStart']
        task_date_end = request.form['idAddTaskDateEnd']
        task_categoria = request.form['idAddCategoria']
        user_id = current_user.id

        new_task = Task(
            title = task_title,
            desc = task_description,
            category = task_categoria,
            date_start = task_date_start,
            date_end = task_date_end,
            id_user = user_id
            )
        db.session.add(new_task)
        db.session.commit()
        return redirect('index')
    dia = datetime.now()
    return render_template('home.html', dia=dia)

@app.route("/register", methods = ["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(
            username = form.username.data,
            email_address=form.email.data,
            password_hash=hashed_password
        )
        db.session.add(user)
        db.session.commit()
        flash('Conta criada com sucesso', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route("/", methods = ["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user and bcrypt.check_password_hash(user.password_hash, form.password.data):
            login_user(user, remember = form.remember.data)
            return redirect('index')
        else:
            flash('Login sem sucesso, verifique o utilizador e password', 'danger')
    return render_template('login.html', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/tasks")
def tasks():
    tasks = Task.query.filter_by(id_user = current_user.id).all()
    return render_template('tarefas.html', tasks=tasks)