from flask import Flask
from app.routes import routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(routes)
    return app

if __name__ == '__main__':
    app = create_app()
    # running the application over the Network
    app.run(debug=True, host='0.0.0.0', port=5000)
