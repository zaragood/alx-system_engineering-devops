#!/usr/bin/python3
""" Python script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress
"""
import csv
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
    all_tasks = [[user_id, user_name,
                  task.get("completed"),
                  task.get("title")]
                 for task in tasks if user_id == task.get("userId")]

    """ convert to csv format """
    with open('{}.csv'.format(user_id), 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        """write each row of data to the csv file"""
        for row in all_tasks:
            writer.writerow(row)
