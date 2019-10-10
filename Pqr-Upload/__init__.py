from flask import Flask  # Import the Flask class
app = Flask(__name__)    # Create an instance of the class for our use


app.config['SECRET_KEY'] = 'This is a string 1234567'
app.config['SQLALCHEMY_DATABASE_URI'] = uri_azure_sql
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

