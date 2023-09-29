from flask import Flask ,request,render_template,redirect,url_for
from pymongo import MongoClient
import urllib.parse
import certifi
ca = certifi.where()
passw = "Aswath22@data"
p = urllib.parse.quote(passw)
app = Flask(__name__,template_folder='template',static_url_path="/static")
cl = MongoClient(f'mongodb+srv://mohammedaswath141:{p}@cluster0.54i4ysr.mongodb.net/?retryWrites=true&w=majority',tlsCAFile=ca)

db = cl['Hospital']
collection = db['Departments']


@app.route('/')
def index():
    data = list(collection.find({}))
    return render_template("index.html",data=data)

if __name__=="__main__":
    app.run(debug=True)
