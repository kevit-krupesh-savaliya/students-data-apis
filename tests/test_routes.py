import json
import pytest
import main


@pytest.fixture
def client():
    """pytest client"""
    app = main.create_students_api_app()
    app.config['TESTING'] = True

    with app.app_context():
        with app.test_client() as client:
            yield client


"""test cases for student APIs"""


def test_get_students(client):
    """test get students"""
    response_data = client.get('/students')
    assert isinstance(json.loads(response_data.data), list)


def test_get_classes_of_student(client):
    """test get classes of student"""
    # if data is available
    response_data = client.get('/student/0/classes')
    response_data = json.loads(response_data.data)
    keys = list(response_data.keys())
    required_keys = ['student_id', 'student_name', 'classes']
    assert isinstance(response_data, dict)
    assert set(required_keys).issubset(set(keys))
    # if data is not available
    response_data = client.get('/student/10000/classes')
    response_data = json.loads(response_data.data)
    assert isinstance(response_data, str)
    assert response_data == 'data not found'


def test_get_performance_of_student(client):
    """test get performance of student"""
    # if data is available
    response_data = client.get('/student/0/performance')
    response_data = json.loads(response_data.data)
    keys = list(response_data.keys())
    required_keys = ['student_id', 'student_name', 'classes']
    assert isinstance(response_data, dict)
    assert set(required_keys).issubset(set(keys))
    # if data is not available
    response_data = client.get('/student/10000/performance')
    response_data = json.loads(response_data.data)
    assert isinstance(response_data, str)
    assert response_data == 'data not found'


"""test cases for class APIs"""


def test_get_classes(client):
    """test get classes"""
    response_data = client.get('/classes')
    assert isinstance(json.loads(response_data.data), list)


def test_get_students_from_class_id(client):
    """test get students for given class"""
    # if data is available
    response_data = client.get('/class/113/students')
    response_data = json.loads(response_data.data)
    keys = list(response_data.keys())
    required_keys = ['class_id', 'students']
    assert isinstance(response_data, dict)
    assert set(required_keys).issubset(set(keys))
    # if data is not available
    response_data = client.get('/class/1333/students')
    response_data = json.loads(response_data.data)
    assert isinstance(response_data, str)
    assert response_data == 'data not found'


def test_get_students_performance_from_class_id(client):
    """test get student performance for given class"""
    # if data is available
    response_data = client.get('/class/113/performance')
    response_data = json.loads(response_data.data)
    keys = list(response_data.keys())
    required_keys = ['class_id', 'students']
    assert isinstance(response_data, dict)
    assert set(required_keys).issubset(set(keys))
    # if data is not available
    response_data = client.get('/class/1333/performance')
    response_data = json.loads(response_data.data)
    assert isinstance(response_data, str)
    assert response_data == 'data not found'


def test_get_students_grade_from_class_id(client):
    """test get student grade for given class"""
    # if data is available
    response_data = client.get('/class/113/final-grade-sheet')
    response_data = json.loads(response_data.data)
    keys = list(response_data.keys())
    required_keys = ['class_id', 'students']
    assert isinstance(response_data, dict)
    assert set(required_keys).issubset(set(keys))
    # if data is not available
    response_data = client.get('/class/1333/final-grade-sheet')
    response_data = json.loads(response_data.data)
    assert isinstance(response_data, str)
    assert response_data == 'data not found'


"""test cases for student + class APIs"""


def test_get_student_with_course(client):
    """test get student with courses for given class"""
    # if data is available
    response_data = client.get('/class/331/student/0')
    response_data = json.loads(response_data.data)
    keys = list(response_data.keys())
    required_keys = ['class_id', 'student_id', 'student_name', 'marks']
    assert isinstance(response_data, dict)
    assert set(required_keys).issubset(set(keys))
    # if data is not available
    response_data = client.get('/class/1333/student/0')
    response_data = json.loads(response_data.data)
    assert isinstance(response_data, str)
    assert response_data == 'data not found'
