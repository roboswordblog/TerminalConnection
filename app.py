import subprocesses 
from flask import Flask, render_template, jsonify, session, request
app = Flask(__name__)
@app.route("/")
def terminal():
  return render_template("terminal.html")

@app.route("/sendCommand")
def sendGetCommand():
  result = subprocess.run(request.get_json("message"), capture_output=True, text=True)

  return jsonify({"output": result.stdout})


if __name__ == "__main__":
  app.run(debug=True)
