from appProyecto import app, db
import appProyecto.models as m
from flask import jsonify, request

# ==== Eventos API ==== #
@app.route('/eventos/', methods=['GET'])
def allEvents():
    events = m.Evento.query.all()
    response = jsonify([event.asdict() for event in events])
    response.headers.add('Access-Control-Allow-Origin', '*')
    db.session.execute('PRAGMA foreign_keys=ON;')
    return response

# ==== Empresas API ==== #

@app.route('/empresas/', methods=['GET'])
def allEmpresas():
    empresas = m.Empresa.query.all()
    response = jsonify([empresa.asdict() for empresa in empresas])
    response.headers.add('Access-Control-Allow-Origin', '*')
    db.session.execute('PRAGMA foreign_keys=ON;')
    return response

@app.route('/empresas/put', methods=['POST'])
def putEmpresa():
    nombre = request.form['nombre']
    ciudad = request.form['ciudad']
    mail = request.form['mail']
    telefono = request.form['telefono']

    empresa = m.Empresa(nombre,ciudad,mail,telefono)
    db.session.add(empresa)
    db.session.commit()
    return jsonify(empresa.asdict())

# ==== Participantes API ==== #

@app.route('/participantes/', methods=['GET'])
def allParticipantes():
    participantes = m.Participante.query.all()
    response = jsonify([participante.asdict() for participante in participantes])
    response.headers.add('Access-Control-Allow-Origin', '*')
    db.session.execute('PRAGMA foreign_keys=ON;')
    return response

@app.route('/participantes/put', methods=['POST'])
def putParticipantes():
    nombre = request.form['nombre']
    localidad = request.form['localidad']
    telefono = request.form['telefono']

    participante = m.Participante(nombre,localidad,telefono)
    db.session.add(participante)
    db.session.commit()
    return jsonify(participante.asdict())

