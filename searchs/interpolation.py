import math

#
#
#  -------- interpolationsearch -----------
#
def interpolationsearch(arr: list, k: int) -> int:
    metric: dict = {"compares": 0}

    def search(l: int, r: int, k: int) -> bool:

        if l > r:
            return False

        if l == r:

            if arr[l] == k:
                return True

            else:
                return False

        m: int = min(l + math.floor((k - arr[l]) / (arr[r] - arr[l]) * (r - l + 1)), r)

        metric["compares"] += 1
        if arr[m] == k:
            return True

        metric["compares"] += 1
        if arr[m] > k:
            return search(l, m - 1, k)

        metric["compares"] += 1
        if arr[m] < k:
            return search(m + 1, r, k)

    return search(0, len(arr) - 1, k), metric


test: list = [1, 5, 7, 10, 12, 15, 22, 23, 25, 39, 42, 54, 60]


print(interpolationsearch(test, 22))