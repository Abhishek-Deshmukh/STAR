"""STAR
author: Abhishek Anil Deshmukh <deshmukhabhishek369@gmail.com>
The rest api to access algorithm via http
"""
import json
from flask import Flask, request, jsonify, Response
from flask_cors import CORS
from my_worker import integrate, ANNOTATIONS


APP = Flask(__name__)
CORS(APP)
TASKS = {}


@APP.route("/", methods=["GET"])
def list_tasks():
    """return the list of tasks"""
    tasks = {task_id: {"ready": task.ready()} for task_id, task in TASKS.items()}
    return jsonify(tasks)


@APP.route("/<int:task_id>", methods=["GET"])
def get_task(task_id):
    """for getting the status of the ongoing process"""
    response = {"task_id": task_id}

    if task_id in TASKS:
        task = TASKS[task_id]
        if task.ready():
            response["result"] = task.get()
    else:
        response = "there is not task with id as " + str(task_id)
    return jsonify(response)


@APP.route("/params", methods=["GET"])
def get_params():
    """for getting the annotations and parameter list"""
    # turning annotations into a jsonifiable object
    # response_data = []
    # i = 0
    for param, annotation in ANNOTATIONS.items():
        if annotation is int:
            ANNOTATIONS[param] = "int"
        elif annotation is float:
            ANNOTATIONS[param] = "float"
        elif annotation is str:
            ANNOTATIONS[param] = "str"
    return ANNOTATIONS


@APP.route("/", methods=["POST"])
def put_task():
    """Function for the call of "/"
    actually runs the algorithm
    """
    print("json:", request.json)
    args = []
    for parameter in ANNOTATIONS:
        try:
            arg = request.json[parameter]
        except:
            return "the parameter '" + parameter + "' seems to be missing"
        if ANNOTATIONS[parameter] == int:
            args.append(int(arg))
        elif ANNOTATIONS[parameter] == float:
            args.append(float(arg))
        elif ANNOTATIONS[parameter] == str:
            args.append(arg)

    task_id = len(TASKS)
    TASKS[task_id] = integrate.delay(*args)
    return jsonify({"task_id": task_id})


if __name__ == "__main__":
    APP.run(debug=True)
