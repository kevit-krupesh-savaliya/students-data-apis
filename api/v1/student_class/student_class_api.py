"""Students-Classes API"""
from flask import Flask, Blueprint, jsonify
from services import database

students_classes_api_v1 = Blueprint('student_class', __name__)

app = Flask(__name__)


@students_classes_api_v1.route('/class/<int:class_id>/student/<int:student_id>', methods=['GET'])
@students_classes_api_v1.route('/student/<int:student_id>/class/<int:class_id>', methods=['GET'])
def get_student_with_marks(student_id, class_id):
    """Get students data along with class"""

    data = database.get_student_with_marks_with_class_id(student_id, class_id)
    if not data['success']:
        return jsonify(data), 500
    return jsonify(list(data['student'])[0]), 200
