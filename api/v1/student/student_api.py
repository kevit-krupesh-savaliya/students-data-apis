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


@students_api_v1.route('/student/<int:student_id>/classes', methods=['GET'])
def get_classes_of_student(student_id):
    """Get student along with classes"""

    data = database.get_student_with_classes(student_id)
    if not data['success']:
        return jsonify(data), 500
    final_data = list(data['student'])
    if not final_data:
        return jsonify('data not found'), 404
    return jsonify(final_data[0]), 200


@students_api_v1.route('/student/<int:student_id>/performance', methods=['GET'])
def get_marks_of_student(student_id):
    """Get student along with classes"""

    data = database.get_student_with_marks(student_id)
    if not data['success']:
        return jsonify(data), 500
    final_data = list(data['student'])
    if not final_data:
        return jsonify('data not found'), 404
    return jsonify(final_data[0]), 200
