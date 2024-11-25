#Create/Connect to VE and install flask, run inside VE 

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return render_template("greet.html", name=request.form.get("name"))
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)

"""
#Old version
@app.route('/')
def index():
    name = "Carl"
    return render_template("index2.html", placeholder=name)
 
#second url  
@app.route('/hello')
def greet(name):
"""