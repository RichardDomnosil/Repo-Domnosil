from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/abeceda')
def abeceda():
    return render_template('abeceda.html')


@app.route('/alfabeta')
def alfabeta():
    return render_template('alfabeta.html')


@app.route('/azbuka')
def azbuka():
    return render_template('azbuka.html')


@app.route('/hebrejstina')
def hebrejstina():
    return render_template('hebrejstina.html')

@app.route('/alfabeto')
def alfabeta():
    return render_template('alfabeto.html')


if __name__ == '__main__':
    app.run(debug=True)
