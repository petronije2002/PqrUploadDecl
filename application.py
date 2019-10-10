from flask import Flask,render_template,flash
from flask_bootstrap import Bootstrap
import logging
import flask
from wtforms import TextField, BooleanField
from werkzeug import secure_filename
# from flask_wtf import Form
# from wtforms import StringField, SubmitField
# from wtforms.validators import Required
# from flask import request
from forms import DelcarationForm
from flask_wtf import FlaskForm

app = Flask(__name__, template_folder="Templates")
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'This is a string 1234567'

@app.route("/")
def hello():
    return render_template("base_menu.html", name="Pera")


@app.route("/Submit/", methods=['GET','POST'])
def hello_user():

    if flask.request.method=='POST':
    
        form = DelcarationForm(flask.request.form)

        print(form.date_.data)
        print(form.incl_btw.data)
        print(form.excl_btw.data)
        print(form.btw.data)
        print(form.description123.data)
        print(form.file_.data)


        return render_template("submitted.html")
    else:
        return render_template("submit_declarations.html",submit_button_text="SUBMIT HERE")





@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
       
            
@app.route("/redirect_url")
def redirect_url(e):
    return render_template("user.html", name="Nije validirano")



# @app.route("/rrr", methods= ['POST','GET'])
# def process_form():
#     return  #render_template("user.html", name="Pera")
 
 
  
  
if __name__ == '__main__':
    app.run(debug=True)

 
 
