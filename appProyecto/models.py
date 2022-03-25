from appProyecto import db

# ==== Eventos MODEL ==== #

class Evento(db.Model):
    #Solo hay que indicar el nombre de la columna se si llama distinto del nombre del atributo
    idEvent = db.Column(db.Integer, primary_key = True)
    mes = db.Column(db.String(30))
    ano = db.Column(db.Integer)
    instalacion = db.Column(db.String(100))
    entidad = db.Column(db.String(100))
    actividad = db.Column(db.String(100))
    deporte = db.Column(db.String(100))

    def __init__(self, mes, ano, instalacion, entidad, actividad, deporte):
        self.mes = mes
        self.ano = ano
        self.instalacion = instalacion
        self.entidad = entidad
        self.actividad = actividad
        self.deporte = deporte

    def asdict(self):

        return {"mes" : self.mes,
                "ano" : self.ano,
                "instalacion" : self.instalacion,
                "entidad" : self.entidad,
                "actividad" : self.actividad,
                "deporte" : self.deporte
        }
