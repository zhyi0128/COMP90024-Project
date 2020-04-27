from App import create_app
import os
from flask_cors import CORS

app = create_app()
CORS(app, resources={r"/*": {"origins": "*"}})

if __name__ == '__main__':
    app.run()
