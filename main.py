from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/current_work')
def current_work():
    return render_template('current_work.html')


if __name__ == '__main__':
    app.run(debug=True)

