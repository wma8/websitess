from flask_bootstrap import Bootstrap
from flask import Flask

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
