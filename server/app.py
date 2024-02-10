from flask import Flask, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, Skills

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/skills')
def skills():

    skills = []
    for skill in Skills.query.all():
        skill_dict = {
            "title": skill.skill,
            "description": skill.description,
        }
        skills.append(skill_dict)

    response = make_response(
        jsonify(skills),
        200
    )
    response.headers["Content-Type"] = "application/json"

    return response


if __name__ == '__main__':
    app.run(port=5555)