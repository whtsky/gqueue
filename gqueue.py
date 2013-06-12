import gevent.monkey
gevent.monkey.patch_all()

import functools
import inspect
import gevent
from gevent.queue import JoinableQueue


_WORKERS = {}
_QUEUES = {}


def create_worker(queue):
    q = _QUEUES.setdefault(queue, JoinableQueue())

    def worker():
        while True:
            args, kwargs = q.get()
            try:
                _WORKERS[queue](*args, **kwargs)
            finally:
                q.task_done()
    return worker


def run_worker(num=1, queue='default'):
    for i in range(num):
        gevent.spawn(create_worker(queue))


def join(queue='default'):
    _QUEUES[queue].join()


def join_all():
    for queue in _QUEUES.values():
        queue.join()


def job(queue):
    if inspect.isfunction(queue):
        return job('default')(queue)

    def wrap(func):

        _WORKERS[queue] = func

        q = _QUEUES.setdefault(queue, JoinableQueue())

        @functools.wraps(func)
        def f(*args, **kwargs):
            q.put([args, kwargs])

        return f

    return wrap
