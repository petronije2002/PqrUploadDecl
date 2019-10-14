from app import app

# import evn variables for DB connection 

# from app import db

class Delcarations(db.Model):
    __tablename__ = 'DECLARATIONS'
    id = db.Column(db.Integer, primary_key=True)
    date_ = db.Column(db.Date, unique=False)
    description = db.Column(db.String , unique=False)

    excl_btw = db.Column(db.Numeric, unique=False,default=0)
    btw = db.Column(db.Numeric, unique=False,default=0)
    incl_btw = db.Column(db.Numeric, unique=False,default=0)

    image=db.Column(db.PickleType, unique=False,nullable=True)

    approved = db.Column(db.Boolean, unique=False, default=False)


    def __repr__(self):
        return '<Delcarations %r>' % self.name