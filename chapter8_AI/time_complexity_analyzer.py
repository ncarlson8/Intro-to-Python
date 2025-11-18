# This code was created via CoPilot, and I had it iterate it a few times by further specifying the method(empirical)
# and then expanding the code to allow for multiple different algorithms(I had it use sorting algorithms since it is most commonly tested for time complexity)
# It also only has the options of O(logn), O(n), and  O(n^2).
# I also made it so that it would show the time elapsed for each test.



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

# --- Sorting algorithms ---
def insertion_sort(arr):
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >=0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def merge_sort(arr):
    arr = arr.copy()
    def _merge_sort(a):
        if len(a) > 1:
            mid = len(a) // 2
            L = a[:mid]
            R = a[mid:]
            _merge_sort(L)
            _merge_sort(R)
            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    a[k] = L[i]
                    i += 1
                else:
                    a[k] = R[j]
                    j += 1
                k += 1
            while i < len(L):
                a[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                a[k] = R[j]
                j += 1
                k += 1
    _merge_sort(arr)

def quick_sort(arr):
    arr = arr.copy()
    def _quick_sort(a):
        if len(a) <= 1:
            return a
        else:
            pivot = a[len(a)//2]
            left = [x for x in a if x < pivot]
            middle = [x for x in a if x == pivot]
            right = [x for x in a if x > pivot]
            return _quick_sort(left) + middle + _quick_sort(right)
    # overwrite arr in-place for fair comparison
    sorted_arr = _quick_sort(arr)
    for i in range(len(arr)):
        arr[i] = sorted_arr[i]

algorithms = {
    'Insertion Sort': insertion_sort,
    'Bubble Sort': bubble_sort,
    'Merge Sort': merge_sort,
    'Quick Sort': quick_sort
}

if __name__ == "__main__":
    sizes = [50, 100, 200, 400, 800]
    input_gen = lambda n: list(range(n, 0, -1))  # Worst case for some sorts

    print("Empirical time complexity analysis for sorting algorithms")
    print("Input sizes:", sizes)
    print("Timing results (seconds):\n")

    for algo_name, func in algorithms.items():
        start = time.perf_counter()
        times = measure_time(func, input_gen, sizes)
        end = time.perf_counter()
        complexity, all_fits = fit_complexity(sizes, times)
        print(f"{algo_name}:")
        for sz, t in zip(sizes, times):
            print(f"  Size {sz}: {t:.5f} s")
        print(f"  Total time elapsed: {end - start:.5f} s")
        print(f"  Estimated time complexity: {complexity}")
        print(f"  Fit errors: {all_fits}\n")