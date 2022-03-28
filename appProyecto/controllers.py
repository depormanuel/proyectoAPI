from appProyecto import app, db
import appProyecto.models as m
from flask import jsonify, request

# ==== Eventos API ==== #
@app.route('/events/', methods=['GET'])
def allEvents():
    events = m.Evento.query.all()
    response = jsonify([event.asdict() for event in events])
    response.headers.add('Access-Control-Allow-Origin', '*')
    db.session.execute('PRAGMA foreign_keys=ON;')
    return response


@app.route('/empresas/', methods=['GET'])
def allEmpresas():
    empresas = m.Empresa.query.all()
    response = jsonify([empresa.asdict() for empresa in empresas])
    response.headers.add('Access-Control-Allow-Origin', '*')
    db.session.execute('PRAGMA foreign_keys=ON;')
    return response


@app.route('/participantes/', methods=['GET'])
def allParticipantes():
    participantes = m.Empresa.query.all()
    response = jsonify([participante.asdict() for participante in participantes])
    response.headers.add('Access-Control-Allow-Origin', '*')
    db.session.execute('PRAGMA foreign_keys=ON;')
    return response


