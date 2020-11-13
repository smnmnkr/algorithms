#
#
#  -------- insertionsort -----------
#
def insertionsort(arr: list) -> list:
    arr = arr.copy()

    metric: dict = {
        "total": 0,
        "compares": 0,
        "swaps": 0,
    }

    for n in range(1, len(arr)):
        m: int = n
        metric["compares"] += 1

        while m > 0 and arr[m] < arr[m - 1]:
            metric["swaps"] += 1
            arr[m - 1], arr[m] = arr[m], arr[m - 1]
            m -= 1

    metric["total"] = metric["compares"] + metric["swaps"]
    return arr, metric