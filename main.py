from flask import Flask, send_file

app = Flask(__name__)


@app.route('/')
def mainroute():
    return send_file('index.html')


if __name__ == "__main__":
    app.run()
