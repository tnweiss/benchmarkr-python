from benchmarkr.benchmarkr import benchmark

from time import sleep


@benchmark(lower_bound_s=1, upper_bound_s=10, custom_properties={'test': 5})
def test_a():
    sleep(2)
