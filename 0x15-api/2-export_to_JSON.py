#!/usr/bin/python3
""" Python script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress
"""
import json
import requests
import sys


if __name__ == "__main__":
    user_id = int(sys.argv[1])

    url = 'https://jsonplaceholder.typicode.com'
    user_endPoint = "{}/users/{}".format(url, user_id)
    user = requests.get(user_endPoint).json()
    user_name = user.get("username")

    task_endPoint = "{}/todos/".format(url)
    tasks = requests.get(task_endPoint).json()
    all_tasks = {user_id: [{"task": task.get("title"),
                            "completed": task.get("completed"),
                            "username": user_name}
                           for task in tasks if task.get("userId") == user_id]
                 }

    """ saves in json file"""
    with open("{}.json".format(user_id), 'w', encoding="utf-8") as json_file:
        json.dump(all_tasks, json_file)
