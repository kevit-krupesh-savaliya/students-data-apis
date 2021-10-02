"""API doc questions answers"""
import pymongo
from services.logger import logger
from config import DB_NAME, DB_URL


def func_q1(db_connection):
    """Get distinct students count"""
    all_students = db_connection['students'].find({}).count()
    logger.info(f'total students: {all_students}')


def func_q2(db_connection):
    """Get distinct courses count"""
    all_courses = len(db_connection['grades'].distinct('scores.type'))
    logger.info(f'total courses: {all_courses}')


if __name__ == "__main__":
    client = pymongo.MongoClient(DB_URL)
    db = client[DB_NAME]
    func_q1(db)
    func_q2(db)
