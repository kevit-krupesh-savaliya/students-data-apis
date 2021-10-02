"""Students API"""
from flask import Flask, Blueprint, jsonify
from services import database

students_api_v1 = Blueprint('students', __name__)

app = Flask(__name__)


@students_api_v1.route('/students', methods=['GET'])
def get_students():
    """Get students and return list of all users"""
    data = database.get_students()
    if not data['success']:
        return jsonify(data), 500
    return jsonify(list(data['students'])), 200


@students_api_v1.route('/student/<student_id>/classes', methods=['GET'])
def get_classes_of_student(student_id):
    """Get student along with classes"""

    try:
        student_id = int(student_id)
    except ValueError:
        return jsonify({'success': False, 'error': 'student id must be number'})

    data = database.get_student_with_classes(student_id)
    if not data['success']:
        return jsonify(data), 500
    return jsonify(list(data['student'])[0]), 200


@students_api_v1.route('/student/<student_id>/performance', methods=['GET'])
def get_marks_of_student(student_id):
    """Get student along with classes"""

    try:
        student_id = int(student_id)
    except ValueError:
        return jsonify({'success': False, 'error': 'student id must be number'})

    data = database.get_student_with_marks(student_id)
    if not data['success']:
        return jsonify(data), 500
    return jsonify(list(data['student'])[0]), 200
