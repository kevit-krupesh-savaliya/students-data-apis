"""Students API"""
import json
from flask import Flask, request, Blueprint, jsonify
from services import database

students_api_v1 = Blueprint('students', __name__)

app = Flask(__name__)


@students_api_v1.route('/students', methods=['GET'])
def get_students():
    """Get students and return list of all users"""

    # Get students from db
    data = database.get_students()
    if not data['success']:
        return jsonify(data), 500
    return jsonify(list(data['students'])), 200

