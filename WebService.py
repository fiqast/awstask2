from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello World!'

@app.route('/aloha')
def aloha():
    return 'Aloha World!'

if __name__ == '__main__':
    app.run(debug=True)