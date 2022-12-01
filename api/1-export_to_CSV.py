#!/usr/bin/python3
'''
This module gathers data from a mockup api.
https://jsonplaceholder.typicode.com/
'''


if __name__ == '__main__':
    import csv
    import json
    from sys import argv
    import urllib.request

    user_id = argv[1]
    user_info_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(
        user_id
    )
    user_req = urllib.request.urlopen(user_info_url)
    user_data = json.loads(user_req.read())
    emp_name = user_data.get('username')
    file_name = user_id + '.csv'

    todo_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
        user_id)
    todo_req = urllib.request.urlopen(todo_url)
    todo_data = json.loads(todo_req.read())
    list_of_todos = []
    for todo in todo_data:
        todo_dict = {}
        todo_dict.update({'USER_ID': user_id})
        todo_dict.update({'USERNAME': emp_name})
        todo_dict.update({'TASK_COMPLETED_STATUS': todo.get('completed')})
        todo_dict.update({'TASK_TITLE': todo.get('title')})
        list_of_todos.append(todo_dict)

    fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]

    with open(file_name, 'w', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writerows(list_of_todos)