"""Common helper fuctions"""
from math import floor


def grade_calculation(data):
    """Grade calculation for student mark sheet"""
    grade_data = sorted(data['students'], key=lambda k: k['total_marks'], reverse=True)
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
        grade_data[i - 1]['grade'] = grade
    data['students'] = grade_data
    return data


def check_duplicate_class_and_add_total(data, mark_field='marks'):
    """Create unique type of class and add total marks"""
    for i, student in enumerate(data):
        new_mark_data = []
        class_type = {}
        for subject in student[mark_field]:
            if subject['type'] not in class_type:
                class_type[subject['type']] = 0
                new_mark_data.append(subject)
            else:
                class_type[subject['type']] += 1
                for m_index, new_mark in enumerate(new_mark_data):
                    if new_mark['type'] == subject['type']:
                        new_mark_data[m_index]['type'] = f'{subject["type"]}{class_type[subject["type"]]}'
                        class_type[subject['type']] += 1
                new_mark_data.append({'type': f'{subject["type"]}{class_type[subject["type"]]}',
                                      'marks': subject['marks']})
        new_mark_data.append({'type': 'total', 'marks': student['total_marks']})
        data[i][mark_field] = new_mark_data
        del data[i]['total_marks']
    return data
