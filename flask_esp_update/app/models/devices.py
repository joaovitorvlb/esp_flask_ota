from app import db


class Firmware(db.Model):
    __tablename__ = "firmware"
    id = db.Column(db.Integer, primary_key=True)
    categoria = db.Column(db.String(128))
    file = db.Column(db.String(128))
    compilado = db.Column(db.String(128))
    versao = db.Column(db.String(128))
    downloads = db.Column(db.Integer)

    def __init__(self, categoria, file, compilado, versao, downloads):
        self.categoria = categoria
        self.file = file
        self.compilado = compilado
        self.versao = versao
        self.downloads = downloads


class Dispositivos(db.Model):
    __tablename__ = "dispositivos"
    id = db.Column(db.Integer, primary_key=True)
    dispositivo = db.Column(db.String(128))
    categoria = db.Column(db.String(128))
    mac = db.Column(db.String(128))

    def __init__(self, dispositivo, categoria, mac):
        self.dispositivo = dispositivo
        self.categoria = categoria
        self.mac = mac
