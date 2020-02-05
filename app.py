from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
import requests

# Init app 
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)

# Request/Reply Class/Model
class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    req = db.Column(db.String(100))
    res = db.Column(db.String(100))

    def __init__(self, req, res):
        self.req = req
        self.res = res

# Request/Reply Schema
class RequestSchema(ma.Schema): 
    class Meta:
        fields = ('id', 'req', 'res')

# Init schema
request_schema = RequestSchema()
requests_schema = RequestSchema() 

# Create a Request
@app.route('/request', methods=['POST'])
def add_request():
    req = request.json['req']
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=ca1d7ede4a2f22cc446260bc15f4239e".format(req)
    r = requests.get(url)
    weather = r.json()
    res = weather['main']['temp']
    new_request = Request(req, res)

    db.session.add(new_request)
    db.session.commit()

    
    print(weather['main']['temp'])
    return request_schema.jsonify(new_request)

#Run Server
if __name__ == '__main__':
    app.run(debug=True)