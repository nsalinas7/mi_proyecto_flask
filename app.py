import os
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return jsonify({"mensaje": "Hola, este es mi servicio web Flask"})

@app.route("/eco", methods=["POST"])
def eco():
    data = request.get_json()
    return jsonify({
        "mensaje": "Este es el eco de tu JSON",
        "dataRecibida": data
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
