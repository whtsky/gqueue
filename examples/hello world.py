from gqueue import job, run_worker, join_all


@job
def hello():
    print("Hello World!")


for _ in range(5):
    hello()


print('----')
run_worker()
join_all()