import subprocess
from flask import Flask, render_template, jsonify, session, request

app = Flask(__name__)


@app.route("/")
def terminal():
    return render_template("terminal.html")


@app.route("/sendGetCommand", methods=["GET", "POST"])
def sendGetCommand():
    result = subprocess.run(request.get_json("message"), capture_output=True, text=True)

    return jsonify({"response": result.stdout})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
