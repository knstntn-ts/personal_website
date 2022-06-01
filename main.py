from flask import Flask, render_template, render_template_string
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///website.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Project(db.Model):
    __tablename__ = "project_details"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    img_main_1 = db.Column(db.String(250), nullable=False)
    img_main_2 = db.Column(db.String(250), nullable=False)
    html_body_path = db.Column(db.String(250), nullable=False)


@app.route('/')
@app.route('/index')
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)


@app.route('/#work')
# @app.route('/work')
def current_work():
    projects = Project.query.all()
    return render_template('current_work.html', current_work=projects)


@app.route('/side_projects')
def side_projects():

    return render_template('side_projects.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route("/project/<int:project_id>", methods=["GET", "POST"])
def show_work(project_id):
    project = Project.query.get(project_id)
    # return render_template_string(project.html, project=project)
    return render_template('project.html', project=project)


if __name__ == '__main__':
    app.run(debug=True)

