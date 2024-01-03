#!/usr/bin/python3
""" Python script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress
"""
import requests
import sys


if __name__ == "__main__":
    user_id = int(sys.argv[1])

    url = 'https://jsonplaceholder.typicode.com'
    user_endPoint = "{}/users/{}".format(url, user_id)
    user = requests.get(user_endPoint).json()
    user_name = user.get("name")

    task_endPoint = "{}/todos/".format(url)
    tasks = requests.get(task_endPoint).json()
    all_tasks = [task for task in tasks if task.get("userId") == user_id]

    tasks_completed = [task for task in all_tasks if task.get("completed")]
    print("Employee {} is done with tasks({}/{}):".format(user_name,
                                                          len(tasks_completed),
                                                          len(all_tasks)))
    for task in tasks_completed:
        title = task.get("title")
        print("\t {}".format(title))
