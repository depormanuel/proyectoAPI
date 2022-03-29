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

@app.route('/eventos/put', methods=['POST'])
def putEventos():
    mes = request.form['mes']
    ano = request.form['ano']
    instalacion = request.form['instalacion']
    idEmpresa = request.form['idEmpresa']
    actividad = request.form['actividad']
    deporte = request.form['deporte']


    evento = m.Evento( mes, ano, instalacion, idEmpresa, actividad, deporte)
    db.session.add(evento)
    db.session.commit()
    return jsonify(evento.asdict())

@app.route('/eventos/delete', methods=['POST'])
def delEventos():
    idEvento = request.form['idEvento']
    evento = m.Evento.geteventobyId(idEvento)
    db.session.delete(evento)
    db.session.commit()
    return jsonify(True)


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

@app.route('/empresas/delete', methods=['POST'])
def delEmpresas():
    idEmpresa= request.form['idEmpresa']
    empresa = m.Empresa.getEmpresaById(idEmpresa)
    db.session.delete(empresa)
    db.session.commit()
    return jsonify(True)


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

@app.route('/participantes/delete', methods=['POST'])
def delParticipante():
    idParticipante = request.form['idParticipante']
    participante = m.Participante.getParticipantebyId(idParticipante)
    db.session.delete(participante)
    db.session.commit()
    return jsonify(True)

@app.route('/participantes/<numTelef>', methods=['GET'])
def searchParticipan():
    participantes = m.Participante.query.all()
    response = jsonify([participante.asdict() for participante in participantes])
    response.headers.add('Access-Control-Allow-Origin', '*')
    db.session.execute('PRAGMA foreign_keys=ON;')
    return response

# ==== Participan API ==== #

# ---- MAÑANA SEGUIMOS------#
@app.route('/participan/<evento>', methods=['GET'])
def allParticipan():
    participan = m.association_table.query.all()
    print(participan)
    response = jsonify([participante.asdict() for participante in participan])
    response.headers.add('Access-Control-Allow-Origin', '*')
    db.session.execute('PRAGMA foreign_keys=ON;')
    return response


@app.route('/participan/put', methods=['POST'])
def putParticipan():
    eventoid = request.form['eventoid']
    participanteid = request.form['participanteid']

    evento = m.Evento.geteventobyId(eventoid)
    participante = m.Participante.getParticipantebyId(participanteid)

    statement = m.association_table.insert().values(id_evento=evento.rowid, id_part=participante.rowid)
    db.session.execute(statement)
    db.session.commit()
    return jsonify(True)