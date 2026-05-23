import os
import pty
import subprocess
import time
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

master, slave = pty.openpty()

shell = subprocess.Popen(
    ["/bin/bash"],
    stdin=slave,
    stdout=slave,
    stderr=slave,
    text=True
)

@app.route("/")
def terminal():
    return render_template("terminal.html")



@app.route("/sendGetCommand", methods=["POST"])
def run():
    cmd = request.get_json()["message"]

    os.write(master, (cmd + "\n").encode())

    output = ""

    # give shell a moment to respond
    time.sleep(0.05)

    # read all available output
    while True:
        try:
            chunk = os.read(master, 4096).decode()
            if not chunk:
                break
            output += chunk

            # stop condition (very basic heuristic)
            if len(chunk) < 4096:
                break
        except OSError:
            break

    return jsonify({"response": output})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
