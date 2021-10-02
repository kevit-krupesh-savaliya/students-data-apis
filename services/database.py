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
