from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Skills(db.Model):
    __tablename__ = 'skills'

    id = db.Column(db.Integer, primary_key=True)
    skill = db.Column(db.String)
    description = db.Column(db.String)

    def __repr__(self):
          return f'<Skills id={self.id}, skill={self.skill}, description={self.description}>'
