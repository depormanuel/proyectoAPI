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

