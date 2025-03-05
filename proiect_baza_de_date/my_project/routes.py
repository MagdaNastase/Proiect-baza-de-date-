from flask import render_template, request, redirect, url_for, flash
from . import db
from .models import Produse, Clienti, Angajati, Comenzi, DetaliiComenzi
from flask import current_app as app
from sqlalchemy import func, select

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/view_data')
def view_data():
    produse = Produse.query.all()
    clienti = Clienti.query.all()
    angajati = Angajati.query.all()
    return render_template('view_data.html', produse=produse, clienti=clienti, angajati=angajati)

@app.route('/add_data', methods=['GET', 'POST'])
def add_data():
    if request.method == 'POST':
        denumire = request.form['denumire']
        pret = request.form['pret']
        descriere = request.form['descriere']
        stoc = request.form['stoc']
        new_product = Produse(Denumire=denumire, Pret=pret, Descriere=descriere, Stoc=stoc)
        db.session.add(new_product)
        db.session.commit()
        return redirect(url_for('view_data'))
    return render_template('add_data.html')

@app.route('/update_data/<int:id>', methods=['GET', 'POST'])
def update_data(id):
    product = Produse.query.get(id)
    if request.method == 'POST':
        product.Denumire = request.form['denumire']
        product.Pret = request.form['pret']
        product.Descriere = request.form['descriere']
        product.Stoc = request.form['stoc']
        db.session.commit()
        return redirect(url_for('view_data'))
    return render_template('update_data.html', product=product)


@app.route('/delete_data/<int:id>', methods=['GET', 'POST'])
def delete_data(id):
    product = Produse.query.get(id)
    try:
        # Șterge toate înregistrările din `detaliicomenzi` care fac referire la acest produs
        DetaliiComenzi.query.filter_by(ID_Produs=id).delete()
        db.session.delete(product)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        flash("Produsul nu poate fi șters deoarece este referit de alte înregistrări.", "error")
    return redirect(url_for('view_data'))


@app.route('/queries')
def queries():
    # Interogări intra-tabel
    produse_stoc_mic = Produse.query.filter(Produse.Stoc < 10).order_by(Produse.Stoc).limit(3).all()
    produse_pret_mare = Produse.query.filter(Produse.Pret > 100).all()
    produse_descriere_necompleta = Produse.query.filter(Produse.Descriere.is_(None) | (Produse.Descriere == '')).all()
    produse_mai_scumpe = Produse.query.filter(Produse.Pret > 50).order_by(Produse.Pret.desc()).limit(5).all()
    produse_nume_lung = Produse.query.filter(func.length(Produse.Denumire) > 10).order_by(func.length(Produse.Denumire)).limit(5).all()

    # Interogări inter-tabele
    clienti_cu_comenzi = db.session.query(Clienti, Comenzi).filter(Clienti.ID_Client == Comenzi.ID_Client).all()
    angajati_cu_comenzi = db.session.query(Angajati, Comenzi).filter(Angajati.ID_Angajat == Comenzi.ID_Angajat).all()

    # Subinterogare
    subquery = db.session.query(DetaliiComenzi.ID_Produs).group_by(DetaliiComenzi.ID_Produs).order_by(func.sum(DetaliiComenzi.Cantitate).desc()).limit(5).subquery()
    produse_cele_mai_vandute = db.session.query(Produse).filter(Produse.ID_Produs.in_(subquery)).all()

    # Funcții scalare și de agregat
    numar_produse = db.session.query(func.count(Produse.ID_Produs)).scalar()
    pret_mediu = db.session.query(func.avg(Produse.Pret)).scalar()

    return render_template('queries.html',
                           produse_stoc_mic=produse_stoc_mic,
                           produse_pret_mare=produse_pret_mare,
                           produse_descriere_necompleta=produse_descriere_necompleta,
                           produse_mai_scumpe=produse_mai_scumpe,
                           produse_nume_lung=produse_nume_lung,
                           clienti_cu_comenzi=clienti_cu_comenzi,
                           angajati_cu_comenzi=angajati_cu_comenzi,
                           produse_cele_mai_vandute=produse_cele_mai_vandute,
                           numar_produse=numar_produse,
                           pret_mediu=pret_mediu)