def bubblesort(arr: list) -> list:
    arr = arr.copy()

    metric: dict = {
        "total": 0,
        "compares": 0,
        "swaps": 0,
    }

    swapped: bool = True
    while swapped:
        swapped = False

        for n in range(len(arr) - 1):
            metric["compares"] += 1

            if arr[n] > arr[n + 1]:
                metric["swaps"] += 1
                arr[n], arr[n + 1] = arr[n + 1], arr[n]
                swapped = True

    metric["total"] = metric["compares"] + metric["swaps"]
    return arr, metric