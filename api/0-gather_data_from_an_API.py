#!/usr/bin/python3
'''
This module gathers data from a mockup api.
https://jsonplaceholder.typicode.com/
'''


if __name__ == '__main__':
    import json
    from sys import argv
    import urllib.request

    user_id = argv[1]
    user_info_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(
        user_id
    )
    user_req = urllib.request.urlopen(user_info_url)
    user_data = json.loads(user_req.read())
    emp_name = user_data['name']

    todo_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
        user_id)
    todo_req = urllib.request.urlopen(todo_url)
    todo_data = json.loads(todo_req.read())
    todo_count = len(todo_data)
    todo_completed = [d for d in todo_data if d.get('completed')]
    len_completed = len(todo_completed)
    first_line = 'Employee {} is done with tasks({}/{}):'.format(
        emp_name,
        len_completed,
        todo_count
    )
    print(first_line)
    for task in todo_completed:
        print('\t {}'.format(task.get('title')))
