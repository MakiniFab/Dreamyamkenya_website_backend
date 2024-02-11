from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates


db = SQLAlchemy()

class Skills(db.Model, SerializerMixin):
    __tablename__ = 'skills'
    serialize_rules = ('-reviews.skill',)

    id = db.Column(db.Integer, primary_key=True)
    skill = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))
    reviews = db.relationship('Review', backref='skill')

    def __repr__(self):
        return f'({self.id}) {self.skill} <br></br> {self.description}'

class Project(db.Model, SerializerMixin):
    __tablename__ = 'projects'
    serialize_rules = ('-reviews.project',)

    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(100), nullable=False)
    project_about = db.Column(db.String(200))
    reviews = db.relationship('Review', backref='project')

    def __repr__(self):
        return f'({self.id}) {self.project_name} <br></br> {self.project_about}'


class Review(db.Model, SerializerMixin):
    __tablename__ = 'reviews'
    serialize_rules = ('skill.reviews', 'project.reviews')

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    skill_id = db.Column(db.Integer, db.ForeignKey('skills.id'), nullable=False)

    def __repr__(self):
        return f'({self.id}) for {self.project} and {self.skill}'