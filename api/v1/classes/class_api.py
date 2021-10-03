"""Classes API"""
from flask import Flask, Blueprint, jsonify
from services import database
from services.common_helper import grade_calculation, check_duplicate_class_and_add_total

classes_api_v1 = Blueprint('classes', __name__)

app = Flask(__name__)


@classes_api_v1.route('/classes', methods=['GET'])
def get_classes():
    """Get all classes"""

    data = database.get_classes()
    if not data['success']:
        return jsonify(data), 500
    return jsonify(list(data['classes'])), 200


@classes_api_v1.route('/class/<int:class_id>/students', methods=['GET'])
def get_students_from_class(class_id):
    """Get students data along with class"""

    data = database.get_students_from_class_id(class_id)
    if not data['success']:
        return jsonify(data), 500
    final_data = list(data['students'])
    if not final_data:
        return jsonify('data not found'), 404
    return jsonify(final_data[0]), 200


@classes_api_v1.route('/class/<int:class_id>/performance', methods=['GET'])
def get_student_marks_from_class(class_id):
    """Get students marks along with classes"""

    data = database.get_students_marks_from_class_id(class_id)
    if not data['success']:
        return jsonify(data), 500
    final_data = list(data['students'])
    if not final_data:
        return jsonify('data not found'), 404
    return jsonify(final_data[0]), 200


@classes_api_v1.route('/class/<int:class_id>/final-grade-sheet', methods=['GET'])
def get_student_grade_sheet(class_id):
    """Get students marks along with classes"""

    data = database.get_student_data(class_id)
    if not data['success']:
        return jsonify(data), 500
    student_data = list(data['students'])
    if not student_data:
        return jsonify('data not found'), 404
    # Now we calculate grade
    student_data = grade_calculation(student_data[0])
    # Now make response as required
    final_data = check_duplicate_class_and_add_total(student_data['students'], mark_field='details')
    student_data['students'] = final_data
    return jsonify(student_data), 200
