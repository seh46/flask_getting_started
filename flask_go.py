from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route("/name", methods=["GET"])
def getName():
    name = {
        "name": "Stephanie"
    }
    return jsonify(name)


@app.route("/hello/<name>", methods=["GET"])
def helloName(name):
    a = "Hello there, " + name
    name_message = {
        "message": a
    }
    return jsonify(name_message)


@app.route("/distance", methods=["POST"])
def findDistance():
    import math
    r = request.get_json()
    point1 = r["a"]
    point2 = r["b"]
    dist = math.sqrt((point1[0]-point2[0])^2+(point1[1]-point2[1])^2)
    dist_out = {
        "distance": dist,
        "a": point1,
        "b": point2
    }
    return jsonify(dist_out)