from flask import Flask, render_template, url_for, request, make_response, redirect, jsonify


app = Flask(__name__)

biographicData = {
    "einstein" : {
        "name": "Albert Einstein",
        "text" : "Relativity theory creator"
    },
    "curye" : {
        "name" : "Marie Curye",
        "text" : "Mother of chemistry"
    },
    "Tesla":{
        "name": "Nikola Tesla",
        "text": "Hated by many, loved for more!"
    }
}

@app.route("/")
def index():
    
    return render_template("index.html", personas=biographicData)


@app.route("/persona/<id>")
def details(id):
    persona = biographicData.get(id,{
        "name": "Bad Request",
        "text": "Sorry but we couldn`t find the scientist :("
    })
    return render_template("index.html", personas=persona)

@app.route("/json/persona/<id>")
def jsonDetail(id):
    persona =  biographicData.get(id,{
        "name": "Bad Request",
        "text": "Sorry but we couldn`t find the scientist :("
    })
    return jsonify(persona)

if __name__ == "__main__":
    app.run(debug=True)