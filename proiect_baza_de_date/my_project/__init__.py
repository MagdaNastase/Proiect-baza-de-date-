from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:2002@localhost/LibrarieOnline'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['TEMPLATES_AUTO_RELOAD'] = True  # Optional: enable auto-reloading of templates
    app.template_folder = 'C:\\Users\\nasta\\OneDrive - Universitatea Politehnica Bucuresti\\Desktop\\proiect_refacut_V2\\templates'

    db.init_app(app)

    with app.app_context():
        from . import routes  # Import routes
        db.create_all()  # Create database tables for our data models

    return app

