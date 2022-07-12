from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return '<h1>Login</h1>'


@app.route('/games')
def reporter():
    return '''<h2>games</h2>
              <a href="/">logout</a>'''


if __name__ == "__main__":
    app.run()
