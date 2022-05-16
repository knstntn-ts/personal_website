from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/current_work')
def current_work():
    return render_template('current_work.html')

@app.route('/side_projects')
def side_projects():
    return render_template('side_projects.html')

@app.route('/contact')
def side_projects():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)

