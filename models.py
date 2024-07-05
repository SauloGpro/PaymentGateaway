from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Otros campos relevantes para la transacción
