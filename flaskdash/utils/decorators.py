

from functools import wraps


def add_data_processor(processor_name):
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            self.data_processors[processor_name] = func
            print '3'
        print '2'
        return wrapper
    print '1'
    return decorator
