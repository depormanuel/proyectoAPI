from appProyecto import app, db
import appProyecto.models as m
from flask import jsonify, request



# ==== MOVIE API ==== #
@app.route('/events/', methods=['GET'])
def allEvents():
    events = m.Evento.query.all()
    response = jsonify([events.asdict() for event in events])
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

