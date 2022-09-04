from threading import Thread
from builtins import list
from json import dumps


class Thread_list(list, Thread):
    """
    python class that store the Threads inside the List
    this class won't return anything
    args:
        default_target: callable object if you want to thread single function
    """
    def __init__(self, default_target: callable = None):
        self.default_target = default_target
        super().__init__()

    def __str__(self) -> str:
        return dumps(
            obj={
                thread_id: thread for thread_id, thread in enumerate(self)},
            indent=2)

    def __call__(self, *, join_trd: bool = False) -> None:
        """
        calling the object will start the threads
        :param join_trd: bool -> if you want to join the threads (all the threads Done)
        :return: None
        """
        for trd in self:
            trd.start()
        if join_trd:
            for trd in self:
                trd.join()

    def add_tread(self, target: callable = None, args: tuple = (), kwargs=None):
        """
        create and add the Thread to class
        :param target: callable function
        :param args: positional args
        :param kwargs: keyword args
        :return: None
        """
        kwargs = {} if not args else kwargs
        target = target if target is not None else self.default_target
        if target is None:
            raise Exception("target is not set")
        self.append(Thread(target=target, args=args, kwargs=kwargs))
