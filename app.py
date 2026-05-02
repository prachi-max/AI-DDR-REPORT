from flask import Flask
from routes.upload_routes import upload_bp

app = Flask(__name__)

app.register_blueprint(upload_bp) 
if __name__ == "__main__":
    app.run(debug=True)