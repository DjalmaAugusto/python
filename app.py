import os
from flask import Flask, request, jsonify

HOST_NAME = os.environ.get('OPENSHIFT_APP_DNS', 'localhost')
APP_NAME = os.environ.get('OPENSHIFT_APP_NAME', 'flask')
IP = os.environ.get('OPENSHIFT_PYTHON_IP', '127.0.0.1')
PORT = int(os.environ.get('OPENSHIFT_PYTHON_PORT', 8080))
HOME_DIR = os.environ.get('OPENSHIFT_HOMEDIR', os.getcwd())

app = Flask(__name__)

print(__name__)

@app.route('/')
def index():
  return jsonify({
        'host_name': HOST_NAME,
        'app_name': APP_NAME,
        'ip': IP,
        'port': PORT,
        'home_dir': HOME_DIR,
        'host': socket.gethostname()
    })

@app.route('/hello')
def hello():
  return 'Hello, greetings from different endpoint'

@app.route('/user', methods=['GET','POST'])
def get_user():
  username = request.args.get('username', default=None, type=None)
  password = request.args.get('password', default=None, type=None)
  #login(arg,arg) is a function that tries to log in and returns true or false
  return 'username: %s / password: %s' % (username, password)

#adding variables
@app.route('/user/<username>')
def show_user(username=None):
  #returns the username
  return 'Username: %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
  #returns the post, the post_id should be an int
  return str(post_id)

@app.route('/login', methods=['GET','POST'])
def login():
  if request.method == 'POST':
    #check user details from db
    return "POST"
  elif request.method == 'GET':
    #serve login page
    return "GET"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
