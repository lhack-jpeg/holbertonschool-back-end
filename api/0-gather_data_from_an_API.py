#!/usr/bin/python3
'''
This module gathers data from a mockup api.
https://jsonplaceholder.typicode.com/
'''


if __name__ == '__main__':
    import requests
    from sys import argv

    user_id = argv[1]
    user_info_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(
        user_id
    )
    user_data = requests.get(user_info_url).json()
    emp_name = user_data.get('name')

    todo_url_req = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
        user_id)
    todo_data = requests.get(todo_url_req).json()
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
