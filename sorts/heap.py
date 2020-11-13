import math

#
#
#  -------- heapsort -----------
#
def heapsort(arr: list) -> list:
    arr = arr.copy()
    n: int = len(arr)

    metric: dict = {
        "total": 0,
        "compares": 0,
        "swaps": 0,
    }

    def sink(i: int, m: int) -> None:

        while 2 * i + 1 <= m:
            metric["compares"] += 1
            j: int = 2 * i + 1

            if 2 * i + 2 <= m and arr[2 * i + 1] < arr[2 * i + 2]:
                j = 2 * i + 2

            if arr[i] < arr[j]:
                metric["swaps"] += 1
                arr[i], arr[j] = arr[j], arr[i]
                i = j

            else:
                i = m

    for i in reversed(range(0, math.ceil(n / 2))):
        sink(i, n - 1)

    for i in reversed(range(0, n)):
        metric["swaps"] += 1
        arr[i], arr[0] = arr[0], arr[i]
        sink(0, i - 1)

    metric["total"] = metric["compares"] + metric["swaps"]
    return arr, metric