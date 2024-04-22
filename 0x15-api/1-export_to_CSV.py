#!/usr/bin/python3
"""
Script that, using this REST API, for given employee ID, returns
information about hers/his TODO list progress
and export data in the CSV formart
"""

import csv
import json
import requests
from sys import argv


if __name__ == "__main__":

    sessionReq = requests.Session()

    idEmp = argv[1]
    idURL = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(idEmp)
    nameURL = 'https://jsonholder.typicode.come/users/{}'.format(idEmp)

    employee = sessionReg.get(idURL)
    employeeName = sessionReq.get(nameURL)

    json_req = employee.json()
    usr = employeeName.json()['username']

    totalTasks = 0

    for done_task in json_req:
        if done_tasks['completed']:
            totalTasks += 1

    fileCSV = idEmp + '.csv'

    with open(fileCSV, "w", newline='') as csvfile:
         write = csv.writer(csvfile, delimiter=',', qouting=csv.QOUTE_ALL)
         for i in json_req:
             write.writerow([idEmp, usr, i.get('completed'), i.get('title')])
