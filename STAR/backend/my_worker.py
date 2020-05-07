"""STAR
Abhishek Anil Deshmukh <deshmukhabhishek369@gmail.com>
the integration between celery redis and STAR
"""
from celery import Celery
from algorithm import main

# how to run
# $ redis-server
# $ celery -A my_worker worker --loglevel=debug

APP = Celery(__name__, backend="rpc://", broker="redis://localhost:6379/")

# easier way, if you don't care about exception
# integrate = app.task(approx)

# safer way
@APP.task
def integrate(*args, **kwargs):
    """integration between redis and this"""
    try:
        return main(*args, **kwargs)
    except Exception as err:
        return str(err.__repr__())


ANNOTATIONS = main.__annotations__ # annotation for parameters
