"""Common helper fuctions"""
from math import floor


def grade_calculation(data):
    """Grade calculation for student mark sheet"""
    student_data = list(data['students'])[0]
    grade_data = sorted(student_data['students'], key=lambda k: k['total_marks'], reverse=True)
    total_students = len(grade_data)
    for i, _ in enumerate(grade_data, 1):
        if i <= floor((1 / 12) * total_students):
            grade = 'A'
        elif i <= floor((1 / 6) * total_students):
            grade = 'B'
        elif i <= floor((1 / 4) * total_students):
            grade = 'C'
        else:
            grade = 'D'
        del grade_data[i - 1]['total_marks']
        grade_data[i - 1]['grade'] = grade
    student_data['students'] = grade_data
    return student_data
