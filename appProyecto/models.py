from appProyecto import db

# ==== Eventos MODEL ==== #

class Evento(db.Model):
    #Solo hay que indicar el nombre de la columna se si llama distinto del nombre del atributo
    rowid = db.Column(db.Integer, primary_key = True)
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

# ==== Empresa MODEL ==== #

class Empresa(db.Model):
    idEmpresa = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(30))
    ciudad = db.Column(db.String(40))
    mail = db.Column(db.String(100))
    telefono = db.Column(db.String(20))

    def __init__(self, nombre, ciudad, mail, telefono):
        self.nombre = nombre
        self.ciudad = ciudad
        self.mail = mail
        self.telefono = telefono

    def asdict(self):

        return {"nombre" : self.nombre,
                "ciudad" : self.ciudad,
                "mail" : self.mail,
                "telefono" : self.telefono
        }

# ==== Participante MODEL ==== #

class Participante(db.Model):
    idParticipante = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(30))
    localidad = db.Column(db.String(40))
    telefono = db.Column(db.String(100))

    def __init__(self, nombre, localidad, telefono):
        self.nombre = nombre
        self.localidad = localidad
        self.telefono = telefono

    def asdict(self):

        return {"nombre" : self.nombre,
                "localidad" : self.localidad,
                "telefono" : self.telefono
        }


# ==== Participan MODEL ==== #

class Participan(db.Model):
    __tablename__ = "participan"
    id_evento = db.Column(db.Integer, primary_key = True)
    id_part = db.Column(db.Integer, primary_key = True)

    def __init__(self, id_evento, id_part):
        self.id_evento = id_evento
        self.localidad = id_part

    def asdict(self):

        return {"id_evento" : self.id_evento,
                "id_part" : self.id_part
        }