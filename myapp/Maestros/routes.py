from flask import Blueprint, request, render_template, redirect, url_for
from main import insertarMaestro, modificarMaestro, consultarMaestros, eliminarMaestro, consultarMaestro
import forms 

maestros = Blueprint('maestros', __name__)

@maestros.route("/addMaestro", methods=['GET', 'POST'])
def addMaestro():
    create_form = forms.MaestroForm(request.form)
    if request.method == 'POST':
        nombres = create_form.nombres.data,
        apellidos = create_form.apellidos.data,
        email = create_form.email.data
        
        insertarMaestro(nombres=nombres, apellidos=apellidos, email=email)
        return redirect(url_for('maestros.getMaestros'))
    
    return render_template('addMaestros.html', form = create_form)

@maestros.route('/getMaestros', methods=['GET', 'POST'])
def getMaestros():
    maestros = consultarMaestros()
    
    return render_template('listaMaestros.html', maestros = maestros)

@maestros.route('/editMaestro', methods=['GET', 'POST'])
def editMaestro():
    create_form = forms.MaestroForm(request.form)
    if request.method=='GET':
        id = request.args.get('id')
        # Select * from maestros where id==idmaestros    
        #alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        maestro = consultarMaestro(id)
        create_form.id.data= maestro[0]
        create_form.nombres.data=maestro[1]
        create_form.apellidos.data=maestro[2]
        create_form.email.data=maestro[3]

    if request.method=='POST':
        id = create_form.id.data
        # Select * from maestros where id==idmaestros    
        #maestro = db.session.query(Maestros).filter(Maestros.id==id).first()
        maestro = consultarMaestro(id)
        maestro[1] = create_form.nombres.data
        maestro[2] = create_form.apellidos.data
        maestro[3] = create_form.email.data
        nombres = maestro[1] 
        apellidos = maestro[2] 
        email = maestro[3]
        modificarMaestro(id= id, nombres=nombres, apellidos=apellidos, email=email)

        return redirect(url_for('maestros.getMaestros'))
    
    return render_template('updateMaestros.html', form=create_form)

@maestros.route('/deleteMaestro', methods=['GET', 'POST'])
def deleteMaestro():
    create_form = forms.MaestroForm(request.form)
    if request.method=='GET':
        id = request.args.get('id')
        # Select * from maestros where id==idmaestros    
        #alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        maestro = consultarMaestro(id)
        create_form.id.data= maestro[0]
        create_form.nombres.data=maestro[1]
        create_form.apellidos.data=maestro[2]
        create_form.email.data=maestro[3]

    if request.method=='POST':
        id = create_form.id.data
        # Select * from maestros where id==idmaestros    
        #maestro = db.session.query(Maestros).filter(Maestros.id==id).first()
        maestro = consultarMaestro(id)
        maestro[0] = create_form.id.data
        idmaestros = maestro[0] 
        
        eliminarMaestro(id= idmaestros)

        return redirect(url_for('maestros.getMaestros'))
    
    return render_template('deleteMaestros.html', form=create_form)
