# Import the SQLAlchemy db object from your Flask application
from app import app, db
from models import Skills

def seed_database():
    # Create an application context
    with app.app_context():
        # Create instances of Skills
        skills = [
            Skills(skill='Python', description='Software development skills'),
            Skills(skill='React', description='Software development skills'),
            Skills(skill='Flask', description='Software development skills'),
            Skills(skill='HTML', description='Software development skills'),
            Skills(skill='JavaScript', description='Analytical skills for data processing'),
            Skills(skill='CSS', description='Software development skills'),
            Skills(skill='SQLAlchemy', description='Software development skills'),
            Skills(skill='API & RESTFUL API', description='Software development skills'),
        ]

        # Add all instances to the database session
        db.session.add_all(skills)

        # Commit the changes to the database
        db.session.commit()

# Entry point to run the seeding process
if __name__ == '__main__':
    seed_database()
