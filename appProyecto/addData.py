from urllib.request import urlopen
import appProyecto.models as m
import json
from appProyecto import app, db
from flask import jsonify

url = "https://datosabiertos.ayto-arganda.es/dataset/422ba3d6-93fb-49c1-8d0c-785fd6dfb631/resource/54c98ef5-60bf-4860-822a-b02b6748535b/download/eventos-febrero.json"

# Guarda la respuesta de la url
try:
    response = urlopen(url)
except:
     print("Error 879: Never Connected")


# Guarda el json response en data
data_json = json.loads(response.read())
  
#newVariableForJsonData = jsonify("{ 'Eventos': "+data_json+"}")

# Imprime json data



arrayBuffer = []
for events in data_json:
    new_entry = m.Evento(mes=events['MES'],
                        ano=events['ANO'],
                        instalacion=events['INSTALACION'],
                        entidad=events['ENTIDAD'],
                        actividad=events['ACTIVIDAD'],
                        deporte=events['DEPORTE'])
    print(new_entry.asdict())
    arrayBuffer.append(new_entry)

db.session.add_all(arrayBuffer)
db.session.commit()