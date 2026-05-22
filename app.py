
from flask import Flask, render_template, jsonify, session
app = Flask(__name__)
app.secret_key = '8767'
# set type to pi5 for the pi5, set type to bob for the normal computer
session[]
@app.route("/")
def terminal():
  return render_template("terminal.html")

@app.route("/sendCommand")
def sendGetCommand():
  pass

if __name__ == "__main__":
  app.run(debug=True)
