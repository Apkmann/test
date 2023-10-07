from flask import Flask,render_template
from pymongo import MongoClient
import certifi
ca = certifi.where()
app = Flask(__name__,template_folder='template')
cl = MongoClient('mongodb+srv://mohammedaswath141:Aswath22%40data@cluster0.54i4ysr.mongodb.net/Hospital?retryWrites=true&w=majority',tlsCAFile=ca)

db = cl['Hospital']
collection = db['Departments']


@app.route('/')
def index():
    data = list(collection.find({}))
    return render_template("index.html",data=data)

if __name__=="__main__":
    app.run(debug=True)
