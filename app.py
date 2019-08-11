from flask import Flask, request

app = Flask(__name__)

print(__name__)

@app.route('/')
def index():
  return 'Index Page'

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
    app.run( host='0.0.0.0', port=8000, debug=True)