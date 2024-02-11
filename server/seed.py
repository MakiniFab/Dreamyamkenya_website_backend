# Import required modules and classes
from app import app, db
from models import Skills, Project, Review

# Define the seed_database function
def seed_database():
    with app.app_context():
        # Delete all existing data in all tables
        db.session.query(Skills).delete()
        db.session.query(Project).delete()
        db.session.query(Review).delete()

        # Commit the deletions
        db.session.commit()

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

        skills_instances = [Skills(**data) for data in skills_data]

        # Add all instances to the database session
        db.session.add_all(skills_instances)

        # Commit the changes to the database
        db.session.commit()

        # Create instances of Projects
        projects_data = [
            {'project_name': 'Project 1', 'project_about': 'Description of Project 1'},
            {'project_name': 'Project 2', 'project_about': 'Description of Project 2'},
        ]

        projects_instances = [Project(**data) for data in projects_data]

        # Add all instances to the database session
        db.session.add_all(projects_instances)

        # Commit the changes to the database
        db.session.commit()

        # Create instances of Reviews and establish relationships
        reviews_data = [
            {'text': 'Review for Project 1', 'project_id': 1, 'skill_id': 1},
            {'text': 'Review for Project 2', 'project_id': 2, 'skill_id': 2},
        ]

        reviews_instances = [Review(**data) for data in reviews_data]

        # Add all instances to the database session
        db.session.add_all(reviews_instances)

        # Commit the changes to the database
        db.session.commit()

# Entry point to run the seeding process
if __name__ == '__main__':
    seed_database()
