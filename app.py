import socket
from flask import Flask,render_template
from flask_socketio import SocketIO, send


app = Flask(__name__)


socketio = SocketIO(app, cors_allowed_origins="*")




@socketio.on("message")
def message(message):
    send(message,broadcast=True)
   



@app.route("/")
def chat_room():
    return render_template("chat.html")




if __name__ == "__main__":
    app.run(debug=True)