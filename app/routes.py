import datetime
from app import app
from app import db
from flask import render_template, redirect, url_for, flash
from app.models import File, User
from app.forms import SearchFileForm, RegisterFileForm, LoginUserForm, RegisterUserform
from flask_login import login_user, logout_user, login_required, current_user

@app.route('/', methods=['POST', 'GET'])
@app.route('/home', methods=['POST', 'GET'])
def home_page():
    form = SearchFileForm()

    if form.validate_on_submit():
        attempend_file = File.query.filter_by(file_number_format=form.number_of_file.data).first()
        if attempend_file:
            flash(f'Encontrado! {attempend_file.file_user_name}', category='success')
            return redirect(url_for('view_file_page', file_number=attempend_file.file_number_format))
        else:
            flash('Expediente no encontrado, verifica bien el numero', category='danger')

    if form.errors != {}:
        for err_message in form.errors.values():
            flash(f'Ocurrio un error! {err_message[0]}', category='danger')

    return render_template('home.html', form=form)

@app.route('/register_file', methods=['POST', 'GET'])
def register_file_page():
    form = RegisterFileForm()

    if form.validate_on_submit():
        files_numbers = db.session.query(File.file_number_format)
        all_numbers = files_numbers.all()
        if all_numbers == []:
            last_number = 0
        else:
            last_number = all_numbers[len(all_numbers)-1]
            last_number = int(last_number[0])

        file_to_create = File(file_number=last_number,
                              file_user_name=form.file_user_name.data,
                              file_user_dni=form.file_user_dni.data,
                              file_user_phone=form.file_user_phone.data,
                              file_user_email=form.file_user_email.data,
                              file_subject=form.file_subject.data,
                              file_justification=form.file_justification.data)

        db.session.add(file_to_create)
        db.session.commit()

        flash(f'Registrado con exito!', category='success')
        # return redirect(url_for('view_file_page', number_of_file=file_to_create.number_file))
        return redirect(url_for('view_file_page', file_number=file_to_create.file_number_format))

    if form.errors != {}:
        for err_message in form.errors.values():
            flash(f'Ocurrio un error! {err_message[0]}', category='danger')

    return render_template('register_file.html', form=form)

@app.route('/file/<file_number>')
def view_file_page(file_number):
    attempend_file = File.query.filter_by(file_number_format=file_number).first()
    date_and_time = attempend_file.file_date
    only_time = datetime.datetime.strftime(date_and_time, '%H:%M:%S')
    only_date = datetime.datetime.strftime(date_and_time, '%Y/%m/%d:')

    return render_template('file.html', attempend_file=attempend_file, time=only_time, date=only_date)

@app.route('/files')
@login_required
def files_page():
    files = File.query.all()
    return render_template('files.html', files = files)

@app.route('/login', methods=['GET', 'POST'])
def login_user_page():
    form = LoginUserForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
            attempted_password=form.password.data
        ):
            login_user(attempted_user)
            flash(f'Inicio de sesion satisfactorio {attempted_user.username}', category='success')
            return redirect(url_for('files_page'))
        else:
            flash('El nombre de usuario y la contraseña no coinciden! por favor intente de nuevo', category='danger')
    return render_template('login_user.html', form=form)

@app.route('/register_user', methods=['POST', 'GET']) 
def register_user_page():
    form = RegisterUserform()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f'Usuario registrado correctamente! Bienvenido {user_to_create.username}', category='success')
        return redirect(url_for('files_page'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'Hubo un error registrando al usuario: {err_msg}', category='danger')

    return render_template('register_user.html', form=form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash("Se cerro sesion correctamente!", category='info')

    return redirect(url_for("home_page"))