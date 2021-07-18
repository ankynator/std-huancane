from app import app
from flask import render_template, redirect, url_for, flash
from app.models import File
from app.forms import SearchFileForm, RegisterFileForm
from app import db

@app.route('/', methods=['POST', 'GET'])
@app.route('/home', methods=['POST', 'GET'])
def home_page():
    form = SearchFileForm()

    if form.validate_on_submit():
        attempend_file = File.query.filter_by(number_file=form.number_of_file.data).first()
        if attempend_file:
            flash(f'Encontrado! {attempend_file.name_file}', category='success')
            return redirect(url_for('view_file_page', number_of_file=attempend_file.number_file))
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
        file_to_create = File(number_file=form.number_of_file.data,
                              name_file=form.name_of_file.data)

        db.session.add(file_to_create)
        db.session.commit()

        flash(f'Registrado con exito!', category='success')
        return redirect(url_for('files_page'))
    
    if form.errors != {}:
        for err_message in form.errors.values():
            flash(f'Ocurrio un error! {err_message[0]}', category='danger')

    return render_template('register_file.html', form=form)

@app.route('/file/<number_of_file>')
def view_file_page(number_of_file):
    attempend_file = File.query.filter_by(number_file=number_of_file).first()

    return render_template('file.html', attempend_file=attempend_file)


@app.route('/files')
def files_page():
    files = File.query.all()
    return render_template('files.html', files = files)

