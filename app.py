from flask import Flask, render_template, request, session, redirect
from flask_socketio import join_room, leave_room, send, SocketIO
from string import ascii_uppercase
import random, os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
socketio = SocketIO(app)    

@app.route('/insa_chat_app', methods=['POST', 'GET'], strict_slashes = False)
def index():
    return render_template("index.html")


if __name__ == "__main__":
    socketio.run(app, debug=True)