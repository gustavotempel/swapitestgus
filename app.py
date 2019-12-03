from flask import Flask

app = Flask(__name__)

app.debug = True

@app.route('/', methods=['GET'])
def index():
    return 'Hello World with GET Method!'

@app.errorhandler(404)
def page_not_found(error):
    return '<title>Ups</title><h1>Ups! I did it again... Page not found!</h1>', 404

if __name__ == "__main__":
    app.run(port=8000)