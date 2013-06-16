import functools
import gevent
from gevent.queue import JoinableQueue


class GQueue(object):
    def __init__(self):
        self.__QUEUE = JoinableQueue()

    def job(self, func):
        @functools.wraps(func)
        def f(*args, **kwargs):
            self.__QUEUE.put([func, args, kwargs])

        return f

    def join(self):
        self.__QUEUE.join()

    def work(self):
        while True:
            func, args, kwargs = self.__QUEUE.get()
            try:
                func(*args, **kwargs)
            finally:
                self.__QUEUE.task_done()

    def run_worker(self, num=1):
        for i in range(num):
            gevent.spawn(self.work)


__gqueue = GQueue()
job = __gqueue.job
join = __gqueue.join
run_worker = __gqueue.run_worker
