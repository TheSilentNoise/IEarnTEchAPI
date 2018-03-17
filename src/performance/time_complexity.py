"""Performance calculation functions.

Creating a function to calculate execution time of any function.
Function can be used as decorators.

Use @timeit_func on any function or class to measure execution time of same.
"""


import time


def timeit_func(method):
    """
    function to calculate machine time complexity of function

    Args:
        method (method): method name |
                timeit_func is decorator for method specified

    Returns:
        timed (executor): Executor with printing time taken by method.
    """
    def timed(*args, **kw):
        _starttime = time.clock()
        result = method(*args, **kw)
        _endtime = time.clock()

        cal_time = (_endtime - _starttime) * 1000
        print('performance of % r function % s MS' %
              (method.__name__, cal_time))
        return result

    return timed
