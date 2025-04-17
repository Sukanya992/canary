from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    version = os.getenv('VERSION', 'canary')
    return f"Hello from canary! This is version {version}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
