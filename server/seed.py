# Import the SQLAlchemy db object from your Flask application
from app import app, db
from models import Skills

def seed_database():
    with app.app_context():
        # Create instances of Skills
        skills_data = [
            {'skill': 'Python', 'description': 'Software development skills'},
            {'skill': 'React', 'description': 'Software development skills'},
            {'skill': 'Flask', 'description': 'Software development skills'},
            {'skill': 'HTML', 'description': 'Software development skills'},
            {'skill': 'JavaScript', 'description': 'Analytical skills for data processing'},
            {'skill': 'CSS', 'description': 'Software development skills'},
            {'skill': 'SQLAlchemy', 'description': 'Software development skills'},
            {'skill': 'API & RESTFUL API', 'description': 'Software development skills'},
        ]

        # Add unique instances to the database session
        for skill_data in skills_data:
            skill = Skills.query.filter_by(skill=skill_data['skill']).first()
            if not skill:
                new_skill = Skills(**skill_data)
                db.session.add(new_skill)

        # Commit the changes to the database
        db.session.commit()

# Entry point to run the seeding process
if __name__ == '__main__':
    seed_database()
