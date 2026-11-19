from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<p>Welkom bij mijn Flask-project!</p>"

if __name__ == '__main__':
    app.run(debug=True)