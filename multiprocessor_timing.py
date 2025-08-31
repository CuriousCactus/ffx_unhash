import multiprocessing
import time
import numpy as np


def expensive_function(arg):
    return np.cos(arg ** arg ** arg ** arg ** arg ** arg) ** arg + np.sin(arg ** arg ** arg ** arg ** arg ** arg) ** arg


if __name__ == '__main__':

    cpu_max = multiprocessing.cpu_count()
    print("CPU max:", cpu_max)
    print("----------------------------")
    PROBLEM_SIZE = 5000000000

    time_perfect = 0.0

    for cpu_count in range(1, cpu_max + 1):
        print("CPU count:", cpu_count)
        with multiprocessing.Pool(cpu_count) as pool:
            start_time = time.time()
            result = pool.imap_unordered(
                expensive_function,
                np.arange(PROBLEM_SIZE),
            )
            print(f"Timing: {time.time()-start_time:g}s")
            if cpu_count == 1:
                time_single = time.time() - start_time
            else:
                # print(f"Perfect scaling time: {time_single / cpu_count:g}s")
                print(f"Actual speed gain: {(time_single) / (time.time()-start_time):g}s")
            print("----------------------------")
