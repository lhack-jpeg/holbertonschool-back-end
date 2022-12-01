#!/usr/bin/python3
'''
This module gathers data from a mockup api.
https://jsonplaceholder.typicode.com/
'''

if __name__ == '__main__':
    import json
    import requests

    file_name = 'todo_all_employees.json'
    user_info_url = 'https://jsonplaceholder.typicode.com/users'
    user_data = requests.get(user_info_url).json()
    todo_url = 'https://jsonplaceholder.typicode.com/todos'

    todo_data = requests.get(todo_url).json()

    json_dict = {}

    for user in user_data:
        json_dict.update({user.get('id'): []})

    for user in user_data:
        user_todos = []
        for todo in todo_data:
            if user.get('id') == todo.get('userId'):
                data = {
                    'username': user.get('username'),
                    'task': todo.get('title'),
                    'completed': todo.get('completed')
                }
                user_todos.append(data)
        json_dict[user.get('id')] = user_todos

    with open(file_name, 'w') as f:
        json.dump(json_dict, f)
