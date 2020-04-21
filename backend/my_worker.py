from celery import Celery
from algorithm import approx

# how to run
# $ redis-server
# $ celery -A worker my_worker --loglevel=debug

app = Celery(__name__, backend='rpc://', broker='redis://localhost:6379')

@app.task
def integration(*args, **kwargs):
    try:
        return approx(*args, **kwargs)
    except Exception:
        return "Something could be wrong with the arguments send here"
