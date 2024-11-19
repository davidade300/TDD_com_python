import time
from .my_code import long_running_function


def test_long_running_function_performance():
    start_time = time.time()
    long_running_function()
    end_time = time.time()
    duration = end_time - start_time

    assert (
        duration < 5
    ), f" a função demorou {duration} a mais do que o esperado"
