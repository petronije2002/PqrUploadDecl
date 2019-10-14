from app import app
from sqlalchemy import SQLAlchemy
# import evn variables for DB connection 

# from app import db
db = SQLAlchemy(app)


class Delcarations_(db.Model):
    __tablename__ = 'DECLARATIONS'

    id = db.Column(db.Integer, primary_key=True)

    date_ = db.Column(db.Date, unique=False)

    created_at = db.Column(db.DateTime)

    description = db.Column(db.String , unique=False)

    excl_btw = db.Column(db.Numeric, unique=False,default=0)

    btw = db.Column(db.Numeric, unique=False,default=0)

    incl_btw = db.Column(db.Numeric, unique=False,default=0)

    image=db.Column(db.PickleType, unique=False,nullable=True)

    ex_status = db.Column(db.Boolean, unique=False, default=False)

    approved = db.Column(db.Boolean, unique=False, default=False)

    manager_triggered = db.Column(db.Boolean, unique=False, default=False)

    manager_note = db.Column(db.String , unique=False,default='')


    def __repr__(self):
        return '<Delcarations %r>' % self.name