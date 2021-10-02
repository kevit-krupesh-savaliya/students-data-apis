"""Database operations"""
import pymongo
from config import DB_URL, DB_NAME
from services.logger import logger

client = pymongo.MongoClient(DB_URL)
db = client[DB_NAME]

"""Use for Students APIs"""


def get_students():
    """Get students from students collection"""
    try:
        students = db['students'].find({}, {'student_id': '$_id', 'student_name': '$name', '_id': 0}).sort(
            [("_id", pymongo.ASCENDING)])
        return {'success': True, 'students': students}
    except Exception as error:
        logger.error(f"F_get_students: {error}")
        return {'success': False}


def get_student_with_classes(student_id):
    """Get student with classes"""
    try:
        query = [
            {
                '$match': {
                    '_id': student_id
                }
            }, {
                '$lookup': {
                    'from': 'grades',
                    'localField': '_id',
                    'foreignField': 'student_id',
                    'as': 'classes'
                }
            }, {
                '$unwind': {
                    'path': '$classes'
                }
            }, {
                '$project': {
                    '_id': 1,
                    'name': 1,
                    'class_id': '$classes.class_id'
                }
            }, {
                '$group': {
                    '_id': '$_id',
                    'classes': {
                        '$push': {
                            'class_id': '$class_id'
                        }
                    },
                    'student_name': {
                        '$first': '$name'
                    }
                }
            }, {
                '$project': {
                    'student_id': '$_id',
                    'student_name': 1,
                    'classes': 1,
                    '_id': 0
                }
            }
        ]
        student_data = db['students'].aggregate(query, allowDiskUse=True)
        return {'success': True, 'student': student_data}
    except Exception as error:
        logger.error(f"F_get_student_with_classes: {error}")
        return {'success': False}


def get_student_with_marks(student_id):
    """Get student with marks"""
    try:
        query = [
            {
                '$match': {
                    '_id': student_id
                }
            }, {
                '$lookup': {
                    'from': 'grades',
                    'localField': '_id',
                    'foreignField': 'student_id',
                    'as': 'classes'
                }
            }, {
                '$unwind': {
                    'path': '$classes'
                }
            }, {
                '$project': {
                    '_id': 1,
                    'name': 1,
                    'class_id': '$classes.class_id',
                    'total_marks': {
                        '$toInt': {
                            '$sum': '$classes.scores.score'
                        }
                    }
                }
            }, {
                '$group': {
                    '_id': '$_id',
                    'classes': {
                        '$push': {
                            'class_id': '$class_id',
                            'total_marks': '$total_marks'
                        }
                    },
                    'student_name': {
                        '$first': '$name'
                    }
                }
            }, {
                '$project': {
                    'student_id': '$_id',
                    'student_name': 1,
                    'classes': 1,
                    '_id': 0
                }
            }
        ]
        student_data = db['students'].aggregate(query, allowDiskUse=True)
        return {'success': True, 'student': student_data}
    except Exception as error:
        logger.error(f"F_get_student_with_marks: {error}")
        return {'success': False}


"""Use for classes APIs"""


def get_classes():
    """Get classes from grades collection"""
    try:
        classes = db['grades'].find({}, {'class_id': 1, '_id': 0}).sort(
            [("_id", pymongo.ASCENDING)])
        return {'success': True, 'classes': classes}
    except Exception as error:
        logger.error(f"F_get_classes: {error}")
        return {'success': False}


def get_students_from_class_id(class_id):
    """Get all students with requested class id"""

    try:
        query = [
            {
                '$match': {
                    'class_id': class_id
                }
            }, {
                '$lookup': {
                    'from': 'students',
                    'localField': 'student_id',
                    'foreignField': '_id',
                    'as': 'student'
                }
            }, {
                '$unwind': {
                    'path': '$student'
                }
            }, {
                '$group': {
                    '_id': '$class_id',
                    'students': {
                        '$push': {
                            'student_name': '$student.name',
                            'student_id': '$student_id'
                        }
                    }
                }
            }, {
                '$project': {
                    'class_id': '$_id',
                    'students': 1,
                    '_id': 0
                }
            }
        ]
        students_data = db['grades'].aggregate(query, allowDiskUse=True)
        return {'success': True, 'students': students_data}
    except Exception as error:
        logger.error(f"F_get_students_from_class_id: {error}")
        return {'success': False}


def get_students_marks_from_class_id(class_id):
    """Get all students marks with requested class id"""

    try:
        query = [
            {
                '$match': {
                    'class_id': class_id
                }
            }, {
                '$lookup': {
                    'from': 'students',
                    'localField': 'student_id',
                    'foreignField': '_id',
                    'as': 'student'
                }
            }, {
                '$unwind': {
                    'path': '$student'
                }
            }, {
                '$project': {
                    'class_id': 1,
                    'student_id': 1,
                    'total_marks': {
                        '$toInt': {
                            '$sum': '$scores.score'
                        }
                    },
                    'student': 1
                }
            }, {
                '$group': {
                    '_id': '$class_id',
                    'students': {
                        '$push': {
                            'student_id': '$student_id',
                            'student_name': '$student.name',
                            'total_marks': '$total_marks'
                        }
                    }
                }
            }, {
                '$project': {
                    'class_id': '$_id',
                    'students': 1,
                    '_id': 0
                }
            }
        ]
        students_data = db['grades'].aggregate(query, allowDiskUse=True)
        return {'success': True, 'students': students_data}
    except Exception as error:
        logger.error(f"F_get_students_from_class_id: {error}")
        return {'success': False}


def get_student_data(class_id):
    """Get student data with marks"""

    try:
        query = [
            {
                '$match': {
                    'class_id': class_id
                }
            }, {
                '$lookup': {
                    'from': 'students',
                    'localField': 'student_id',
                    'foreignField': '_id',
                    'as': 'student'
                }
            }, {
                '$unwind': {
                    'path': '$student'
                }
            }, {
                '$project': {
                    'class_id': 1,
                    'student_id': 1,
                    'student_name': '$student.name',
                    'total_marks': {
                        '$toInt': {
                            '$sum': '$scores.score'
                        }
                    },
                    'details': {
                        '$map': {
                            'input': '$scores',
                            'as': 'score',
                            'in': {
                                'type': '$$score.type',
                                'marks': {
                                    '$toInt': '$$score.score'
                                }
                            }
                        }
                    },
                    '_id': 0
                }
            }, {
                '$group': {
                    '_id': '$class_id',
                    'students': {
                        '$push': {
                            'student_id': '$student_id',
                            'student_name': '$student_name',
                            'details': '$details',
                            'total_marks': '$total_marks'
                        }
                    }
                }
            }, {
                '$project': {
                    'class_id': '$_id',
                    'students': 1,
                    '_id': 0
                }
            }
        ]
        students_data = db['grades'].aggregate(query, allowDiskUse=True)
        return {'success': True, 'students': students_data}
    except Exception as error:
        logger.error(f"F_get_student_data: {error}")
        return {'success': False}


"""Use for Student and Class Api"""


def get_student_with_marks_with_class_id(student_id, class_id):
    """Get student with marks for provided class id"""

    try:
        query = [
            {
                '$match': {
                    'class_id': class_id,
                    'student_id': student_id
                }
            }, {
                '$lookup': {
                    'from': 'students',
                    'localField': 'student_id',
                    'foreignField': '_id',
                    'as': 'student'
                }
            }, {
                '$unwind': {
                    'path': '$student'
                }
            }, {
                '$project': {
                    'class_id': 1,
                    'student_id': 1,
                    'student_name': '$student.name',
                    'marks': {
                        '$map': {
                            'input': '$scores',
                            'as': 'score',
                            'in': {
                                'type': '$$score.type',
                                'marks': {
                                    '$toInt': '$$score.score'
                                }
                            }
                        }
                    },
                    '_id': 0
                }
            }
        ]
        student_data = db['grades'].aggregate(query, allowDiskUse=True)
        return {'success': True, 'student': student_data}
    except Exception as error:
        logger.error(f"F_get_students_from_class_id: {error}")
        return {'success': False}
