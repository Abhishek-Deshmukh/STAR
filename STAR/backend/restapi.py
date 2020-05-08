"""STAR
author: Abhishek Anil Deshmukh <deshmukhabhishek369@gmail.com>
The rest api to access algorithm via http
"""
import json
from flask import Flask, request, jsonify, Response
from my_worker import integrate, ANNOTATIONS

APP = Flask(__name__)
TASKS = {}


@APP.route("/", methods=["GET"])
def list_tasks():
    """return the list of tasks"""
    tasks = {task_id: {"ready": task.ready()} for task_id, task in TASKS.items()}
    # coz CORS thing
    response = Response(json.dumps(tasks))
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response


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
    # coz CORS thing
    response = Response(json.dumps(response))
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response


@APP.route("/params", methods=["GET"])
def get_params():
    """for getting the annotations and parameter list"""
    # turning annotations into a jsonifiable object
    response_data = []
    i = 0
    for param, annotation in ANNOTATIONS.items():
        if annotation is int:
            field = {"name": param, "type": "int", "id": i}
        elif annotation is float:
            field = {"name": param, "type": "float", "id": i}
        elif annotation is str:
            field = {"name": param, "type": "str", "id": i}
        i += 1
        response_data.append(field)
    response = Response(json.dumps(response_data))
    # coz CORS thing
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response


@APP.route("/", methods=["PUT"])
def put_task():
    """Function for the call of "/"
    actually runs the algorithm
    """
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
    # coz CORS things
    response = Response(json.dumps({"task_id": task_id}))
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response


if __name__ == "__main__":
    APP.run(debug=True)
