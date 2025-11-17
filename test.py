import time
import numpy as np
from scipy.optimize import curve_fit

def measure_time(func, input_generator, sizes):
    times = []
    for size in sizes:
        data = input_generator(size)
        start = time.perf_counter()
        func(data)
        end = time.perf_counter()
        times.append(end - start)
    return times

def fit_complexity(sizes, times):
    def linear(n, a, b): return a*n + b
    def quadratic(n, a, b): return a*n**2 + b
    def log(n, a, b): return a*np.log(n + 1) + b
    fits = {}
    for f, name in [(linear, 'O(n)'), (quadratic, 'O(n^2)'), (log, 'O(log n)')]:
        popt, _ = curve_fit(f, sizes, times)
        error = np.linalg.norm(f(np.array(sizes), *popt) - np.array(times))
        fits[name] = error
    best = min(fits, key=fits.get)
    return best, fits

if __name__ == "__main__":
    # Example usage: analyze sorting function
    def insertion_sort(arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >=0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    input_gen = lambda n: list(range(n, 0, -1))
    sizes = [50, 100, 200, 400]
    times = measure_time(insertion_sort, input_gen, sizes)
    complexity, all_fits = fit_complexity(sizes, times)
    print(f"Estimated time complexity: {complexity}")
    print("Fit errors:", all_fits)