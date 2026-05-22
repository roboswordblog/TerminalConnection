
from flask import Flask, render_template, jsonify, session
app = Flask(__name__)
app.secret_key = '8767'

@app.route("/")
def terminal():
  return render_template("terminal.html")

@app.route("/sendCommand")
def sendGetCommand():
  pass

if __name__ == "__main__":
  app.run(debug=True)
