from flask import Flask, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, Skills, Project, Review
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False
migrate = Migrate(app, db)

db.init_app(app)

# Routes
@app.route('/')
def index():
    response = make_response(
        '<h1>Welcome</h1>',
        200
    )
    return response

@app.route('/projects')
def projects():
    projects = Project.query.all()
    project_list = []
    for project in projects:
        project_dict = {
            'id': project.id,
            'project_name': project.project_name,
            'project_about': project.project_about
        }
        project_list.append(project_dict)
    return jsonify(project_list)

@app.route('/skills')
def skills():
    skills = Skills.query.all()
    skill_list = []
    for skill in skills:
        skill_dict = {
            'id': skill.id,
            'skill': skill.skill,
            'description': skill.description
        }
        skill_list.append(skill_dict)
    return jsonify(skill_list)

@app.route('/reviews')
def reviews():
    reviews = Review.query.all()
    review_list = []
    for review in reviews:
        review_dict = {
            'id': review.id,
            'text': review.text,
        }
        review_list.append(review_dict)
    return jsonify(review_list)

if __name__ == '__main__':
    app.run(port=5555)