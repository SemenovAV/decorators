from datetime import datetime


def logger(path):
    def log(func):
        def foo(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(path, 'a', encoding='utf8') as f:
                print(datetime.today(), func.__name__, args, kwargs, result, file=f)
            return func(*args, **kwargs)
        return foo
    return log
