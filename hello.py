from flask import Flask

app = Flask(__name__)

@app.route('/')
def firstApp():
    return "Hello World!! Welcome to Source Code Management, in feature-1 branch"
if __name__ == '__main__':
    app.run(debug = True)