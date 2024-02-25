import json
from flask import Flask, jsonify, request


schedule = [
    {'day': 'Monday', 'task': 'Take meds', 'date': '02/24/2024', 'time': '8am'},
    {'day': 'Monday', 'task': 'Write in journal', 'date': '02/24/2024', 'time': '4pm'},
    {'day': 'Tuesday', 'task': 'Take meds', 'date': '02/24/2024', 'time': '8am'},
    {'day': 'Wednesday', 'task': 'Take meds', 'date': '02/24/2024', 'time': '8am'},
    {'day': 'Wednesday', 'task': 'Write in journal', 'date': '02/24/2024', 'time': '4pm'},
    {'day': 'Thursday', 'task': 'Take meds', 'date': '02/24/2024', 'time': '8am'},
    {'day': 'Friday', 'task': 'Take meds', 'date': '02/24/2024', 'time': '8am'},
    {'day': 'Friday', 'task': 'Write in journal', 'date': '02/24/2024', 'time': '4pm'}
    ]

def get_schedule():
    return jsonify(schedule)

def get_schedule_by_date(date):
    task = get_task(date)
    if task is None:
        return jsonify({'error': 'Date does not exist'}), 404
    return jsonify(task)


def get_task(date):
    return next((e for e in schedule if e['date']==date), None)

def get_task(task):
    return next((e for e in schedule if e['task']==task), None)

def date_is_valid(date):
    for key in date.keys():
        if key != 'date':
            return False
    return True


def create_task():

    task = json.loads(request.data)
    if not date_is_valid(task):
        return jsonify({'error': 'Invalid date.'}), 400
    
    task['day'] = input('Day of the Week: ')
    task['task'] = input('Task: ')
    task['date'] = input('Date (MM/DD/YY): ')
    task['time'] = input('Time (am/pm): ')
    schedule.append(task)

    return '', 201, {'location': f'/schedule/{task}'}

def update_task(task):
    up_task = get_task(task)
    if up_task is None:
        return jsonify({'error': 'Task does not exist.'}), 404
    
    updated_schedule = json.loads(request.data)
    up_task.update(updated_schedule)
    return jsonify(up_task)
    
def delete_task(task):
    global schedule
    cur_task = get_task(task)
    if cur_task is None:
        return jsonify({'error': 'Task does not exist.'}), 404
    
    schedule = [e for e in schedule if e['task']!=task]
    return jsonify(cur_task), 200