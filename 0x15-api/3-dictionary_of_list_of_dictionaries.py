#!/usr/bin/python3
""" Python script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress
"""
import json
import requests
import sys


if __name__ == "__main__":

    url = 'https://jsonplaceholder.typicode.com'
    user_endPoint = "{}/users".format(url)
    users = requests.get(user_endPoint).json()

    task_endPoint = "{}/todos/".format(url)
    tasks = requests.get(task_endPoint).json()
    all_tasks = {user.get("id"): [{"username": user.get("username"),
                                   "task": task.get("title"),
                                   "completed": task.get("completed")}
                                  for task in tasks
                                  if task.get("userId") == user.get("id")]
                 for user in users
                 }

    """ saves in json file"""
    with open("todo_all_employees.json", 'w', encoding="utf-8") as json_file:
        json.dump(all_tasks, json_file)
