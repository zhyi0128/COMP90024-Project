from App import create_app
import os

env = os.environ.get("FLASK_ENV") or "development"

app = create_app(env)

if __name__ == '__main__':
    app.run()
