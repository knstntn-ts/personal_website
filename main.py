from flask import Flask, render_template, render_template_string, redirect
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import unquote, quote


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


class SideProject(db.Model):
    __tablename__ = "side_project_details"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    img_main_1 = db.Column(db.String(250), nullable=False)
    img_main_2 = db.Column(db.String(250), nullable=False)
    html_body_path = db.Column(db.String(250), nullable=False)


# db.create_all()


@app.route('/#home')
@app.route('/')
def index():
    projects = Project.query.all()
    side_projects_in = SideProject.query.all()
    return render_template('index.html', projects=projects, side_projects=side_projects_in)


@app.route('/current_work')
def current_work():
    return redirect('/#work')


@app.route('/side_projects')
def side_projects():
    return redirect('/#side_projects')


@app.route('/contact')
def contact():
    return redirect('/#contact')


@app.route("/project/<int:project_id>", methods=["GET", "POST"])
def show_work(project_id):
    project = Project.query.get(project_id)
    return render_template('project.html', project=project)


@app.route("/side_project/<int:project_id>", methods=["GET", "POST"])
def show_side_project(project_id):
    project = SideProject.query.get(project_id)
    return render_template('project.html', project=project)


if __name__ == '__main__':
    app.run(debug=True)

