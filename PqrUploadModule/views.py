from flask import Flask,render_template,flash
from flask_bootstrap import Bootstrap
import logging
import flask
from wtforms import TextField, BooleanField
from werkzeug import secure_filename

import sys
import os
from flask_bootstrap import Bootstrap

from . import app
from . import forms

from . import bootstrap



@app.route("/")
def hello():
    

    name = flask.request.headers.get("X-MS-CLIENT-PRINCIPAL-NAME")
    name_id = flask.request.headers.get("X-MS-CLIENT-PRINCIPAL-ID")


    return render_template("base_menu.html", name=name)
 

@app.route("/Submit/", methods=['GET','POST'])
def hello_user():

    if flask.request.method=='POST':
    
        form = forms.DelcarationForm(flask.request.form)

        print(form.date_.data)
        print(form.incl_btw.data)
        print(form.excl_btw.data)
        print(form.btw.data)
        print(form.description123.data)
        print(form.file_.data)

        name = flask.request.headers.get("X-MS-CLIENT-PRINCIPAL-NAME")
        name_id = flask.request.headers.get("X-MS-CLIENT-PRINCIPAL-ID")


        return render_template("submitted.html",name=name)
    else:

        # print(flask.request.headers.get("X-MS-CLIENT-PRINCIPAL-NAME"))
        # print(flask.request.headers.get("X-MS-CLIENT-PRINCIPAL-ID"))

        name = flask.request.headers.get("X-MS-CLIENT-PRINCIPAL-NAME")
        name_id = flask.request.headers.get("X-MS-CLIENT-PRINCIPAL-ID")
      

        return render_template("submit_declarations.html",name=name,submit_button_text="SUBMIT HERE")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
       
            
@app.route("/redirect_url")
def redirect_url(e):
    return render_template("user.html", name="Nije validirano")
  
# if __name__ == '__main__':
#     app.run(debug=False)

 
 
