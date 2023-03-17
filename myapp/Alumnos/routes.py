from flask import Blueprint, request, render_template, redirect, url_for
from main import insertarAlumno, modificarAlumno, consultarAlumno, eliminarAlumno, consultarAlumnos
import forms 
from models import db
from models import Alumnos


alumnos = Blueprint('alumnos', __name__)

@alumnos.route("/addAlumno", methods=['GET', 'POST'])
def addMaestro():
    create_form = forms.UserForm(request.form)
    if request.method == 'POST':
        alum = Alumnos(nombres = create_form.nombres.data,
        apellidos = create_form.apellidos.data,
        email = create_form.email.data)
        
        #insertarAlumno(nombres=nombres, apellidos=apellidos, email=email)
        # Insert en la BD
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for('alumnos.getAlumnos'))
    
    return render_template('addAlumnos.html', form = create_form)

@alumnos.route('/getAlumnos', methods=['GET', 'POST'])
def getAlumnos():
    #alumnos = consultarAlumnos()
    create_form = forms.UserForm(request.form)
    alumnos = Alumnos.query.all()
    return render_template('listaAlumnos.html', form=create_form ,alumnos = alumnos)

@alumnos.route('/editAlumno', methods=['GET', 'POST'])
def editAlumno():
    create_form = forms.UserForm(request.form)
    if request.method=='GET':
        id = request.args.get('id')
        # Select * from maestros where id==idmaestros    
        #alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        create_form.id.data=alum1.id
        create_form.nombres.data=alum1.nombres
        create_form.apellidos.data=alum1.apellidos
        create_form.email.data=alum1.email

    if request.method=='POST':
        id = create_form.id.data
        # Select * from alumnos where id==id    
        alum=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        alum.nombres = create_form.nombres.data
        alum.apellidos = create_form.apellidos.data
        alum.email = create_form.email.data
        db.session.add(alum)
        db.session.commit()

        return redirect(url_for('alumnos.getAlumnos'))
    
    return render_template('updateAlumnos.html', form=create_form)

@alumnos.route('/deleteAlumno', methods=['GET', 'POST'])
def deleteAlumno():
    create_form = forms.UserForm(request.form)
    if request.method=='GET':
        id = request.args.get('id')
        # Select * from alumnos where id==id    
        alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        create_form.id.data=alum1.id
        create_form.nombres.data=alum1.nombres
        create_form.apellidos.data=alum1.apellidos
        create_form.email.data=alum1.email

    if request.method=='POST':
        id = create_form.id.data
        # Select * from alumnos where id==id    
        alum=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        db.session.delete(alum)
        db.session.commit()

        return redirect(url_for('alumnos.getAlumnos'))
    
    return render_template('deleteAlumnos.html', form=create_form)
