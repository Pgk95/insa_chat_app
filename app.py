from flask import Flask, render_template, request, session, redirect
from flask_socketio import join_room, leave_room, send, SocketIO
from string import ascii_uppercase
import random, os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
socketio = SocketIO(app)    

@app.route('/', methods=['POST', 'GET'], strict_slashes=False)
def index():
    return render_template("index.html")

@app.route('/signup', methods=['POST', 'GET'], strict_slashes=False)
def signup():
    return render_template("signup.html")

@app.route('/login', methods=['POST', 'GET'], strict_slashes=False)
def login():
    return render_template("login.html")

@app.route('/chat', methods=['POST', 'GET'], strict_slashes=False)
def chat():
    return render_template("chat.html")



if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port="9000", debug=True)