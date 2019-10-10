from application import app

from flask_sqlalchemy import SQLAlchemy
# import evn variables for DB connection 

db = SQLAlchemy(app)








class Delcarations(db.Model):
    __tablename__ = 'declarations'
    id = db.Column(db.Integer, primary_key=True)
    date_ = db.Column(db.Date, unique=False)
    description = db.Column(db.String , unique=False)

    excl_btw = db.Column(db.Numeric, unique=False)
    btw = db.Column(db.Numeric, unique=False)
    incl_btw = db.Column(db.Numeric, unique=False)

    image=db.Column(db.PickleType, unique=False)


    def __repr__(self):
        return '<Delcarations %r>' % self.name