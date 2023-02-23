from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/user/<username>')
def user_profile(username):
    return f'Hello, {username}!'

with app.test_request_context():
    print(url_for('index')) # Output: "/"
    print(url_for('user_profile', username='John')) # Output: "/user/John"

if __name__=="__main__":
    app.run(host="0.0.0.0")