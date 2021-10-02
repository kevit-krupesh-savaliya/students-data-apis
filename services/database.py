"""Database operations"""
import pymongo
from config import DB_URL, DB_NAME
from services.logger import logger

client = pymongo.MongoClient(DB_URL)
db = client[DB_NAME]


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
