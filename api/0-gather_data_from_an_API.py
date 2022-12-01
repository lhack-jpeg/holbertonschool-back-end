#!/usr/bin/python3
'''
This module gathers data from a mockup api.
https://jsonplaceholder.typicode.com/
'''


if __name__ == '__main__':
    import json
    import requests
    from sys import argv

    user_id = argv[1]
    user_info_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(
        user_id
    )
    user_req = requests.get(user_info_url)
    user_data = json.loads(user_req.text)
    emp_name = user_data.get('name')

    todo_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
        user_id)
    todo_req = requests.get(todo_url)
    todo_data = json.loads(todo_req.text)
    todo_count = len(todo_data)
    todo_completed = len([d for d in todo_data if d.get('completed')])
    first_line = 'Employee {} is done with tasks({}/{}):'.format(
        emp_name,
        todo_completed,
        todo_count
    )
    print(first_line)
    for task in todo_data:
        print('\t {}'.format(task.get('title')))
