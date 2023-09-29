from flask import Flask ,request,render_template,redirect,url_for


app = Flask(__name__,template_folder='template')


@app.route('/')
def index():
    return render_template("index.html") 

if __name__=="__main__":
    app.run()