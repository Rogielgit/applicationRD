import os
from flask import Flask


app = Flask(__name__)

@app.route("/")
def index():
    name = raw_input("Digite um nome");
    return "<h1>Hello World</hi>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
