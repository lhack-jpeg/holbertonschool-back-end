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
    file_name = user_id + '.json'

    user_info_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(
        user_id
    )
    user_data = requests.get(user_info_url).json()
    emp_username = user_data.get('username')
    todo_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
        user_id)

    todo_data = requests.get(todo_url).json()

    json_dict = {user_id: []}

    for todo in todo_data:
        data = {
            'task': todo.get('title'),
            'completed': todo.get('completed'),
            'username': emp_username,
        }
        json_dict[user_id].append(data)

    with open(file_name, 'w') as f:
        json.dump(json_dict, f)
