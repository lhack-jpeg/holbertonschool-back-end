#!/usr/bin/python3
'''
This module gathers data from a mockup api.
https://jsonplaceholder.typicode.com/
'''


if __name__ == '__main__':
    import csv
    import requests
    from sys import argv

    user_id = argv[1]
    user_info_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(
        user_id
    )
    user_data = requests.get(user_info_url).json()
    emp_name = user_data.get('username')
    file_name = user_id + '.csv'

    todo_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
        user_id)
    todo_data = requests.get(todo_url).json()

    with open(file_name, 'w', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL)

        for todo in todo_data:
            todo_list = [user_id, emp_name,
                         todo.get('completed'), todo.get('title')]
            writer.writerow(todo_list)
