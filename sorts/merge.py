#
#
#  -------- merge -----------
#
def merge(
    arr: list,
    l: int,
    m: int,
    r: int,
    metric: dict,
) -> None:

    l_cp: list = arr[l:m]
    r_cp: list = arr[m : r + 1]

    l_cp_idx: int = 0
    r_cp_idx: int = 0
    sort_idx: int = l

    while l_cp_idx < len(l_cp) and r_cp_idx < len(r_cp):
        metric["compares"] += 1
        metric["swaps"] += 1

        if l_cp[l_cp_idx] <= r_cp[r_cp_idx]:
            arr[sort_idx] = l_cp[l_cp_idx]
            l_cp_idx += 1

        else:
            arr[sort_idx] = r_cp[r_cp_idx]
            r_cp_idx += 1

        sort_idx += 1

    while l_cp_idx < len(l_cp):
        metric["swaps"] += 1
        arr[sort_idx] = l_cp[l_cp_idx]
        l_cp_idx += 1
        sort_idx += 1

    while r_cp_idx < len(r_cp):
        metric["swaps"] += 1
        arr[sort_idx] = r_cp[r_cp_idx]
        r_cp_idx += 1
        sort_idx += 1


#
#
#  -------- sort_default -----------
#
def sort_default(arr: list, metric: dict) -> None:

    #  -------- sort -----------
    #
    def sort(l: int = 0, r: int = len(arr) - 1) -> None:

        if l < r:
            m: int = int((l + r) / 2)

            sort(l, m)
            sort(m + 1, r)
            merge(arr, l, m + 1, r, metric)

    sort()


#
#
#  -------- sort_straight -----------
#
def sort_straight(arr: list, metric: dict) -> None:

    l: int = 0
    r: int = len(arr) - 1
    s: int = 1

    while s < r - l + 1:
        ll: int = l

        while ll + s < r + 1:
            mm: int = ll + s
            rr: int = mm + s - 1

            if rr > r:
                rr = r

            merge(arr, ll, mm, rr, metric)
            ll = rr + 1

        s = s * 2


#
#
#  -------- sort_natural -----------
#
def sort_natural(arr: list, metric: dict) -> None:

    l: int = 0
    r: int = len(arr) - 1
    b: bool = True

    while b:
        b = False
        ll: int = l

        while ll < r:
            mm: int = ll + 1

            while mm <= r and arr[mm - 1] <= arr[mm]:
                mm += 1

            rr: int = mm + 1

            while rr <= r and arr[rr - 1] <= arr[rr]:
                rr += 1

            rr -= 1

            if mm <= r:
                b = True
                merge(arr, ll, mm, rr, metric)

            ll = rr + 1


#
#
#  -------- mergesort -----------
#
def mergesort(arr: list, type: str = "natural") -> list:
    arr = arr.copy()

    metric: dict = {
        "total": 0,
        "compares": 0,
        "swaps": 0,
    }

    if type == "default":
        sort_default(arr, metric)

    elif type == "straight":
        sort_straight(arr, metric)

    elif type == "natural":
        sort_natural(arr, metric)

    metric["total"] = metric["compares"] + metric["swaps"]
    return arr, metric
