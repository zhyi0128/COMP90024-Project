from flask import Flask
import os
app = Flask(__name__)


@app.route('/')
def index():
    return f"Severd from {os.getpid()}"


if __name__ == '__main__':
    app.run()
