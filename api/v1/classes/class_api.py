"""Classes API"""
from flask import Flask, Blueprint, jsonify
from services import database

classes_api_v1 = Blueprint('classes', __name__)

app = Flask(__name__)


@classes_api_v1.route('/classes', methods=['GET'])
def get_classes():
    """Get all classes"""
    data = database.get_classes()
    if not data['success']:
        return jsonify(data), 500
    return jsonify(list(data['classes'])), 200


@classes_api_v1.route('/class/<class_id>/students', methods=['GET'])
def get_students_from_class(class_id):
    """Get students data along with class"""

    try:
        class_id = int(class_id)
    except ValueError:
        return jsonify({'success': False, 'error': 'student id must be number'})

    data = database.get_students_from_class_id(class_id)
    if not data['success']:
        return jsonify(data), 500
    return jsonify(list(data['students'])[0]), 200


@classes_api_v1.route('/class/<class_id>/performance', methods=['GET'])
def get_student_marks_from_class(class_id):
    """Get students marks along with classes"""

    try:
        class_id = int(class_id)
    except ValueError:
        return jsonify({'success': False, 'error': 'student id must be number'})

    data = database.get_students_marks_from_class_id(class_id)
    if not data['success']:
        return jsonify(data), 500
    return jsonify(list(data['students'])[0]), 200
