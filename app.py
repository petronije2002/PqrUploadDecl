from flask import Flask,render_template,flash
from flask_bootstrap import Bootstrap
from flask import redirect, url_for,session
import logging
import flask
from wtforms import TextField, BooleanField
from werkzeug import secure_filename
from sql_settings import uri_azure_sql
import sys
import os
import urllib
import pyodbc
import datetime 
import datetime
from flask_bootstrap import Bootstrap
from forms import DelcarationForm
from flask_sqlalchemy import SQLAlchemy
import requests



app=Flask(__name__,template_folder='templates',static_folder='')
app.config['SQLALCHEMY_DATABASE_URI'] = uri_azure_sql
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
app.config['SECRET_KEY']='2132132dsadasd'

bootstrap = Bootstrap(app)

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


@app.route("/")
def hello():

    if 'tkn' in session:
        name = flask.request.headers.get("X-MS-CLIENT-PRINCIPAL-NAME")
        name_id = flask.request.headers.get("X-MS-CLIENT-PRINCIPAL-ID")

        tkn = flask.request.headers.get("X-MS-TOKEN-AAD-ACCESS-TOKEN")

    else:

        session['tkn'] = flask.request.headers.get("X-MS-TOKEN-AAD-ACCESS-TOKEN")

        tkn = session['tkn']


   
    # name = flask.request.headers.get("X-MS-CLIENT-PRINCIPAL-NAME")
    # name_id = flask.request.headers.get("X-MS-CLIENT-PRINCIPAL-ID")

    # token = flask.request.headers.get("X-MS-TOKEN-AAD-ACCESS-TOKEN")

    return render_template("base_menu.html", name=tkn)
 

@app.route("/Submit/", methods=['GET','POST'])
def hello_user():

    

    if flask.request.method=='POST':
    
        form = DelcarationForm(flask.request.form,csrf_enabled=False)

        print(form.date_.data)
        print(form.incl_btw.data)
        print(form.excl_btw.data)
        print(form.btw.data)
        print(form.description123.data)
        print(form.file_.data)
        
        
        name = flask.request.headers.get("X-MS-CLIENT-PRINCIPAL-NAME")
        name_id = flask.request.headers.get("X-MS-CLIENT-PRINCIPAL-ID")

        declr = Delcarations_()

        declr.date_ =  form.date_.data
        
        declr.created_at = datetime.datetime.now()
        declr.description = str(form.description123.data)
        declr.excl_btw = float(form.excl_btw.data)
        declr.btw = float(form.btw.data)
        declr.incl_btw = float(form.incl_btw.data)
        declr.image = form.file_.data

        db.session.add(declr)
        db.session.commit()




        return render_template("submitted.html",name=name)
    else:

        name = flask.request.headers.get("X-MS-CLIENT-PRINCIPAL-NAME")
        name_id = flask.request.headers.get("X-MS-CLIENT-PRINCIPAL-ID")
      

        return render_template("submit_declarations.html",name=name_id,submit_button_text="SUBMIT HERE")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
       
        
# @app.route("/redirect_url")
# def redirect_url(e):
#     return render_template("user.html", name="Nije validirano")
  
 


if __name__=="__main__":
    
    app.run(debug=True)


