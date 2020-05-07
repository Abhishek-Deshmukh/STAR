"""STAR
author: Abhishek Anil Deshmukh <deshmukhabhishek369@gmail.com>
The rest api to access algorithm via http
"""
from flask import Flask, request, jsonify
from my_worker import integrate, ANNOTATIONS

APP = Flask(__name__)
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
        response["result"] = "this id does not existing yet ;)"
    return jsonify(response)


@APP.route("/", methods=["PUT"])
def put_task():
    """Function for the call of "/"
    actually runs the algorithm
    """
    args = []
    for parameter in ANNOTATIONS:
        if ANNOTATIONS[parameter] == int:
            args.append(int(request.json[parameter]))
        elif ANNOTATIONS[parameter] == float:
            args.append(float(request.json[parameter]))
        else:
            args.append(request.json[parameter])

    task_id = len(TASKS)
    TASKS[task_id] = integrate.delay(*args)
    response = {"task_id": task_id}
    return jsonify(response)


if __name__ == "__main__":
    APP.run(debug=True)
