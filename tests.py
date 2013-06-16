import gqueue


def test_queue():
    t = []
    @gqueue.job
    def add():
        t.append(2)

    add()
    assert t == []
    gqueue.run_worker()
    assert t == []
    gqueue.join()
    assert t == [2]
