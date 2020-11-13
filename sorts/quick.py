#
#
#  -------- quicksort -----------
#
def quicksort(arr: list) -> list:
    arr = arr.copy()

    metric: dict = {
        "total": 0,
        "compares": 0,
        "swaps": 0,
    }

    #  -------- sort -----------
    #
    def sort(l: int = 0, r: int = len(arr) - 1) -> None:

        if l < r:
            p: int = r
            i: int = l
            j: int = r - 1

            repeat: bool = True
            while repeat:
                metric["compares"] += 1

                while i <= j and arr[i] <= arr[p]:
                    metric["compares"] += 1
                    i += 1

                while i <= j and arr[j] >= arr[p]:
                    metric["compares"] += 1
                    j -= 1

                if i < j:
                    metric["swaps"] += 1
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
                    j -= 1

                if i > j:
                    repeat = False

            metric["swaps"] += 1
            arr[i], arr[r] = arr[r], arr[i]
            sort(l, i - 1)
            sort(i + 1, r)

    sort()
    metric["total"] = metric["compares"] + metric["swaps"]
    return arr, metric
