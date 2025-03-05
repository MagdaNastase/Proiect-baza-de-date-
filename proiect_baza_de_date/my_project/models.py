from . import db

class Produse(db.Model):
    __tablename__ = 'Produse'
    ID_Produs = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Denumire = db.Column(db.String(255), nullable=False)
    Pret = db.Column(db.Numeric(10, 2), nullable=False)
    Descriere = db.Column(db.Text)
    Stoc = db.Column(db.Integer, nullable=False)

class Clienti(db.Model):
    __tablename__ = 'Clienti'
    ID_Client = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Nume = db.Column(db.String(255), nullable=False)
    Prenume = db.Column(db.String(255))
    Email = db.Column(db.String(255), unique=True)
    Telefon = db.Column(db.String(15))
    DataInregistrare = db.Column(db.Date)
    Adresa = db.Column(db.Text)

class Angajati(db.Model):
    __tablename__ = 'Angajati'
    ID_Angajat = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Nume = db.Column(db.String(255), nullable=False)
    Prenume = db.Column(db.String(255))
    Email = db.Column(db.String(255), unique=True)
    Telefon = db.Column(db.String(15))
    DataAngajare = db.Column(db.Date, nullable=False)
    Salariu = db.Column(db.Numeric(10, 2), nullable=False)

class Comenzi(db.Model):
    __tablename__ = 'Comenzi'
    ID_Comanda = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ID_Client = db.Column(db.Integer, db.ForeignKey('Clienti.ID_Client'))
    ID_Angajat = db.Column(db.Integer, db.ForeignKey('Angajati.ID_Angajat'))
    DataComanda = db.Column(db.Date, nullable=False)
    Total = db.Column(db.Numeric(10, 2))

class DetaliiComenzi(db.Model):
    __tablename__ = 'DetaliiComenzi'
    ID_Comanda = db.Column(db.Integer, db.ForeignKey('Comenzi.ID_Comanda'), primary_key=True)
    ID_Produs = db.Column(db.Integer, db.ForeignKey('Produse.ID_Produs'), primary_key=True)
    Cantitate = db.Column(db.Integer, nullable=False)
    PretUnitar = db.Column(db.Numeric(10, 2))
