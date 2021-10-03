"""Creating and run flask app"""
from flask import Flask
from config import APP_PORT
from api.v1.student.student_api import students_api_v1
from api.v1.classes.class_api import classes_api_v1
from api.v1.student_class.student_class_api import students_classes_api_v1


def create_students_api_app():
    """Create flask app and register blueprint"""
    app = Flask(__name__)
    app.register_blueprint(students_api_v1)
    app.register_blueprint(classes_api_v1)
    app.register_blueprint(students_classes_api_v1)
    return app


def run_students_api_app():
    """Run app"""
    student_api_app = create_students_api_app()
    student_api_app.run(debug=False, threaded=True, port=APP_PORT)


if __name__ == '__main__':
    run_students_api_app()
