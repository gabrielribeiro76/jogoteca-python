from flask import Flask

app = Flask(__name__)

@app.route('/home')
def ola():
    return 'Ola Mundo!'


app.run()